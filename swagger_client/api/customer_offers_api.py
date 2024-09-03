# coding: utf-8

"""
    Main - Floriday Suppliers API

    ﻿Every endpoint requires at least the `role:app` scope and the header `X-Api-Key` populated with your given API-key. Most endpoints also require an additional scope which is listed in their descriptions.  - 🗝 [Authorization server (staging)](https://idm.staging.floriday.io/oauth2/ausmw6b47z1BnlHkw0h7/.well-known/oauth-authorization-server) - 🗝 [Authorization server (live)](https://idm.floriday.io/oauth2/aus3testdcf2vyfs70i7/.well-known/oauth-authorization-server) - 📚 [Documentation](https://developer.floriday.io/docs/welcome) - ▶ [Coding screencast: getting started (NL)](https://www.youtube.com/watch?v=fdqzP7_Y_s8)  ---  _The current state of this version 2024v1 is **Main**._ * This version will be deprecated after October 2024. * This version will be removed after April 2025.  ---  🔗 2023v2: [Customers API](https://api.staging.floriday.io/customers-api-2023v2/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2023v2/swagger/index.html) 🔗 2024v1: [Customers API](https://api.staging.floriday.io/customers-api-2024v1/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2024v1/swagger/index.html) 🔗 2024v2: [Customers API](https://api.staging.floriday.io/customers-api-2024v2/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2024v2/swagger/index.html)   # noqa: E501

    OpenAPI spec version: 2024v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CustomerOffersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_customer_offer(self, body, **kwargs):  # noqa: E501
        """supply:write - create a customer offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_customer_offer(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddCustomerOffer body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_customer_offer_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_customer_offer_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_customer_offer_with_http_info(self, body, **kwargs):  # noqa: E501
        """supply:write - create a customer offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_customer_offer_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddCustomerOffer body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_customer_offer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_customer_offer`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT Token', 'X-Api-Key']  # noqa: E501

        return self.api_client.call_api(
            '/customer-offers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_customer_offers(self, supply_line_id, **kwargs):  # noqa: E501
        """supply:write - delete a customer offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_customer_offers(supply_line_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str supply_line_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_customer_offers_with_http_info(supply_line_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_customer_offers_with_http_info(supply_line_id, **kwargs)  # noqa: E501
            return data

    def delete_customer_offers_with_http_info(self, supply_line_id, **kwargs):  # noqa: E501
        """supply:write - delete a customer offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_customer_offers_with_http_info(supply_line_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str supply_line_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supply_line_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_customer_offers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supply_line_id' is set
        if ('supply_line_id' not in params or
                params['supply_line_id'] is None):
            raise ValueError("Missing the required parameter `supply_line_id` when calling `delete_customer_offers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supply_line_id' in params:
            path_params['supplyLineId'] = params['supply_line_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT Token', 'X-Api-Key']  # noqa: E501

        return self.api_client.call_api(
            '/customer-offers/{supplyLineId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def edit_customer_offer(self, body, supply_line_id, **kwargs):  # noqa: E501
        """supply:write - update a customer offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_customer_offer(body, supply_line_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EditCustomerOffer body: (required)
        :param str supply_line_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_customer_offer_with_http_info(body, supply_line_id, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_customer_offer_with_http_info(body, supply_line_id, **kwargs)  # noqa: E501
            return data

    def edit_customer_offer_with_http_info(self, body, supply_line_id, **kwargs):  # noqa: E501
        """supply:write - update a customer offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_customer_offer_with_http_info(body, supply_line_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EditCustomerOffer body: (required)
        :param str supply_line_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'supply_line_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_customer_offer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `edit_customer_offer`")  # noqa: E501
        # verify the required parameter 'supply_line_id' is set
        if ('supply_line_id' not in params or
                params['supply_line_id'] is None):
            raise ValueError("Missing the required parameter `supply_line_id` when calling `edit_customer_offer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'supply_line_id' in params:
            path_params['supplyLineId'] = params['supply_line_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT Token', 'X-Api-Key']  # noqa: E501

        return self.api_client.call_api(
            '/customer-offers/{supplyLineId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
