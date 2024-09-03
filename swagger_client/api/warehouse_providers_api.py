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


class WarehouseProvidersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_fulfillment_orders_inbound_by_sequence_number(self, sequence_number, **kwargs):  # noqa: E501
        """fulfillment:read - Returns a list of inbound fulfillment orders.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fulfillment_orders_inbound_by_sequence_number(sequence_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sequence_number: (required)
        :param int limit_result:
        :return: SyncResultOfFulfillmentOrderInbound
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fulfillment_orders_inbound_by_sequence_number_with_http_info(sequence_number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fulfillment_orders_inbound_by_sequence_number_with_http_info(sequence_number, **kwargs)  # noqa: E501
            return data

    def get_fulfillment_orders_inbound_by_sequence_number_with_http_info(self, sequence_number, **kwargs):  # noqa: E501
        """fulfillment:read - Returns a list of inbound fulfillment orders.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fulfillment_orders_inbound_by_sequence_number_with_http_info(sequence_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sequence_number: (required)
        :param int limit_result:
        :return: SyncResultOfFulfillmentOrderInbound
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sequence_number', 'limit_result']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fulfillment_orders_inbound_by_sequence_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sequence_number' is set
        if ('sequence_number' not in params or
                params['sequence_number'] is None):
            raise ValueError("Missing the required parameter `sequence_number` when calling `get_fulfillment_orders_inbound_by_sequence_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sequence_number' in params:
            path_params['sequenceNumber'] = params['sequence_number']  # noqa: E501

        query_params = []
        if 'limit_result' in params:
            query_params.append(('limitResult', params['limit_result']))  # noqa: E501

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
            '/fulfillment-orders/inbound/sync/{sequenceNumber}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SyncResultOfFulfillmentOrderInbound',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_fulfillment_order_receipt(self, body, fulfillment_order_id, **kwargs):  # noqa: E501
        """fulfillment:write - Receive a inbound fulfillment order.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_fulfillment_order_receipt(body, fulfillment_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GoodsReceipt body: (required)
        :param str fulfillment_order_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_fulfillment_order_receipt_with_http_info(body, fulfillment_order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_fulfillment_order_receipt_with_http_info(body, fulfillment_order_id, **kwargs)  # noqa: E501
            return data

    def set_fulfillment_order_receipt_with_http_info(self, body, fulfillment_order_id, **kwargs):  # noqa: E501
        """fulfillment:write - Receive a inbound fulfillment order.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_fulfillment_order_receipt_with_http_info(body, fulfillment_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GoodsReceipt body: (required)
        :param str fulfillment_order_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'fulfillment_order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_fulfillment_order_receipt" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_fulfillment_order_receipt`")  # noqa: E501
        # verify the required parameter 'fulfillment_order_id' is set
        if ('fulfillment_order_id' not in params or
                params['fulfillment_order_id'] is None):
            raise ValueError("Missing the required parameter `fulfillment_order_id` when calling `set_fulfillment_order_receipt`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fulfillment_order_id' in params:
            path_params['fulfillmentOrderId'] = params['fulfillment_order_id']  # noqa: E501

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
            '/fulfillment-orders/{fulfillmentOrderId}/goods-receipt', 'PUT',
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
