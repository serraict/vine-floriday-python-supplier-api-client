# AddCustomerOfferLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_offer_line_id** | **str** |  | 
**trade_item_id** | **str** |  | 
**despatch_warehouse_id** | **str** |  | 
**number_of_pieces** | **int** |  | 
**price_per_piece** | [**Price**](Price.md) |  | 
**volume_prices** | [**list[AddVolumePrice]**](AddVolumePrice.md) |  | [optional] 
**sales_unit** | [**SalesUnit**](SalesUnit.md) |  | 
**order_period** | [**TradePeriod**](TradePeriod.md) |  | 
**delivery_period** | [**TradePeriod**](TradePeriod.md) |  | 
**uses_catalog_availability** | **bool** | Determines if the offer line number of pieces is limited or if the trade item availability is used. | 
**batch_id** | **str** |  | [optional] 
**packing_configuration** | [**PackingConfigurationBase**](PackingConfigurationBase.md) |  | [optional] 
**included_services** | [**list[CommercialService]**](CommercialService.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

