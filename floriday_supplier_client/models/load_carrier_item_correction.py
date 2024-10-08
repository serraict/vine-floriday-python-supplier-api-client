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

class LoadCarrierItemCorrection(object):
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
        'is_deleted': 'bool',
        'number_of_packages': 'int',
        'packing_agent_organization_id': 'str',
        'delivery_note_code': 'str',
        'delivery_note_letter': 'str'
    }

    attribute_map = {
        'is_deleted': 'isDeleted',
        'number_of_packages': 'numberOfPackages',
        'packing_agent_organization_id': 'packingAgentOrganizationId',
        'delivery_note_code': 'deliveryNoteCode',
        'delivery_note_letter': 'deliveryNoteLetter'
    }

    def __init__(self, is_deleted=None, number_of_packages=None, packing_agent_organization_id=None, delivery_note_code=None, delivery_note_letter=None):  # noqa: E501
        """LoadCarrierItemCorrection - a model defined in Swagger"""  # noqa: E501
        self._is_deleted = None
        self._number_of_packages = None
        self._packing_agent_organization_id = None
        self._delivery_note_code = None
        self._delivery_note_letter = None
        self.discriminator = None
        self.is_deleted = is_deleted
        self.number_of_packages = number_of_packages
        if packing_agent_organization_id is not None:
            self.packing_agent_organization_id = packing_agent_organization_id
        self.delivery_note_code = delivery_note_code
        self.delivery_note_letter = delivery_note_letter

    @property
    def is_deleted(self):
        """Gets the is_deleted of this LoadCarrierItemCorrection.  # noqa: E501


        :return: The is_deleted of this LoadCarrierItemCorrection.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this LoadCarrierItemCorrection.


        :param is_deleted: The is_deleted of this LoadCarrierItemCorrection.  # noqa: E501
        :type: bool
        """
        if is_deleted is None:
            raise ValueError("Invalid value for `is_deleted`, must not be `None`")  # noqa: E501

        self._is_deleted = is_deleted

    @property
    def number_of_packages(self):
        """Gets the number_of_packages of this LoadCarrierItemCorrection.  # noqa: E501


        :return: The number_of_packages of this LoadCarrierItemCorrection.  # noqa: E501
        :rtype: int
        """
        return self._number_of_packages

    @number_of_packages.setter
    def number_of_packages(self, number_of_packages):
        """Sets the number_of_packages of this LoadCarrierItemCorrection.


        :param number_of_packages: The number_of_packages of this LoadCarrierItemCorrection.  # noqa: E501
        :type: int
        """
        if number_of_packages is None:
            raise ValueError("Invalid value for `number_of_packages`, must not be `None`")  # noqa: E501

        self._number_of_packages = number_of_packages

    @property
    def packing_agent_organization_id(self):
        """Gets the packing_agent_organization_id of this LoadCarrierItemCorrection.  # noqa: E501


        :return: The packing_agent_organization_id of this LoadCarrierItemCorrection.  # noqa: E501
        :rtype: str
        """
        return self._packing_agent_organization_id

    @packing_agent_organization_id.setter
    def packing_agent_organization_id(self, packing_agent_organization_id):
        """Sets the packing_agent_organization_id of this LoadCarrierItemCorrection.


        :param packing_agent_organization_id: The packing_agent_organization_id of this LoadCarrierItemCorrection.  # noqa: E501
        :type: str
        """

        self._packing_agent_organization_id = packing_agent_organization_id

    @property
    def delivery_note_code(self):
        """Gets the delivery_note_code of this LoadCarrierItemCorrection.  # noqa: E501


        :return: The delivery_note_code of this LoadCarrierItemCorrection.  # noqa: E501
        :rtype: str
        """
        return self._delivery_note_code

    @delivery_note_code.setter
    def delivery_note_code(self, delivery_note_code):
        """Sets the delivery_note_code of this LoadCarrierItemCorrection.


        :param delivery_note_code: The delivery_note_code of this LoadCarrierItemCorrection.  # noqa: E501
        :type: str
        """
        if delivery_note_code is None:
            raise ValueError("Invalid value for `delivery_note_code`, must not be `None`")  # noqa: E501

        self._delivery_note_code = delivery_note_code

    @property
    def delivery_note_letter(self):
        """Gets the delivery_note_letter of this LoadCarrierItemCorrection.  # noqa: E501


        :return: The delivery_note_letter of this LoadCarrierItemCorrection.  # noqa: E501
        :rtype: str
        """
        return self._delivery_note_letter

    @delivery_note_letter.setter
    def delivery_note_letter(self, delivery_note_letter):
        """Sets the delivery_note_letter of this LoadCarrierItemCorrection.


        :param delivery_note_letter: The delivery_note_letter of this LoadCarrierItemCorrection.  # noqa: E501
        :type: str
        """
        if delivery_note_letter is None:
            raise ValueError("Invalid value for `delivery_note_letter`, must not be `None`")  # noqa: E501

        self._delivery_note_letter = delivery_note_letter

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
        if issubclass(LoadCarrierItemCorrection, dict):
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
        if not isinstance(other, LoadCarrierItemCorrection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
