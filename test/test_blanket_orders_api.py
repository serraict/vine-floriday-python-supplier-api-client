# coding: utf-8

"""
    Main - Floriday Suppliers API

    ﻿Every endpoint requires at least the `role:app` scope and the header `X-Api-Key` populated with your given API-key. Most endpoints also require an additional scope which is listed in their descriptions.  - 🗝 [Authorization server (staging)](https://idm.staging.floriday.io/oauth2/ausmw6b47z1BnlHkw0h7/.well-known/oauth-authorization-server) - 🗝 [Authorization server (live)](https://idm.floriday.io/oauth2/aus3testdcf2vyfs70i7/.well-known/oauth-authorization-server) - 📚 [Documentation](https://developer.floriday.io/docs/welcome) - ▶ [Coding screencast: getting started (NL)](https://www.youtube.com/watch?v=fdqzP7_Y_s8)  ---  _The current state of this version 2024v1 is **Main**._ * This version will be deprecated after October 2024. * This version will be removed after April 2025.  ---  🔗 2023v2: [Customers API](https://api.staging.floriday.io/customers-api-2023v2/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2023v2/swagger/index.html) 🔗 2024v1: [Customers API](https://api.staging.floriday.io/customers-api-2024v1/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2024v1/swagger/index.html) 🔗 2024v2: [Customers API](https://api.staging.floriday.io/customers-api-2024v2/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2024v2/swagger/index.html)   # noqa: E501

    OpenAPI spec version: 2024v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import floriday_supplier_client
from floriday_supplier_client.api.blanket_orders_api import BlanketOrdersApi  # noqa: E501
from floriday_supplier_client.rest import ApiException


class TestBlanketOrdersApi(unittest.TestCase):
    """BlanketOrdersApi unit test stubs"""

    def setUp(self):
        self.api = BlanketOrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_blanket_order(self):
        """Test case for add_blanket_order

        contract:write - Creates a blanket order  # noqa: E501
        """
        pass

    def test_delete_blanket_order(self):
        """Test case for delete_blanket_order

        contract:write - Deletes a blanket order.  # noqa: E501
        """
        pass

    def test_edit_blanket_order(self):
        """Test case for edit_blanket_order

        contract:write - Modifies an existing blanket order.  # noqa: E501
        """
        pass

    def test_get_blanket_order_by_id(self):
        """Test case for get_blanket_order_by_id

        contract:read - Returns a blanket order by id.  # noqa: E501
        """
        pass

    def test_get_blanket_orders_by_sequence_number(self):
        """Test case for get_blanket_orders_by_sequence_number

        contract:read - rate limit: 3.4 per second - burst limit: 1000 - Returns a list of max 1000 contracts starting from a specified sequence number.  # noqa: E501
        """
        pass

    def test_get_blanket_orders_max_sequence(self):
        """Test case for get_blanket_orders_max_sequence

        contract:read - rate limit: 3.4 per second - burst limit: 1000 - Returns the maximum sequence number found in blanket orders.  # noqa: E501
        """
        pass

    def test_set_blanket_order_approved(self):
        """Test case for set_blanket_order_approved

        contract:write - Approves a blanket order  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
