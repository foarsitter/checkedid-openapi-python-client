# checkedid.InvitationApi

All URIs are relative to *https://api.checkedid.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invitees_create_invitations**](InvitationApi.md#invitees_create_invitations) | **POST** /invitations | Create Invitations
[**invitees_delete_invitation**](InvitationApi.md#invitees_delete_invitation) | **DELETE** /invitation/{customerCode}/{invitationCode} | Delete Invitation
[**invitees_update_invitations**](InvitationApi.md#invitees_update_invitations) | **PATCH** /invitations | Update Invitations


# **invitees_create_invitations**
> CustomerDetails invitees_create_invitations(authorization, details)

Create Invitations

This API creates Invitations for using the CheckedID app. An Invitation provides an invitee of a CheckedID registered customer access to the app for one transaction, during a limited period of time. With this API CheckedID customers can integrate the sending of Invitations in their own – e.g. CRM, HR – environment.  <br /> Place the request JSON in details, enter the token with bearer prefix in Authorization header.   <br /><br /> CustomerCode and EmployeeCode are integers as registered with CheckedID.  <br /> InviteeEmail is string used as unique identifier for Invitations.  <br /> InviteeFirstName is string to be used for personally addressing the invitee.  <br /> CustomerReference is string to be used by customers for identifying this Invitation in their own environment.  <br /> AppFlow is string with possible values ‘10’ to ‘29’.  <br /> Validity is integer indicating the number of hours the Invitation is valid after being generated.  <br /> PreferredLanguage is string with possible values \"nl\", \"en\", \"fr\", \"de\" (Used in sending invitation through email)  <br /><br /> Invitations as requested are generated with new InvitationCode and InvitedTime, and these will be provided with the response.

### Example


```python
import time
import checkedid
from checkedid.api import invitation_api
from checkedid.model.create_invitation_details import CreateInvitationDetails
from checkedid.model.customer_details import CustomerDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = invitation_api.InvitationApi(api_client)
    authorization = "Authorization_example" # str | 
    details = CreateInvitationDetails(
        customer_code=1,
        invitations=[
            CreateInvitationRequest(
                employee_code=1,
                invitee_email="invitee_email_example",
                invitee_first_name="invitee_first_name_example",
                invitee_last_name="invitee_last_name_example",
                customer_reference="customer_reference_example",
                app_flow="app_flow_example",
                validity=1,
                preferred_language="preferred_language_example",
            ),
        ],
    ) # CreateInvitationDetails | 

    # example passing only required values which don't have defaults set
    try:
        # Create Invitations
        api_response = api_instance.invitees_create_invitations(authorization, details)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling InvitationApi->invitees_create_invitations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **details** | [**CreateInvitationDetails**](CreateInvitationDetails.md)|  |

### Return type

[**CustomerDetails**](CustomerDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invitees_delete_invitation**
> bool, date, datetime, dict, float, int, list, str, none_type invitees_delete_invitation(customer_code, invitation_code, authorization)

Delete Invitation

### Example


```python
import time
import checkedid
from checkedid.api import invitation_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = invitation_api.InvitationApi(api_client)
    customer_code = 1 # int | 
    invitation_code = "invitationCode_example" # str | 
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Invitation
        api_response = api_instance.invitees_delete_invitation(customer_code, invitation_code, authorization)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling InvitationApi->invitees_delete_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_code** | **int**|  |
 **invitation_code** | **str**|  |
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

# **invitees_update_invitations**
> CustomerDetails invitees_update_invitations(authorization, details)

Update Invitations

This API creates Invitations for using the CheckedID app. An Invitation provides an invitee of a CheckedID registered customer access to the app for one transaction, during a limited period of time. With this API CheckedID customers can integrate the sending of Invitations in their own – e.g. CRM, HR – environment.  <br /> Place the request JSON in details, enter the token with bearer prefix in Authorization header.   <br /><br /> CustomerCode and EmployeeCode are integers as registered with CheckedID.  <br /> InviteeEmail is string used as unique identifier for Invitations.  <br /> InviteeFirstName is string to be used for personally addressing the invitee.  <br /> CustomerReference is string to be used by customers for identifying this Invitation in their own environment.  <br /> AppFlow is string with possible values ‘10’ to ‘29’.  <br /> Validity is integer indicating the number of hours the Invitation is valid after being generated.  <br /> PreferredLanguage is string with possible values \"nl\", \"en\", \"fr\", \"de\" (Used in sending invitation through email)  <br /><br /> Invitations as requested are generated with renewed InvitationCode and InvitedTime, and these will be provided with the response.

### Example


```python
import time
import checkedid
from checkedid.api import invitation_api
from checkedid.model.update_invitation_details import UpdateInvitationDetails
from checkedid.model.customer_details import CustomerDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = invitation_api.InvitationApi(api_client)
    authorization = "Authorization_example" # str | 
    details = UpdateInvitationDetails(
        customer_code=1,
        invitations=[
            UpdateInvitationRequest(
                invitation_code="invitation_code_example",
                invitee_first_name="invitee_first_name_example",
                invitee_last_name="invitee_last_name_example",
                customer_reference="customer_reference_example",
                app_flow="app_flow_example",
                validity=1,
                preferred_language="preferred_language_example",
            ),
        ],
    ) # UpdateInvitationDetails | 

    # example passing only required values which don't have defaults set
    try:
        # Update Invitations
        api_response = api_instance.invitees_update_invitations(authorization, details)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling InvitationApi->invitees_update_invitations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **details** | [**UpdateInvitationDetails**](UpdateInvitationDetails.md)|  |

### Return type

[**CustomerDetails**](CustomerDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

