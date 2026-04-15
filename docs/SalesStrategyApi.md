# floriday_supplier_client.SalesStrategyApi

All URIs are relative to *https://api.staging.floriday.io/suppliers-api-2025v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_sales_strategy**](SalesStrategyApi.md#add_sales_strategy) | **POST** /sales-strategies | clock-supply:write - Creates a new sales strategy.
[**delete_sales_strategy**](SalesStrategyApi.md#delete_sales_strategy) | **DELETE** /sales-strategies/{salesStrategyId} | clock-supply:write - Delete a sales strategy
[**get_sales_strategies_by_sequence_number**](SalesStrategyApi.md#get_sales_strategies_by_sequence_number) | **GET** /sales-strategies/sync/{sequenceNumber} | clock-supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 sales strategies starting from a specified sequence number.
[**get_sales_strategies_max_sequence_number**](SalesStrategyApi.md#get_sales_strategies_max_sequence_number) | **GET** /sales-strategies/sync/max-sequence-number | clock-supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns the maximum sequence number found in specified sequence number.
[**set_sales_strategy_presales_prices**](SalesStrategyApi.md#set_sales_strategy_presales_prices) | **PATCH** /sales-strategies/{salesStrategyId}/presales-prices | clock-supply:write - Edits the presales prices of a sales strategy.
[**set_sales_strategy_quantities**](SalesStrategyApi.md#set_sales_strategy_quantities) | **PATCH** /sales-strategies/{salesStrategyId}/quantities | clock-supply:write - Edits the quantities of a sales strategy.

# **add_sales_strategy**
> add_sales_strategy(body)

clock-supply:write - Creates a new sales strategy.

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
api_instance = floriday_supplier_client.SalesStrategyApi(floriday_supplier_client.ApiClient(configuration))
body = floriday_supplier_client.AddSalesStrategy() # AddSalesStrategy | 

try:
    # clock-supply:write - Creates a new sales strategy.
    api_instance.add_sales_strategy(body)
except ApiException as e:
    print("Exception when calling SalesStrategyApi->add_sales_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddSalesStrategy**](AddSalesStrategy.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sales_strategy**
> delete_sales_strategy(sales_strategy_id)

clock-supply:write - Delete a sales strategy

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
api_instance = floriday_supplier_client.SalesStrategyApi(floriday_supplier_client.ApiClient(configuration))
sales_strategy_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # clock-supply:write - Delete a sales strategy
    api_instance.delete_sales_strategy(sales_strategy_id)
except ApiException as e:
    print("Exception when calling SalesStrategyApi->delete_sales_strategy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_strategy_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_strategies_by_sequence_number**
> SyncResultOfSalesStrategy get_sales_strategies_by_sequence_number(sequence_number, limit_result=limit_result)

clock-supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 sales strategies starting from a specified sequence number.

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
api_instance = floriday_supplier_client.SalesStrategyApi(floriday_supplier_client.ApiClient(configuration))
sequence_number = 789 # int | 
limit_result = 1000 # int |  (optional) (default to 1000)

try:
    # clock-supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 sales strategies starting from a specified sequence number.
    api_response = api_instance.get_sales_strategies_by_sequence_number(sequence_number, limit_result=limit_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesStrategyApi->get_sales_strategies_by_sequence_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_number** | **int**|  | 
 **limit_result** | **int**|  | [optional] [default to 1000]

### Return type

[**SyncResultOfSalesStrategy**](SyncResultOfSalesStrategy.md)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_strategies_max_sequence_number**
> int get_sales_strategies_max_sequence_number()

clock-supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns the maximum sequence number found in specified sequence number.

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
api_instance = floriday_supplier_client.SalesStrategyApi(floriday_supplier_client.ApiClient(configuration))

try:
    # clock-supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns the maximum sequence number found in specified sequence number.
    api_response = api_instance.get_sales_strategies_max_sequence_number()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesStrategyApi->get_sales_strategies_max_sequence_number: %s\n" % e)
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

# **set_sales_strategy_presales_prices**
> set_sales_strategy_presales_prices(body, sales_strategy_id)

clock-supply:write - Edits the presales prices of a sales strategy.

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
api_instance = floriday_supplier_client.SalesStrategyApi(floriday_supplier_client.ApiClient(configuration))
body = floriday_supplier_client.SetSalesStrategyPresalesPrices() # SetSalesStrategyPresalesPrices | 
sales_strategy_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # clock-supply:write - Edits the presales prices of a sales strategy.
    api_instance.set_sales_strategy_presales_prices(body, sales_strategy_id)
except ApiException as e:
    print("Exception when calling SalesStrategyApi->set_sales_strategy_presales_prices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetSalesStrategyPresalesPrices**](SetSalesStrategyPresalesPrices.md)|  | 
 **sales_strategy_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sales_strategy_quantities**
> set_sales_strategy_quantities(body, sales_strategy_id)

clock-supply:write - Edits the quantities of a sales strategy.

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
api_instance = floriday_supplier_client.SalesStrategyApi(floriday_supplier_client.ApiClient(configuration))
body = floriday_supplier_client.SetSalesStrategyQuantities() # SetSalesStrategyQuantities | 
sales_strategy_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # clock-supply:write - Edits the quantities of a sales strategy.
    api_instance.set_sales_strategy_quantities(body, sales_strategy_id)
except ApiException as e:
    print("Exception when calling SalesStrategyApi->set_sales_strategy_quantities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetSalesStrategyQuantities**](SetSalesStrategyQuantities.md)|  | 
 **sales_strategy_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

