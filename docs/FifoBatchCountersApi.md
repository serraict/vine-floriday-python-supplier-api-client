# floriday_supplier_client.FifoBatchCountersApi

All URIs are relative to *https://api.staging.floriday.io/suppliers-api-2026v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fifo_batch_counter**](FifoBatchCountersApi.md#add_fifo_batch_counter) | **POST** /fifo-batch-counters | supply:write - create a FIFO batch counter.
[**delete_fifo_batch_counter**](FifoBatchCountersApi.md#delete_fifo_batch_counter) | **DELETE** /fifo-batch-counters/{fifoBatchCounterId} | supply:write - delete a FIFO batch counter.
[**edit_fifo_batch_counter**](FifoBatchCountersApi.md#edit_fifo_batch_counter) | **PUT** /fifo-batch-counters/{fifoBatchCounterId} | supply:write - update a FIFO batch counter.

# **add_fifo_batch_counter**
> add_fifo_batch_counter(body)

supply:write - create a FIFO batch counter.

### Example
```python
from __future__ import print_function
import time
import floriday_supplier_client
from floriday_supplier_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT Token
configuration = floriday_supplier_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: X-Api-Key
configuration = floriday_supplier_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = floriday_supplier_client.FifoBatchCountersApi(floriday_supplier_client.ApiClient(configuration))
body = floriday_supplier_client.AddFifoBatchCounter() # AddFifoBatchCounter | 

try:
    # supply:write - create a FIFO batch counter.
    api_instance.add_fifo_batch_counter(body)
except ApiException as e:
    print("Exception when calling FifoBatchCountersApi->add_fifo_batch_counter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddFifoBatchCounter**](AddFifoBatchCounter.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fifo_batch_counter**
> delete_fifo_batch_counter(fifo_batch_counter_id)

supply:write - delete a FIFO batch counter.

### Example
```python
from __future__ import print_function
import time
import floriday_supplier_client
from floriday_supplier_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT Token
configuration = floriday_supplier_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: X-Api-Key
configuration = floriday_supplier_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = floriday_supplier_client.FifoBatchCountersApi(floriday_supplier_client.ApiClient(configuration))
fifo_batch_counter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # supply:write - delete a FIFO batch counter.
    api_instance.delete_fifo_batch_counter(fifo_batch_counter_id)
except ApiException as e:
    print("Exception when calling FifoBatchCountersApi->delete_fifo_batch_counter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fifo_batch_counter_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_fifo_batch_counter**
> edit_fifo_batch_counter(body, fifo_batch_counter_id)

supply:write - update a FIFO batch counter.

### Example
```python
from __future__ import print_function
import time
import floriday_supplier_client
from floriday_supplier_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: JWT Token
configuration = floriday_supplier_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: X-Api-Key
configuration = floriday_supplier_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = floriday_supplier_client.FifoBatchCountersApi(floriday_supplier_client.ApiClient(configuration))
body = floriday_supplier_client.EditFifoBatchCounter() # EditFifoBatchCounter | 
fifo_batch_counter_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # supply:write - update a FIFO batch counter.
    api_instance.edit_fifo_batch_counter(body, fifo_batch_counter_id)
except ApiException as e:
    print("Exception when calling FifoBatchCountersApi->edit_fifo_batch_counter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditFifoBatchCounter**](EditFifoBatchCounter.md)|  | 
 **fifo_batch_counter_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

