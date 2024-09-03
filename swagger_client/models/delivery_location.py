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

class DeliveryLocation(object):
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
        'location_id': 'str',
        'organization_id': 'str',
        'gln': 'str',
        'address': 'Address',
        'is_deleted': 'bool',
        'is_default': 'bool',
        'last_modified_date_time': 'datetime',
        'creation_date_time': 'datetime',
        'sequence_number': 'int'
    }

    attribute_map = {
        'location_id': 'locationId',
        'organization_id': 'organizationId',
        'gln': 'gln',
        'address': 'address',
        'is_deleted': 'isDeleted',
        'is_default': 'isDefault',
        'last_modified_date_time': 'lastModifiedDateTime',
        'creation_date_time': 'creationDateTime',
        'sequence_number': 'sequenceNumber'
    }

    def __init__(self, location_id=None, organization_id=None, gln=None, address=None, is_deleted=None, is_default=None, last_modified_date_time=None, creation_date_time=None, sequence_number=None):  # noqa: E501
        """DeliveryLocation - a model defined in Swagger"""  # noqa: E501
        self._location_id = None
        self._organization_id = None
        self._gln = None
        self._address = None
        self._is_deleted = None
        self._is_default = None
        self._last_modified_date_time = None
        self._creation_date_time = None
        self._sequence_number = None
        self.discriminator = None
        self.location_id = location_id
        self.organization_id = organization_id
        self.gln = gln
        if address is not None:
            self.address = address
        self.is_deleted = is_deleted
        self.is_default = is_default
        self.last_modified_date_time = last_modified_date_time
        self.creation_date_time = creation_date_time
        self.sequence_number = sequence_number

    @property
    def location_id(self):
        """Gets the location_id of this DeliveryLocation.  # noqa: E501


        :return: The location_id of this DeliveryLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this DeliveryLocation.


        :param location_id: The location_id of this DeliveryLocation.  # noqa: E501
        :type: str
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def organization_id(self):
        """Gets the organization_id of this DeliveryLocation.  # noqa: E501


        :return: The organization_id of this DeliveryLocation.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this DeliveryLocation.


        :param organization_id: The organization_id of this DeliveryLocation.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def gln(self):
        """Gets the gln of this DeliveryLocation.  # noqa: E501


        :return: The gln of this DeliveryLocation.  # noqa: E501
        :rtype: str
        """
        return self._gln

    @gln.setter
    def gln(self, gln):
        """Sets the gln of this DeliveryLocation.


        :param gln: The gln of this DeliveryLocation.  # noqa: E501
        :type: str
        """
        if gln is None:
            raise ValueError("Invalid value for `gln`, must not be `None`")  # noqa: E501

        self._gln = gln

    @property
    def address(self):
        """Gets the address of this DeliveryLocation.  # noqa: E501


        :return: The address of this DeliveryLocation.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this DeliveryLocation.


        :param address: The address of this DeliveryLocation.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def is_deleted(self):
        """Gets the is_deleted of this DeliveryLocation.  # noqa: E501


        :return: The is_deleted of this DeliveryLocation.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this DeliveryLocation.


        :param is_deleted: The is_deleted of this DeliveryLocation.  # noqa: E501
        :type: bool
        """
        if is_deleted is None:
            raise ValueError("Invalid value for `is_deleted`, must not be `None`")  # noqa: E501

        self._is_deleted = is_deleted

    @property
    def is_default(self):
        """Gets the is_default of this DeliveryLocation.  # noqa: E501


        :return: The is_default of this DeliveryLocation.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this DeliveryLocation.


        :param is_default: The is_default of this DeliveryLocation.  # noqa: E501
        :type: bool
        """
        if is_default is None:
            raise ValueError("Invalid value for `is_default`, must not be `None`")  # noqa: E501

        self._is_default = is_default

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this DeliveryLocation.  # noqa: E501


        :return: The last_modified_date_time of this DeliveryLocation.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this DeliveryLocation.


        :param last_modified_date_time: The last_modified_date_time of this DeliveryLocation.  # noqa: E501
        :type: datetime
        """
        if last_modified_date_time is None:
            raise ValueError("Invalid value for `last_modified_date_time`, must not be `None`")  # noqa: E501

        self._last_modified_date_time = last_modified_date_time

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this DeliveryLocation.  # noqa: E501


        :return: The creation_date_time of this DeliveryLocation.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this DeliveryLocation.


        :param creation_date_time: The creation_date_time of this DeliveryLocation.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def sequence_number(self):
        """Gets the sequence_number of this DeliveryLocation.  # noqa: E501


        :return: The sequence_number of this DeliveryLocation.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this DeliveryLocation.


        :param sequence_number: The sequence_number of this DeliveryLocation.  # noqa: E501
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
        if issubclass(DeliveryLocation, dict):
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
        if not isinstance(other, DeliveryLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
