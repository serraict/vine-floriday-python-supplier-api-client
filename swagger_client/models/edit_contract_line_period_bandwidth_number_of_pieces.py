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

class EditContractLinePeriodBandwidthNumberOfPieces(object):
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
        'lower_margin_number_of_pieces': 'int',
        'upper_margin_number_of_pieces': 'int',
        'lower_margin_percentage': 'int',
        'upper_margin_percentage': 'int'
    }

    attribute_map = {
        'lower_margin_number_of_pieces': 'lowerMarginNumberOfPieces',
        'upper_margin_number_of_pieces': 'upperMarginNumberOfPieces',
        'lower_margin_percentage': 'lowerMarginPercentage',
        'upper_margin_percentage': 'upperMarginPercentage'
    }

    def __init__(self, lower_margin_number_of_pieces=None, upper_margin_number_of_pieces=None, lower_margin_percentage=None, upper_margin_percentage=None):  # noqa: E501
        """EditContractLinePeriodBandwidthNumberOfPieces - a model defined in Swagger"""  # noqa: E501
        self._lower_margin_number_of_pieces = None
        self._upper_margin_number_of_pieces = None
        self._lower_margin_percentage = None
        self._upper_margin_percentage = None
        self.discriminator = None
        if lower_margin_number_of_pieces is not None:
            self.lower_margin_number_of_pieces = lower_margin_number_of_pieces
        if upper_margin_number_of_pieces is not None:
            self.upper_margin_number_of_pieces = upper_margin_number_of_pieces
        if lower_margin_percentage is not None:
            self.lower_margin_percentage = lower_margin_percentage
        if upper_margin_percentage is not None:
            self.upper_margin_percentage = upper_margin_percentage

    @property
    def lower_margin_number_of_pieces(self):
        """Gets the lower_margin_number_of_pieces of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501


        :return: The lower_margin_number_of_pieces of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501
        :rtype: int
        """
        return self._lower_margin_number_of_pieces

    @lower_margin_number_of_pieces.setter
    def lower_margin_number_of_pieces(self, lower_margin_number_of_pieces):
        """Sets the lower_margin_number_of_pieces of this EditContractLinePeriodBandwidthNumberOfPieces.


        :param lower_margin_number_of_pieces: The lower_margin_number_of_pieces of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501
        :type: int
        """

        self._lower_margin_number_of_pieces = lower_margin_number_of_pieces

    @property
    def upper_margin_number_of_pieces(self):
        """Gets the upper_margin_number_of_pieces of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501


        :return: The upper_margin_number_of_pieces of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501
        :rtype: int
        """
        return self._upper_margin_number_of_pieces

    @upper_margin_number_of_pieces.setter
    def upper_margin_number_of_pieces(self, upper_margin_number_of_pieces):
        """Sets the upper_margin_number_of_pieces of this EditContractLinePeriodBandwidthNumberOfPieces.


        :param upper_margin_number_of_pieces: The upper_margin_number_of_pieces of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501
        :type: int
        """

        self._upper_margin_number_of_pieces = upper_margin_number_of_pieces

    @property
    def lower_margin_percentage(self):
        """Gets the lower_margin_percentage of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501


        :return: The lower_margin_percentage of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501
        :rtype: int
        """
        return self._lower_margin_percentage

    @lower_margin_percentage.setter
    def lower_margin_percentage(self, lower_margin_percentage):
        """Sets the lower_margin_percentage of this EditContractLinePeriodBandwidthNumberOfPieces.


        :param lower_margin_percentage: The lower_margin_percentage of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501
        :type: int
        """

        self._lower_margin_percentage = lower_margin_percentage

    @property
    def upper_margin_percentage(self):
        """Gets the upper_margin_percentage of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501


        :return: The upper_margin_percentage of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501
        :rtype: int
        """
        return self._upper_margin_percentage

    @upper_margin_percentage.setter
    def upper_margin_percentage(self, upper_margin_percentage):
        """Sets the upper_margin_percentage of this EditContractLinePeriodBandwidthNumberOfPieces.


        :param upper_margin_percentage: The upper_margin_percentage of this EditContractLinePeriodBandwidthNumberOfPieces.  # noqa: E501
        :type: int
        """

        self._upper_margin_percentage = upper_margin_percentage

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
        if issubclass(EditContractLinePeriodBandwidthNumberOfPieces, dict):
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
        if not isinstance(other, EditContractLinePeriodBandwidthNumberOfPieces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
