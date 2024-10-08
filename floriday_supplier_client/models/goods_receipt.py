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

class GoodsReceipt(object):
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
        'goods_receipt_id': 'str',
        'receipt_date_time': 'datetime',
        'sscc_codes': 'list[str]'
    }

    attribute_map = {
        'goods_receipt_id': 'goodsReceiptId',
        'receipt_date_time': 'receiptDateTime',
        'sscc_codes': 'ssccCodes'
    }

    def __init__(self, goods_receipt_id=None, receipt_date_time=None, sscc_codes=None):  # noqa: E501
        """GoodsReceipt - a model defined in Swagger"""  # noqa: E501
        self._goods_receipt_id = None
        self._receipt_date_time = None
        self._sscc_codes = None
        self.discriminator = None
        self.goods_receipt_id = goods_receipt_id
        self.receipt_date_time = receipt_date_time
        if sscc_codes is not None:
            self.sscc_codes = sscc_codes

    @property
    def goods_receipt_id(self):
        """Gets the goods_receipt_id of this GoodsReceipt.  # noqa: E501


        :return: The goods_receipt_id of this GoodsReceipt.  # noqa: E501
        :rtype: str
        """
        return self._goods_receipt_id

    @goods_receipt_id.setter
    def goods_receipt_id(self, goods_receipt_id):
        """Sets the goods_receipt_id of this GoodsReceipt.


        :param goods_receipt_id: The goods_receipt_id of this GoodsReceipt.  # noqa: E501
        :type: str
        """
        if goods_receipt_id is None:
            raise ValueError("Invalid value for `goods_receipt_id`, must not be `None`")  # noqa: E501

        self._goods_receipt_id = goods_receipt_id

    @property
    def receipt_date_time(self):
        """Gets the receipt_date_time of this GoodsReceipt.  # noqa: E501


        :return: The receipt_date_time of this GoodsReceipt.  # noqa: E501
        :rtype: datetime
        """
        return self._receipt_date_time

    @receipt_date_time.setter
    def receipt_date_time(self, receipt_date_time):
        """Sets the receipt_date_time of this GoodsReceipt.


        :param receipt_date_time: The receipt_date_time of this GoodsReceipt.  # noqa: E501
        :type: datetime
        """
        if receipt_date_time is None:
            raise ValueError("Invalid value for `receipt_date_time`, must not be `None`")  # noqa: E501

        self._receipt_date_time = receipt_date_time

    @property
    def sscc_codes(self):
        """Gets the sscc_codes of this GoodsReceipt.  # noqa: E501


        :return: The sscc_codes of this GoodsReceipt.  # noqa: E501
        :rtype: list[str]
        """
        return self._sscc_codes

    @sscc_codes.setter
    def sscc_codes(self, sscc_codes):
        """Sets the sscc_codes of this GoodsReceipt.


        :param sscc_codes: The sscc_codes of this GoodsReceipt.  # noqa: E501
        :type: list[str]
        """

        self._sscc_codes = sscc_codes

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
        if issubclass(GoodsReceipt, dict):
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
        if not isinstance(other, GoodsReceipt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
