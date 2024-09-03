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

class TradeSetting(object):
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
        'is_active': 'bool',
        'exempted_organization_ids': 'list[str]',
        'last_modified': 'datetime'
    }

    attribute_map = {
        'is_active': 'isActive',
        'exempted_organization_ids': 'exemptedOrganizationIds',
        'last_modified': 'lastModified'
    }

    def __init__(self, is_active=None, exempted_organization_ids=None, last_modified=None):  # noqa: E501
        """TradeSetting - a model defined in Swagger"""  # noqa: E501
        self._is_active = None
        self._exempted_organization_ids = None
        self._last_modified = None
        self.discriminator = None
        self.is_active = is_active
        self.exempted_organization_ids = exempted_organization_ids
        if last_modified is not None:
            self.last_modified = last_modified

    @property
    def is_active(self):
        """Gets the is_active of this TradeSetting.  # noqa: E501


        :return: The is_active of this TradeSetting.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this TradeSetting.


        :param is_active: The is_active of this TradeSetting.  # noqa: E501
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def exempted_organization_ids(self):
        """Gets the exempted_organization_ids of this TradeSetting.  # noqa: E501


        :return: The exempted_organization_ids of this TradeSetting.  # noqa: E501
        :rtype: list[str]
        """
        return self._exempted_organization_ids

    @exempted_organization_ids.setter
    def exempted_organization_ids(self, exempted_organization_ids):
        """Sets the exempted_organization_ids of this TradeSetting.


        :param exempted_organization_ids: The exempted_organization_ids of this TradeSetting.  # noqa: E501
        :type: list[str]
        """
        if exempted_organization_ids is None:
            raise ValueError("Invalid value for `exempted_organization_ids`, must not be `None`")  # noqa: E501

        self._exempted_organization_ids = exempted_organization_ids

    @property
    def last_modified(self):
        """Gets the last_modified of this TradeSetting.  # noqa: E501


        :return: The last_modified of this TradeSetting.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this TradeSetting.


        :param last_modified: The last_modified of this TradeSetting.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

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
        if issubclass(TradeSetting, dict):
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
        if not isinstance(other, TradeSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
