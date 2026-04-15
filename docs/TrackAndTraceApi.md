# floriday_supplier_client.TrackAndTraceApi

All URIs are relative to *https://api.staging.floriday.io/suppliers-api-2025v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_track_and_trace_scan**](TrackAndTraceApi.md#add_track_and_trace_scan) | **POST** /track-and-trace/scans | fulfillment:write - Create a track and trace scan
[**get_track_and_trace_scans_by_sequence_number**](TrackAndTraceApi.md#get_track_and_trace_scans_by_sequence_number) | **GET** /track-and-trace/scans/sync/{sequenceNumber} | fulfillment:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 track and trace scans starting from a specified sequence number.
[**get_track_and_trace_scans_max_sequence**](TrackAndTraceApi.md#get_track_and_trace_scans_max_sequence) | **GET** /track-and-trace/scans/current-max-sequence | fulfillment:read - Returns the maximum sequence number found in track and trace scans.

# **add_track_and_trace_scan**
> add_track_and_trace_scan(body)

fulfillment:write - Create a track and trace scan

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
api_instance = floriday_supplier_client.TrackAndTraceApi(floriday_supplier_client.ApiClient(configuration))
body = floriday_supplier_client.AddTrackAndTraceScan() # AddTrackAndTraceScan | 

try:
    # fulfillment:write - Create a track and trace scan
    api_instance.add_track_and_trace_scan(body)
except ApiException as e:
    print("Exception when calling TrackAndTraceApi->add_track_and_trace_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddTrackAndTraceScan**](AddTrackAndTraceScan.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_track_and_trace_scans_by_sequence_number**
> SyncResultOfTrackAndTraceScan get_track_and_trace_scans_by_sequence_number(sequence_number, limit_result=limit_result)

fulfillment:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 track and trace scans starting from a specified sequence number.

**Synchronization endpoint** Fetches the succeeding modified records based on `Limit` and the given `SequenceNumber`.  **Note** Your data is up to date when your given `SequenceNumber` is equal to the received `MaximumSequenceNumber`.

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
api_instance = floriday_supplier_client.TrackAndTraceApi(floriday_supplier_client.ApiClient(configuration))
sequence_number = 789 # int | 
limit_result = 1000 # int |  (optional) (default to 1000)

try:
    # fulfillment:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 track and trace scans starting from a specified sequence number.
    api_response = api_instance.get_track_and_trace_scans_by_sequence_number(sequence_number, limit_result=limit_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackAndTraceApi->get_track_and_trace_scans_by_sequence_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_number** | **int**|  | 
 **limit_result** | **int**|  | [optional] [default to 1000]

### Return type

[**SyncResultOfTrackAndTraceScan**](SyncResultOfTrackAndTraceScan.md)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_track_and_trace_scans_max_sequence**
> int get_track_and_trace_scans_max_sequence()

fulfillment:read - Returns the maximum sequence number found in track and trace scans.

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
api_instance = floriday_supplier_client.TrackAndTraceApi(floriday_supplier_client.ApiClient(configuration))

try:
    # fulfillment:read - Returns the maximum sequence number found in track and trace scans.
    api_response = api_instance.get_track_and_trace_scans_max_sequence()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackAndTraceApi->get_track_and_trace_scans_max_sequence: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

