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


def sync_trade_items(start_seq_number=None, limit_result=50, batch_size=None, rate_limit=None):
    """Sync trade items using our new sync_entities function.
    
    Args:
        start_seq_number: Optional starting sequence number.
        limit_result: Limit for the API call (not used directly in sync_entities).
        batch_size: Optional batch size for each API call. Default is 50.
        rate_limit: Optional rate limit delay in seconds. Default is 0.5s.
    """
    factory = ApiFactory()
    client = factory.get_api_client()
    api_instance = TradeItemsApi(client)

    def persist_item(item):
        """Simple persistence function that just prints the item name."""
        print(f"Would persist trade item: {item.trade_item_id} - {item.trade_item_name}")
        return item.trade_item_id

    print("\n=== Syncing trade items ===\n")
    
    # Build sync parameters
    sync_params = {
        "entity_type": "trade_items",
        "get_by_sequence": api_instance.get_trade_items_by_sequence_number,
        "persist_entity": persist_item,
        "start_seq_number": start_seq_number,
    }
    
    # Add optional configuration parameters if provided
    if batch_size is not None:
        sync_params["batch_size"] = batch_size
    if rate_limit is not None:
        sync_params["rate_limit_delay"] = rate_limit
    
    # Call sync_entities with parameters
    result = sync_entities(**sync_params)
    
    print("\n=== Sync result ===\n")
    pprint(result)


if __name__ == "__main__":
    # Run original examples
    print_original_examples()
    
    # Run sync example with default configuration
    sync_trade_items(start_seq_number=0, limit_result=10)
    
    # Uncomment to run with custom configuration
    # sync_trade_items(
    #     start_seq_number=0,
    #     limit_result=10,
    #     batch_size=25,  # Smaller batch size
    #     rate_limit=1.0  # Slower rate limit (1 second between requests)
    # )
