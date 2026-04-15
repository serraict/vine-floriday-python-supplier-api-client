# floriday_supplier_client.MediaApi

All URIs are relative to *https://api.staging.floriday.io/suppliers-api-2025v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_image**](MediaApi.md#add_image) | **POST** /media | catalog:write - rate limit: 2.0 per second - burst limit: 200 - Uploads an image.
[**get_beeldbank_id_from_image**](MediaApi.md#get_beeldbank_id_from_image) | **GET** /media/{imageId}/beeldbank | Retrieve the beeldbankId referring to the image.
[**get_image_from_beeldbank_id**](MediaApi.md#get_image_from_beeldbank_id) | **GET** /media/beeldbank/{beeldbankId} | Retrieve the imageId referring to the beeldbank image.

# **add_image**
> MediaReference add_image(image)

catalog:write - rate limit: 2.0 per second - burst limit: 200 - Uploads an image.

Successfully posted images can be accessed with the url: https://image.floriday.io/{mediaId}

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
api_instance = floriday_supplier_client.MediaApi(floriday_supplier_client.ApiClient(configuration))
image = 'image_example' # str | 

try:
    # catalog:write - rate limit: 2.0 per second - burst limit: 200 - Uploads an image.
    api_response = api_instance.add_image(image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->add_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **str**|  | 

### Return type

[**MediaReference**](MediaReference.md)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beeldbank_id_from_image**
> ImageBeeldbank get_beeldbank_id_from_image(image_id)

Retrieve the beeldbankId referring to the image.

Creates and returns a beeldbankId referring to the image and make the beeldbank image available the url: https://image.floriday.io/beeldbank/{beeldbankId}. Each unique imageId will have their own referred unique beeldbankId.

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
api_instance = floriday_supplier_client.MediaApi(floriday_supplier_client.ApiClient(configuration))
image_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve the beeldbankId referring to the image.
    api_response = api_instance.get_beeldbank_id_from_image(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_beeldbank_id_from_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | [**str**](.md)|  | 

### Return type

[**ImageBeeldbank**](ImageBeeldbank.md)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_from_beeldbank_id**
> ImageBeeldbank get_image_from_beeldbank_id(beeldbank_id)

Retrieve the imageId referring to the beeldbank image.

Returns the imageId referring to the beeldbankId. In case the beeldbank image was not uploaded via Floriday a copy of the beeldbank image will be created, retrieved images can be accessed with the url: https://image.floriday.io/{imageId}

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
api_instance = floriday_supplier_client.MediaApi(floriday_supplier_client.ApiClient(configuration))
beeldbank_id = 'beeldbank_id_example' # str | 

try:
    # Retrieve the imageId referring to the beeldbank image.
    api_response = api_instance.get_image_from_beeldbank_id(beeldbank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_image_from_beeldbank_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beeldbank_id** | **str**|  | 

### Return type

[**ImageBeeldbank**](ImageBeeldbank.md)

### Authorization

[JWT Token](../README.md#JWT Token), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

