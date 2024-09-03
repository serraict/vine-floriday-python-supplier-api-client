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

class SalesOrderMutables(object):
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
        'custom_package_id': 'str',
        'incoterm': 'AllOfSalesOrderMutablesIncoterm',
        'number_of_pieces': 'int',
        'pieces_per_package': 'int',
        'vbn_package_code': 'int',
        'price_per_piece': 'float',
        'delivery_price_per_piece': 'float',
        'total_price_per_piece': 'float'
    }

    attribute_map = {
        'custom_package_id': 'customPackageId',
        'incoterm': 'incoterm',
        'number_of_pieces': 'numberOfPieces',
        'pieces_per_package': 'piecesPerPackage',
        'vbn_package_code': 'vbnPackageCode',
        'price_per_piece': 'pricePerPiece',
        'delivery_price_per_piece': 'deliveryPricePerPiece',
        'total_price_per_piece': 'totalPricePerPiece'
    }

    def __init__(self, custom_package_id=None, incoterm=None, number_of_pieces=None, pieces_per_package=None, vbn_package_code=None, price_per_piece=None, delivery_price_per_piece=None, total_price_per_piece=None):  # noqa: E501
        """SalesOrderMutables - a model defined in Swagger"""  # noqa: E501
        self._custom_package_id = None
        self._incoterm = None
        self._number_of_pieces = None
        self._pieces_per_package = None
        self._vbn_package_code = None
        self._price_per_piece = None
        self._delivery_price_per_piece = None
        self._total_price_per_piece = None
        self.discriminator = None
        if custom_package_id is not None:
            self.custom_package_id = custom_package_id
        if incoterm is not None:
            self.incoterm = incoterm
        self.number_of_pieces = number_of_pieces
        self.pieces_per_package = pieces_per_package
        self.vbn_package_code = vbn_package_code
        self.price_per_piece = price_per_piece
        self.delivery_price_per_piece = delivery_price_per_piece
        self.total_price_per_piece = total_price_per_piece

    @property
    def custom_package_id(self):
        """Gets the custom_package_id of this SalesOrderMutables.  # noqa: E501


        :return: The custom_package_id of this SalesOrderMutables.  # noqa: E501
        :rtype: str
        """
        return self._custom_package_id

    @custom_package_id.setter
    def custom_package_id(self, custom_package_id):
        """Sets the custom_package_id of this SalesOrderMutables.


        :param custom_package_id: The custom_package_id of this SalesOrderMutables.  # noqa: E501
        :type: str
        """

        self._custom_package_id = custom_package_id

    @property
    def incoterm(self):
        """Gets the incoterm of this SalesOrderMutables.  # noqa: E501

        Incoterm is null only in corrections made before the second quarter of 2023  # noqa: E501

        :return: The incoterm of this SalesOrderMutables.  # noqa: E501
        :rtype: AllOfSalesOrderMutablesIncoterm
        """
        return self._incoterm

    @incoterm.setter
    def incoterm(self, incoterm):
        """Sets the incoterm of this SalesOrderMutables.

        Incoterm is null only in corrections made before the second quarter of 2023  # noqa: E501

        :param incoterm: The incoterm of this SalesOrderMutables.  # noqa: E501
        :type: AllOfSalesOrderMutablesIncoterm
        """

        self._incoterm = incoterm

    @property
    def number_of_pieces(self):
        """Gets the number_of_pieces of this SalesOrderMutables.  # noqa: E501


        :return: The number_of_pieces of this SalesOrderMutables.  # noqa: E501
        :rtype: int
        """
        return self._number_of_pieces

    @number_of_pieces.setter
    def number_of_pieces(self, number_of_pieces):
        """Sets the number_of_pieces of this SalesOrderMutables.


        :param number_of_pieces: The number_of_pieces of this SalesOrderMutables.  # noqa: E501
        :type: int
        """
        if number_of_pieces is None:
            raise ValueError("Invalid value for `number_of_pieces`, must not be `None`")  # noqa: E501

        self._number_of_pieces = number_of_pieces

    @property
    def pieces_per_package(self):
        """Gets the pieces_per_package of this SalesOrderMutables.  # noqa: E501


        :return: The pieces_per_package of this SalesOrderMutables.  # noqa: E501
        :rtype: int
        """
        return self._pieces_per_package

    @pieces_per_package.setter
    def pieces_per_package(self, pieces_per_package):
        """Sets the pieces_per_package of this SalesOrderMutables.


        :param pieces_per_package: The pieces_per_package of this SalesOrderMutables.  # noqa: E501
        :type: int
        """
        if pieces_per_package is None:
            raise ValueError("Invalid value for `pieces_per_package`, must not be `None`")  # noqa: E501

        self._pieces_per_package = pieces_per_package

    @property
    def vbn_package_code(self):
        """Gets the vbn_package_code of this SalesOrderMutables.  # noqa: E501


        :return: The vbn_package_code of this SalesOrderMutables.  # noqa: E501
        :rtype: int
        """
        return self._vbn_package_code

    @vbn_package_code.setter
    def vbn_package_code(self, vbn_package_code):
        """Sets the vbn_package_code of this SalesOrderMutables.


        :param vbn_package_code: The vbn_package_code of this SalesOrderMutables.  # noqa: E501
        :type: int
        """
        if vbn_package_code is None:
            raise ValueError("Invalid value for `vbn_package_code`, must not be `None`")  # noqa: E501

        self._vbn_package_code = vbn_package_code

    @property
    def price_per_piece(self):
        """Gets the price_per_piece of this SalesOrderMutables.  # noqa: E501


        :return: The price_per_piece of this SalesOrderMutables.  # noqa: E501
        :rtype: float
        """
        return self._price_per_piece

    @price_per_piece.setter
    def price_per_piece(self, price_per_piece):
        """Sets the price_per_piece of this SalesOrderMutables.


        :param price_per_piece: The price_per_piece of this SalesOrderMutables.  # noqa: E501
        :type: float
        """
        if price_per_piece is None:
            raise ValueError("Invalid value for `price_per_piece`, must not be `None`")  # noqa: E501

        self._price_per_piece = price_per_piece

    @property
    def delivery_price_per_piece(self):
        """Gets the delivery_price_per_piece of this SalesOrderMutables.  # noqa: E501


        :return: The delivery_price_per_piece of this SalesOrderMutables.  # noqa: E501
        :rtype: float
        """
        return self._delivery_price_per_piece

    @delivery_price_per_piece.setter
    def delivery_price_per_piece(self, delivery_price_per_piece):
        """Sets the delivery_price_per_piece of this SalesOrderMutables.


        :param delivery_price_per_piece: The delivery_price_per_piece of this SalesOrderMutables.  # noqa: E501
        :type: float
        """
        if delivery_price_per_piece is None:
            raise ValueError("Invalid value for `delivery_price_per_piece`, must not be `None`")  # noqa: E501

        self._delivery_price_per_piece = delivery_price_per_piece

    @property
    def total_price_per_piece(self):
        """Gets the total_price_per_piece of this SalesOrderMutables.  # noqa: E501


        :return: The total_price_per_piece of this SalesOrderMutables.  # noqa: E501
        :rtype: float
        """
        return self._total_price_per_piece

    @total_price_per_piece.setter
    def total_price_per_piece(self, total_price_per_piece):
        """Sets the total_price_per_piece of this SalesOrderMutables.


        :param total_price_per_piece: The total_price_per_piece of this SalesOrderMutables.  # noqa: E501
        :type: float
        """
        if total_price_per_piece is None:
            raise ValueError("Invalid value for `total_price_per_piece`, must not be `None`")  # noqa: E501

        self._total_price_per_piece = total_price_per_piece

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
        if issubclass(SalesOrderMutables, dict):
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
        if not isinstance(other, SalesOrderMutables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
