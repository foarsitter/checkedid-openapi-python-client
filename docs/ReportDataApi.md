# checkedid.ReportDataApi

All URIs are relative to *https://api.checkedid.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**report_data_get_report_data_v2**](ReportDataApi.md#report_data_get_report_data_v2) | **GET** /reportdata/{dossierNumber}/{scope} | Get report details based on dossier number and scope
[**report_data_get_report_data_v2_pdf**](ReportDataApi.md#report_data_get_report_data_v2_pdf) | **GET** /report/{dossierNumber} | Get report pdf based on dossier number


# **report_data_get_report_data_v2**
> ReportDataV3 report_data_get_report_data_v2(dossier_number, scope, authorization)

Get report details based on dossier number and scope

This API retrieves data from verification reports previously received by CheckedID customers. These – personal – data can thus be imported in customer’s own environment.  <br /> The API allows for one-by-one importing of data only, in order to facilitate that customer has explicitly ensured the data is appropriate for further processing.  <br /> Note that reports are accessible for a maximum of seven days after they’re created. After that period their data can no longer be retrieved.  <br /><br /> DossierNumber is string known from the CheckedID report received.  <br /> Scope is string with possible values ‘10’, ‘11’, ‘12’, ‘13’.

### Example


```python
import time
import checkedid
from checkedid.api import report_data_api
from checkedid.model.report_data_v3 import ReportDataV3
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_data_api.ReportDataApi(api_client)
    dossier_number = "dossierNumber_example" # str | 
    scope = "scope_example" # str | 
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get report details based on dossier number and scope
        api_response = api_instance.report_data_get_report_data_v2(dossier_number, scope, authorization)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling ReportDataApi->report_data_get_report_data_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dossier_number** | **str**|  |
 **scope** | **str**|  |
 **authorization** | **str**|  |

### Return type

[**ReportDataV3**](ReportDataV3.md)

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

# **report_data_get_report_data_v2_pdf**
> ReportResponse report_data_get_report_data_v2_pdf(dossier_number, authorization)

Get report pdf based on dossier number

This API retrieves data from verification reports previously received by CheckedID customers.   <br /> Note that reports are accessible for a maximum of seven days after they’re created. After that period their data can no longer be retrieved.  <br /><br /> DossierNumber is string known from the CheckedID report received.

### Example


```python
import time
import checkedid
from checkedid.api import report_data_api
from checkedid.model.report_response import ReportResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = report_data_api.ReportDataApi(api_client)
    dossier_number = "dossierNumber_example" # str | 
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get report pdf based on dossier number
        api_response = api_instance.report_data_get_report_data_v2_pdf(dossier_number, authorization)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling ReportDataApi->report_data_get_report_data_v2_pdf: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dossier_number** | **str**|  |
 **authorization** | **str**|  |

### Return type

[**ReportResponse**](ReportResponse.md)

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

