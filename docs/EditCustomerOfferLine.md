# EditCustomerOfferLine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_pieces** | **int** |  | 
**price_per_piece** | **float** |  | 
**volume_prices** | [**list[AddVolumePrice]**](AddVolumePrice.md) |  | [optional] 
**sales_unit** | [**SalesUnit**](SalesUnit.md) |  | 
**order_period** | [**TradePeriod**](TradePeriod.md) |  | 
**delivery_period** | [**TradePeriod**](TradePeriod.md) |  | 
**included_additional_service_ids** | **list[str]** |  | [optional] 
**is_available** | **bool** | Indicates if the supply line is available when it uses catalog availability, this can be manually set. If the value is null, it follows the soon te be deprecated catalog availability or it has a batch it follows. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

