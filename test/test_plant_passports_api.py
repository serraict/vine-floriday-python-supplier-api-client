# coding: utf-8

"""
    Main - Floriday Suppliers API

    ﻿Every endpoint requires at least the `role:app` scope and the header `X-Api-Key` populated with your given API-key. Most endpoints also require an additional scope which is listed in their descriptions.  - 🗝 [Authorization server (staging)](https://idm.staging.floriday.io/oauth2/ausmw6b47z1BnlHkw0h7/.well-known/oauth-authorization-server) - 🗝 [Authorization server (live)](https://idm.floriday.io/oauth2/aus3testdcf2vyfs70i7/.well-known/oauth-authorization-server) - 📚 [Documentation](https://developer.floriday.io/docs/welcome) - ▶ [Coding screencast: getting started (NL)](https://www.youtube.com/watch?v=fdqzP7_Y_s8)  ---  _The current state of this version 2024v1 is **Main**._ * This version will be deprecated after October 2024. * This version will be removed after April 2025.  ---  🔗 2023v2: [Customers API](https://api.staging.floriday.io/customers-api-2023v2/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2023v2/swagger/index.html) 🔗 2024v1: [Customers API](https://api.staging.floriday.io/customers-api-2024v1/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2024v1/swagger/index.html) 🔗 2024v2: [Customers API](https://api.staging.floriday.io/customers-api-2024v2/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2024v2/swagger/index.html)   # noqa: E501

    OpenAPI spec version: 2024v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.plant_passports_api import PlantPassportsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPlantPassportsApi(unittest.TestCase):
    """PlantPassportsApi unit test stubs"""

    def setUp(self):
        self.api = PlantPassportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_plant_passport_pdf(self):
        """Test case for get_plant_passport_pdf

        fulfillment:read - Returns the plant passport PDF for the BatchIds.  # noqa: E501
        """
        pass

    def test_get_plant_passport_pdf_by_sales_channel_order_id(self):
        """Test case for get_plant_passport_pdf_by_sales_channel_order_id

        fulfillment:read - Returns plant passport PDF for the sales order.  # noqa: E501
        """
        pass

    def test_get_plant_passport_pdf_by_sales_order_id(self):
        """Test case for get_plant_passport_pdf_by_sales_order_id

        fulfillment:read - Returns plant passport PDF for the sales order.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
