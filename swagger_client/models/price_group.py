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

class PriceGroup(object):
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
        'price_group_id': 'str',
        'name': 'str',
        'type': 'PriceGroupType',
        'sales_unit': 'SalesUnit',
        'included_services': 'list[CommercialService]',
        'customers': 'list[str]',
        'is_deleted': 'bool',
        'last_modified_date_time': 'datetime',
        'sequence_number': 'int'
    }

    attribute_map = {
        'price_group_id': 'priceGroupId',
        'name': 'name',
        'type': 'type',
        'sales_unit': 'salesUnit',
        'included_services': 'includedServices',
        'customers': 'customers',
        'is_deleted': 'isDeleted',
        'last_modified_date_time': 'lastModifiedDateTime',
        'sequence_number': 'sequenceNumber'
    }

    def __init__(self, price_group_id=None, name=None, type=None, sales_unit=None, included_services=None, customers=None, is_deleted=None, last_modified_date_time=None, sequence_number=None):  # noqa: E501
        """PriceGroup - a model defined in Swagger"""  # noqa: E501
        self._price_group_id = None
        self._name = None
        self._type = None
        self._sales_unit = None
        self._included_services = None
        self._customers = None
        self._is_deleted = None
        self._last_modified_date_time = None
        self._sequence_number = None
        self.discriminator = None
        self.price_group_id = price_group_id
        self.name = name
        self.type = type
        self.sales_unit = sales_unit
        self.included_services = included_services
        self.customers = customers
        self.is_deleted = is_deleted
        self.last_modified_date_time = last_modified_date_time
        self.sequence_number = sequence_number

    @property
    def price_group_id(self):
        """Gets the price_group_id of this PriceGroup.  # noqa: E501


        :return: The price_group_id of this PriceGroup.  # noqa: E501
        :rtype: str
        """
        return self._price_group_id

    @price_group_id.setter
    def price_group_id(self, price_group_id):
        """Sets the price_group_id of this PriceGroup.


        :param price_group_id: The price_group_id of this PriceGroup.  # noqa: E501
        :type: str
        """
        if price_group_id is None:
            raise ValueError("Invalid value for `price_group_id`, must not be `None`")  # noqa: E501

        self._price_group_id = price_group_id

    @property
    def name(self):
        """Gets the name of this PriceGroup.  # noqa: E501


        :return: The name of this PriceGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PriceGroup.


        :param name: The name of this PriceGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this PriceGroup.  # noqa: E501


        :return: The type of this PriceGroup.  # noqa: E501
        :rtype: PriceGroupType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PriceGroup.


        :param type: The type of this PriceGroup.  # noqa: E501
        :type: PriceGroupType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def sales_unit(self):
        """Gets the sales_unit of this PriceGroup.  # noqa: E501


        :return: The sales_unit of this PriceGroup.  # noqa: E501
        :rtype: SalesUnit
        """
        return self._sales_unit

    @sales_unit.setter
    def sales_unit(self, sales_unit):
        """Sets the sales_unit of this PriceGroup.


        :param sales_unit: The sales_unit of this PriceGroup.  # noqa: E501
        :type: SalesUnit
        """
        if sales_unit is None:
            raise ValueError("Invalid value for `sales_unit`, must not be `None`")  # noqa: E501

        self._sales_unit = sales_unit

    @property
    def included_services(self):
        """Gets the included_services of this PriceGroup.  # noqa: E501


        :return: The included_services of this PriceGroup.  # noqa: E501
        :rtype: list[CommercialService]
        """
        return self._included_services

    @included_services.setter
    def included_services(self, included_services):
        """Sets the included_services of this PriceGroup.


        :param included_services: The included_services of this PriceGroup.  # noqa: E501
        :type: list[CommercialService]
        """
        if included_services is None:
            raise ValueError("Invalid value for `included_services`, must not be `None`")  # noqa: E501

        self._included_services = included_services

    @property
    def customers(self):
        """Gets the customers of this PriceGroup.  # noqa: E501


        :return: The customers of this PriceGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """Sets the customers of this PriceGroup.


        :param customers: The customers of this PriceGroup.  # noqa: E501
        :type: list[str]
        """
        if customers is None:
            raise ValueError("Invalid value for `customers`, must not be `None`")  # noqa: E501

        self._customers = customers

    @property
    def is_deleted(self):
        """Gets the is_deleted of this PriceGroup.  # noqa: E501


        :return: The is_deleted of this PriceGroup.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this PriceGroup.


        :param is_deleted: The is_deleted of this PriceGroup.  # noqa: E501
        :type: bool
        """
        if is_deleted is None:
            raise ValueError("Invalid value for `is_deleted`, must not be `None`")  # noqa: E501

        self._is_deleted = is_deleted

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this PriceGroup.  # noqa: E501


        :return: The last_modified_date_time of this PriceGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this PriceGroup.


        :param last_modified_date_time: The last_modified_date_time of this PriceGroup.  # noqa: E501
        :type: datetime
        """
        if last_modified_date_time is None:
            raise ValueError("Invalid value for `last_modified_date_time`, must not be `None`")  # noqa: E501

        self._last_modified_date_time = last_modified_date_time

    @property
    def sequence_number(self):
        """Gets the sequence_number of this PriceGroup.  # noqa: E501


        :return: The sequence_number of this PriceGroup.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this PriceGroup.


        :param sequence_number: The sequence_number of this PriceGroup.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501

        self._sequence_number = sequence_number

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
        if issubclass(PriceGroup, dict):
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
        if not isinstance(other, PriceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
