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

class AdditionalStickerServiceInformation(object):
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
        'sticker_type': 'AdditionalStickerServiceType',
        'deliver_separately': 'bool',
        'supported_sticker_sizes': 'list[Size]',
        'is_default': 'bool'
    }

    attribute_map = {
        'sticker_type': 'stickerType',
        'deliver_separately': 'deliverSeparately',
        'supported_sticker_sizes': 'supportedStickerSizes',
        'is_default': 'isDefault'
    }

    def __init__(self, sticker_type=None, deliver_separately=None, supported_sticker_sizes=None, is_default=None):  # noqa: E501
        """AdditionalStickerServiceInformation - a model defined in Swagger"""  # noqa: E501
        self._sticker_type = None
        self._deliver_separately = None
        self._supported_sticker_sizes = None
        self._is_default = None
        self.discriminator = None
        self.sticker_type = sticker_type
        self.deliver_separately = deliver_separately
        self.supported_sticker_sizes = supported_sticker_sizes
        self.is_default = is_default

    @property
    def sticker_type(self):
        """Gets the sticker_type of this AdditionalStickerServiceInformation.  # noqa: E501


        :return: The sticker_type of this AdditionalStickerServiceInformation.  # noqa: E501
        :rtype: AdditionalStickerServiceType
        """
        return self._sticker_type

    @sticker_type.setter
    def sticker_type(self, sticker_type):
        """Sets the sticker_type of this AdditionalStickerServiceInformation.


        :param sticker_type: The sticker_type of this AdditionalStickerServiceInformation.  # noqa: E501
        :type: AdditionalStickerServiceType
        """
        if sticker_type is None:
            raise ValueError("Invalid value for `sticker_type`, must not be `None`")  # noqa: E501

        self._sticker_type = sticker_type

    @property
    def deliver_separately(self):
        """Gets the deliver_separately of this AdditionalStickerServiceInformation.  # noqa: E501


        :return: The deliver_separately of this AdditionalStickerServiceInformation.  # noqa: E501
        :rtype: bool
        """
        return self._deliver_separately

    @deliver_separately.setter
    def deliver_separately(self, deliver_separately):
        """Sets the deliver_separately of this AdditionalStickerServiceInformation.


        :param deliver_separately: The deliver_separately of this AdditionalStickerServiceInformation.  # noqa: E501
        :type: bool
        """
        if deliver_separately is None:
            raise ValueError("Invalid value for `deliver_separately`, must not be `None`")  # noqa: E501

        self._deliver_separately = deliver_separately

    @property
    def supported_sticker_sizes(self):
        """Gets the supported_sticker_sizes of this AdditionalStickerServiceInformation.  # noqa: E501


        :return: The supported_sticker_sizes of this AdditionalStickerServiceInformation.  # noqa: E501
        :rtype: list[Size]
        """
        return self._supported_sticker_sizes

    @supported_sticker_sizes.setter
    def supported_sticker_sizes(self, supported_sticker_sizes):
        """Sets the supported_sticker_sizes of this AdditionalStickerServiceInformation.


        :param supported_sticker_sizes: The supported_sticker_sizes of this AdditionalStickerServiceInformation.  # noqa: E501
        :type: list[Size]
        """
        if supported_sticker_sizes is None:
            raise ValueError("Invalid value for `supported_sticker_sizes`, must not be `None`")  # noqa: E501

        self._supported_sticker_sizes = supported_sticker_sizes

    @property
    def is_default(self):
        """Gets the is_default of this AdditionalStickerServiceInformation.  # noqa: E501


        :return: The is_default of this AdditionalStickerServiceInformation.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this AdditionalStickerServiceInformation.


        :param is_default: The is_default of this AdditionalStickerServiceInformation.  # noqa: E501
        :type: bool
        """
        if is_default is None:
            raise ValueError("Invalid value for `is_default`, must not be `None`")  # noqa: E501

        self._is_default = is_default

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
        if issubclass(AdditionalStickerServiceInformation, dict):
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
        if not isinstance(other, AdditionalStickerServiceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
