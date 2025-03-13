import logging
from pprint import pprint

from floriday_supplier_client import TradeItemsApi
from floriday_supplier_client.api_factory import ApiFactory
from floriday_supplier_client.rest import ApiException
from floriday_supplier_client.sync import sync_entities

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
# Set specific logger levels if needed
# logging.getLogger("floriday_supplier_client.sync").setLevel(logging.DEBUG)


# ============================================================================
# ORIGINAL EXAMPLES
# ============================================================================


def print_original_examples():
    """Run the original examples to verify connection to the staging server."""
    factory = ApiFactory()
    client = factory.get_api_client()
    api_instance = TradeItemsApi(client)

    try:
        print("\n=== Get trade items by id ===\n")
        api_response = api_instance.get_trade_items_summary(
            trade_item_ids=["1987a15c-2c28-4ba6-89a1-3780e585b42c"]
        )
        pprint(api_response)

        print("\n=== Get trade items by supplier organization id ===\n")
        api_response = api_instance.get_trade_items_summary(
            supplier_organization_id="64a03e85-7792-3ce9-b5be-70b5ee7fa96c"
        )
        pprint(api_response)

    except ApiException as e:
        print(
            "Exception when calling AdditionalServicesApi->get_additional_service_by_id: %s\n"
            % e
        )


# ============================================================================
# SYNC EXAMPLES
# ============================================================================


def example_1_basic_trade_items_sync():
    """
    Example 1: Basic synchronization of trade items.

    This example demonstrates the simplest way to use sync_entities to synchronize
    trade items from the Floriday API. It shows:

    1. How to initialize the API client
    2. How to create a simple persistence function
    3. How to call sync_entities with basic parameters
    4. How to handle the result
    """
    print("\n=== Example 1: Basic Trade Items Sync ===\n")

    # Step 1: Initialize API client
    factory = ApiFactory()
    client = factory.get_api_client()
    api_instance = TradeItemsApi(client)

    # Step 2: Define a persistence function
    # This function will be called for each entity retrieved
    def persist_item(item):
        """
        Simple persistence function that just prints the item details.

        In a real application, this would save the item to a database.
        """
        print(
            f"Processing trade item: {item.trade_item_id} - {getattr(item, 'trade_item_name', 'N/A')}"
        )
        # Return a unique identifier for the persisted entity
        return item.trade_item_id

    print("Starting synchronization of trade items...")

    # Step 3: Call sync_entities with basic parameters
    result = sync_entities(
        # Type of entity being synchronized (for logging and tracking)
        entity_type="trade_items",
        # Function that retrieves entities by sequence number
        # This should be a method from the appropriate API class
        get_by_sequence=api_instance.get_trade_items_by_sequence_number,
        # Function to persist each entity (optional)
        # If omitted, entities will be retrieved but not persisted
        persist_entity=persist_item,
        # Starting sequence number (0 to start from the beginning)
        start_seq_number=0,
    )

    # Step 4: Handle the result
    print("\n=== Sync completed ===\n")
    print(f"Started at sequence: {result['start_sequence_number']}")
    print(f"Ended at sequence: {result['end_sequence_number']}")
    print(f"Processed {result['entities_processed']} trade items")
    print(f"Success: {result['success']}")

    # If the sync failed, the result will include an error message
    if not result["success"]:
        print(f"Error: {result['error']}")


if __name__ == "__main__":
    # Run the basic trade items sync example
    example_1_basic_trade_items_sync()

    # Original examples (uncomment to run)
    # print_original_examples()
