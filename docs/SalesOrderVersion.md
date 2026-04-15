# SalesOrderVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_order_id** | **str** |  | 
**sales_channel_order_id** | **str** |  | 
**customer_order_id** | **str** |  | 
**supplier_organization_id** | **str** |  | 
**customer_organization_id** | **str** |  | 
**supply_line_id** | **str** |  | 
**trade_item_id** | **str** |  | 
**sales_channel** | [**SalesChannel**](SalesChannel.md) |  | 
**number_of_pieces** | **int** |  | 
**trade_instrument** | [**TradeInstrument**](TradeInstrument.md) |  | 
**packing_configuration** | [**SalesOrderPackingConfiguration**](SalesOrderPackingConfiguration.md) |  | 
**order_date_time** | **datetime** |  | 
**price_per_piece** | [**Price**](Price.md) |  | 
**delivery** | [**SalesOrderDelivery**](SalesOrderDelivery.md) |  | 
**additional_services** | [**list[OrderedAdditionalService]**](OrderedAdditionalService.md) |  | 
**cancellation_deadline** | **datetime** |  | 
**status** | [**SalesOrderStatus**](SalesOrderStatus.md) |  | 
**credit_claim_status** | [**CreditClaimStatus**](CreditClaimStatus.md) |  | 
**credit_claim_expiration_date_time** | **datetime** |  | 
**sequence_number** | **int** |  | 
**trade_item_version** | **int** |  | 
**version** | **int** |  | 
**contract_id** | **str** |  | 
**blanket_order_line_id** | **str** |  | 
**calculated_fields** | [**SalesOrderCalculatedFields**](SalesOrderCalculatedFields.md) |  | 
**payment_provider** | [**PaymentProvider**](PaymentProvider.md) |  | 
**delivery_remarks** | **str** |  | 
**delivery_price_per_piece** | [**Price**](Price.md) |  | 
**despatch_warehouse_id** | **str** |  | 
**creation_date_time** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**created_by_supplier** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

