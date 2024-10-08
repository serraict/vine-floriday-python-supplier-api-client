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

class BlanketOrder(object):
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
        'blanket_order_id': 'str',
        'contract_id': 'str',
        'delivery_date_time': 'datetime',
        'customer_organization_id': 'str',
        'carrier_organization_id': 'str',
        'status': 'BlanketOrderStatus',
        'blanket_order_lines': 'list[BlanketOrderLine]',
        'is_initiated_by_supplier': 'bool',
        'creation_date_time': 'datetime',
        'last_modified_date_time': 'datetime',
        'is_last_modified_by_supplier': 'bool',
        'sales_channel_interface': 'SalesChannelInterface',
        'sequence_number': 'int'
    }

    attribute_map = {
        'blanket_order_id': 'blanketOrderId',
        'contract_id': 'contractId',
        'delivery_date_time': 'deliveryDateTime',
        'customer_organization_id': 'customerOrganizationId',
        'carrier_organization_id': 'carrierOrganizationId',
        'status': 'status',
        'blanket_order_lines': 'blanketOrderLines',
        'is_initiated_by_supplier': 'isInitiatedBySupplier',
        'creation_date_time': 'creationDateTime',
        'last_modified_date_time': 'lastModifiedDateTime',
        'is_last_modified_by_supplier': 'isLastModifiedBySupplier',
        'sales_channel_interface': 'salesChannelInterface',
        'sequence_number': 'sequenceNumber'
    }

    def __init__(self, blanket_order_id=None, contract_id=None, delivery_date_time=None, customer_organization_id=None, carrier_organization_id=None, status=None, blanket_order_lines=None, is_initiated_by_supplier=None, creation_date_time=None, last_modified_date_time=None, is_last_modified_by_supplier=None, sales_channel_interface=None, sequence_number=None):  # noqa: E501
        """BlanketOrder - a model defined in Swagger"""  # noqa: E501
        self._blanket_order_id = None
        self._contract_id = None
        self._delivery_date_time = None
        self._customer_organization_id = None
        self._carrier_organization_id = None
        self._status = None
        self._blanket_order_lines = None
        self._is_initiated_by_supplier = None
        self._creation_date_time = None
        self._last_modified_date_time = None
        self._is_last_modified_by_supplier = None
        self._sales_channel_interface = None
        self._sequence_number = None
        self.discriminator = None
        self.blanket_order_id = blanket_order_id
        self.contract_id = contract_id
        self.delivery_date_time = delivery_date_time
        self.customer_organization_id = customer_organization_id
        if carrier_organization_id is not None:
            self.carrier_organization_id = carrier_organization_id
        self.status = status
        self.blanket_order_lines = blanket_order_lines
        self.is_initiated_by_supplier = is_initiated_by_supplier
        self.creation_date_time = creation_date_time
        self.last_modified_date_time = last_modified_date_time
        if is_last_modified_by_supplier is not None:
            self.is_last_modified_by_supplier = is_last_modified_by_supplier
        self.sales_channel_interface = sales_channel_interface
        self.sequence_number = sequence_number

    @property
    def blanket_order_id(self):
        """Gets the blanket_order_id of this BlanketOrder.  # noqa: E501


        :return: The blanket_order_id of this BlanketOrder.  # noqa: E501
        :rtype: str
        """
        return self._blanket_order_id

    @blanket_order_id.setter
    def blanket_order_id(self, blanket_order_id):
        """Sets the blanket_order_id of this BlanketOrder.


        :param blanket_order_id: The blanket_order_id of this BlanketOrder.  # noqa: E501
        :type: str
        """
        if blanket_order_id is None:
            raise ValueError("Invalid value for `blanket_order_id`, must not be `None`")  # noqa: E501

        self._blanket_order_id = blanket_order_id

    @property
    def contract_id(self):
        """Gets the contract_id of this BlanketOrder.  # noqa: E501


        :return: The contract_id of this BlanketOrder.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this BlanketOrder.


        :param contract_id: The contract_id of this BlanketOrder.  # noqa: E501
        :type: str
        """
        if contract_id is None:
            raise ValueError("Invalid value for `contract_id`, must not be `None`")  # noqa: E501

        self._contract_id = contract_id

    @property
    def delivery_date_time(self):
        """Gets the delivery_date_time of this BlanketOrder.  # noqa: E501


        :return: The delivery_date_time of this BlanketOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._delivery_date_time

    @delivery_date_time.setter
    def delivery_date_time(self, delivery_date_time):
        """Sets the delivery_date_time of this BlanketOrder.


        :param delivery_date_time: The delivery_date_time of this BlanketOrder.  # noqa: E501
        :type: datetime
        """
        if delivery_date_time is None:
            raise ValueError("Invalid value for `delivery_date_time`, must not be `None`")  # noqa: E501

        self._delivery_date_time = delivery_date_time

    @property
    def customer_organization_id(self):
        """Gets the customer_organization_id of this BlanketOrder.  # noqa: E501


        :return: The customer_organization_id of this BlanketOrder.  # noqa: E501
        :rtype: str
        """
        return self._customer_organization_id

    @customer_organization_id.setter
    def customer_organization_id(self, customer_organization_id):
        """Sets the customer_organization_id of this BlanketOrder.


        :param customer_organization_id: The customer_organization_id of this BlanketOrder.  # noqa: E501
        :type: str
        """
        if customer_organization_id is None:
            raise ValueError("Invalid value for `customer_organization_id`, must not be `None`")  # noqa: E501

        self._customer_organization_id = customer_organization_id

    @property
    def carrier_organization_id(self):
        """Gets the carrier_organization_id of this BlanketOrder.  # noqa: E501


        :return: The carrier_organization_id of this BlanketOrder.  # noqa: E501
        :rtype: str
        """
        return self._carrier_organization_id

    @carrier_organization_id.setter
    def carrier_organization_id(self, carrier_organization_id):
        """Sets the carrier_organization_id of this BlanketOrder.


        :param carrier_organization_id: The carrier_organization_id of this BlanketOrder.  # noqa: E501
        :type: str
        """

        self._carrier_organization_id = carrier_organization_id

    @property
    def status(self):
        """Gets the status of this BlanketOrder.  # noqa: E501


        :return: The status of this BlanketOrder.  # noqa: E501
        :rtype: BlanketOrderStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BlanketOrder.


        :param status: The status of this BlanketOrder.  # noqa: E501
        :type: BlanketOrderStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def blanket_order_lines(self):
        """Gets the blanket_order_lines of this BlanketOrder.  # noqa: E501


        :return: The blanket_order_lines of this BlanketOrder.  # noqa: E501
        :rtype: list[BlanketOrderLine]
        """
        return self._blanket_order_lines

    @blanket_order_lines.setter
    def blanket_order_lines(self, blanket_order_lines):
        """Sets the blanket_order_lines of this BlanketOrder.


        :param blanket_order_lines: The blanket_order_lines of this BlanketOrder.  # noqa: E501
        :type: list[BlanketOrderLine]
        """
        if blanket_order_lines is None:
            raise ValueError("Invalid value for `blanket_order_lines`, must not be `None`")  # noqa: E501

        self._blanket_order_lines = blanket_order_lines

    @property
    def is_initiated_by_supplier(self):
        """Gets the is_initiated_by_supplier of this BlanketOrder.  # noqa: E501


        :return: The is_initiated_by_supplier of this BlanketOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_initiated_by_supplier

    @is_initiated_by_supplier.setter
    def is_initiated_by_supplier(self, is_initiated_by_supplier):
        """Sets the is_initiated_by_supplier of this BlanketOrder.


        :param is_initiated_by_supplier: The is_initiated_by_supplier of this BlanketOrder.  # noqa: E501
        :type: bool
        """
        if is_initiated_by_supplier is None:
            raise ValueError("Invalid value for `is_initiated_by_supplier`, must not be `None`")  # noqa: E501

        self._is_initiated_by_supplier = is_initiated_by_supplier

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this BlanketOrder.  # noqa: E501


        :return: The creation_date_time of this BlanketOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this BlanketOrder.


        :param creation_date_time: The creation_date_time of this BlanketOrder.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this BlanketOrder.  # noqa: E501


        :return: The last_modified_date_time of this BlanketOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this BlanketOrder.


        :param last_modified_date_time: The last_modified_date_time of this BlanketOrder.  # noqa: E501
        :type: datetime
        """
        if last_modified_date_time is None:
            raise ValueError("Invalid value for `last_modified_date_time`, must not be `None`")  # noqa: E501

        self._last_modified_date_time = last_modified_date_time

    @property
    def is_last_modified_by_supplier(self):
        """Gets the is_last_modified_by_supplier of this BlanketOrder.  # noqa: E501


        :return: The is_last_modified_by_supplier of this BlanketOrder.  # noqa: E501
        :rtype: bool
        """
        return self._is_last_modified_by_supplier

    @is_last_modified_by_supplier.setter
    def is_last_modified_by_supplier(self, is_last_modified_by_supplier):
        """Sets the is_last_modified_by_supplier of this BlanketOrder.


        :param is_last_modified_by_supplier: The is_last_modified_by_supplier of this BlanketOrder.  # noqa: E501
        :type: bool
        """

        self._is_last_modified_by_supplier = is_last_modified_by_supplier

    @property
    def sales_channel_interface(self):
        """Gets the sales_channel_interface of this BlanketOrder.  # noqa: E501


        :return: The sales_channel_interface of this BlanketOrder.  # noqa: E501
        :rtype: SalesChannelInterface
        """
        return self._sales_channel_interface

    @sales_channel_interface.setter
    def sales_channel_interface(self, sales_channel_interface):
        """Sets the sales_channel_interface of this BlanketOrder.


        :param sales_channel_interface: The sales_channel_interface of this BlanketOrder.  # noqa: E501
        :type: SalesChannelInterface
        """
        if sales_channel_interface is None:
            raise ValueError("Invalid value for `sales_channel_interface`, must not be `None`")  # noqa: E501

        self._sales_channel_interface = sales_channel_interface

    @property
    def sequence_number(self):
        """Gets the sequence_number of this BlanketOrder.  # noqa: E501


        :return: The sequence_number of this BlanketOrder.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this BlanketOrder.


        :param sequence_number: The sequence_number of this BlanketOrder.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501

        self._sequence_number = sequence_number

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
        if issubclass(BlanketOrder, dict):
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
        if not isinstance(other, BlanketOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
