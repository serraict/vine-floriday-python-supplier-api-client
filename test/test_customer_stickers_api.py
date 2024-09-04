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
from floriday_supplier_client.api.customer_stickers_api import CustomerStickersApi  # noqa: E501
from floriday_supplier_client.rest import ApiException


class TestCustomerStickersApi(unittest.TestCase):
    """CustomerStickersApi unit test stubs"""

    def setUp(self):
        self.api = CustomerStickersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_customer_sticker_pdf_by_id(self):
        """Test case for get_customer_sticker_pdf_by_id

        sticker:read - Returns customer sticker in pdf format  # noqa: E501
        """
        pass

    def test_get_customer_sticker_pdf_by_ids(self):
        """Test case for get_customer_sticker_pdf_by_ids

        sticker:read - Returns customer stickers in pdf format. Pages are duplicated based on the number of copies in the customer sticker.  # noqa: E501
        """
        pass

    def test_get_customer_stickers_by_sequence_number(self):
        """Test case for get_customer_stickers_by_sequence_number

        sticker:read - Returns a list of max 1000 customer stickers metadata starting from a specified sequence number.  # noqa: E501
        """
        pass

    def test_get_customer_stickers_max_sequence(self):
        """Test case for get_customer_stickers_max_sequence

        sticker:read - Returns the maximum sequence number found in customer stickers.  # noqa: E501
        """
        pass

    def test_set_customer_stickers_is_handled(self):
        """Test case for set_customer_stickers_is_handled

        sticker:write - Indicate which stickers are printed and placed.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
