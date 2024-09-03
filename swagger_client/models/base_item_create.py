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

class BaseItemCreate(object):
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
        'base_item_id': 'str',
        'base_item_name': 'str',
        'base_item_type': 'BaseItemType',
        'seasonal_periods': 'list[SeasonalPeriod]',
        'image_url': 'str'
    }

    attribute_map = {
        'base_item_id': 'baseItemId',
        'base_item_name': 'baseItemName',
        'base_item_type': 'baseItemType',
        'seasonal_periods': 'seasonalPeriods',
        'image_url': 'imageUrl'
    }

    def __init__(self, base_item_id=None, base_item_name=None, base_item_type=None, seasonal_periods=None, image_url=None):  # noqa: E501
        """BaseItemCreate - a model defined in Swagger"""  # noqa: E501
        self._base_item_id = None
        self._base_item_name = None
        self._base_item_type = None
        self._seasonal_periods = None
        self._image_url = None
        self.discriminator = None
        self.base_item_id = base_item_id
        self.base_item_name = base_item_name
        self.base_item_type = base_item_type
        if seasonal_periods is not None:
            self.seasonal_periods = seasonal_periods
        if image_url is not None:
            self.image_url = image_url

    @property
    def base_item_id(self):
        """Gets the base_item_id of this BaseItemCreate.  # noqa: E501


        :return: The base_item_id of this BaseItemCreate.  # noqa: E501
        :rtype: str
        """
        return self._base_item_id

    @base_item_id.setter
    def base_item_id(self, base_item_id):
        """Sets the base_item_id of this BaseItemCreate.


        :param base_item_id: The base_item_id of this BaseItemCreate.  # noqa: E501
        :type: str
        """
        if base_item_id is None:
            raise ValueError("Invalid value for `base_item_id`, must not be `None`")  # noqa: E501

        self._base_item_id = base_item_id

    @property
    def base_item_name(self):
        """Gets the base_item_name of this BaseItemCreate.  # noqa: E501


        :return: The base_item_name of this BaseItemCreate.  # noqa: E501
        :rtype: str
        """
        return self._base_item_name

    @base_item_name.setter
    def base_item_name(self, base_item_name):
        """Sets the base_item_name of this BaseItemCreate.


        :param base_item_name: The base_item_name of this BaseItemCreate.  # noqa: E501
        :type: str
        """
        if base_item_name is None:
            raise ValueError("Invalid value for `base_item_name`, must not be `None`")  # noqa: E501

        self._base_item_name = base_item_name

    @property
    def base_item_type(self):
        """Gets the base_item_type of this BaseItemCreate.  # noqa: E501


        :return: The base_item_type of this BaseItemCreate.  # noqa: E501
        :rtype: BaseItemType
        """
        return self._base_item_type

    @base_item_type.setter
    def base_item_type(self, base_item_type):
        """Sets the base_item_type of this BaseItemCreate.


        :param base_item_type: The base_item_type of this BaseItemCreate.  # noqa: E501
        :type: BaseItemType
        """
        if base_item_type is None:
            raise ValueError("Invalid value for `base_item_type`, must not be `None`")  # noqa: E501

        self._base_item_type = base_item_type

    @property
    def seasonal_periods(self):
        """Gets the seasonal_periods of this BaseItemCreate.  # noqa: E501


        :return: The seasonal_periods of this BaseItemCreate.  # noqa: E501
        :rtype: list[SeasonalPeriod]
        """
        return self._seasonal_periods

    @seasonal_periods.setter
    def seasonal_periods(self, seasonal_periods):
        """Sets the seasonal_periods of this BaseItemCreate.


        :param seasonal_periods: The seasonal_periods of this BaseItemCreate.  # noqa: E501
        :type: list[SeasonalPeriod]
        """

        self._seasonal_periods = seasonal_periods

    @property
    def image_url(self):
        """Gets the image_url of this BaseItemCreate.  # noqa: E501

        Image URLs posted as Floriday media must conform with the following format https://image.floriday.io/.  # noqa: E501

        :return: The image_url of this BaseItemCreate.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this BaseItemCreate.

        Image URLs posted as Floriday media must conform with the following format https://image.floriday.io/.  # noqa: E501

        :param image_url: The image_url of this BaseItemCreate.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

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
        if issubclass(BaseItemCreate, dict):
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
        if not isinstance(other, BaseItemCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
