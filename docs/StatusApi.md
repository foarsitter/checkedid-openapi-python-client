# checkedid.StatusApi

All URIs are relative to *https://api.checkedid.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get_result_callback_status**](StatusApi.md#status_get_result_callback_status) | **GET** /result/status/{invitationCode} | Get result callback based on Invitation Code
[**status_get_status_v2**](StatusApi.md#status_get_status_v2) | **GET** /admin/health/status | API Status


# **status_get_result_callback_status**
> ResultCallbackStatus status_get_result_callback_status(invitation_code, authorization)

Get result callback based on Invitation Code

This API retrieves result callback details of the report based on Invitation Code

### Example


```python
import time
import checkedid
from checkedid.api import status_api
from checkedid.model.result_callback_status import ResultCallbackStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)
    invitation_code = "invitationCode_example" # str | 
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get result callback based on Invitation Code
        api_response = api_instance.status_get_result_callback_status(invitation_code, authorization)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling StatusApi->status_get_result_callback_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_code** | **str**|  |
 **authorization** | **str**|  |

### Return type

[**ResultCallbackStatus**](ResultCallbackStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get_status_v2**
> bool, date, datetime, dict, float, int, list, str, none_type status_get_status_v2(authorization)

API Status

This is used to check the status of the API

### Example


```python
import time
import checkedid
from checkedid.api import status_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # API Status
        api_response = api_instance.status_get_status_v2(authorization)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling StatusApi->status_get_status_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

