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
from floriday_supplier_client.api.catalog_prices_api import CatalogPricesApi  # noqa: E501
from floriday_supplier_client.rest import ApiException


class TestCatalogPricesApi(unittest.TestCase):
    """CatalogPricesApi unit test stubs"""

    def setUp(self):
        self.api = CatalogPricesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_weekly_supply_line(self):
        """Test case for add_weekly_supply_line

        supply:write - Creates a new weekly supply line for trade item.  # noqa: E501
        """
        pass

    def test_delete_weekly_supply_lines(self):
        """Test case for delete_weekly_supply_lines

        supply:write - Deletes a weekly supply line.  # noqa: E501
        """
        pass

    def test_edit_continuous_stock(self):
        """Test case for edit_continuous_stock

        supply:write - rate limit: 10 per second - burst limit: 1000 - Set availabilities for a trade item  # noqa: E501
        """
        pass

    def test_edit_weekly_base_supply(self):
        """Test case for edit_weekly_base_supply

        supply:write - rate limit: 10 per second - burst limit: 1000 - Generates new weekly supply lines based on pre-entered price groups.  # noqa: E501
        """
        pass

    def test_edit_weekly_base_supply_lines(self):
        """Test case for edit_weekly_base_supply_lines

        supply:write - rate limit: 10 per second - burst limit: 1000 - Generates new weekly supply lines for multiple trade items based on calculated and manual price groups.  # noqa: E501
        """
        pass

    def test_edit_weekly_supply_line(self):
        """Test case for edit_weekly_supply_line

        supply:write - Updates a weekly supply line for trade item.  # noqa: E501
        """
        pass

    def test_get_continuous_stock(self):
        """Test case for get_continuous_stock

        supply:read - Returns the availability of a trade item.  # noqa: E501
        """
        pass

    def test_get_trade_item_availabilities(self):
        """Test case for get_trade_item_availabilities

        supply:read - rate limit: 2 per second - burst limit: 200 - Returns the current availability of all trade items.  # noqa: E501
        """
        pass

    def test_get_trade_item_availabilities_by_sequence_number(self):
        """Test case for get_trade_item_availabilities_by_sequence_number

        supply:read - Returns a list of max 1000 trade item availabilities starting from a specified sequence number.  # noqa: E501
        """
        pass

    def test_get_trade_item_availabilities_max_sequence(self):
        """Test case for get_trade_item_availabilities_max_sequence

        supply:read - Returns the maximum sequence number found in trade item availabilities.  # noqa: E501
        """
        pass

    def test_get_weekly_base_supplies(self):
        """Test case for get_weekly_base_supplies

        supply:read - rate limit: 1 per second - burst limit: 20 - Returns the base supply per year/week for trade items.  # noqa: E501
        """
        pass

    def test_set_trade_item_warehouse(self):
        """Test case for set_trade_item_warehouse

        supply:write - Add a warehouse for a trade item ( only continuous stock )  # noqa: E501
        """
        pass

    def test_set_weekly_base_supply_number_of_pieces(self):
        """Test case for set_weekly_base_supply_number_of_pieces

        supply:write - rate limit: 10 per second - burst limit: 1000 - Patch the number of pieces of an existing base supply.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
