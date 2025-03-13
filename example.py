import logging
from pprint import pprint

from floriday_supplier_client import TradeItemsApi
from floriday_supplier_client.api_factory import ApiFactory
from floriday_supplier_client.sync import sync_entities, EntitySynchronizer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def ex1_print_a_trade_item():
    factory = ApiFactory()
    client = factory.get_api_client()
    api_instance = TradeItemsApi(client)

    print("\n=== Example 1: Print a known trade item ===\n")
    api_response = api_instance.get_trade_items_summary(
        trade_item_ids=["1987a15c-2c28-4ba6-89a1-3780e585b42c"]
    )
    pprint(api_response)


def persist_item(item):
    """Example persistence function for trade items."""
    print(
        f"Processing: {item.trade_item_id} - {getattr(item, 'trade_item_name', 'N/A')}"
    )
    return item.trade_item_id


def ex2_basic_trade_items_sync():
    print("\n=== Example 2: Basic Trade Items Sync ===\n")

    factory = ApiFactory()
    client = factory.get_api_client()
    api_instance = TradeItemsApi(client)

    result = sync_entities(
        # Type of entity being synchronized (for logging and tracking)
        entity_type="trade_items",
        # Function that retrieves entities by sequence number:
        fetch_entities_callback=api_instance.get_trade_items_by_sequence_number,
        # Function to persist each entity:
        persist_entity_callback=persist_item,
        # Starting sequence number, set to 0 to start from the beginning
        start_seq_number=0,
    )

    print(result)


def ex3_context_manager_sync():
    print("\n=== Example 3: Using EntitySynchronizer with Context Manager ===\n")

    factory = ApiFactory()
    client = factory.get_api_client()
    api_instance = TradeItemsApi(client)
    with EntitySynchronizer(
        entity_type="trade_items",
        fetch_entities_callback=api_instance.get_trade_items_by_sequence_number,
        persist_entity_callback=persist_item,
        start_seq_number=0,  # Starting sequence number, set to 0 to start from the beginning
    ) as synchronizer:
        result = synchronizer.sync()
        print(result)


if __name__ == "__main__":
    ex1_print_a_trade_item()
    ex2_basic_trade_items_sync()
    ex3_context_manager_sync()
