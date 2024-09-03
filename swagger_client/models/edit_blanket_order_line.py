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

class EditBlanketOrderLine(object):
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
        'blanket_order_line_id': 'str',
        'contract_line_period_id': 'str',
        'trade_item_id': 'str',
        'batch_id': 'str',
        'despatch_warehouse_id': 'str',
        'additional_service_ids': 'list[str]',
        'customer_order_reference': 'str',
        'packing_configuration': 'PackingConfigurationBase',
        'number_of_pieces': 'int',
        'price_per_piece': 'Price',
        'delivery_location_gln': 'str',
        'incoterm': 'Incoterm'
    }

    attribute_map = {
        'blanket_order_line_id': 'blanketOrderLineId',
        'contract_line_period_id': 'contractLinePeriodId',
        'trade_item_id': 'tradeItemId',
        'batch_id': 'batchId',
        'despatch_warehouse_id': 'despatchWarehouseId',
        'additional_service_ids': 'additionalServiceIds',
        'customer_order_reference': 'customerOrderReference',
        'packing_configuration': 'packingConfiguration',
        'number_of_pieces': 'numberOfPieces',
        'price_per_piece': 'pricePerPiece',
        'delivery_location_gln': 'deliveryLocationGln',
        'incoterm': 'incoterm'
    }

    def __init__(self, blanket_order_line_id=None, contract_line_period_id=None, trade_item_id=None, batch_id=None, despatch_warehouse_id=None, additional_service_ids=None, customer_order_reference=None, packing_configuration=None, number_of_pieces=None, price_per_piece=None, delivery_location_gln=None, incoterm=None):  # noqa: E501
        """EditBlanketOrderLine - a model defined in Swagger"""  # noqa: E501
        self._blanket_order_line_id = None
        self._contract_line_period_id = None
        self._trade_item_id = None
        self._batch_id = None
        self._despatch_warehouse_id = None
        self._additional_service_ids = None
        self._customer_order_reference = None
        self._packing_configuration = None
        self._number_of_pieces = None
        self._price_per_piece = None
        self._delivery_location_gln = None
        self._incoterm = None
        self.discriminator = None
        self.blanket_order_line_id = blanket_order_line_id
        self.contract_line_period_id = contract_line_period_id
        self.trade_item_id = trade_item_id
        if batch_id is not None:
            self.batch_id = batch_id
        self.despatch_warehouse_id = despatch_warehouse_id
        if additional_service_ids is not None:
            self.additional_service_ids = additional_service_ids
        if customer_order_reference is not None:
            self.customer_order_reference = customer_order_reference
        self.packing_configuration = packing_configuration
        self.number_of_pieces = number_of_pieces
        self.price_per_piece = price_per_piece
        if delivery_location_gln is not None:
            self.delivery_location_gln = delivery_location_gln
        self.incoterm = incoterm

    @property
    def blanket_order_line_id(self):
        """Gets the blanket_order_line_id of this EditBlanketOrderLine.  # noqa: E501


        :return: The blanket_order_line_id of this EditBlanketOrderLine.  # noqa: E501
        :rtype: str
        """
        return self._blanket_order_line_id

    @blanket_order_line_id.setter
    def blanket_order_line_id(self, blanket_order_line_id):
        """Sets the blanket_order_line_id of this EditBlanketOrderLine.


        :param blanket_order_line_id: The blanket_order_line_id of this EditBlanketOrderLine.  # noqa: E501
        :type: str
        """
        if blanket_order_line_id is None:
            raise ValueError("Invalid value for `blanket_order_line_id`, must not be `None`")  # noqa: E501

        self._blanket_order_line_id = blanket_order_line_id

    @property
    def contract_line_period_id(self):
        """Gets the contract_line_period_id of this EditBlanketOrderLine.  # noqa: E501


        :return: The contract_line_period_id of this EditBlanketOrderLine.  # noqa: E501
        :rtype: str
        """
        return self._contract_line_period_id

    @contract_line_period_id.setter
    def contract_line_period_id(self, contract_line_period_id):
        """Sets the contract_line_period_id of this EditBlanketOrderLine.


        :param contract_line_period_id: The contract_line_period_id of this EditBlanketOrderLine.  # noqa: E501
        :type: str
        """
        if contract_line_period_id is None:
            raise ValueError("Invalid value for `contract_line_period_id`, must not be `None`")  # noqa: E501

        self._contract_line_period_id = contract_line_period_id

    @property
    def trade_item_id(self):
        """Gets the trade_item_id of this EditBlanketOrderLine.  # noqa: E501


        :return: The trade_item_id of this EditBlanketOrderLine.  # noqa: E501
        :rtype: str
        """
        return self._trade_item_id

    @trade_item_id.setter
    def trade_item_id(self, trade_item_id):
        """Sets the trade_item_id of this EditBlanketOrderLine.


        :param trade_item_id: The trade_item_id of this EditBlanketOrderLine.  # noqa: E501
        :type: str
        """
        if trade_item_id is None:
            raise ValueError("Invalid value for `trade_item_id`, must not be `None`")  # noqa: E501

        self._trade_item_id = trade_item_id

    @property
    def batch_id(self):
        """Gets the batch_id of this EditBlanketOrderLine.  # noqa: E501


        :return: The batch_id of this EditBlanketOrderLine.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this EditBlanketOrderLine.


        :param batch_id: The batch_id of this EditBlanketOrderLine.  # noqa: E501
        :type: str
        """

        self._batch_id = batch_id

    @property
    def despatch_warehouse_id(self):
        """Gets the despatch_warehouse_id of this EditBlanketOrderLine.  # noqa: E501


        :return: The despatch_warehouse_id of this EditBlanketOrderLine.  # noqa: E501
        :rtype: str
        """
        return self._despatch_warehouse_id

    @despatch_warehouse_id.setter
    def despatch_warehouse_id(self, despatch_warehouse_id):
        """Sets the despatch_warehouse_id of this EditBlanketOrderLine.


        :param despatch_warehouse_id: The despatch_warehouse_id of this EditBlanketOrderLine.  # noqa: E501
        :type: str
        """
        if despatch_warehouse_id is None:
            raise ValueError("Invalid value for `despatch_warehouse_id`, must not be `None`")  # noqa: E501

        self._despatch_warehouse_id = despatch_warehouse_id

    @property
    def additional_service_ids(self):
        """Gets the additional_service_ids of this EditBlanketOrderLine.  # noqa: E501


        :return: The additional_service_ids of this EditBlanketOrderLine.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_service_ids

    @additional_service_ids.setter
    def additional_service_ids(self, additional_service_ids):
        """Sets the additional_service_ids of this EditBlanketOrderLine.


        :param additional_service_ids: The additional_service_ids of this EditBlanketOrderLine.  # noqa: E501
        :type: list[str]
        """

        self._additional_service_ids = additional_service_ids

    @property
    def customer_order_reference(self):
        """Gets the customer_order_reference of this EditBlanketOrderLine.  # noqa: E501


        :return: The customer_order_reference of this EditBlanketOrderLine.  # noqa: E501
        :rtype: str
        """
        return self._customer_order_reference

    @customer_order_reference.setter
    def customer_order_reference(self, customer_order_reference):
        """Sets the customer_order_reference of this EditBlanketOrderLine.


        :param customer_order_reference: The customer_order_reference of this EditBlanketOrderLine.  # noqa: E501
        :type: str
        """

        self._customer_order_reference = customer_order_reference

    @property
    def packing_configuration(self):
        """Gets the packing_configuration of this EditBlanketOrderLine.  # noqa: E501


        :return: The packing_configuration of this EditBlanketOrderLine.  # noqa: E501
        :rtype: PackingConfigurationBase
        """
        return self._packing_configuration

    @packing_configuration.setter
    def packing_configuration(self, packing_configuration):
        """Sets the packing_configuration of this EditBlanketOrderLine.


        :param packing_configuration: The packing_configuration of this EditBlanketOrderLine.  # noqa: E501
        :type: PackingConfigurationBase
        """
        if packing_configuration is None:
            raise ValueError("Invalid value for `packing_configuration`, must not be `None`")  # noqa: E501

        self._packing_configuration = packing_configuration

    @property
    def number_of_pieces(self):
        """Gets the number_of_pieces of this EditBlanketOrderLine.  # noqa: E501


        :return: The number_of_pieces of this EditBlanketOrderLine.  # noqa: E501
        :rtype: int
        """
        return self._number_of_pieces

    @number_of_pieces.setter
    def number_of_pieces(self, number_of_pieces):
        """Sets the number_of_pieces of this EditBlanketOrderLine.


        :param number_of_pieces: The number_of_pieces of this EditBlanketOrderLine.  # noqa: E501
        :type: int
        """
        if number_of_pieces is None:
            raise ValueError("Invalid value for `number_of_pieces`, must not be `None`")  # noqa: E501

        self._number_of_pieces = number_of_pieces

    @property
    def price_per_piece(self):
        """Gets the price_per_piece of this EditBlanketOrderLine.  # noqa: E501


        :return: The price_per_piece of this EditBlanketOrderLine.  # noqa: E501
        :rtype: Price
        """
        return self._price_per_piece

    @price_per_piece.setter
    def price_per_piece(self, price_per_piece):
        """Sets the price_per_piece of this EditBlanketOrderLine.


        :param price_per_piece: The price_per_piece of this EditBlanketOrderLine.  # noqa: E501
        :type: Price
        """
        if price_per_piece is None:
            raise ValueError("Invalid value for `price_per_piece`, must not be `None`")  # noqa: E501

        self._price_per_piece = price_per_piece

    @property
    def delivery_location_gln(self):
        """Gets the delivery_location_gln of this EditBlanketOrderLine.  # noqa: E501


        :return: The delivery_location_gln of this EditBlanketOrderLine.  # noqa: E501
        :rtype: str
        """
        return self._delivery_location_gln

    @delivery_location_gln.setter
    def delivery_location_gln(self, delivery_location_gln):
        """Sets the delivery_location_gln of this EditBlanketOrderLine.


        :param delivery_location_gln: The delivery_location_gln of this EditBlanketOrderLine.  # noqa: E501
        :type: str
        """

        self._delivery_location_gln = delivery_location_gln

    @property
    def incoterm(self):
        """Gets the incoterm of this EditBlanketOrderLine.  # noqa: E501


        :return: The incoterm of this EditBlanketOrderLine.  # noqa: E501
        :rtype: Incoterm
        """
        return self._incoterm

    @incoterm.setter
    def incoterm(self, incoterm):
        """Sets the incoterm of this EditBlanketOrderLine.


        :param incoterm: The incoterm of this EditBlanketOrderLine.  # noqa: E501
        :type: Incoterm
        """
        if incoterm is None:
            raise ValueError("Invalid value for `incoterm`, must not be `None`")  # noqa: E501

        self._incoterm = incoterm

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
        if issubclass(EditBlanketOrderLine, dict):
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
        if not isinstance(other, EditBlanketOrderLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
