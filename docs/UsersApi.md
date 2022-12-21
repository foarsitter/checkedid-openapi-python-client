# checkedid.UsersApi

All URIs are relative to *https://api.checkedid.eu*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invitees_activate_employees**](UsersApi.md#invitees_activate_employees) | **PATCH** /activateusers | Activate Users
[**invitees_create_employee**](UsersApi.md#invitees_create_employee) | **POST** /users | Create Users
[**invitees_delete_user**](UsersApi.md#invitees_delete_user) | **DELETE** /user/{customerCode}/{userCode} | Delete User
[**invitees_update_employees**](UsersApi.md#invitees_update_employees) | **PATCH** /users | Update Users


# **invitees_activate_employees**
> ActivateUsersResponse invitees_activate_employees(authorization, details)

Activate Users

This API updates Employees for using CheckedID. Employees may be users of the Customer portal and registered (or: activated) users of app.  <br /> Place the request JSON in details, enter the token with bearer prefix in Authorization header.   <br /><br /> CustomerCode is integer as registered with CheckedID.  <br /> UserCode is required.   <br />

### Example


```python
import time
import checkedid
from checkedid.api import users_api
from checkedid.model.activate_users_response import ActivateUsersResponse
from checkedid.model.activate_users import ActivateUsers
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    authorization = "Authorization_example" # str | 
    details = ActivateUsers(
        customer_code=1,
        users=[
            ActivateUserRequest(
                user_code=1,
            ),
        ],
    ) # ActivateUsers | 

    # example passing only required values which don't have defaults set
    try:
        # Activate Users
        api_response = api_instance.invitees_activate_employees(authorization, details)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling UsersApi->invitees_activate_employees: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **details** | [**ActivateUsers**](ActivateUsers.md)|  |

### Return type

[**ActivateUsersResponse**](ActivateUsersResponse.md)

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

# **invitees_create_employee**
> CreateUserDetailsResponse invitees_create_employee(authorization, details)

Create Users

This API creates Employees for using CheckedID. Employees may be users of the Customer portal and registered (or: activated) users of app.  <br /> Place the request JSON in details, enter the token with bearer prefix in Authorization header.   <br /><br /> CustomerCode is integer as registered with CheckedID.  <br /> Email is string used as unique identifier for Users.  <br /> FirstName is string to be used for personally addressing the user.  <br /> Role of the user (Admin/Basic/AppOnly)  <br /> Holder Confirmation By (App user/CheckedID Auto)  <br /> User type (Internal/External)  <br /><br /> FirstName, LastName, Role, Email, Password, StartDate and HolderConfirmationBy are required. When UserCode is sent this value needs to be unique for CustomerCode; when UserCode is not sent a 5-digit code will be generated. An ActivationCode will always be generated.  <br /><br /> Users as requested are generated with new ActivationCode, and these will be provided with the response.

### Example


```python
import time
import checkedid
from checkedid.api import users_api
from checkedid.model.create_user_details import CreateUserDetails
from checkedid.model.create_user_details_response import CreateUserDetailsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    authorization = "Authorization_example" # str | 
    details = CreateUserDetails(
        customer_code=1,
        users=[
            CreateUserRequest(
                user_code=1,
                first_name="first_name_example",
                last_name="last_name_example",
                role="role_example",
                email="email_example",
                password="password_example",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                holder_confirmation_by="holder_confirmation_by_example",
                user_type="user_type_example",
                user_reference="user_reference_example",
                report_email_address="report_email_address_example",
                notification_email_address="notification_email_address_example",
            ),
        ],
    ) # CreateUserDetails | 

    # example passing only required values which don't have defaults set
    try:
        # Create Users
        api_response = api_instance.invitees_create_employee(authorization, details)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling UsersApi->invitees_create_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **details** | [**CreateUserDetails**](CreateUserDetails.md)|  |

### Return type

[**CreateUserDetailsResponse**](CreateUserDetailsResponse.md)

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

# **invitees_delete_user**
> bool, date, datetime, dict, float, int, list, str, none_type invitees_delete_user(customer_code, user_code, authorization)

Delete User

### Example


```python
import time
import checkedid
from checkedid.api import users_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    customer_code = 1 # int | 
    user_code = 1 # int | 
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete User
        api_response = api_instance.invitees_delete_user(customer_code, user_code, authorization)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling UsersApi->invitees_delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_code** | **int**|  |
 **user_code** | **int**|  |
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

# **invitees_update_employees**
> UpdateUserDetailsResponse invitees_update_employees(authorization, details)

Update Users

This API updates Employees for using CheckedID. Employees may be users of the Customer portal and registered (or: activated) users of app.  <br /> Place the request JSON in details, enter the token with bearer prefix in Authorization header.   <br /><br /> CustomerCode is integer as registered with CheckedID.  <br /> Email is string used as unique identifier for Users.  <br /> FirstName is string to be used for personally addressing the user.  <br /> Role of the user (Admin/Basic/AppOnly)  <br /> Holder Confirmation By (App user/CheckedID Auto)  <br /> User type (Internal/External)  <br /><br />Only UserCode is required. Fields not sent will not be updated for Employee. If indicated \"true\" for all UserCodes sent ActivationCodes will be regenerated.  <br /><br /> Users as requested are generated with renewed ActivationCode, and these will be provided with the response.

### Example


```python
import time
import checkedid
from checkedid.api import users_api
from checkedid.model.update_user_details import UpdateUserDetails
from checkedid.model.update_user_details_response import UpdateUserDetailsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.checkedid.eu
# See configuration.py for a list of all supported configuration parameters.
configuration = checkedid.Configuration(
    host = "https://api.checkedid.eu"
)


# Enter a context with an instance of the API client
with checkedid.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    authorization = "Authorization_example" # str | 
    details = UpdateUserDetails(
        customer_code=1,
        users=[
            UserRequest(
                user_code=1,
                first_name="first_name_example",
                last_name="last_name_example",
                role="role_example",
                email="email_example",
                password="password_example",
                start_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                end_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                holder_confirmation_by="holder_confirmation_by_example",
                user_type="user_type_example",
                user_reference="user_reference_example",
                report_email_address="report_email_address_example",
                notification_email_address="notification_email_address_example",
            ),
        ],
    ) # UpdateUserDetails | 

    # example passing only required values which don't have defaults set
    try:
        # Update Users
        api_response = api_instance.invitees_update_employees(authorization, details)
        pprint(api_response)
    except checkedid.ApiException as e:
        print("Exception when calling UsersApi->invitees_update_employees: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **details** | [**UpdateUserDetails**](UpdateUserDetails.md)|  |

### Return type

[**UpdateUserDetailsResponse**](UpdateUserDetailsResponse.md)

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

