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
from checkedid.model.report_data_v3 import ReportDataV3
from checkedid.model.report_response import ReportResponse
from checkedid.model_utils import (check_allowed_values,  # noqa: F401
                                   check_validations, date, datetime,
                                   file_type, none_type,
                                   validate_and_convert_types)


class ReportDataApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.report_data_get_report_data_v2_endpoint = _Endpoint(
            settings={
                "response_type": (ReportDataV3,),
                "auth": [],
                "endpoint_path": "/reportdata/{dossierNumber}/{scope}",
                "operation_id": "report_data_get_report_data_v2",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "dossier_number",
                    "scope",
                    "authorization",
                ],
                "required": [
                    "dossier_number",
                    "scope",
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
                    "dossier_number": (str,),
                    "scope": (str,),
                    "authorization": (str,),
                },
                "attribute_map": {
                    "dossier_number": "dossierNumber",
                    "scope": "scope",
                    "authorization": "Authorization",
                },
                "location_map": {
                    "dossier_number": "path",
                    "scope": "path",
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
        self.report_data_get_report_data_v2_pdf_endpoint = _Endpoint(
            settings={
                "response_type": (ReportResponse,),
                "auth": [],
                "endpoint_path": "/report/{dossierNumber}",
                "operation_id": "report_data_get_report_data_v2_pdf",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "dossier_number",
                    "authorization",
                ],
                "required": [
                    "dossier_number",
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
                    "dossier_number": (str,),
                    "authorization": (str,),
                },
                "attribute_map": {
                    "dossier_number": "dossierNumber",
                    "authorization": "Authorization",
                },
                "location_map": {
                    "dossier_number": "path",
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

    def report_data_get_report_data_v2(
        self, dossier_number, scope, authorization, **kwargs
    ):
        """Get report details based on dossier number and scope  # noqa: E501

        This API retrieves data from verification reports previously received by CheckedID customers. These – personal – data can thus be imported in customer’s own environment.  <br /> The API allows for one-by-one importing of data only, in order to facilitate that customer has explicitly ensured the data is appropriate for further processing.  <br /> Note that reports are accessible for a maximum of seven days after they’re created. After that period their data can no longer be retrieved.  <br /><br /> DossierNumber is string known from the CheckedID report received.  <br /> Scope is string with possible values ‘10’, ‘11’, ‘12’, ‘13’.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.report_data_get_report_data_v2(dossier_number, scope, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            dossier_number (str):
            scope (str):
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
            ReportDataV3
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
        kwargs["dossier_number"] = dossier_number
        kwargs["scope"] = scope
        kwargs["authorization"] = authorization
        return self.report_data_get_report_data_v2_endpoint.call_with_http_info(
            **kwargs
        )

    def report_data_get_report_data_v2_pdf(
        self, dossier_number, authorization, **kwargs
    ):
        """Get report pdf based on dossier number  # noqa: E501

        This API retrieves data from verification reports previously received by CheckedID customers.   <br /> Note that reports are accessible for a maximum of seven days after they’re created. After that period their data can no longer be retrieved.  <br /><br /> DossierNumber is string known from the CheckedID report received.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.report_data_get_report_data_v2_pdf(dossier_number, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            dossier_number (str):
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
            ReportResponse
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
        kwargs["dossier_number"] = dossier_number
        kwargs["authorization"] = authorization
        return self.report_data_get_report_data_v2_pdf_endpoint.call_with_http_info(
            **kwargs
        )