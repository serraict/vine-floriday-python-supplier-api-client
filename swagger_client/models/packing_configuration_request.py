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

class PackingConfigurationRequest(object):
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
        'packing_configuration_request_id': 'str',
        'supplier_organization_id': 'str',
        'customer_organization_id': 'str',
        'trade_item_id': 'str',
        'status': 'RequestStatus',
        'sequence_number': 'int',
        'remark': 'str',
        'expires_at_date_time': 'datetime',
        'creation_date_time': 'datetime',
        'last_modified_date_time': 'datetime',
        'pieces_per_package': 'int',
        'package': 'Package',
        'packages_per_layer': 'int',
        'layers_per_load_carrier': 'int',
        'load_carrier': 'SupplyLoadCarrierType'
    }

    attribute_map = {
        'packing_configuration_request_id': 'packingConfigurationRequestId',
        'supplier_organization_id': 'supplierOrganizationId',
        'customer_organization_id': 'customerOrganizationId',
        'trade_item_id': 'tradeItemId',
        'status': 'status',
        'sequence_number': 'sequenceNumber',
        'remark': 'remark',
        'expires_at_date_time': 'expiresAtDateTime',
        'creation_date_time': 'creationDateTime',
        'last_modified_date_time': 'lastModifiedDateTime',
        'pieces_per_package': 'piecesPerPackage',
        'package': 'package',
        'packages_per_layer': 'packagesPerLayer',
        'layers_per_load_carrier': 'layersPerLoadCarrier',
        'load_carrier': 'loadCarrier'
    }

    def __init__(self, packing_configuration_request_id=None, supplier_organization_id=None, customer_organization_id=None, trade_item_id=None, status=None, sequence_number=None, remark=None, expires_at_date_time=None, creation_date_time=None, last_modified_date_time=None, pieces_per_package=None, package=None, packages_per_layer=None, layers_per_load_carrier=None, load_carrier=None):  # noqa: E501
        """PackingConfigurationRequest - a model defined in Swagger"""  # noqa: E501
        self._packing_configuration_request_id = None
        self._supplier_organization_id = None
        self._customer_organization_id = None
        self._trade_item_id = None
        self._status = None
        self._sequence_number = None
        self._remark = None
        self._expires_at_date_time = None
        self._creation_date_time = None
        self._last_modified_date_time = None
        self._pieces_per_package = None
        self._package = None
        self._packages_per_layer = None
        self._layers_per_load_carrier = None
        self._load_carrier = None
        self.discriminator = None
        self.packing_configuration_request_id = packing_configuration_request_id
        self.supplier_organization_id = supplier_organization_id
        self.customer_organization_id = customer_organization_id
        self.trade_item_id = trade_item_id
        self.status = status
        self.sequence_number = sequence_number
        if remark is not None:
            self.remark = remark
        self.expires_at_date_time = expires_at_date_time
        self.creation_date_time = creation_date_time
        self.last_modified_date_time = last_modified_date_time
        self.pieces_per_package = pieces_per_package
        self.package = package
        self.packages_per_layer = packages_per_layer
        self.layers_per_load_carrier = layers_per_load_carrier
        self.load_carrier = load_carrier

    @property
    def packing_configuration_request_id(self):
        """Gets the packing_configuration_request_id of this PackingConfigurationRequest.  # noqa: E501


        :return: The packing_configuration_request_id of this PackingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._packing_configuration_request_id

    @packing_configuration_request_id.setter
    def packing_configuration_request_id(self, packing_configuration_request_id):
        """Sets the packing_configuration_request_id of this PackingConfigurationRequest.


        :param packing_configuration_request_id: The packing_configuration_request_id of this PackingConfigurationRequest.  # noqa: E501
        :type: str
        """
        if packing_configuration_request_id is None:
            raise ValueError("Invalid value for `packing_configuration_request_id`, must not be `None`")  # noqa: E501

        self._packing_configuration_request_id = packing_configuration_request_id

    @property
    def supplier_organization_id(self):
        """Gets the supplier_organization_id of this PackingConfigurationRequest.  # noqa: E501


        :return: The supplier_organization_id of this PackingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._supplier_organization_id

    @supplier_organization_id.setter
    def supplier_organization_id(self, supplier_organization_id):
        """Sets the supplier_organization_id of this PackingConfigurationRequest.


        :param supplier_organization_id: The supplier_organization_id of this PackingConfigurationRequest.  # noqa: E501
        :type: str
        """
        if supplier_organization_id is None:
            raise ValueError("Invalid value for `supplier_organization_id`, must not be `None`")  # noqa: E501

        self._supplier_organization_id = supplier_organization_id

    @property
    def customer_organization_id(self):
        """Gets the customer_organization_id of this PackingConfigurationRequest.  # noqa: E501


        :return: The customer_organization_id of this PackingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._customer_organization_id

    @customer_organization_id.setter
    def customer_organization_id(self, customer_organization_id):
        """Sets the customer_organization_id of this PackingConfigurationRequest.


        :param customer_organization_id: The customer_organization_id of this PackingConfigurationRequest.  # noqa: E501
        :type: str
        """
        if customer_organization_id is None:
            raise ValueError("Invalid value for `customer_organization_id`, must not be `None`")  # noqa: E501

        self._customer_organization_id = customer_organization_id

    @property
    def trade_item_id(self):
        """Gets the trade_item_id of this PackingConfigurationRequest.  # noqa: E501


        :return: The trade_item_id of this PackingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._trade_item_id

    @trade_item_id.setter
    def trade_item_id(self, trade_item_id):
        """Sets the trade_item_id of this PackingConfigurationRequest.


        :param trade_item_id: The trade_item_id of this PackingConfigurationRequest.  # noqa: E501
        :type: str
        """
        if trade_item_id is None:
            raise ValueError("Invalid value for `trade_item_id`, must not be `None`")  # noqa: E501

        self._trade_item_id = trade_item_id

    @property
    def status(self):
        """Gets the status of this PackingConfigurationRequest.  # noqa: E501


        :return: The status of this PackingConfigurationRequest.  # noqa: E501
        :rtype: RequestStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PackingConfigurationRequest.


        :param status: The status of this PackingConfigurationRequest.  # noqa: E501
        :type: RequestStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def sequence_number(self):
        """Gets the sequence_number of this PackingConfigurationRequest.  # noqa: E501


        :return: The sequence_number of this PackingConfigurationRequest.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this PackingConfigurationRequest.


        :param sequence_number: The sequence_number of this PackingConfigurationRequest.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501

        self._sequence_number = sequence_number

    @property
    def remark(self):
        """Gets the remark of this PackingConfigurationRequest.  # noqa: E501


        :return: The remark of this PackingConfigurationRequest.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this PackingConfigurationRequest.


        :param remark: The remark of this PackingConfigurationRequest.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def expires_at_date_time(self):
        """Gets the expires_at_date_time of this PackingConfigurationRequest.  # noqa: E501


        :return: The expires_at_date_time of this PackingConfigurationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at_date_time

    @expires_at_date_time.setter
    def expires_at_date_time(self, expires_at_date_time):
        """Sets the expires_at_date_time of this PackingConfigurationRequest.


        :param expires_at_date_time: The expires_at_date_time of this PackingConfigurationRequest.  # noqa: E501
        :type: datetime
        """
        if expires_at_date_time is None:
            raise ValueError("Invalid value for `expires_at_date_time`, must not be `None`")  # noqa: E501

        self._expires_at_date_time = expires_at_date_time

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this PackingConfigurationRequest.  # noqa: E501


        :return: The creation_date_time of this PackingConfigurationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this PackingConfigurationRequest.


        :param creation_date_time: The creation_date_time of this PackingConfigurationRequest.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this PackingConfigurationRequest.  # noqa: E501


        :return: The last_modified_date_time of this PackingConfigurationRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this PackingConfigurationRequest.


        :param last_modified_date_time: The last_modified_date_time of this PackingConfigurationRequest.  # noqa: E501
        :type: datetime
        """
        if last_modified_date_time is None:
            raise ValueError("Invalid value for `last_modified_date_time`, must not be `None`")  # noqa: E501

        self._last_modified_date_time = last_modified_date_time

    @property
    def pieces_per_package(self):
        """Gets the pieces_per_package of this PackingConfigurationRequest.  # noqa: E501


        :return: The pieces_per_package of this PackingConfigurationRequest.  # noqa: E501
        :rtype: int
        """
        return self._pieces_per_package

    @pieces_per_package.setter
    def pieces_per_package(self, pieces_per_package):
        """Sets the pieces_per_package of this PackingConfigurationRequest.


        :param pieces_per_package: The pieces_per_package of this PackingConfigurationRequest.  # noqa: E501
        :type: int
        """
        if pieces_per_package is None:
            raise ValueError("Invalid value for `pieces_per_package`, must not be `None`")  # noqa: E501

        self._pieces_per_package = pieces_per_package

    @property
    def package(self):
        """Gets the package of this PackingConfigurationRequest.  # noqa: E501


        :return: The package of this PackingConfigurationRequest.  # noqa: E501
        :rtype: Package
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this PackingConfigurationRequest.


        :param package: The package of this PackingConfigurationRequest.  # noqa: E501
        :type: Package
        """
        if package is None:
            raise ValueError("Invalid value for `package`, must not be `None`")  # noqa: E501

        self._package = package

    @property
    def packages_per_layer(self):
        """Gets the packages_per_layer of this PackingConfigurationRequest.  # noqa: E501


        :return: The packages_per_layer of this PackingConfigurationRequest.  # noqa: E501
        :rtype: int
        """
        return self._packages_per_layer

    @packages_per_layer.setter
    def packages_per_layer(self, packages_per_layer):
        """Sets the packages_per_layer of this PackingConfigurationRequest.


        :param packages_per_layer: The packages_per_layer of this PackingConfigurationRequest.  # noqa: E501
        :type: int
        """
        if packages_per_layer is None:
            raise ValueError("Invalid value for `packages_per_layer`, must not be `None`")  # noqa: E501

        self._packages_per_layer = packages_per_layer

    @property
    def layers_per_load_carrier(self):
        """Gets the layers_per_load_carrier of this PackingConfigurationRequest.  # noqa: E501


        :return: The layers_per_load_carrier of this PackingConfigurationRequest.  # noqa: E501
        :rtype: int
        """
        return self._layers_per_load_carrier

    @layers_per_load_carrier.setter
    def layers_per_load_carrier(self, layers_per_load_carrier):
        """Sets the layers_per_load_carrier of this PackingConfigurationRequest.


        :param layers_per_load_carrier: The layers_per_load_carrier of this PackingConfigurationRequest.  # noqa: E501
        :type: int
        """
        if layers_per_load_carrier is None:
            raise ValueError("Invalid value for `layers_per_load_carrier`, must not be `None`")  # noqa: E501

        self._layers_per_load_carrier = layers_per_load_carrier

    @property
    def load_carrier(self):
        """Gets the load_carrier of this PackingConfigurationRequest.  # noqa: E501


        :return: The load_carrier of this PackingConfigurationRequest.  # noqa: E501
        :rtype: SupplyLoadCarrierType
        """
        return self._load_carrier

    @load_carrier.setter
    def load_carrier(self, load_carrier):
        """Sets the load_carrier of this PackingConfigurationRequest.


        :param load_carrier: The load_carrier of this PackingConfigurationRequest.  # noqa: E501
        :type: SupplyLoadCarrierType
        """
        if load_carrier is None:
            raise ValueError("Invalid value for `load_carrier`, must not be `None`")  # noqa: E501

        self._load_carrier = load_carrier

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
        if issubclass(PackingConfigurationRequest, dict):
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
        if not isinstance(other, PackingConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
