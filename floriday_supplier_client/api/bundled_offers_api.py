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

from floriday_supplier_client.api_client import ApiClient


class BundledOffersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_bundled_offer(self, body, **kwargs):  # noqa: E501
        """supply:write - creates a bundled offer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_bundled_offer(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddBundledOffer body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_bundled_offer_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_bundled_offer_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_bundled_offer_with_http_info(self, body, **kwargs):  # noqa: E501
        """supply:write - creates a bundled offer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_bundled_offer_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddBundledOffer body: (required)
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
                    " to method add_bundled_offer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_bundled_offer`")  # noqa: E501

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
            '/bundled-offers', 'POST',
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

    def delete_bundled_offer(self, bundled_offer_id, **kwargs):  # noqa: E501
        """supply:write - delete a bundled offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bundled_offer(bundled_offer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bundled_offer_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bundled_offer_with_http_info(bundled_offer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_bundled_offer_with_http_info(bundled_offer_id, **kwargs)  # noqa: E501
            return data

    def delete_bundled_offer_with_http_info(self, bundled_offer_id, **kwargs):  # noqa: E501
        """supply:write - delete a bundled offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bundled_offer_with_http_info(bundled_offer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bundled_offer_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bundled_offer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bundled_offer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundled_offer_id' is set
        if ('bundled_offer_id' not in params or
                params['bundled_offer_id'] is None):
            raise ValueError("Missing the required parameter `bundled_offer_id` when calling `delete_bundled_offer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bundled_offer_id' in params:
            path_params['bundledOfferId'] = params['bundled_offer_id']  # noqa: E501

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
            '/bundled-offers/{bundledOfferId}', 'DELETE',
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

    def edit_bundled_offer(self, body, bundled_offer_id, **kwargs):  # noqa: E501
        """supply:write - update a bundled offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_bundled_offer(body, bundled_offer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EditBundledOffer body: (required)
        :param str bundled_offer_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.edit_bundled_offer_with_http_info(body, bundled_offer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.edit_bundled_offer_with_http_info(body, bundled_offer_id, **kwargs)  # noqa: E501
            return data

    def edit_bundled_offer_with_http_info(self, body, bundled_offer_id, **kwargs):  # noqa: E501
        """supply:write - update a bundled offer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.edit_bundled_offer_with_http_info(body, bundled_offer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EditBundledOffer body: (required)
        :param str bundled_offer_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bundled_offer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_bundled_offer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `edit_bundled_offer`")  # noqa: E501
        # verify the required parameter 'bundled_offer_id' is set
        if ('bundled_offer_id' not in params or
                params['bundled_offer_id'] is None):
            raise ValueError("Missing the required parameter `bundled_offer_id` when calling `edit_bundled_offer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bundled_offer_id' in params:
            path_params['bundledOfferId'] = params['bundled_offer_id']  # noqa: E501

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
            '/bundled-offers/{bundledOfferId}', 'PUT',
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

    def get_bundled_offer_by_bundled_offer_line_id(self, bundled_offer_line_id, **kwargs):  # noqa: E501
        """supply:read - Returns a bundled offer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundled_offer_by_bundled_offer_line_id(bundled_offer_line_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bundled_offer_line_id: (required)
        :return: BundledOffer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bundled_offer_by_bundled_offer_line_id_with_http_info(bundled_offer_line_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bundled_offer_by_bundled_offer_line_id_with_http_info(bundled_offer_line_id, **kwargs)  # noqa: E501
            return data

    def get_bundled_offer_by_bundled_offer_line_id_with_http_info(self, bundled_offer_line_id, **kwargs):  # noqa: E501
        """supply:read - Returns a bundled offer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundled_offer_by_bundled_offer_line_id_with_http_info(bundled_offer_line_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bundled_offer_line_id: (required)
        :return: BundledOffer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bundled_offer_line_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bundled_offer_by_bundled_offer_line_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundled_offer_line_id' is set
        if ('bundled_offer_line_id' not in params or
                params['bundled_offer_line_id'] is None):
            raise ValueError("Missing the required parameter `bundled_offer_line_id` when calling `get_bundled_offer_by_bundled_offer_line_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bundled_offer_line_id' in params:
            query_params.append(('bundledOfferLineId', params['bundled_offer_line_id']))  # noqa: E501

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
            '/bundled-offers/by-bundled-offer-line-id', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BundledOffer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bundled_offer_by_id(self, bundled_offer_id, **kwargs):  # noqa: E501
        """supply:read - Returns a bundled offer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundled_offer_by_id(bundled_offer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bundled_offer_id: (required)
        :return: BundledOffer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bundled_offer_by_id_with_http_info(bundled_offer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bundled_offer_by_id_with_http_info(bundled_offer_id, **kwargs)  # noqa: E501
            return data

    def get_bundled_offer_by_id_with_http_info(self, bundled_offer_id, **kwargs):  # noqa: E501
        """supply:read - Returns a bundled offer.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundled_offer_by_id_with_http_info(bundled_offer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bundled_offer_id: (required)
        :return: BundledOffer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bundled_offer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bundled_offer_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundled_offer_id' is set
        if ('bundled_offer_id' not in params or
                params['bundled_offer_id'] is None):
            raise ValueError("Missing the required parameter `bundled_offer_id` when calling `get_bundled_offer_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bundled_offer_id' in params:
            path_params['bundledOfferId'] = params['bundled_offer_id']  # noqa: E501

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
            '/bundled-offers/{bundledOfferId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BundledOffer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bundled_offers_by_sequence_number(self, sequence_number, **kwargs):  # noqa: E501
        """supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 Bundled offers starting from a specified sequence number.  # noqa: E501

        **Synchronization endpoint** Fetches the succeeding modified records (including deleted records) based on `Limit` and the given `SequenceNumber`.  **Note** Your data is up to date when your given `SequenceNumber` is equal to the received `MaximumSequenceNumber`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundled_offers_by_sequence_number(sequence_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sequence_number: (required)
        :param int limit_result:
        :return: SyncResultOfBundledOffer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bundled_offers_by_sequence_number_with_http_info(sequence_number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bundled_offers_by_sequence_number_with_http_info(sequence_number, **kwargs)  # noqa: E501
            return data

    def get_bundled_offers_by_sequence_number_with_http_info(self, sequence_number, **kwargs):  # noqa: E501
        """supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 Bundled offers starting from a specified sequence number.  # noqa: E501

        **Synchronization endpoint** Fetches the succeeding modified records (including deleted records) based on `Limit` and the given `SequenceNumber`.  **Note** Your data is up to date when your given `SequenceNumber` is equal to the received `MaximumSequenceNumber`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundled_offers_by_sequence_number_with_http_info(sequence_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sequence_number: (required)
        :param int limit_result:
        :return: SyncResultOfBundledOffer
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
                    " to method get_bundled_offers_by_sequence_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sequence_number' is set
        if ('sequence_number' not in params or
                params['sequence_number'] is None):
            raise ValueError("Missing the required parameter `sequence_number` when calling `get_bundled_offers_by_sequence_number`")  # noqa: E501

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
            '/bundled-offers/sync/{sequenceNumber}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SyncResultOfBundledOffer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bundled_offers_max_sequence(self, **kwargs):  # noqa: E501
        """supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns the maximum sequence number found in bundled offers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundled_offers_max_sequence(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bundled_offers_max_sequence_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_bundled_offers_max_sequence_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_bundled_offers_max_sequence_with_http_info(self, **kwargs):  # noqa: E501
        """supply:read - rate limit: 3.4 per second - burst limit: 1000 - Returns the maximum sequence number found in bundled offers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bundled_offers_max_sequence_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bundled_offers_max_sequence" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/bundled-offers/current-max-sequence', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
