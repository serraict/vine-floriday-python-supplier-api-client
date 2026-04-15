# SalesOrderCorrectionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sales_order_correction_request_id** | **str** |  | 
**sales_order_id** | **str** |  | 
**status** | [**CorrectionRequestStatus**](CorrectionRequestStatus.md) |  | 
**is_sales_order_created_by_supplier** | **bool** |  | 
**initiated_by** | [**OrganizationType**](OrganizationType.md) |  | 
**expires_at_date_time** | **datetime** |  | 
**creation_date_time** | **datetime** |  | 
**last_modified_date_time** | **datetime** |  | 
**sequence_number** | **int** |  | 
**customer_organization_id** | **str** |  | 
**price_per_piece** | [**Price**](Price.md) |  | 
**package** | [**Package**](Package.md) |  | 
**number_of_pieces** | **int** |  | 
**pieces_per_package** | **int** |  | 
**incoterm** | [**Incoterm**](Incoterm.md) |  | 
**should_return_packages** | **bool** |  | 
**reason** | **str** |  | 
**is_cancel_request** | **bool** |  | 
**sales_order_version_after_correction** | **int** |  | 
**created_by_user_name** | **str** | Name of the contact person responsible for the sales order correction request | 
**stock_application** | [**SalesOrderCorrectionStockApplication**](SalesOrderCorrectionStockApplication.md) |  | 
**latest_delivery_date_time** | **datetime** |  | 
**delivery_location** | [**CorrectionDeliveryLocation**](CorrectionDeliveryLocation.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

