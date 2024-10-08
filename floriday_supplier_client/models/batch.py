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

class Batch(object):
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
        'batch_date': 'datetime',
        'batch_id': 'str',
        'trade_item_id': 'str',
        'number_of_pieces': 'int',
        'initial_number_of_pieces': 'int',
        'packing_configuration': 'BatchPackingConfiguration',
        'warehouse_id': 'str',
        'image_url': 'str',
        'batch_reference': 'str',
        'custom_reference': 'str',
        'sequence_number': 'int',
        'transit_status': 'TransitStatus',
        'trade_item_version': 'int',
        'is_deleted': 'bool',
        'creation_date_time': 'datetime',
        'last_modified_date_time': 'datetime'
    }

    attribute_map = {
        'batch_date': 'batchDate',
        'batch_id': 'batchId',
        'trade_item_id': 'tradeItemId',
        'number_of_pieces': 'numberOfPieces',
        'initial_number_of_pieces': 'initialNumberOfPieces',
        'packing_configuration': 'packingConfiguration',
        'warehouse_id': 'warehouseId',
        'image_url': 'imageUrl',
        'batch_reference': 'batchReference',
        'custom_reference': 'customReference',
        'sequence_number': 'sequenceNumber',
        'transit_status': 'transitStatus',
        'trade_item_version': 'tradeItemVersion',
        'is_deleted': 'isDeleted',
        'creation_date_time': 'creationDateTime',
        'last_modified_date_time': 'lastModifiedDateTime'
    }

    def __init__(self, batch_date=None, batch_id=None, trade_item_id=None, number_of_pieces=None, initial_number_of_pieces=None, packing_configuration=None, warehouse_id=None, image_url=None, batch_reference=None, custom_reference=None, sequence_number=None, transit_status=None, trade_item_version=None, is_deleted=None, creation_date_time=None, last_modified_date_time=None):  # noqa: E501
        """Batch - a model defined in Swagger"""  # noqa: E501
        self._batch_date = None
        self._batch_id = None
        self._trade_item_id = None
        self._number_of_pieces = None
        self._initial_number_of_pieces = None
        self._packing_configuration = None
        self._warehouse_id = None
        self._image_url = None
        self._batch_reference = None
        self._custom_reference = None
        self._sequence_number = None
        self._transit_status = None
        self._trade_item_version = None
        self._is_deleted = None
        self._creation_date_time = None
        self._last_modified_date_time = None
        self.discriminator = None
        self.batch_date = batch_date
        self.batch_id = batch_id
        self.trade_item_id = trade_item_id
        self.number_of_pieces = number_of_pieces
        if initial_number_of_pieces is not None:
            self.initial_number_of_pieces = initial_number_of_pieces
        self.packing_configuration = packing_configuration
        self.warehouse_id = warehouse_id
        if image_url is not None:
            self.image_url = image_url
        if batch_reference is not None:
            self.batch_reference = batch_reference
        if custom_reference is not None:
            self.custom_reference = custom_reference
        self.sequence_number = sequence_number
        if transit_status is not None:
            self.transit_status = transit_status
        if trade_item_version is not None:
            self.trade_item_version = trade_item_version
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if creation_date_time is not None:
            self.creation_date_time = creation_date_time
        if last_modified_date_time is not None:
            self.last_modified_date_time = last_modified_date_time

    @property
    def batch_date(self):
        """Gets the batch_date of this Batch.  # noqa: E501


        :return: The batch_date of this Batch.  # noqa: E501
        :rtype: datetime
        """
        return self._batch_date

    @batch_date.setter
    def batch_date(self, batch_date):
        """Sets the batch_date of this Batch.


        :param batch_date: The batch_date of this Batch.  # noqa: E501
        :type: datetime
        """
        if batch_date is None:
            raise ValueError("Invalid value for `batch_date`, must not be `None`")  # noqa: E501

        self._batch_date = batch_date

    @property
    def batch_id(self):
        """Gets the batch_id of this Batch.  # noqa: E501


        :return: The batch_id of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this Batch.


        :param batch_id: The batch_id of this Batch.  # noqa: E501
        :type: str
        """
        if batch_id is None:
            raise ValueError("Invalid value for `batch_id`, must not be `None`")  # noqa: E501

        self._batch_id = batch_id

    @property
    def trade_item_id(self):
        """Gets the trade_item_id of this Batch.  # noqa: E501


        :return: The trade_item_id of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._trade_item_id

    @trade_item_id.setter
    def trade_item_id(self, trade_item_id):
        """Sets the trade_item_id of this Batch.


        :param trade_item_id: The trade_item_id of this Batch.  # noqa: E501
        :type: str
        """
        if trade_item_id is None:
            raise ValueError("Invalid value for `trade_item_id`, must not be `None`")  # noqa: E501

        self._trade_item_id = trade_item_id

    @property
    def number_of_pieces(self):
        """Gets the number_of_pieces of this Batch.  # noqa: E501


        :return: The number_of_pieces of this Batch.  # noqa: E501
        :rtype: int
        """
        return self._number_of_pieces

    @number_of_pieces.setter
    def number_of_pieces(self, number_of_pieces):
        """Sets the number_of_pieces of this Batch.


        :param number_of_pieces: The number_of_pieces of this Batch.  # noqa: E501
        :type: int
        """
        if number_of_pieces is None:
            raise ValueError("Invalid value for `number_of_pieces`, must not be `None`")  # noqa: E501

        self._number_of_pieces = number_of_pieces

    @property
    def initial_number_of_pieces(self):
        """Gets the initial_number_of_pieces of this Batch.  # noqa: E501


        :return: The initial_number_of_pieces of this Batch.  # noqa: E501
        :rtype: int
        """
        return self._initial_number_of_pieces

    @initial_number_of_pieces.setter
    def initial_number_of_pieces(self, initial_number_of_pieces):
        """Sets the initial_number_of_pieces of this Batch.


        :param initial_number_of_pieces: The initial_number_of_pieces of this Batch.  # noqa: E501
        :type: int
        """

        self._initial_number_of_pieces = initial_number_of_pieces

    @property
    def packing_configuration(self):
        """Gets the packing_configuration of this Batch.  # noqa: E501


        :return: The packing_configuration of this Batch.  # noqa: E501
        :rtype: BatchPackingConfiguration
        """
        return self._packing_configuration

    @packing_configuration.setter
    def packing_configuration(self, packing_configuration):
        """Sets the packing_configuration of this Batch.


        :param packing_configuration: The packing_configuration of this Batch.  # noqa: E501
        :type: BatchPackingConfiguration
        """
        if packing_configuration is None:
            raise ValueError("Invalid value for `packing_configuration`, must not be `None`")  # noqa: E501

        self._packing_configuration = packing_configuration

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this Batch.  # noqa: E501


        :return: The warehouse_id of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this Batch.


        :param warehouse_id: The warehouse_id of this Batch.  # noqa: E501
        :type: str
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def image_url(self):
        """Gets the image_url of this Batch.  # noqa: E501


        :return: The image_url of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Batch.


        :param image_url: The image_url of this Batch.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def batch_reference(self):
        """Gets the batch_reference of this Batch.  # noqa: E501


        :return: The batch_reference of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._batch_reference

    @batch_reference.setter
    def batch_reference(self, batch_reference):
        """Sets the batch_reference of this Batch.


        :param batch_reference: The batch_reference of this Batch.  # noqa: E501
        :type: str
        """

        self._batch_reference = batch_reference

    @property
    def custom_reference(self):
        """Gets the custom_reference of this Batch.  # noqa: E501


        :return: The custom_reference of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._custom_reference

    @custom_reference.setter
    def custom_reference(self, custom_reference):
        """Sets the custom_reference of this Batch.


        :param custom_reference: The custom_reference of this Batch.  # noqa: E501
        :type: str
        """

        self._custom_reference = custom_reference

    @property
    def sequence_number(self):
        """Gets the sequence_number of this Batch.  # noqa: E501


        :return: The sequence_number of this Batch.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this Batch.


        :param sequence_number: The sequence_number of this Batch.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501

        self._sequence_number = sequence_number

    @property
    def transit_status(self):
        """Gets the transit_status of this Batch.  # noqa: E501


        :return: The transit_status of this Batch.  # noqa: E501
        :rtype: TransitStatus
        """
        return self._transit_status

    @transit_status.setter
    def transit_status(self, transit_status):
        """Sets the transit_status of this Batch.


        :param transit_status: The transit_status of this Batch.  # noqa: E501
        :type: TransitStatus
        """

        self._transit_status = transit_status

    @property
    def trade_item_version(self):
        """Gets the trade_item_version of this Batch.  # noqa: E501


        :return: The trade_item_version of this Batch.  # noqa: E501
        :rtype: int
        """
        return self._trade_item_version

    @trade_item_version.setter
    def trade_item_version(self, trade_item_version):
        """Sets the trade_item_version of this Batch.


        :param trade_item_version: The trade_item_version of this Batch.  # noqa: E501
        :type: int
        """

        self._trade_item_version = trade_item_version

    @property
    def is_deleted(self):
        """Gets the is_deleted of this Batch.  # noqa: E501


        :return: The is_deleted of this Batch.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this Batch.


        :param is_deleted: The is_deleted of this Batch.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this Batch.  # noqa: E501


        :return: The creation_date_time of this Batch.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this Batch.


        :param creation_date_time: The creation_date_time of this Batch.  # noqa: E501
        :type: datetime
        """

        self._creation_date_time = creation_date_time

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this Batch.  # noqa: E501


        :return: The last_modified_date_time of this Batch.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this Batch.


        :param last_modified_date_time: The last_modified_date_time of this Batch.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date_time = last_modified_date_time

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
        if issubclass(Batch, dict):
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
        if not isinstance(other, Batch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
