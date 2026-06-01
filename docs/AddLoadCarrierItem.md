# AddLoadCarrierItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_request_id** | **str** |  | 
**load_carrier_item_id** | **str** | Identifier for the item on the loadcarrier. Will be generated if not given. Required after 2026v1. | [optional] 
**number_of_packages** | **int** |  | 
**service_code** | **int** |  | [optional] 
**packing_agent_organization_id** | **str** |  | [optional] 
**sort_index** | **int** | The index related to the item&#x27;s position on the loadcarrier | [optional] 
**delivery_remarks** | **str** | The delivery remarks will be printed on the connect EAB document. A &#x60;NULL&#x60; value indicates the use of the default delivery remarks found in the FulfillmentRequest or will ignore the value in an update. | [optional] 
**commercial_invoice_reference** | **str** | Own reference reflected on the invoice. | [optional] 
**alternative_display_name** | **str** | Alternative text to display on the logistic label instead of the trade item name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

