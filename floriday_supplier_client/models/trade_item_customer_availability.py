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

class TradeItemCustomerAvailability(object):
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
        'customer_organization_id': 'str',
        'is_available': 'bool'
    }

    attribute_map = {
        'customer_organization_id': 'customerOrganizationId',
        'is_available': 'isAvailable'
    }

    def __init__(self, customer_organization_id=None, is_available=None):  # noqa: E501
        """TradeItemCustomerAvailability - a model defined in Swagger"""  # noqa: E501
        self._customer_organization_id = None
        self._is_available = None
        self.discriminator = None
        self.customer_organization_id = customer_organization_id
        self.is_available = is_available

    @property
    def customer_organization_id(self):
        """Gets the customer_organization_id of this TradeItemCustomerAvailability.  # noqa: E501


        :return: The customer_organization_id of this TradeItemCustomerAvailability.  # noqa: E501
        :rtype: str
        """
        return self._customer_organization_id

    @customer_organization_id.setter
    def customer_organization_id(self, customer_organization_id):
        """Sets the customer_organization_id of this TradeItemCustomerAvailability.


        :param customer_organization_id: The customer_organization_id of this TradeItemCustomerAvailability.  # noqa: E501
        :type: str
        """
        if customer_organization_id is None:
            raise ValueError("Invalid value for `customer_organization_id`, must not be `None`")  # noqa: E501

        self._customer_organization_id = customer_organization_id

    @property
    def is_available(self):
        """Gets the is_available of this TradeItemCustomerAvailability.  # noqa: E501


        :return: The is_available of this TradeItemCustomerAvailability.  # noqa: E501
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this TradeItemCustomerAvailability.


        :param is_available: The is_available of this TradeItemCustomerAvailability.  # noqa: E501
        :type: bool
        """
        if is_available is None:
            raise ValueError("Invalid value for `is_available`, must not be `None`")  # noqa: E501

        self._is_available = is_available

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
        if issubclass(TradeItemCustomerAvailability, dict):
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
        if not isinstance(other, TradeItemCustomerAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
