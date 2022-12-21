# checkedid.AuthenticationApi

All URIs are relative to *https://api.checkedid.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_token_post**](AuthenticationApi.md#oauth_token_post) | **POST** /oauth/token | OAuth process to generate the authentication token


# **oauth_token_post**
> bool, date, datetime, dict, float, int, list, str, none_type oauth_token_post(grant_type, username, password)

OAuth process to generate the authentication token

Provide the username, password and grant_type as password and request for token. On successful authentication, token with validity will be returned

### Example


```python
import time
import checkedid
from checkedid.api import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    grant_type = "grant_type_example" # str | Should set as 'password'
    username = "username_example" # str | Username shared for the API access
    password = "password_example" # str | Password shared for the API access

    # example passing only required values which don't have defaults set
    try:
        # OAuth process to generate the authentication token
        api_response = api_instance.oauth_token_post(grant_type, username, password)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling AuthenticationApi->oauth_token_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Should set as &#39;password&#39; |
 **username** | **str**| Username shared for the API access |
 **password** | **str**| Password shared for the API access |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*, access_token, token_type, expires_in, refresh_token


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

