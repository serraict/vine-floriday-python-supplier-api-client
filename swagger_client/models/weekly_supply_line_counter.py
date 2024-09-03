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

class WeeklySupplyLineCounter(object):
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
        'weekly_supply_line_counter_id': 'str',
        'supplier_organization_id': 'str',
        'initial_number_of_pieces': 'int',
        'claimed_number_of_pieces': 'int',
        'added': 'datetime'
    }

    attribute_map = {
        'weekly_supply_line_counter_id': 'weeklySupplyLineCounterId',
        'supplier_organization_id': 'supplierOrganizationId',
        'initial_number_of_pieces': 'initialNumberOfPieces',
        'claimed_number_of_pieces': 'claimedNumberOfPieces',
        'added': 'added'
    }

    def __init__(self, weekly_supply_line_counter_id=None, supplier_organization_id=None, initial_number_of_pieces=None, claimed_number_of_pieces=None, added=None):  # noqa: E501
        """WeeklySupplyLineCounter - a model defined in Swagger"""  # noqa: E501
        self._weekly_supply_line_counter_id = None
        self._supplier_organization_id = None
        self._initial_number_of_pieces = None
        self._claimed_number_of_pieces = None
        self._added = None
        self.discriminator = None
        self.weekly_supply_line_counter_id = weekly_supply_line_counter_id
        self.supplier_organization_id = supplier_organization_id
        self.initial_number_of_pieces = initial_number_of_pieces
        self.claimed_number_of_pieces = claimed_number_of_pieces
        self.added = added

    @property
    def weekly_supply_line_counter_id(self):
        """Gets the weekly_supply_line_counter_id of this WeeklySupplyLineCounter.  # noqa: E501


        :return: The weekly_supply_line_counter_id of this WeeklySupplyLineCounter.  # noqa: E501
        :rtype: str
        """
        return self._weekly_supply_line_counter_id

    @weekly_supply_line_counter_id.setter
    def weekly_supply_line_counter_id(self, weekly_supply_line_counter_id):
        """Sets the weekly_supply_line_counter_id of this WeeklySupplyLineCounter.


        :param weekly_supply_line_counter_id: The weekly_supply_line_counter_id of this WeeklySupplyLineCounter.  # noqa: E501
        :type: str
        """
        if weekly_supply_line_counter_id is None:
            raise ValueError("Invalid value for `weekly_supply_line_counter_id`, must not be `None`")  # noqa: E501

        self._weekly_supply_line_counter_id = weekly_supply_line_counter_id

    @property
    def supplier_organization_id(self):
        """Gets the supplier_organization_id of this WeeklySupplyLineCounter.  # noqa: E501


        :return: The supplier_organization_id of this WeeklySupplyLineCounter.  # noqa: E501
        :rtype: str
        """
        return self._supplier_organization_id

    @supplier_organization_id.setter
    def supplier_organization_id(self, supplier_organization_id):
        """Sets the supplier_organization_id of this WeeklySupplyLineCounter.


        :param supplier_organization_id: The supplier_organization_id of this WeeklySupplyLineCounter.  # noqa: E501
        :type: str
        """
        if supplier_organization_id is None:
            raise ValueError("Invalid value for `supplier_organization_id`, must not be `None`")  # noqa: E501

        self._supplier_organization_id = supplier_organization_id

    @property
    def initial_number_of_pieces(self):
        """Gets the initial_number_of_pieces of this WeeklySupplyLineCounter.  # noqa: E501


        :return: The initial_number_of_pieces of this WeeklySupplyLineCounter.  # noqa: E501
        :rtype: int
        """
        return self._initial_number_of_pieces

    @initial_number_of_pieces.setter
    def initial_number_of_pieces(self, initial_number_of_pieces):
        """Sets the initial_number_of_pieces of this WeeklySupplyLineCounter.


        :param initial_number_of_pieces: The initial_number_of_pieces of this WeeklySupplyLineCounter.  # noqa: E501
        :type: int
        """
        if initial_number_of_pieces is None:
            raise ValueError("Invalid value for `initial_number_of_pieces`, must not be `None`")  # noqa: E501

        self._initial_number_of_pieces = initial_number_of_pieces

    @property
    def claimed_number_of_pieces(self):
        """Gets the claimed_number_of_pieces of this WeeklySupplyLineCounter.  # noqa: E501


        :return: The claimed_number_of_pieces of this WeeklySupplyLineCounter.  # noqa: E501
        :rtype: int
        """
        return self._claimed_number_of_pieces

    @claimed_number_of_pieces.setter
    def claimed_number_of_pieces(self, claimed_number_of_pieces):
        """Sets the claimed_number_of_pieces of this WeeklySupplyLineCounter.


        :param claimed_number_of_pieces: The claimed_number_of_pieces of this WeeklySupplyLineCounter.  # noqa: E501
        :type: int
        """
        if claimed_number_of_pieces is None:
            raise ValueError("Invalid value for `claimed_number_of_pieces`, must not be `None`")  # noqa: E501

        self._claimed_number_of_pieces = claimed_number_of_pieces

    @property
    def added(self):
        """Gets the added of this WeeklySupplyLineCounter.  # noqa: E501


        :return: The added of this WeeklySupplyLineCounter.  # noqa: E501
        :rtype: datetime
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this WeeklySupplyLineCounter.


        :param added: The added of this WeeklySupplyLineCounter.  # noqa: E501
        :type: datetime
        """
        if added is None:
            raise ValueError("Invalid value for `added`, must not be `None`")  # noqa: E501

        self._added = added

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
        if issubclass(WeeklySupplyLineCounter, dict):
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
        if not isinstance(other, WeeklySupplyLineCounter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
