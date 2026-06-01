# CustomerOfferLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_offer_line_id** | **str** |  | 
**supply_request_line_id** | **str** |  | [optional] 
**number_of_pieces** | **int** |  | 
**trade_period** | [**TradePeriod**](TradePeriod.md) |  | 
**delivery_period** | [**TradePeriod**](TradePeriod.md) |  | [optional] 
**trade_item_id** | **str** |  | 
**trade_item_version** | **int** |  | [optional] 
**warehouse_id** | **str** |  | 
**price_per_piece** | [**Price**](Price.md) |  | 
**volume_prices** | [**list[VolumePrice]**](VolumePrice.md) |  | 
**sales_unit** | [**SalesUnit**](SalesUnit.md) |  | 
**uses_catalog_availability** | **bool** |  | 
**is_available** | **bool** | Indicates if the supply line is available when it uses catalog availability, this can be manually set. If the value is null, it follows the soon te be deprecated catalog availability or it has a batch it follows. | [optional] 
**included_services** | [**list[CommercialService]**](CommercialService.md) |  | 
**packing_configuration** | [**PackingConfigurationBase**](PackingConfigurationBase.md) |  | [optional] 
**counter_id** | **str** |  | [optional] 
**is_deleted** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

