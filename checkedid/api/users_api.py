"""
    CheckedID API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from checkedid.api_client import ApiClient
from checkedid.api_client import Endpoint as _Endpoint
from checkedid.model.activate_users import ActivateUsers
from checkedid.model.activate_users_response import ActivateUsersResponse
from checkedid.model.create_user_details import CreateUserDetails
from checkedid.model.create_user_details_response import \
    CreateUserDetailsResponse
from checkedid.model.update_user_details import UpdateUserDetails
from checkedid.model.update_user_details_response import \
    UpdateUserDetailsResponse
from checkedid.model_utils import (check_allowed_values,  # noqa: F401
                                   check_validations, date, datetime,
                                   file_type, none_type,
                                   validate_and_convert_types)


class UsersApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.invitees_activate_employees_endpoint = _Endpoint(
            settings={
                "response_type": (ActivateUsersResponse,),
                "auth": [],
                "endpoint_path": "/activateusers",
                "operation_id": "invitees_activate_employees",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": [
                    "authorization",
                    "details",
                ],
                "required": [
                    "authorization",
                    "details",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "authorization": (str,),
                    "details": (ActivateUsers,),
                },
                "attribute_map": {
                    "authorization": "Authorization",
                },
                "location_map": {
                    "authorization": "header",
                    "details": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json", "text/json", "text/xml"],
                "content_type": [
                    "application/json",
                    "text/json",
                    "text/xml",
                    "application/x-www-form-urlencoded",
                ],
            },
            api_client=api_client,
        )
        self.invitees_create_employee_endpoint = _Endpoint(
            settings={
                "response_type": (CreateUserDetailsResponse,),
                "auth": [],
                "endpoint_path": "/users",
                "operation_id": "invitees_create_employee",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "authorization",
                    "details",
                ],
                "required": [
                    "authorization",
                    "details",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "authorization": (str,),
                    "details": (CreateUserDetails,),
                },
                "attribute_map": {
                    "authorization": "Authorization",
                },
                "location_map": {
                    "authorization": "header",
                    "details": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json", "text/json", "text/xml"],
                "content_type": [
                    "application/json",
                    "text/json",
                    "text/xml",
                    "application/x-www-form-urlencoded",
                ],
            },
            api_client=api_client,
        )
        self.invitees_delete_user_endpoint = _Endpoint(
            settings={
                "response_type": (
                    bool,
                    date,
                    datetime,
                    dict,
                    float,
                    int,
                    list,
                    str,
                    none_type,
                ),
                "auth": [],
                "endpoint_path": "/user/{customerCode}/{userCode}",
                "operation_id": "invitees_delete_user",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "customer_code",
                    "user_code",
                    "authorization",
                ],
                "required": [
                    "customer_code",
                    "user_code",
                    "authorization",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "customer_code": (int,),
                    "user_code": (int,),
                    "authorization": (str,),
                },
                "attribute_map": {
                    "customer_code": "customerCode",
                    "user_code": "userCode",
                    "authorization": "Authorization",
                },
                "location_map": {
                    "customer_code": "path",
                    "user_code": "path",
                    "authorization": "header",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json", "text/json", "text/xml"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.invitees_update_employees_endpoint = _Endpoint(
            settings={
                "response_type": (UpdateUserDetailsResponse,),
                "auth": [],
                "endpoint_path": "/users",
                "operation_id": "invitees_update_employees",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": [
                    "authorization",
                    "details",
                ],
                "required": [
                    "authorization",
                    "details",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "authorization": (str,),
                    "details": (UpdateUserDetails,),
                },
                "attribute_map": {
                    "authorization": "Authorization",
                },
                "location_map": {
                    "authorization": "header",
                    "details": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json", "text/json", "text/xml"],
                "content_type": [
                    "application/json",
                    "text/json",
                    "text/xml",
                    "application/x-www-form-urlencoded",
                ],
            },
            api_client=api_client,
        )

    def invitees_activate_employees(self, authorization, details, **kwargs):
        """Activate Users  # noqa: E501

        This API updates Employees for using CheckedID. Employees may be users of the Customer portal and registered (or: activated) users of app.  <br /> Place the request JSON in details, enter the token with bearer prefix in Authorization header.   <br /><br /> CustomerCode is integer as registered with CheckedID.  <br /> UserCode is required.   <br />  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.invitees_activate_employees(authorization, details, async_req=True)
        >>> result = thread.get()

        Args:
            authorization (str):
            details (ActivateUsers):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ActivateUsersResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["authorization"] = authorization
        kwargs["details"] = details
        return self.invitees_activate_employees_endpoint.call_with_http_info(**kwargs)

    def invitees_create_employee(self, authorization, details, **kwargs):
        """Create Users  # noqa: E501

        This API creates Employees for using CheckedID. Employees may be users of the Customer portal and registered (or: activated) users of app.  <br /> Place the request JSON in details, enter the token with bearer prefix in Authorization header.   <br /><br /> CustomerCode is integer as registered with CheckedID.  <br /> Email is string used as unique identifier for Users.  <br /> FirstName is string to be used for personally addressing the user.  <br /> Role of the user (Admin/Basic/AppOnly)  <br /> Holder Confirmation By (App user/CheckedID Auto)  <br /> User type (Internal/External)  <br /><br /> FirstName, LastName, Role, Email, Password, StartDate and HolderConfirmationBy are required. When UserCode is sent this value needs to be unique for CustomerCode; when UserCode is not sent a 5-digit code will be generated. An ActivationCode will always be generated.  <br /><br /> Users as requested are generated with new ActivationCode, and these will be provided with the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.invitees_create_employee(authorization, details, async_req=True)
        >>> result = thread.get()

        Args:
            authorization (str):
            details (CreateUserDetails):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CreateUserDetailsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["authorization"] = authorization
        kwargs["details"] = details
        return self.invitees_create_employee_endpoint.call_with_http_info(**kwargs)

    def invitees_delete_user(self, customer_code, user_code, authorization, **kwargs):
        """Delete User  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.invitees_delete_user(customer_code, user_code, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            customer_code (int):
            user_code (int):
            authorization (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["customer_code"] = customer_code
        kwargs["user_code"] = user_code
        kwargs["authorization"] = authorization
        return self.invitees_delete_user_endpoint.call_with_http_info(**kwargs)

    def invitees_update_employees(self, authorization, details, **kwargs):
        """Update Users  # noqa: E501

        This API updates Employees for using CheckedID. Employees may be users of the Customer portal and registered (or: activated) users of app.  <br /> Place the request JSON in details, enter the token with bearer prefix in Authorization header.   <br /><br /> CustomerCode is integer as registered with CheckedID.  <br /> Email is string used as unique identifier for Users.  <br /> FirstName is string to be used for personally addressing the user.  <br /> Role of the user (Admin/Basic/AppOnly)  <br /> Holder Confirmation By (App user/CheckedID Auto)  <br /> User type (Internal/External)  <br /><br />Only UserCode is required. Fields not sent will not be updated for Employee. If indicated \"true\" for all UserCodes sent ActivationCodes will be regenerated.  <br /><br /> Users as requested are generated with renewed ActivationCode, and these will be provided with the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.invitees_update_employees(authorization, details, async_req=True)
        >>> result = thread.get()

        Args:
            authorization (str):
            details (UpdateUserDetails):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            UpdateUserDetailsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["authorization"] = authorization
        kwargs["details"] = details
        return self.invitees_update_employees_endpoint.call_with_http_info(**kwargs)
