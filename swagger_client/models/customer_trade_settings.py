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

class CustomerTradeSettings(object):
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
        'customer_organization_id': 'str',
        'accepts_direct_orders': 'AllOfCustomerTradeSettingsAcceptsDirectOrders',
        'automatically_accepts_correction_requests_on_direct_orders': 'AllOfCustomerTradeSettingsAutomaticallyAcceptsCorrectionRequestsOnDirectOrders',
        'automatically_accepts_correction_requests_on_supply_orders': 'AllOfCustomerTradeSettingsAutomaticallyAcceptsCorrectionRequestsOnSupplyOrders',
        'allow_suppliers_to_manage_selected_trade_item_assortment': 'AllOfCustomerTradeSettingsAllowSuppliersToManageSelectedTradeItemAssortment',
        'accepts_supply_of_type_purchase_tip': 'AllOfCustomerTradeSettingsAcceptsSupplyOfTypePurchaseTip',
        'uses_contracts': 'AllOfCustomerTradeSettingsUsesContracts',
        'accepts_transport_cost': 'AllOfCustomerTradeSettingsAcceptsTransportCost',
        'sequence_number': 'int'
    }

    attribute_map = {
        'customer_organization_id': 'customerOrganizationId',
        'accepts_direct_orders': 'acceptsDirectOrders',
        'automatically_accepts_correction_requests_on_direct_orders': 'automaticallyAcceptsCorrectionRequestsOnDirectOrders',
        'automatically_accepts_correction_requests_on_supply_orders': 'automaticallyAcceptsCorrectionRequestsOnSupplyOrders',
        'allow_suppliers_to_manage_selected_trade_item_assortment': 'allowSuppliersToManageSelectedTradeItemAssortment',
        'accepts_supply_of_type_purchase_tip': 'acceptsSupplyOfTypePurchaseTip',
        'uses_contracts': 'usesContracts',
        'accepts_transport_cost': 'acceptsTransportCost',
        'sequence_number': 'sequenceNumber'
    }

    def __init__(self, customer_organization_id=None, accepts_direct_orders=None, automatically_accepts_correction_requests_on_direct_orders=None, automatically_accepts_correction_requests_on_supply_orders=None, allow_suppliers_to_manage_selected_trade_item_assortment=None, accepts_supply_of_type_purchase_tip=None, uses_contracts=None, accepts_transport_cost=None, sequence_number=None):  # noqa: E501
        """CustomerTradeSettings - a model defined in Swagger"""  # noqa: E501
        self._customer_organization_id = None
        self._accepts_direct_orders = None
        self._automatically_accepts_correction_requests_on_direct_orders = None
        self._automatically_accepts_correction_requests_on_supply_orders = None
        self._allow_suppliers_to_manage_selected_trade_item_assortment = None
        self._accepts_supply_of_type_purchase_tip = None
        self._uses_contracts = None
        self._accepts_transport_cost = None
        self._sequence_number = None
        self.discriminator = None
        self.customer_organization_id = customer_organization_id
        self.accepts_direct_orders = accepts_direct_orders
        self.automatically_accepts_correction_requests_on_direct_orders = automatically_accepts_correction_requests_on_direct_orders
        self.automatically_accepts_correction_requests_on_supply_orders = automatically_accepts_correction_requests_on_supply_orders
        self.allow_suppliers_to_manage_selected_trade_item_assortment = allow_suppliers_to_manage_selected_trade_item_assortment
        self.accepts_supply_of_type_purchase_tip = accepts_supply_of_type_purchase_tip
        self.uses_contracts = uses_contracts
        self.accepts_transport_cost = accepts_transport_cost
        self.sequence_number = sequence_number

    @property
    def customer_organization_id(self):
        """Gets the customer_organization_id of this CustomerTradeSettings.  # noqa: E501


        :return: The customer_organization_id of this CustomerTradeSettings.  # noqa: E501
        :rtype: str
        """
        return self._customer_organization_id

    @customer_organization_id.setter
    def customer_organization_id(self, customer_organization_id):
        """Sets the customer_organization_id of this CustomerTradeSettings.


        :param customer_organization_id: The customer_organization_id of this CustomerTradeSettings.  # noqa: E501
        :type: str
        """
        if customer_organization_id is None:
            raise ValueError("Invalid value for `customer_organization_id`, must not be `None`")  # noqa: E501

        self._customer_organization_id = customer_organization_id

    @property
    def accepts_direct_orders(self):
        """Gets the accepts_direct_orders of this CustomerTradeSettings.  # noqa: E501

        As a customer, you set whether suppliers are allowed to create orders manually.  # noqa: E501

        :return: The accepts_direct_orders of this CustomerTradeSettings.  # noqa: E501
        :rtype: AllOfCustomerTradeSettingsAcceptsDirectOrders
        """
        return self._accepts_direct_orders

    @accepts_direct_orders.setter
    def accepts_direct_orders(self, accepts_direct_orders):
        """Sets the accepts_direct_orders of this CustomerTradeSettings.

        As a customer, you set whether suppliers are allowed to create orders manually.  # noqa: E501

        :param accepts_direct_orders: The accepts_direct_orders of this CustomerTradeSettings.  # noqa: E501
        :type: AllOfCustomerTradeSettingsAcceptsDirectOrders
        """
        if accepts_direct_orders is None:
            raise ValueError("Invalid value for `accepts_direct_orders`, must not be `None`")  # noqa: E501

        self._accepts_direct_orders = accepts_direct_orders

    @property
    def automatically_accepts_correction_requests_on_direct_orders(self):
        """Gets the automatically_accepts_correction_requests_on_direct_orders of this CustomerTradeSettings.  # noqa: E501

        With this you set that corrections requested by suppliers on orders that the supplier has created are automatically accepted.  # noqa: E501

        :return: The automatically_accepts_correction_requests_on_direct_orders of this CustomerTradeSettings.  # noqa: E501
        :rtype: AllOfCustomerTradeSettingsAutomaticallyAcceptsCorrectionRequestsOnDirectOrders
        """
        return self._automatically_accepts_correction_requests_on_direct_orders

    @automatically_accepts_correction_requests_on_direct_orders.setter
    def automatically_accepts_correction_requests_on_direct_orders(self, automatically_accepts_correction_requests_on_direct_orders):
        """Sets the automatically_accepts_correction_requests_on_direct_orders of this CustomerTradeSettings.

        With this you set that corrections requested by suppliers on orders that the supplier has created are automatically accepted.  # noqa: E501

        :param automatically_accepts_correction_requests_on_direct_orders: The automatically_accepts_correction_requests_on_direct_orders of this CustomerTradeSettings.  # noqa: E501
        :type: AllOfCustomerTradeSettingsAutomaticallyAcceptsCorrectionRequestsOnDirectOrders
        """
        if automatically_accepts_correction_requests_on_direct_orders is None:
            raise ValueError("Invalid value for `automatically_accepts_correction_requests_on_direct_orders`, must not be `None`")  # noqa: E501

        self._automatically_accepts_correction_requests_on_direct_orders = automatically_accepts_correction_requests_on_direct_orders

    @property
    def automatically_accepts_correction_requests_on_supply_orders(self):
        """Gets the automatically_accepts_correction_requests_on_supply_orders of this CustomerTradeSettings.  # noqa: E501

        With this you set that corrections requested by suppliers on orders placed by you as a customer are automatically accepted.  # noqa: E501

        :return: The automatically_accepts_correction_requests_on_supply_orders of this CustomerTradeSettings.  # noqa: E501
        :rtype: AllOfCustomerTradeSettingsAutomaticallyAcceptsCorrectionRequestsOnSupplyOrders
        """
        return self._automatically_accepts_correction_requests_on_supply_orders

    @automatically_accepts_correction_requests_on_supply_orders.setter
    def automatically_accepts_correction_requests_on_supply_orders(self, automatically_accepts_correction_requests_on_supply_orders):
        """Sets the automatically_accepts_correction_requests_on_supply_orders of this CustomerTradeSettings.

        With this you set that corrections requested by suppliers on orders placed by you as a customer are automatically accepted.  # noqa: E501

        :param automatically_accepts_correction_requests_on_supply_orders: The automatically_accepts_correction_requests_on_supply_orders of this CustomerTradeSettings.  # noqa: E501
        :type: AllOfCustomerTradeSettingsAutomaticallyAcceptsCorrectionRequestsOnSupplyOrders
        """
        if automatically_accepts_correction_requests_on_supply_orders is None:
            raise ValueError("Invalid value for `automatically_accepts_correction_requests_on_supply_orders`, must not be `None`")  # noqa: E501

        self._automatically_accepts_correction_requests_on_supply_orders = automatically_accepts_correction_requests_on_supply_orders

    @property
    def allow_suppliers_to_manage_selected_trade_item_assortment(self):
        """Gets the allow_suppliers_to_manage_selected_trade_item_assortment of this CustomerTradeSettings.  # noqa: E501

        Determine whether suppliers may add trade items to my selected assortment.  # noqa: E501

        :return: The allow_suppliers_to_manage_selected_trade_item_assortment of this CustomerTradeSettings.  # noqa: E501
        :rtype: AllOfCustomerTradeSettingsAllowSuppliersToManageSelectedTradeItemAssortment
        """
        return self._allow_suppliers_to_manage_selected_trade_item_assortment

    @allow_suppliers_to_manage_selected_trade_item_assortment.setter
    def allow_suppliers_to_manage_selected_trade_item_assortment(self, allow_suppliers_to_manage_selected_trade_item_assortment):
        """Sets the allow_suppliers_to_manage_selected_trade_item_assortment of this CustomerTradeSettings.

        Determine whether suppliers may add trade items to my selected assortment.  # noqa: E501

        :param allow_suppliers_to_manage_selected_trade_item_assortment: The allow_suppliers_to_manage_selected_trade_item_assortment of this CustomerTradeSettings.  # noqa: E501
        :type: AllOfCustomerTradeSettingsAllowSuppliersToManageSelectedTradeItemAssortment
        """
        if allow_suppliers_to_manage_selected_trade_item_assortment is None:
            raise ValueError("Invalid value for `allow_suppliers_to_manage_selected_trade_item_assortment`, must not be `None`")  # noqa: E501

        self._allow_suppliers_to_manage_selected_trade_item_assortment = allow_suppliers_to_manage_selected_trade_item_assortment

    @property
    def accepts_supply_of_type_purchase_tip(self):
        """Gets the accepts_supply_of_type_purchase_tip of this CustomerTradeSettings.  # noqa: E501

        Organization works with purchase tips.  # noqa: E501

        :return: The accepts_supply_of_type_purchase_tip of this CustomerTradeSettings.  # noqa: E501
        :rtype: AllOfCustomerTradeSettingsAcceptsSupplyOfTypePurchaseTip
        """
        return self._accepts_supply_of_type_purchase_tip

    @accepts_supply_of_type_purchase_tip.setter
    def accepts_supply_of_type_purchase_tip(self, accepts_supply_of_type_purchase_tip):
        """Sets the accepts_supply_of_type_purchase_tip of this CustomerTradeSettings.

        Organization works with purchase tips.  # noqa: E501

        :param accepts_supply_of_type_purchase_tip: The accepts_supply_of_type_purchase_tip of this CustomerTradeSettings.  # noqa: E501
        :type: AllOfCustomerTradeSettingsAcceptsSupplyOfTypePurchaseTip
        """
        if accepts_supply_of_type_purchase_tip is None:
            raise ValueError("Invalid value for `accepts_supply_of_type_purchase_tip`, must not be `None`")  # noqa: E501

        self._accepts_supply_of_type_purchase_tip = accepts_supply_of_type_purchase_tip

    @property
    def uses_contracts(self):
        """Gets the uses_contracts of this CustomerTradeSettings.  # noqa: E501

        Organization works with contracts.  # noqa: E501

        :return: The uses_contracts of this CustomerTradeSettings.  # noqa: E501
        :rtype: AllOfCustomerTradeSettingsUsesContracts
        """
        return self._uses_contracts

    @uses_contracts.setter
    def uses_contracts(self, uses_contracts):
        """Sets the uses_contracts of this CustomerTradeSettings.

        Organization works with contracts.  # noqa: E501

        :param uses_contracts: The uses_contracts of this CustomerTradeSettings.  # noqa: E501
        :type: AllOfCustomerTradeSettingsUsesContracts
        """
        if uses_contracts is None:
            raise ValueError("Invalid value for `uses_contracts`, must not be `None`")  # noqa: E501

        self._uses_contracts = uses_contracts

    @property
    def accepts_transport_cost(self):
        """Gets the accepts_transport_cost of this CustomerTradeSettings.  # noqa: E501

        Organization works with transport costs. Please note: when deactivating this setting, orders can only be placed on supply where transport costs are included in the price.  # noqa: E501

        :return: The accepts_transport_cost of this CustomerTradeSettings.  # noqa: E501
        :rtype: AllOfCustomerTradeSettingsAcceptsTransportCost
        """
        return self._accepts_transport_cost

    @accepts_transport_cost.setter
    def accepts_transport_cost(self, accepts_transport_cost):
        """Sets the accepts_transport_cost of this CustomerTradeSettings.

        Organization works with transport costs. Please note: when deactivating this setting, orders can only be placed on supply where transport costs are included in the price.  # noqa: E501

        :param accepts_transport_cost: The accepts_transport_cost of this CustomerTradeSettings.  # noqa: E501
        :type: AllOfCustomerTradeSettingsAcceptsTransportCost
        """
        if accepts_transport_cost is None:
            raise ValueError("Invalid value for `accepts_transport_cost`, must not be `None`")  # noqa: E501

        self._accepts_transport_cost = accepts_transport_cost

    @property
    def sequence_number(self):
        """Gets the sequence_number of this CustomerTradeSettings.  # noqa: E501


        :return: The sequence_number of this CustomerTradeSettings.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this CustomerTradeSettings.


        :param sequence_number: The sequence_number of this CustomerTradeSettings.  # noqa: E501
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
        if issubclass(CustomerTradeSettings, dict):
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
        if not isinstance(other, CustomerTradeSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
