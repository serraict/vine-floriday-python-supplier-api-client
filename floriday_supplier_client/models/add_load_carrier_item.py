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

class AddLoadCarrierItem(object):
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
        'fulfillment_request_id': 'str',
        'number_of_packages': 'int',
        'service_code': 'int',
        'packing_agent_organization_id': 'str',
        'sort_index': 'int',
        'delivery_remarks': 'str',
        'commercial_invoice_reference': 'str'
    }

    attribute_map = {
        'fulfillment_request_id': 'fulfillmentRequestId',
        'number_of_packages': 'numberOfPackages',
        'service_code': 'serviceCode',
        'packing_agent_organization_id': 'packingAgentOrganizationId',
        'sort_index': 'sortIndex',
        'delivery_remarks': 'deliveryRemarks',
        'commercial_invoice_reference': 'commercialInvoiceReference'
    }

    def __init__(self, fulfillment_request_id=None, number_of_packages=None, service_code=None, packing_agent_organization_id=None, sort_index=None, delivery_remarks=None, commercial_invoice_reference=None):  # noqa: E501
        """AddLoadCarrierItem - a model defined in Swagger"""  # noqa: E501
        self._fulfillment_request_id = None
        self._number_of_packages = None
        self._service_code = None
        self._packing_agent_organization_id = None
        self._sort_index = None
        self._delivery_remarks = None
        self._commercial_invoice_reference = None
        self.discriminator = None
        self.fulfillment_request_id = fulfillment_request_id
        self.number_of_packages = number_of_packages
        if service_code is not None:
            self.service_code = service_code
        if packing_agent_organization_id is not None:
            self.packing_agent_organization_id = packing_agent_organization_id
        if sort_index is not None:
            self.sort_index = sort_index
        if delivery_remarks is not None:
            self.delivery_remarks = delivery_remarks
        if commercial_invoice_reference is not None:
            self.commercial_invoice_reference = commercial_invoice_reference

    @property
    def fulfillment_request_id(self):
        """Gets the fulfillment_request_id of this AddLoadCarrierItem.  # noqa: E501


        :return: The fulfillment_request_id of this AddLoadCarrierItem.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_request_id

    @fulfillment_request_id.setter
    def fulfillment_request_id(self, fulfillment_request_id):
        """Sets the fulfillment_request_id of this AddLoadCarrierItem.


        :param fulfillment_request_id: The fulfillment_request_id of this AddLoadCarrierItem.  # noqa: E501
        :type: str
        """
        if fulfillment_request_id is None:
            raise ValueError("Invalid value for `fulfillment_request_id`, must not be `None`")  # noqa: E501

        self._fulfillment_request_id = fulfillment_request_id

    @property
    def number_of_packages(self):
        """Gets the number_of_packages of this AddLoadCarrierItem.  # noqa: E501


        :return: The number_of_packages of this AddLoadCarrierItem.  # noqa: E501
        :rtype: int
        """
        return self._number_of_packages

    @number_of_packages.setter
    def number_of_packages(self, number_of_packages):
        """Sets the number_of_packages of this AddLoadCarrierItem.


        :param number_of_packages: The number_of_packages of this AddLoadCarrierItem.  # noqa: E501
        :type: int
        """
        if number_of_packages is None:
            raise ValueError("Invalid value for `number_of_packages`, must not be `None`")  # noqa: E501

        self._number_of_packages = number_of_packages

    @property
    def service_code(self):
        """Gets the service_code of this AddLoadCarrierItem.  # noqa: E501


        :return: The service_code of this AddLoadCarrierItem.  # noqa: E501
        :rtype: int
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        """Sets the service_code of this AddLoadCarrierItem.


        :param service_code: The service_code of this AddLoadCarrierItem.  # noqa: E501
        :type: int
        """

        self._service_code = service_code

    @property
    def packing_agent_organization_id(self):
        """Gets the packing_agent_organization_id of this AddLoadCarrierItem.  # noqa: E501


        :return: The packing_agent_organization_id of this AddLoadCarrierItem.  # noqa: E501
        :rtype: str
        """
        return self._packing_agent_organization_id

    @packing_agent_organization_id.setter
    def packing_agent_organization_id(self, packing_agent_organization_id):
        """Sets the packing_agent_organization_id of this AddLoadCarrierItem.


        :param packing_agent_organization_id: The packing_agent_organization_id of this AddLoadCarrierItem.  # noqa: E501
        :type: str
        """

        self._packing_agent_organization_id = packing_agent_organization_id

    @property
    def sort_index(self):
        """Gets the sort_index of this AddLoadCarrierItem.  # noqa: E501

        The index related to the item's position on the loadcarrier  # noqa: E501

        :return: The sort_index of this AddLoadCarrierItem.  # noqa: E501
        :rtype: int
        """
        return self._sort_index

    @sort_index.setter
    def sort_index(self, sort_index):
        """Sets the sort_index of this AddLoadCarrierItem.

        The index related to the item's position on the loadcarrier  # noqa: E501

        :param sort_index: The sort_index of this AddLoadCarrierItem.  # noqa: E501
        :type: int
        """

        self._sort_index = sort_index

    @property
    def delivery_remarks(self):
        """Gets the delivery_remarks of this AddLoadCarrierItem.  # noqa: E501

        The delivery remarks will be printed on the connect EAB document. A `NULL` value indicates the use of the default delivery remarks found in the FulfillmentRequest or will ignore the value in an update.  # noqa: E501

        :return: The delivery_remarks of this AddLoadCarrierItem.  # noqa: E501
        :rtype: str
        """
        return self._delivery_remarks

    @delivery_remarks.setter
    def delivery_remarks(self, delivery_remarks):
        """Sets the delivery_remarks of this AddLoadCarrierItem.

        The delivery remarks will be printed on the connect EAB document. A `NULL` value indicates the use of the default delivery remarks found in the FulfillmentRequest or will ignore the value in an update.  # noqa: E501

        :param delivery_remarks: The delivery_remarks of this AddLoadCarrierItem.  # noqa: E501
        :type: str
        """

        self._delivery_remarks = delivery_remarks

    @property
    def commercial_invoice_reference(self):
        """Gets the commercial_invoice_reference of this AddLoadCarrierItem.  # noqa: E501

        Own reference reflected on the invoice.  # noqa: E501

        :return: The commercial_invoice_reference of this AddLoadCarrierItem.  # noqa: E501
        :rtype: str
        """
        return self._commercial_invoice_reference

    @commercial_invoice_reference.setter
    def commercial_invoice_reference(self, commercial_invoice_reference):
        """Sets the commercial_invoice_reference of this AddLoadCarrierItem.

        Own reference reflected on the invoice.  # noqa: E501

        :param commercial_invoice_reference: The commercial_invoice_reference of this AddLoadCarrierItem.  # noqa: E501
        :type: str
        """

        self._commercial_invoice_reference = commercial_invoice_reference

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
        if issubclass(AddLoadCarrierItem, dict):
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
        if not isinstance(other, AddLoadCarrierItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
