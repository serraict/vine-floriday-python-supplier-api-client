# floriday_supplier_client.AdminApi

All URIs are relative to *https://api.staging.floriday.io/suppliers-api-2025v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_cache_entries_of_sync_endpoint**](AdminApi.md#clear_cache_entries_of_sync_endpoint) | **DELETE** /sync-endpoint-cache/{modelName} | Clear the sequences for all organizations of a specific endpoint in the cache.
[**get_sync_endpoint_cache_max_sequences**](AdminApi.md#get_sync_endpoint_cache_max_sequences) | **GET** /sync-endpoint-cache/max-sequences | Returns the max sequences according to the sync endpoint cache.
[**get_sync_endpoint_cache_sequences_of_endpoint**](AdminApi.md#get_sync_endpoint_cache_sequences_of_endpoint) | **GET** /sync-endpoint-cache/{modelName} | Returns the sequences for all organizations of a specific endpoint in the cache.

# **clear_cache_entries_of_sync_endpoint**
> clear_cache_entries_of_sync_endpoint(model_name)

Clear the sequences for all organizations of a specific endpoint in the cache.

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
api_instance = floriday_supplier_client.AdminApi(floriday_supplier_client.ApiClient(configuration))
model_name = 'model_name_example' # str | 

try:
    # Clear the sequences for all organizations of a specific endpoint in the cache.
    api_instance.clear_cache_entries_of_sync_endpoint(model_name)
except ApiException as e:
    print("Exception when calling AdminApi->clear_cache_entries_of_sync_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_endpoint_cache_max_sequences**
> list[CacheNameAndMaxSequence] get_sync_endpoint_cache_max_sequences()

Returns the max sequences according to the sync endpoint cache.

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
api_instance = floriday_supplier_client.AdminApi(floriday_supplier_client.ApiClient(configuration))

try:
    # Returns the max sequences according to the sync endpoint cache.
    api_response = api_instance.get_sync_endpoint_cache_max_sequences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_sync_endpoint_cache_max_sequences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CacheNameAndMaxSequence]**](CacheNameAndMaxSequence.md)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_endpoint_cache_sequences_of_endpoint**
> dict(str, int) get_sync_endpoint_cache_sequences_of_endpoint(model_name)

Returns the sequences for all organizations of a specific endpoint in the cache.

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
api_instance = floriday_supplier_client.AdminApi(floriday_supplier_client.ApiClient(configuration))
model_name = 'model_name_example' # str | 

try:
    # Returns the sequences for all organizations of a specific endpoint in the cache.
    api_response = api_instance.get_sync_endpoint_cache_sequences_of_endpoint(model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_sync_endpoint_cache_sequences_of_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | 

### Return type

**dict(str, int)**

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

