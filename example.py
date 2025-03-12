import logging
from pprint import pprint

from floriday_supplier_client import TradeItemsApi
from floriday_supplier_client.api_factory import ApiFactory
from floriday_supplier_client.rest import ApiException
from floriday_supplier_client.sync import sync_entities

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
# Set specific logger levels if needed
# logging.getLogger("floriday_supplier_client.sync").setLevel(logging.DEBUG)


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


def sync_trade_items(start_seq_number=None, limit_result=50):
    """Sync trade items using our new sync_entities function."""
    factory = ApiFactory()
    client = factory.get_api_client()
    api_instance = TradeItemsApi(client)

    def persist_item(item):
        """Simple persistence function that just prints the item name."""
        print(f"Would persist trade item: {item.trade_item_id} - {item.trade_item_name}")
        return item.trade_item_id

    print("\n=== Syncing trade items ===\n")
    result = sync_entities(
        entity_type="trade_items",
        get_by_sequence=api_instance.get_trade_items_by_sequence_number,
        persist_entity=persist_item,
        start_seq_number=start_seq_number,
    )
    
    print("\n=== Sync result ===\n")
    pprint(result)


if __name__ == "__main__":
    # Run original examples
    print_original_examples()
    
    # Run sync example
    sync_trade_items(start_seq_number=0, limit_result=10)
