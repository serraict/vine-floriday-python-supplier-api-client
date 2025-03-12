# coding: utf-8

"""
Tests for the entity_sync module.
"""

import pytest
from unittest.mock import Mock, patch

from floriday_supplier_client.sync.entity_sync import sync_entities


class MockEntity:
    """Mock entity for testing."""
    
    def __init__(self, id, sequence_number):
        self.id = id
        self.sequence_number = sequence_number


class MockSyncResult:
    """Mock SyncResult for testing."""
    
    def __init__(self, maximum_sequence_number, results):
        self._maximum_sequence_number = maximum_sequence_number
        self._results = results
    
    @property
    def maximum_sequence_number(self):
        return self._maximum_sequence_number
    
    @property
    def results(self):
        return self._results


@patch('time.sleep')  # Mock sleep to speed up tests
def test_sync_entities_basic(mock_sleep):
    """Test basic functionality of sync_entities."""
    # Setup test data
    entity_type = "test_entity"
    
    # Create mock entities with sequence numbers
    entities_batch1 = [
        MockEntity(f"id_{i}", i) for i in range(1, 6)
    ]
    entities_batch2 = [
        MockEntity(f"id_{i}", i) for i in range(6, 11)
    ]
    
    # Create mock sync results
    result1 = MockSyncResult(5, entities_batch1)
    result2 = MockSyncResult(10, entities_batch2)
    # Final result with no new entities and same max sequence number to signal end of sync
    result3 = MockSyncResult(10, [])
    
    # Mock get_by_sequence function
    mock_get_by_sequence = Mock()
    mock_get_by_sequence.side_effect = [result1, result2, result3]
    
    # Mock persist_entity function
    mock_persist_entity = Mock()
    mock_persist_entity.side_effect = lambda entity: entity.id
    
    # Call sync_entities
    result = sync_entities(
        entity_type=entity_type,
        get_by_sequence=mock_get_by_sequence,
        persist_entity=mock_persist_entity,
        start_seq_number=0
    )
    
    # Verify results
    assert result['entity_type'] == entity_type
    assert result['start_sequence_number'] == 0
    assert result['end_sequence_number'] == 10
    assert result['entities_processed'] == 10
    assert result['success'] is True
    
    # Verify mock calls
    assert mock_get_by_sequence.call_count == 3
    mock_get_by_sequence.assert_any_call(sequence_number=0, limit_result=50)
    mock_get_by_sequence.assert_any_call(sequence_number=5, limit_result=50)
    mock_get_by_sequence.assert_any_call(sequence_number=10, limit_result=50)
    
    assert mock_persist_entity.call_count == 10
    for entity in entities_batch1 + entities_batch2:
        mock_persist_entity.assert_any_call(entity)
    
    # Verify sleep was called for rate limiting
    mock_sleep.assert_called_with(0.5)


def test_sync_entities_no_persistence():
    """Test sync_entities without persistence."""
    # Setup test data
    entity_type = "test_entity"
    
    # Create mock entities with sequence numbers
    entities = [MockEntity(f"id_{i}", i) for i in range(1, 6)]
    
    # Create mock sync result
    result = MockSyncResult(5, entities)
    
    # Mock get_by_sequence function
    mock_get_by_sequence = Mock()
    mock_get_by_sequence.return_value = result
    
    # Call sync_entities without persist_entity
    with patch('time.sleep'):  # Mock sleep to speed up tests
        sync_result = sync_entities(
            entity_type=entity_type,
            get_by_sequence=mock_get_by_sequence,
            start_seq_number=0
        )
    
    # Verify results
    assert sync_result['entities_processed'] == 5
    assert sync_result['success'] is True


def test_sync_entities_with_get_max_sequence_number():
    """Test sync_entities with get_max_sequence_number."""
    # Setup test data
    entity_type = "test_entity"
    
    # Create mock entities with sequence numbers
    entities = [MockEntity(f"id_{i}", i) for i in range(101, 106)]
    
    # Create mock sync result
    result = MockSyncResult(105, entities)
    
    # Mock get_by_sequence function
    mock_get_by_sequence = Mock()
    mock_get_by_sequence.return_value = result
    
    # Mock get_max_sequence_number function
    mock_get_max_sequence_number = Mock()
    mock_get_max_sequence_number.return_value = 100
    
    # Call sync_entities with get_max_sequence_number
    with patch('time.sleep'):  # Mock sleep to speed up tests
        sync_result = sync_entities(
            entity_type=entity_type,
            get_by_sequence=mock_get_by_sequence,
            get_max_sequence_number=mock_get_max_sequence_number
        )
    
    # Verify results
    assert sync_result['start_sequence_number'] == 100
    assert sync_result['entities_processed'] == 5
    assert sync_result['success'] is True
    
    # Verify get_max_sequence_number was called
    mock_get_max_sequence_number.assert_called_once_with(entity_type)


def test_sync_entities_error_handling():
    """Test sync_entities error handling."""
    # Setup test data
    entity_type = "test_entity"
    
    # Mock get_by_sequence function that raises an exception
    mock_get_by_sequence = Mock()
    mock_get_by_sequence.side_effect = Exception("Test error")
    
    # Call sync_entities
    with patch('time.sleep'):  # Mock sleep to speed up tests
        result = sync_entities(
            entity_type=entity_type,
            get_by_sequence=mock_get_by_sequence,
            start_seq_number=0
        )
    
    # Verify results
    assert result['entity_type'] == entity_type
    assert result['start_sequence_number'] == 0
    assert result['entities_processed'] == 0
    assert result['success'] is False
    assert result['error'] == "Test error"


def test_sync_entities_missing_parameters():
    """Test sync_entities with missing parameters."""
    # Setup test data
    entity_type = "test_entity"
    mock_get_by_sequence = Mock()
    
    # Call sync_entities without start_seq_number or get_max_sequence_number
    with pytest.raises(ValueError) as excinfo:
        sync_entities(
            entity_type=entity_type,
            get_by_sequence=mock_get_by_sequence
        )
    
    # Verify error message
    assert "Either start_seq_number or get_max_sequence_number must be provided" in str(excinfo.value)
