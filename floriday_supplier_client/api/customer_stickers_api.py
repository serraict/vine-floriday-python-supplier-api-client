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


class CustomerStickersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_customer_sticker_pdf_by_id(self, sticker_id, duplicate_pages_based_on_number_of_copies, **kwargs):  # noqa: E501
        """sticker:read - Returns customer sticker in pdf format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_sticker_pdf_by_id(sticker_id, duplicate_pages_based_on_number_of_copies, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sticker_id: (required)
        :param bool duplicate_pages_based_on_number_of_copies: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_sticker_pdf_by_id_with_http_info(sticker_id, duplicate_pages_based_on_number_of_copies, **kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_sticker_pdf_by_id_with_http_info(sticker_id, duplicate_pages_based_on_number_of_copies, **kwargs)  # noqa: E501
            return data

    def get_customer_sticker_pdf_by_id_with_http_info(self, sticker_id, duplicate_pages_based_on_number_of_copies, **kwargs):  # noqa: E501
        """sticker:read - Returns customer sticker in pdf format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_sticker_pdf_by_id_with_http_info(sticker_id, duplicate_pages_based_on_number_of_copies, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sticker_id: (required)
        :param bool duplicate_pages_based_on_number_of_copies: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sticker_id', 'duplicate_pages_based_on_number_of_copies']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_sticker_pdf_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sticker_id' is set
        if ('sticker_id' not in params or
                params['sticker_id'] is None):
            raise ValueError("Missing the required parameter `sticker_id` when calling `get_customer_sticker_pdf_by_id`")  # noqa: E501
        # verify the required parameter 'duplicate_pages_based_on_number_of_copies' is set
        if ('duplicate_pages_based_on_number_of_copies' not in params or
                params['duplicate_pages_based_on_number_of_copies'] is None):
            raise ValueError("Missing the required parameter `duplicate_pages_based_on_number_of_copies` when calling `get_customer_sticker_pdf_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sticker_id' in params:
            path_params['stickerId'] = params['sticker_id']  # noqa: E501

        query_params = []
        if 'duplicate_pages_based_on_number_of_copies' in params:
            query_params.append(('duplicatePagesBasedOnNumberOfCopies', params['duplicate_pages_based_on_number_of_copies']))  # noqa: E501

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
            '/customer-stickers/{stickerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customer_sticker_pdf_by_ids(self, sticker_ids, **kwargs):  # noqa: E501
        """sticker:read - Returns customer stickers in pdf format. Pages are duplicated based on the number of copies in the customer sticker.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_sticker_pdf_by_ids(sticker_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] sticker_ids: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_sticker_pdf_by_ids_with_http_info(sticker_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_sticker_pdf_by_ids_with_http_info(sticker_ids, **kwargs)  # noqa: E501
            return data

    def get_customer_sticker_pdf_by_ids_with_http_info(self, sticker_ids, **kwargs):  # noqa: E501
        """sticker:read - Returns customer stickers in pdf format. Pages are duplicated based on the number of copies in the customer sticker.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_sticker_pdf_by_ids_with_http_info(sticker_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] sticker_ids: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sticker_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_sticker_pdf_by_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sticker_ids' is set
        if ('sticker_ids' not in params or
                params['sticker_ids'] is None):
            raise ValueError("Missing the required parameter `sticker_ids` when calling `get_customer_sticker_pdf_by_ids`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sticker_ids' in params:
            query_params.append(('stickerIds', params['sticker_ids']))  # noqa: E501
            collection_formats['stickerIds'] = 'multi'  # noqa: E501

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
            '/customer-stickers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customer_stickers_by_sequence_number(self, sequence_number, **kwargs):  # noqa: E501
        """sticker:read - Returns a list of max 1000 customer stickers metadata starting from a specified sequence number.  # noqa: E501

        **Synchronization endpoint** Fetches the succeeding modified records (including deleted records) based on `Limit` and the given `SequenceNumber`.  **Note** Your data is up to date when your given `SequenceNumber` is equal to the received `MaximumSequenceNumber`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_stickers_by_sequence_number(sequence_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sequence_number: (required)
        :param int limit_result:
        :return: SyncResultOfCustomerSticker
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_stickers_by_sequence_number_with_http_info(sequence_number, **kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_stickers_by_sequence_number_with_http_info(sequence_number, **kwargs)  # noqa: E501
            return data

    def get_customer_stickers_by_sequence_number_with_http_info(self, sequence_number, **kwargs):  # noqa: E501
        """sticker:read - Returns a list of max 1000 customer stickers metadata starting from a specified sequence number.  # noqa: E501

        **Synchronization endpoint** Fetches the succeeding modified records (including deleted records) based on `Limit` and the given `SequenceNumber`.  **Note** Your data is up to date when your given `SequenceNumber` is equal to the received `MaximumSequenceNumber`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_stickers_by_sequence_number_with_http_info(sequence_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int sequence_number: (required)
        :param int limit_result:
        :return: SyncResultOfCustomerSticker
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
                    " to method get_customer_stickers_by_sequence_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sequence_number' is set
        if ('sequence_number' not in params or
                params['sequence_number'] is None):
            raise ValueError("Missing the required parameter `sequence_number` when calling `get_customer_stickers_by_sequence_number`")  # noqa: E501

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
            '/customer-stickers/sync/{sequenceNumber}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SyncResultOfCustomerSticker',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_customer_stickers_max_sequence(self, **kwargs):  # noqa: E501
        """sticker:read - Returns the maximum sequence number found in customer stickers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_stickers_max_sequence(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_customer_stickers_max_sequence_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_customer_stickers_max_sequence_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_customer_stickers_max_sequence_with_http_info(self, **kwargs):  # noqa: E501
        """sticker:read - Returns the maximum sequence number found in customer stickers.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_customer_stickers_max_sequence_with_http_info(async_req=True)
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
                    " to method get_customer_stickers_max_sequence" % key
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
            '/customer-stickers/current-max-sequence', 'GET',
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

    def set_customer_stickers_is_handled(self, sticker_ids, **kwargs):  # noqa: E501
        """sticker:write - Indicate which stickers are printed and placed.  # noqa: E501

        IsHandled indication will be set to true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_customer_stickers_is_handled(sticker_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] sticker_ids: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_customer_stickers_is_handled_with_http_info(sticker_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.set_customer_stickers_is_handled_with_http_info(sticker_ids, **kwargs)  # noqa: E501
            return data

    def set_customer_stickers_is_handled_with_http_info(self, sticker_ids, **kwargs):  # noqa: E501
        """sticker:write - Indicate which stickers are printed and placed.  # noqa: E501

        IsHandled indication will be set to true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_customer_stickers_is_handled_with_http_info(sticker_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] sticker_ids: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sticker_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_customer_stickers_is_handled" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sticker_ids' is set
        if ('sticker_ids' not in params or
                params['sticker_ids'] is None):
            raise ValueError("Missing the required parameter `sticker_ids` when calling `set_customer_stickers_is_handled`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sticker_ids' in params:
            query_params.append(('stickerIds', params['sticker_ids']))  # noqa: E501
            collection_formats['stickerIds'] = 'multi'  # noqa: E501

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
            '/customer-stickers/handled', 'PATCH',
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
