# coding: utf-8

"""
Entity synchronization utilities for Floriday Supplier API Client.

This module provides tools for synchronizing entities from the Floriday API
using sequence numbers.
"""

import logging
import time
from dataclasses import dataclass
from typing import TypeVar, Generic, Callable, List, Optional, Any, Protocol

# Configure logger
logger = logging.getLogger(__name__)

# Type variables for generic typing
T = TypeVar("T")

# Rate limiting constants
# Floriday API rate limits (as per documentation)
FLORIDAY_RATE_LIMIT_CALLS_PER_SECOND = 3.4  # 204 per minute
FLORIDAY_RATE_LIMIT_BURST_LIMIT = 1000

# Default conservative rate limit used by this module
DEFAULT_RATE_LIMIT_DELAY = 0.5  # seconds between calls (2 calls/second)
DEFAULT_BATCH_SIZE = 50


class ApiSyncResult(Protocol, Generic[T]):
    """Protocol defining the structure of a SyncResult object returned by Floriday API."""

    @property
    def maximum_sequence_number(self) -> int:
        """Gets the maximum sequence number in this result set."""
        ...

    @property
    def results(self) -> List[T]:
        """Gets the list of entities in this result set."""
        ...


@dataclass
class EntitySyncResult:
    """Result of a sync_entities operation."""

    entity_type: str
    """The type of entity that was synchronized."""

    start_sequence_number: int
    """The sequence number the sync started from."""

    end_sequence_number: int
    """The highest sequence number processed."""

    entities_processed: int
    """The number of entities processed during the sync."""

    success: bool
    """Whether the sync completed successfully."""

    error: Optional[str] = None
    """Error message if success is False, None otherwise."""
    
    def __str__(self) -> str:
        """Return a human-readable string representation of the sync result."""
        if self.success:
            return (
                f"Sync of {self.entity_type}: SUCCESS\n"
                f"Processed {self.entities_processed} entities\n"
                f"Sequence range: {self.start_sequence_number} → {self.end_sequence_number}"
            )
        else:
            return (
                f"Sync of {self.entity_type}: FAILED\n"
                f"Processed {self.entities_processed} entities before failure\n"
                f"Sequence range: {self.start_sequence_number} → {self.end_sequence_number}\n"
                f"Error: {self.error}"
            )


def sync_entities(
    entity_type: str,
    fetch_entities_callback: Callable[[int, int], ApiSyncResult[T]],
    persist_entity_callback: Optional[Callable[[T], Any]] = None,
    start_seq_number: Optional[int] = None,
    get_max_sequence_number: Optional[Callable[[str], int]] = None,
    batch_size: int = DEFAULT_BATCH_SIZE,
    rate_limit_delay: float = DEFAULT_RATE_LIMIT_DELAY,
) -> EntitySyncResult:
    """Synchronize entities from Floriday API using sequence numbers.

    Args:
        entity_type: A string identifier for the type of entity being synchronized.
        fetch_entities_callback: A function that retrieves entities by sequence number.
            It should accept a sequence number and limit, and return an ApiSyncResult.
        persist_entity_callback: Optional function to persist each entity. If None, entities
            will not be persisted.
        start_seq_number: Optional starting sequence number. If None and get_max_sequence_number
            is provided, it will be used to retrieve the starting sequence number.
        get_max_sequence_number: Optional function to retrieve the maximum sequence number
            for the given entity type from persistence. Required if start_seq_number is None.
        batch_size: Number of entities to retrieve in each API call. Default is DEFAULT_BATCH_SIZE (50).
        rate_limit_delay: Delay in seconds between API calls to avoid rate limiting.
            Default is DEFAULT_RATE_LIMIT_DELAY (0.5s), which is more conservative than
            Floriday's limit of FLORIDAY_RATE_LIMIT_CALLS_PER_SECOND (3.4 calls/second).
            A warning will be logged if the specified delay could exceed Floriday's rate limits.

    Returns:
        An EntitySyncResult containing sync statistics.

    Raises:
        ValueError: If both start_seq_number and get_max_sequence_number are None.
    """
    # Determine starting sequence number
    if start_seq_number is None:
        if get_max_sequence_number is None:
            raise ValueError(
                "Either start_seq_number or get_max_sequence_number must be provided"
            )
        start_seq_number = get_max_sequence_number(entity_type)

    next_sequence_start_number = start_seq_number
    entities_processed = 0

    logger.info(
        f"Syncing {entity_type} from sequence number {next_sequence_start_number}"
    )

    # Validate rate limit delay to ensure we don't exceed Floriday's limits
    min_safe_delay = 1.0 / FLORIDAY_RATE_LIMIT_CALLS_PER_SECOND
    if rate_limit_delay < min_safe_delay:
        logger.warning(
            f"Specified rate_limit_delay ({rate_limit_delay}s) is faster than Floriday's "
            f"limit of {FLORIDAY_RATE_LIMIT_CALLS_PER_SECOND} calls/second "
            f"(minimum safe delay: {min_safe_delay:.2f}s). "
            f"This may result in API rate limiting."
        )

    # Log configuration settings
    logger.debug(
        f"Sync configuration: batch_size={batch_size}, rate_limit_delay={rate_limit_delay}s "
        f"({1.0 / rate_limit_delay:.1f} calls/second)"
    )

    try:
        while True:
            sync_result = fetch_entities_callback(
                sequence_number=next_sequence_start_number, limit_result=batch_size
            )

            # Check if we've reached the end of the data
            if next_sequence_start_number >= sync_result.maximum_sequence_number:
                logger.info(f"Reached maximum sequence number for {entity_type}")
                break

            # Log sequence information for debugging
            logger.debug(
                f"Current sequence: {next_sequence_start_number}, Max sequence: {sync_result.maximum_sequence_number}"
            )

            # Process entities
            for entity in sync_result.results:
                entities_processed += 1

                if persist_entity_callback:
                    result_id = persist_entity_callback(entity)
                    logger.debug(
                        f"Seq nr {getattr(entity, 'sequence_number', 'N/A')}: "
                        f"Persisted {entity_type} {result_id}"
                    )

            # Update sequence number for next batch
            next_sequence_start_number = sync_result.maximum_sequence_number

            # Apply rate limiting
            time.sleep(rate_limit_delay)

    except Exception as e:
        logger.error(f"Error during {entity_type} sync: {str(e)}", exc_info=True)
        return EntitySyncResult(
            entity_type=entity_type,
            start_sequence_number=start_seq_number,
            end_sequence_number=next_sequence_start_number,
            entities_processed=entities_processed,
            success=False,
            error=str(e),
        )

    logger.info(
        f"Done syncing {entity_type}. "
        f"Processed {entities_processed} entities from {start_seq_number} to {next_sequence_start_number}"
    )

    return EntitySyncResult(
        entity_type=entity_type,
        start_sequence_number=start_seq_number,
        end_sequence_number=next_sequence_start_number,
        entities_processed=entities_processed,
        success=True,
    )
