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

class ContractLinePeriod(object):
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
        'contract_line_period_id': 'str',
        'start_date_time': 'datetime',
        'end_date_time': 'datetime',
        'price_per_piece': 'float',
        'price_per_piece_margin': 'ContractLinePeriodBandwidthPricePerPiece',
        'number_of_pieces': 'int',
        'number_of_pieces_margin': 'ContractLinePeriodBandwidthNumberOfPieces'
    }

    attribute_map = {
        'contract_line_period_id': 'contractLinePeriodId',
        'start_date_time': 'startDateTime',
        'end_date_time': 'endDateTime',
        'price_per_piece': 'pricePerPiece',
        'price_per_piece_margin': 'pricePerPieceMargin',
        'number_of_pieces': 'numberOfPieces',
        'number_of_pieces_margin': 'numberOfPiecesMargin'
    }

    def __init__(self, contract_line_period_id=None, start_date_time=None, end_date_time=None, price_per_piece=None, price_per_piece_margin=None, number_of_pieces=None, number_of_pieces_margin=None):  # noqa: E501
        """ContractLinePeriod - a model defined in Swagger"""  # noqa: E501
        self._contract_line_period_id = None
        self._start_date_time = None
        self._end_date_time = None
        self._price_per_piece = None
        self._price_per_piece_margin = None
        self._number_of_pieces = None
        self._number_of_pieces_margin = None
        self.discriminator = None
        self.contract_line_period_id = contract_line_period_id
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.price_per_piece = price_per_piece
        if price_per_piece_margin is not None:
            self.price_per_piece_margin = price_per_piece_margin
        self.number_of_pieces = number_of_pieces
        if number_of_pieces_margin is not None:
            self.number_of_pieces_margin = number_of_pieces_margin

    @property
    def contract_line_period_id(self):
        """Gets the contract_line_period_id of this ContractLinePeriod.  # noqa: E501


        :return: The contract_line_period_id of this ContractLinePeriod.  # noqa: E501
        :rtype: str
        """
        return self._contract_line_period_id

    @contract_line_period_id.setter
    def contract_line_period_id(self, contract_line_period_id):
        """Sets the contract_line_period_id of this ContractLinePeriod.


        :param contract_line_period_id: The contract_line_period_id of this ContractLinePeriod.  # noqa: E501
        :type: str
        """
        if contract_line_period_id is None:
            raise ValueError("Invalid value for `contract_line_period_id`, must not be `None`")  # noqa: E501

        self._contract_line_period_id = contract_line_period_id

    @property
    def start_date_time(self):
        """Gets the start_date_time of this ContractLinePeriod.  # noqa: E501


        :return: The start_date_time of this ContractLinePeriod.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this ContractLinePeriod.


        :param start_date_time: The start_date_time of this ContractLinePeriod.  # noqa: E501
        :type: datetime
        """
        if start_date_time is None:
            raise ValueError("Invalid value for `start_date_time`, must not be `None`")  # noqa: E501

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this ContractLinePeriod.  # noqa: E501


        :return: The end_date_time of this ContractLinePeriod.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this ContractLinePeriod.


        :param end_date_time: The end_date_time of this ContractLinePeriod.  # noqa: E501
        :type: datetime
        """
        if end_date_time is None:
            raise ValueError("Invalid value for `end_date_time`, must not be `None`")  # noqa: E501

        self._end_date_time = end_date_time

    @property
    def price_per_piece(self):
        """Gets the price_per_piece of this ContractLinePeriod.  # noqa: E501


        :return: The price_per_piece of this ContractLinePeriod.  # noqa: E501
        :rtype: float
        """
        return self._price_per_piece

    @price_per_piece.setter
    def price_per_piece(self, price_per_piece):
        """Sets the price_per_piece of this ContractLinePeriod.


        :param price_per_piece: The price_per_piece of this ContractLinePeriod.  # noqa: E501
        :type: float
        """
        if price_per_piece is None:
            raise ValueError("Invalid value for `price_per_piece`, must not be `None`")  # noqa: E501

        self._price_per_piece = price_per_piece

    @property
    def price_per_piece_margin(self):
        """Gets the price_per_piece_margin of this ContractLinePeriod.  # noqa: E501


        :return: The price_per_piece_margin of this ContractLinePeriod.  # noqa: E501
        :rtype: ContractLinePeriodBandwidthPricePerPiece
        """
        return self._price_per_piece_margin

    @price_per_piece_margin.setter
    def price_per_piece_margin(self, price_per_piece_margin):
        """Sets the price_per_piece_margin of this ContractLinePeriod.


        :param price_per_piece_margin: The price_per_piece_margin of this ContractLinePeriod.  # noqa: E501
        :type: ContractLinePeriodBandwidthPricePerPiece
        """

        self._price_per_piece_margin = price_per_piece_margin

    @property
    def number_of_pieces(self):
        """Gets the number_of_pieces of this ContractLinePeriod.  # noqa: E501


        :return: The number_of_pieces of this ContractLinePeriod.  # noqa: E501
        :rtype: int
        """
        return self._number_of_pieces

    @number_of_pieces.setter
    def number_of_pieces(self, number_of_pieces):
        """Sets the number_of_pieces of this ContractLinePeriod.


        :param number_of_pieces: The number_of_pieces of this ContractLinePeriod.  # noqa: E501
        :type: int
        """
        if number_of_pieces is None:
            raise ValueError("Invalid value for `number_of_pieces`, must not be `None`")  # noqa: E501

        self._number_of_pieces = number_of_pieces

    @property
    def number_of_pieces_margin(self):
        """Gets the number_of_pieces_margin of this ContractLinePeriod.  # noqa: E501


        :return: The number_of_pieces_margin of this ContractLinePeriod.  # noqa: E501
        :rtype: ContractLinePeriodBandwidthNumberOfPieces
        """
        return self._number_of_pieces_margin

    @number_of_pieces_margin.setter
    def number_of_pieces_margin(self, number_of_pieces_margin):
        """Sets the number_of_pieces_margin of this ContractLinePeriod.


        :param number_of_pieces_margin: The number_of_pieces_margin of this ContractLinePeriod.  # noqa: E501
        :type: ContractLinePeriodBandwidthNumberOfPieces
        """

        self._number_of_pieces_margin = number_of_pieces_margin

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
        if issubclass(ContractLinePeriod, dict):
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
        if not isinstance(other, ContractLinePeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
