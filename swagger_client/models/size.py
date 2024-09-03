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

class Size(object):
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
        'width_in_mm': 'int',
        'height_in_mm': 'int'
    }

    attribute_map = {
        'width_in_mm': 'widthInMm',
        'height_in_mm': 'heightInMm'
    }

    def __init__(self, width_in_mm=None, height_in_mm=None):  # noqa: E501
        """Size - a model defined in Swagger"""  # noqa: E501
        self._width_in_mm = None
        self._height_in_mm = None
        self.discriminator = None
        self.width_in_mm = width_in_mm
        self.height_in_mm = height_in_mm

    @property
    def width_in_mm(self):
        """Gets the width_in_mm of this Size.  # noqa: E501


        :return: The width_in_mm of this Size.  # noqa: E501
        :rtype: int
        """
        return self._width_in_mm

    @width_in_mm.setter
    def width_in_mm(self, width_in_mm):
        """Sets the width_in_mm of this Size.


        :param width_in_mm: The width_in_mm of this Size.  # noqa: E501
        :type: int
        """
        if width_in_mm is None:
            raise ValueError("Invalid value for `width_in_mm`, must not be `None`")  # noqa: E501

        self._width_in_mm = width_in_mm

    @property
    def height_in_mm(self):
        """Gets the height_in_mm of this Size.  # noqa: E501


        :return: The height_in_mm of this Size.  # noqa: E501
        :rtype: int
        """
        return self._height_in_mm

    @height_in_mm.setter
    def height_in_mm(self, height_in_mm):
        """Sets the height_in_mm of this Size.


        :param height_in_mm: The height_in_mm of this Size.  # noqa: E501
        :type: int
        """
        if height_in_mm is None:
            raise ValueError("Invalid value for `height_in_mm`, must not be `None`")  # noqa: E501

        self._height_in_mm = height_in_mm

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
        if issubclass(Size, dict):
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
        if not isinstance(other, Size):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
