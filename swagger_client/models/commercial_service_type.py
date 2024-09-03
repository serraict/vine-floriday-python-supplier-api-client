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

class CommercialServiceType(object):
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
        'commercial_service_type_id': 'str',
        'commercial_service_type_name': 'str',
        'sequence_number': 'int'
    }

    attribute_map = {
        'commercial_service_type_id': 'commercialServiceTypeId',
        'commercial_service_type_name': 'commercialServiceTypeName',
        'sequence_number': 'sequenceNumber'
    }

    def __init__(self, commercial_service_type_id=None, commercial_service_type_name=None, sequence_number=None):  # noqa: E501
        """CommercialServiceType - a model defined in Swagger"""  # noqa: E501
        self._commercial_service_type_id = None
        self._commercial_service_type_name = None
        self._sequence_number = None
        self.discriminator = None
        self.commercial_service_type_id = commercial_service_type_id
        if commercial_service_type_name is not None:
            self.commercial_service_type_name = commercial_service_type_name
        self.sequence_number = sequence_number

    @property
    def commercial_service_type_id(self):
        """Gets the commercial_service_type_id of this CommercialServiceType.  # noqa: E501


        :return: The commercial_service_type_id of this CommercialServiceType.  # noqa: E501
        :rtype: str
        """
        return self._commercial_service_type_id

    @commercial_service_type_id.setter
    def commercial_service_type_id(self, commercial_service_type_id):
        """Sets the commercial_service_type_id of this CommercialServiceType.


        :param commercial_service_type_id: The commercial_service_type_id of this CommercialServiceType.  # noqa: E501
        :type: str
        """
        if commercial_service_type_id is None:
            raise ValueError("Invalid value for `commercial_service_type_id`, must not be `None`")  # noqa: E501

        self._commercial_service_type_id = commercial_service_type_id

    @property
    def commercial_service_type_name(self):
        """Gets the commercial_service_type_name of this CommercialServiceType.  # noqa: E501


        :return: The commercial_service_type_name of this CommercialServiceType.  # noqa: E501
        :rtype: str
        """
        return self._commercial_service_type_name

    @commercial_service_type_name.setter
    def commercial_service_type_name(self, commercial_service_type_name):
        """Sets the commercial_service_type_name of this CommercialServiceType.


        :param commercial_service_type_name: The commercial_service_type_name of this CommercialServiceType.  # noqa: E501
        :type: str
        """

        self._commercial_service_type_name = commercial_service_type_name

    @property
    def sequence_number(self):
        """Gets the sequence_number of this CommercialServiceType.  # noqa: E501


        :return: The sequence_number of this CommercialServiceType.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this CommercialServiceType.


        :param sequence_number: The sequence_number of this CommercialServiceType.  # noqa: E501
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
        if issubclass(CommercialServiceType, dict):
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
        if not isinstance(other, CommercialServiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
