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

class AddFulfillmentOrderCorrection(object):
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
        'correction_id': 'str',
        'delivery_location_gln': 'str',
        'load_carrier_corrections': 'list[AddLoadCarrierCorrection]'
    }

    attribute_map = {
        'correction_id': 'correctionId',
        'delivery_location_gln': 'deliveryLocationGln',
        'load_carrier_corrections': 'loadCarrierCorrections'
    }

    def __init__(self, correction_id=None, delivery_location_gln=None, load_carrier_corrections=None):  # noqa: E501
        """AddFulfillmentOrderCorrection - a model defined in Swagger"""  # noqa: E501
        self._correction_id = None
        self._delivery_location_gln = None
        self._load_carrier_corrections = None
        self.discriminator = None
        self.correction_id = correction_id
        if delivery_location_gln is not None:
            self.delivery_location_gln = delivery_location_gln
        self.load_carrier_corrections = load_carrier_corrections

    @property
    def correction_id(self):
        """Gets the correction_id of this AddFulfillmentOrderCorrection.  # noqa: E501


        :return: The correction_id of this AddFulfillmentOrderCorrection.  # noqa: E501
        :rtype: str
        """
        return self._correction_id

    @correction_id.setter
    def correction_id(self, correction_id):
        """Sets the correction_id of this AddFulfillmentOrderCorrection.


        :param correction_id: The correction_id of this AddFulfillmentOrderCorrection.  # noqa: E501
        :type: str
        """
        if correction_id is None:
            raise ValueError("Invalid value for `correction_id`, must not be `None`")  # noqa: E501

        self._correction_id = correction_id

    @property
    def delivery_location_gln(self):
        """Gets the delivery_location_gln of this AddFulfillmentOrderCorrection.  # noqa: E501


        :return: The delivery_location_gln of this AddFulfillmentOrderCorrection.  # noqa: E501
        :rtype: str
        """
        return self._delivery_location_gln

    @delivery_location_gln.setter
    def delivery_location_gln(self, delivery_location_gln):
        """Sets the delivery_location_gln of this AddFulfillmentOrderCorrection.


        :param delivery_location_gln: The delivery_location_gln of this AddFulfillmentOrderCorrection.  # noqa: E501
        :type: str
        """

        self._delivery_location_gln = delivery_location_gln

    @property
    def load_carrier_corrections(self):
        """Gets the load_carrier_corrections of this AddFulfillmentOrderCorrection.  # noqa: E501


        :return: The load_carrier_corrections of this AddFulfillmentOrderCorrection.  # noqa: E501
        :rtype: list[AddLoadCarrierCorrection]
        """
        return self._load_carrier_corrections

    @load_carrier_corrections.setter
    def load_carrier_corrections(self, load_carrier_corrections):
        """Sets the load_carrier_corrections of this AddFulfillmentOrderCorrection.


        :param load_carrier_corrections: The load_carrier_corrections of this AddFulfillmentOrderCorrection.  # noqa: E501
        :type: list[AddLoadCarrierCorrection]
        """
        if load_carrier_corrections is None:
            raise ValueError("Invalid value for `load_carrier_corrections`, must not be `None`")  # noqa: E501

        self._load_carrier_corrections = load_carrier_corrections

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
        if issubclass(AddFulfillmentOrderCorrection, dict):
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
        if not isinstance(other, AddFulfillmentOrderCorrection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
