# coding: utf-8

"""
    Main - Floriday Suppliers API

    ﻿Every endpoint requires at least the `role:app` scope and the header `X-Api-Key` populated with your given API-key. Most endpoints also require an additional scope which is listed in their descriptions.  - 🗝 [Authorization server (staging)](https://idm.staging.floriday.io/oauth2/ausmw6b47z1BnlHkw0h7/.well-known/oauth-authorization-server) - 🗝 [Authorization server (live)](https://idm.floriday.io/oauth2/aus3testdcf2vyfs70i7/.well-known/oauth-authorization-server) - 📚 [Documentation](https://developer.floriday.io/docs/welcome) - ▶ [Coding screencast: getting started (NL)](https://www.youtube.com/watch?v=fdqzP7_Y_s8)  ---  _The current state of this version 2024v1 is **Main**._ * This version will be deprecated after October 2024. * This version will be removed after April 2025.  ---  🔗 2023v2: [Customers API](https://api.staging.floriday.io/customers-api-2023v2/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2023v2/swagger/index.html) 🔗 2024v1: [Customers API](https://api.staging.floriday.io/customers-api-2024v1/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2024v1/swagger/index.html) 🔗 2024v2: [Customers API](https://api.staging.floriday.io/customers-api-2024v2/swagger/index.html) | [Suppliers API](https://api.staging.floriday.io/suppliers-api-2024v2/swagger/index.html)   # noqa: E501

    OpenAPI spec version: 2024v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AddClockPresalesSupplyLine(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'clock_supply_line_id': 'str',
        'price_per_piece': 'float'
    }

    attribute_map = {
        'clock_supply_line_id': 'clockSupplyLineId',
        'price_per_piece': 'pricePerPiece'
    }

    def __init__(self, clock_supply_line_id=None, price_per_piece=None):  # noqa: E501
        """AddClockPresalesSupplyLine - a model defined in Swagger"""  # noqa: E501
        self._clock_supply_line_id = None
        self._price_per_piece = None
        self.discriminator = None
        self.clock_supply_line_id = clock_supply_line_id
        self.price_per_piece = price_per_piece

    @property
    def clock_supply_line_id(self):
        """Gets the clock_supply_line_id of this AddClockPresalesSupplyLine.  # noqa: E501


        :return: The clock_supply_line_id of this AddClockPresalesSupplyLine.  # noqa: E501
        :rtype: str
        """
        return self._clock_supply_line_id

    @clock_supply_line_id.setter
    def clock_supply_line_id(self, clock_supply_line_id):
        """Sets the clock_supply_line_id of this AddClockPresalesSupplyLine.


        :param clock_supply_line_id: The clock_supply_line_id of this AddClockPresalesSupplyLine.  # noqa: E501
        :type: str
        """
        if clock_supply_line_id is None:
            raise ValueError("Invalid value for `clock_supply_line_id`, must not be `None`")  # noqa: E501

        self._clock_supply_line_id = clock_supply_line_id

    @property
    def price_per_piece(self):
        """Gets the price_per_piece of this AddClockPresalesSupplyLine.  # noqa: E501


        :return: The price_per_piece of this AddClockPresalesSupplyLine.  # noqa: E501
        :rtype: float
        """
        return self._price_per_piece

    @price_per_piece.setter
    def price_per_piece(self, price_per_piece):
        """Sets the price_per_piece of this AddClockPresalesSupplyLine.


        :param price_per_piece: The price_per_piece of this AddClockPresalesSupplyLine.  # noqa: E501
        :type: float
        """
        if price_per_piece is None:
            raise ValueError("Invalid value for `price_per_piece`, must not be `None`")  # noqa: E501

        self._price_per_piece = price_per_piece

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AddClockPresalesSupplyLine, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddClockPresalesSupplyLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
