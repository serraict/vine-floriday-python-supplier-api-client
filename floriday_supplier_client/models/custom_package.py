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

class CustomPackage(object):
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
        'code': 'str',
        'name': 'str',
        'description': 'str',
        'photo_url': 'str',
        'package_length_in_mm': 'int',
        'package_width_in_mm': 'int',
        'package_height_in_mm': 'int',
        'package_weight_in_gram': 'int',
        'fallback_vbn_package_code': 'int',
        'material_type_id': 'str',
        'is_deleted': 'bool',
        'creation_date_time': 'datetime',
        'last_modified_date_time': 'datetime',
        'sequence_number': 'int',
        'material_type': 'MaterialType'
    }

    attribute_map = {
        'custom_package_id': 'customPackageId',
        'code': 'code',
        'name': 'name',
        'description': 'description',
        'photo_url': 'photoUrl',
        'package_length_in_mm': 'packageLengthInMm',
        'package_width_in_mm': 'packageWidthInMm',
        'package_height_in_mm': 'packageHeightInMm',
        'package_weight_in_gram': 'packageWeightInGram',
        'fallback_vbn_package_code': 'fallbackVbnPackageCode',
        'material_type_id': 'materialTypeId',
        'is_deleted': 'isDeleted',
        'creation_date_time': 'creationDateTime',
        'last_modified_date_time': 'lastModifiedDateTime',
        'sequence_number': 'sequenceNumber',
        'material_type': 'materialType'
    }

    def __init__(self, custom_package_id=None, code=None, name=None, description=None, photo_url=None, package_length_in_mm=None, package_width_in_mm=None, package_height_in_mm=None, package_weight_in_gram=None, fallback_vbn_package_code=None, material_type_id=None, is_deleted=None, creation_date_time=None, last_modified_date_time=None, sequence_number=None, material_type=None):  # noqa: E501
        """CustomPackage - a model defined in Swagger"""  # noqa: E501
        self._custom_package_id = None
        self._code = None
        self._name = None
        self._description = None
        self._photo_url = None
        self._package_length_in_mm = None
        self._package_width_in_mm = None
        self._package_height_in_mm = None
        self._package_weight_in_gram = None
        self._fallback_vbn_package_code = None
        self._material_type_id = None
        self._is_deleted = None
        self._creation_date_time = None
        self._last_modified_date_time = None
        self._sequence_number = None
        self._material_type = None
        self.discriminator = None
        self.custom_package_id = custom_package_id
        self.code = code
        self.name = name
        self.description = description
        if photo_url is not None:
            self.photo_url = photo_url
        self.package_length_in_mm = package_length_in_mm
        self.package_width_in_mm = package_width_in_mm
        self.package_height_in_mm = package_height_in_mm
        if package_weight_in_gram is not None:
            self.package_weight_in_gram = package_weight_in_gram
        self.fallback_vbn_package_code = fallback_vbn_package_code
        if material_type_id is not None:
            self.material_type_id = material_type_id
        if is_deleted is not None:
            self.is_deleted = is_deleted
        self.creation_date_time = creation_date_time
        self.last_modified_date_time = last_modified_date_time
        self.sequence_number = sequence_number
        if material_type is not None:
            self.material_type = material_type

    @property
    def custom_package_id(self):
        """Gets the custom_package_id of this CustomPackage.  # noqa: E501


        :return: The custom_package_id of this CustomPackage.  # noqa: E501
        :rtype: str
        """
        return self._custom_package_id

    @custom_package_id.setter
    def custom_package_id(self, custom_package_id):
        """Sets the custom_package_id of this CustomPackage.


        :param custom_package_id: The custom_package_id of this CustomPackage.  # noqa: E501
        :type: str
        """
        if custom_package_id is None:
            raise ValueError("Invalid value for `custom_package_id`, must not be `None`")  # noqa: E501

        self._custom_package_id = custom_package_id

    @property
    def code(self):
        """Gets the code of this CustomPackage.  # noqa: E501


        :return: The code of this CustomPackage.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CustomPackage.


        :param code: The code of this CustomPackage.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def name(self):
        """Gets the name of this CustomPackage.  # noqa: E501


        :return: The name of this CustomPackage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomPackage.


        :param name: The name of this CustomPackage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CustomPackage.  # noqa: E501


        :return: The description of this CustomPackage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomPackage.


        :param description: The description of this CustomPackage.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def photo_url(self):
        """Gets the photo_url of this CustomPackage.  # noqa: E501

        Image URLs posted as Floriday media must conform with the following format https://image.floriday.io/.  # noqa: E501

        :return: The photo_url of this CustomPackage.  # noqa: E501
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url):
        """Sets the photo_url of this CustomPackage.

        Image URLs posted as Floriday media must conform with the following format https://image.floriday.io/.  # noqa: E501

        :param photo_url: The photo_url of this CustomPackage.  # noqa: E501
        :type: str
        """

        self._photo_url = photo_url

    @property
    def package_length_in_mm(self):
        """Gets the package_length_in_mm of this CustomPackage.  # noqa: E501


        :return: The package_length_in_mm of this CustomPackage.  # noqa: E501
        :rtype: int
        """
        return self._package_length_in_mm

    @package_length_in_mm.setter
    def package_length_in_mm(self, package_length_in_mm):
        """Sets the package_length_in_mm of this CustomPackage.


        :param package_length_in_mm: The package_length_in_mm of this CustomPackage.  # noqa: E501
        :type: int
        """
        if package_length_in_mm is None:
            raise ValueError("Invalid value for `package_length_in_mm`, must not be `None`")  # noqa: E501

        self._package_length_in_mm = package_length_in_mm

    @property
    def package_width_in_mm(self):
        """Gets the package_width_in_mm of this CustomPackage.  # noqa: E501


        :return: The package_width_in_mm of this CustomPackage.  # noqa: E501
        :rtype: int
        """
        return self._package_width_in_mm

    @package_width_in_mm.setter
    def package_width_in_mm(self, package_width_in_mm):
        """Sets the package_width_in_mm of this CustomPackage.


        :param package_width_in_mm: The package_width_in_mm of this CustomPackage.  # noqa: E501
        :type: int
        """
        if package_width_in_mm is None:
            raise ValueError("Invalid value for `package_width_in_mm`, must not be `None`")  # noqa: E501

        self._package_width_in_mm = package_width_in_mm

    @property
    def package_height_in_mm(self):
        """Gets the package_height_in_mm of this CustomPackage.  # noqa: E501


        :return: The package_height_in_mm of this CustomPackage.  # noqa: E501
        :rtype: int
        """
        return self._package_height_in_mm

    @package_height_in_mm.setter
    def package_height_in_mm(self, package_height_in_mm):
        """Sets the package_height_in_mm of this CustomPackage.


        :param package_height_in_mm: The package_height_in_mm of this CustomPackage.  # noqa: E501
        :type: int
        """
        if package_height_in_mm is None:
            raise ValueError("Invalid value for `package_height_in_mm`, must not be `None`")  # noqa: E501

        self._package_height_in_mm = package_height_in_mm

    @property
    def package_weight_in_gram(self):
        """Gets the package_weight_in_gram of this CustomPackage.  # noqa: E501


        :return: The package_weight_in_gram of this CustomPackage.  # noqa: E501
        :rtype: int
        """
        return self._package_weight_in_gram

    @package_weight_in_gram.setter
    def package_weight_in_gram(self, package_weight_in_gram):
        """Sets the package_weight_in_gram of this CustomPackage.


        :param package_weight_in_gram: The package_weight_in_gram of this CustomPackage.  # noqa: E501
        :type: int
        """

        self._package_weight_in_gram = package_weight_in_gram

    @property
    def fallback_vbn_package_code(self):
        """Gets the fallback_vbn_package_code of this CustomPackage.  # noqa: E501


        :return: The fallback_vbn_package_code of this CustomPackage.  # noqa: E501
        :rtype: int
        """
        return self._fallback_vbn_package_code

    @fallback_vbn_package_code.setter
    def fallback_vbn_package_code(self, fallback_vbn_package_code):
        """Sets the fallback_vbn_package_code of this CustomPackage.


        :param fallback_vbn_package_code: The fallback_vbn_package_code of this CustomPackage.  # noqa: E501
        :type: int
        """
        if fallback_vbn_package_code is None:
            raise ValueError("Invalid value for `fallback_vbn_package_code`, must not be `None`")  # noqa: E501

        self._fallback_vbn_package_code = fallback_vbn_package_code

    @property
    def material_type_id(self):
        """Gets the material_type_id of this CustomPackage.  # noqa: E501


        :return: The material_type_id of this CustomPackage.  # noqa: E501
        :rtype: str
        """
        return self._material_type_id

    @material_type_id.setter
    def material_type_id(self, material_type_id):
        """Sets the material_type_id of this CustomPackage.


        :param material_type_id: The material_type_id of this CustomPackage.  # noqa: E501
        :type: str
        """

        self._material_type_id = material_type_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this CustomPackage.  # noqa: E501


        :return: The is_deleted of this CustomPackage.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this CustomPackage.


        :param is_deleted: The is_deleted of this CustomPackage.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this CustomPackage.  # noqa: E501


        :return: The creation_date_time of this CustomPackage.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this CustomPackage.


        :param creation_date_time: The creation_date_time of this CustomPackage.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this CustomPackage.  # noqa: E501


        :return: The last_modified_date_time of this CustomPackage.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this CustomPackage.


        :param last_modified_date_time: The last_modified_date_time of this CustomPackage.  # noqa: E501
        :type: datetime
        """
        if last_modified_date_time is None:
            raise ValueError("Invalid value for `last_modified_date_time`, must not be `None`")  # noqa: E501

        self._last_modified_date_time = last_modified_date_time

    @property
    def sequence_number(self):
        """Gets the sequence_number of this CustomPackage.  # noqa: E501


        :return: The sequence_number of this CustomPackage.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this CustomPackage.


        :param sequence_number: The sequence_number of this CustomPackage.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501

        self._sequence_number = sequence_number

    @property
    def material_type(self):
        """Gets the material_type of this CustomPackage.  # noqa: E501


        :return: The material_type of this CustomPackage.  # noqa: E501
        :rtype: MaterialType
        """
        return self._material_type

    @material_type.setter
    def material_type(self, material_type):
        """Sets the material_type of this CustomPackage.


        :param material_type: The material_type of this CustomPackage.  # noqa: E501
        :type: MaterialType
        """

        self._material_type = material_type

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
        if issubclass(CustomPackage, dict):
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
        if not isinstance(other, CustomPackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
