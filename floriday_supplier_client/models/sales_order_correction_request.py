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

class SalesOrderCorrectionRequest(object):
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
        'sales_order_correction_request_id': 'str',
        'sales_order_id': 'str',
        'status': 'CorrectionRequestStatus',
        'is_sales_order_created_by_supplier': 'bool',
        'initiated_by': 'OrganizationType',
        'expires_at_date_time': 'datetime',
        'creation_date_time': 'datetime',
        'last_modified_date_time': 'datetime',
        'sequence_number': 'int',
        'customer_organization_id': 'str',
        'price_per_piece': 'Price',
        'package': 'Package',
        'number_of_pieces': 'int',
        'pieces_per_package': 'int',
        'incoterm': 'Incoterm',
        'reason': 'str',
        'is_cancel_request': 'bool',
        'sales_order_version_after_correction': 'int',
        'created_by_user_name': 'str',
        'stock_application': 'SalesOrderCorrectionStockApplication'
    }

    attribute_map = {
        'sales_order_correction_request_id': 'salesOrderCorrectionRequestId',
        'sales_order_id': 'salesOrderId',
        'status': 'status',
        'is_sales_order_created_by_supplier': 'isSalesOrderCreatedBySupplier',
        'initiated_by': 'initiatedBy',
        'expires_at_date_time': 'expiresAtDateTime',
        'creation_date_time': 'creationDateTime',
        'last_modified_date_time': 'lastModifiedDateTime',
        'sequence_number': 'sequenceNumber',
        'customer_organization_id': 'customerOrganizationId',
        'price_per_piece': 'pricePerPiece',
        'package': 'package',
        'number_of_pieces': 'numberOfPieces',
        'pieces_per_package': 'piecesPerPackage',
        'incoterm': 'incoterm',
        'reason': 'reason',
        'is_cancel_request': 'isCancelRequest',
        'sales_order_version_after_correction': 'salesOrderVersionAfterCorrection',
        'created_by_user_name': 'createdByUserName',
        'stock_application': 'stockApplication'
    }

    def __init__(self, sales_order_correction_request_id=None, sales_order_id=None, status=None, is_sales_order_created_by_supplier=None, initiated_by=None, expires_at_date_time=None, creation_date_time=None, last_modified_date_time=None, sequence_number=None, customer_organization_id=None, price_per_piece=None, package=None, number_of_pieces=None, pieces_per_package=None, incoterm=None, reason=None, is_cancel_request=None, sales_order_version_after_correction=None, created_by_user_name=None, stock_application=None):  # noqa: E501
        """SalesOrderCorrectionRequest - a model defined in Swagger"""  # noqa: E501
        self._sales_order_correction_request_id = None
        self._sales_order_id = None
        self._status = None
        self._is_sales_order_created_by_supplier = None
        self._initiated_by = None
        self._expires_at_date_time = None
        self._creation_date_time = None
        self._last_modified_date_time = None
        self._sequence_number = None
        self._customer_organization_id = None
        self._price_per_piece = None
        self._package = None
        self._number_of_pieces = None
        self._pieces_per_package = None
        self._incoterm = None
        self._reason = None
        self._is_cancel_request = None
        self._sales_order_version_after_correction = None
        self._created_by_user_name = None
        self._stock_application = None
        self.discriminator = None
        self.sales_order_correction_request_id = sales_order_correction_request_id
        self.sales_order_id = sales_order_id
        self.status = status
        self.is_sales_order_created_by_supplier = is_sales_order_created_by_supplier
        self.initiated_by = initiated_by
        self.expires_at_date_time = expires_at_date_time
        self.creation_date_time = creation_date_time
        self.last_modified_date_time = last_modified_date_time
        self.sequence_number = sequence_number
        self.customer_organization_id = customer_organization_id
        if price_per_piece is not None:
            self.price_per_piece = price_per_piece
        if package is not None:
            self.package = package
        if number_of_pieces is not None:
            self.number_of_pieces = number_of_pieces
        if pieces_per_package is not None:
            self.pieces_per_package = pieces_per_package
        if incoterm is not None:
            self.incoterm = incoterm
        if reason is not None:
            self.reason = reason
        self.is_cancel_request = is_cancel_request
        if sales_order_version_after_correction is not None:
            self.sales_order_version_after_correction = sales_order_version_after_correction
        if created_by_user_name is not None:
            self.created_by_user_name = created_by_user_name
        self.stock_application = stock_application

    @property
    def sales_order_correction_request_id(self):
        """Gets the sales_order_correction_request_id of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The sales_order_correction_request_id of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._sales_order_correction_request_id

    @sales_order_correction_request_id.setter
    def sales_order_correction_request_id(self, sales_order_correction_request_id):
        """Sets the sales_order_correction_request_id of this SalesOrderCorrectionRequest.


        :param sales_order_correction_request_id: The sales_order_correction_request_id of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: str
        """
        if sales_order_correction_request_id is None:
            raise ValueError("Invalid value for `sales_order_correction_request_id`, must not be `None`")  # noqa: E501

        self._sales_order_correction_request_id = sales_order_correction_request_id

    @property
    def sales_order_id(self):
        """Gets the sales_order_id of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The sales_order_id of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._sales_order_id

    @sales_order_id.setter
    def sales_order_id(self, sales_order_id):
        """Sets the sales_order_id of this SalesOrderCorrectionRequest.


        :param sales_order_id: The sales_order_id of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: str
        """
        if sales_order_id is None:
            raise ValueError("Invalid value for `sales_order_id`, must not be `None`")  # noqa: E501

        self._sales_order_id = sales_order_id

    @property
    def status(self):
        """Gets the status of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The status of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: CorrectionRequestStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SalesOrderCorrectionRequest.


        :param status: The status of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: CorrectionRequestStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def is_sales_order_created_by_supplier(self):
        """Gets the is_sales_order_created_by_supplier of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The is_sales_order_created_by_supplier of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_sales_order_created_by_supplier

    @is_sales_order_created_by_supplier.setter
    def is_sales_order_created_by_supplier(self, is_sales_order_created_by_supplier):
        """Sets the is_sales_order_created_by_supplier of this SalesOrderCorrectionRequest.


        :param is_sales_order_created_by_supplier: The is_sales_order_created_by_supplier of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: bool
        """
        if is_sales_order_created_by_supplier is None:
            raise ValueError("Invalid value for `is_sales_order_created_by_supplier`, must not be `None`")  # noqa: E501

        self._is_sales_order_created_by_supplier = is_sales_order_created_by_supplier

    @property
    def initiated_by(self):
        """Gets the initiated_by of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The initiated_by of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: OrganizationType
        """
        return self._initiated_by

    @initiated_by.setter
    def initiated_by(self, initiated_by):
        """Sets the initiated_by of this SalesOrderCorrectionRequest.


        :param initiated_by: The initiated_by of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: OrganizationType
        """
        if initiated_by is None:
            raise ValueError("Invalid value for `initiated_by`, must not be `None`")  # noqa: E501

        self._initiated_by = initiated_by

    @property
    def expires_at_date_time(self):
        """Gets the expires_at_date_time of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The expires_at_date_time of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at_date_time

    @expires_at_date_time.setter
    def expires_at_date_time(self, expires_at_date_time):
        """Sets the expires_at_date_time of this SalesOrderCorrectionRequest.


        :param expires_at_date_time: The expires_at_date_time of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: datetime
        """
        if expires_at_date_time is None:
            raise ValueError("Invalid value for `expires_at_date_time`, must not be `None`")  # noqa: E501

        self._expires_at_date_time = expires_at_date_time

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The creation_date_time of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this SalesOrderCorrectionRequest.


        :param creation_date_time: The creation_date_time of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The last_modified_date_time of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this SalesOrderCorrectionRequest.


        :param last_modified_date_time: The last_modified_date_time of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: datetime
        """
        if last_modified_date_time is None:
            raise ValueError("Invalid value for `last_modified_date_time`, must not be `None`")  # noqa: E501

        self._last_modified_date_time = last_modified_date_time

    @property
    def sequence_number(self):
        """Gets the sequence_number of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The sequence_number of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this SalesOrderCorrectionRequest.


        :param sequence_number: The sequence_number of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501

        self._sequence_number = sequence_number

    @property
    def customer_organization_id(self):
        """Gets the customer_organization_id of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The customer_organization_id of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._customer_organization_id

    @customer_organization_id.setter
    def customer_organization_id(self, customer_organization_id):
        """Sets the customer_organization_id of this SalesOrderCorrectionRequest.


        :param customer_organization_id: The customer_organization_id of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: str
        """
        if customer_organization_id is None:
            raise ValueError("Invalid value for `customer_organization_id`, must not be `None`")  # noqa: E501

        self._customer_organization_id = customer_organization_id

    @property
    def price_per_piece(self):
        """Gets the price_per_piece of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The price_per_piece of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: Price
        """
        return self._price_per_piece

    @price_per_piece.setter
    def price_per_piece(self, price_per_piece):
        """Sets the price_per_piece of this SalesOrderCorrectionRequest.


        :param price_per_piece: The price_per_piece of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: Price
        """

        self._price_per_piece = price_per_piece

    @property
    def package(self):
        """Gets the package of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The package of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: Package
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this SalesOrderCorrectionRequest.


        :param package: The package of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: Package
        """

        self._package = package

    @property
    def number_of_pieces(self):
        """Gets the number_of_pieces of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The number_of_pieces of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: int
        """
        return self._number_of_pieces

    @number_of_pieces.setter
    def number_of_pieces(self, number_of_pieces):
        """Sets the number_of_pieces of this SalesOrderCorrectionRequest.


        :param number_of_pieces: The number_of_pieces of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: int
        """

        self._number_of_pieces = number_of_pieces

    @property
    def pieces_per_package(self):
        """Gets the pieces_per_package of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The pieces_per_package of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: int
        """
        return self._pieces_per_package

    @pieces_per_package.setter
    def pieces_per_package(self, pieces_per_package):
        """Sets the pieces_per_package of this SalesOrderCorrectionRequest.


        :param pieces_per_package: The pieces_per_package of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: int
        """

        self._pieces_per_package = pieces_per_package

    @property
    def incoterm(self):
        """Gets the incoterm of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The incoterm of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: Incoterm
        """
        return self._incoterm

    @incoterm.setter
    def incoterm(self, incoterm):
        """Sets the incoterm of this SalesOrderCorrectionRequest.


        :param incoterm: The incoterm of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: Incoterm
        """

        self._incoterm = incoterm

    @property
    def reason(self):
        """Gets the reason of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The reason of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this SalesOrderCorrectionRequest.


        :param reason: The reason of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def is_cancel_request(self):
        """Gets the is_cancel_request of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The is_cancel_request of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_cancel_request

    @is_cancel_request.setter
    def is_cancel_request(self, is_cancel_request):
        """Sets the is_cancel_request of this SalesOrderCorrectionRequest.


        :param is_cancel_request: The is_cancel_request of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: bool
        """
        if is_cancel_request is None:
            raise ValueError("Invalid value for `is_cancel_request`, must not be `None`")  # noqa: E501

        self._is_cancel_request = is_cancel_request

    @property
    def sales_order_version_after_correction(self):
        """Gets the sales_order_version_after_correction of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The sales_order_version_after_correction of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: int
        """
        return self._sales_order_version_after_correction

    @sales_order_version_after_correction.setter
    def sales_order_version_after_correction(self, sales_order_version_after_correction):
        """Sets the sales_order_version_after_correction of this SalesOrderCorrectionRequest.


        :param sales_order_version_after_correction: The sales_order_version_after_correction of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: int
        """

        self._sales_order_version_after_correction = sales_order_version_after_correction

    @property
    def created_by_user_name(self):
        """Gets the created_by_user_name of this SalesOrderCorrectionRequest.  # noqa: E501

        Name of the contact person responsible for the sales order correction request  # noqa: E501

        :return: The created_by_user_name of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_name

    @created_by_user_name.setter
    def created_by_user_name(self, created_by_user_name):
        """Sets the created_by_user_name of this SalesOrderCorrectionRequest.

        Name of the contact person responsible for the sales order correction request  # noqa: E501

        :param created_by_user_name: The created_by_user_name of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: str
        """

        self._created_by_user_name = created_by_user_name

    @property
    def stock_application(self):
        """Gets the stock_application of this SalesOrderCorrectionRequest.  # noqa: E501


        :return: The stock_application of this SalesOrderCorrectionRequest.  # noqa: E501
        :rtype: SalesOrderCorrectionStockApplication
        """
        return self._stock_application

    @stock_application.setter
    def stock_application(self, stock_application):
        """Sets the stock_application of this SalesOrderCorrectionRequest.


        :param stock_application: The stock_application of this SalesOrderCorrectionRequest.  # noqa: E501
        :type: SalesOrderCorrectionStockApplication
        """
        if stock_application is None:
            raise ValueError("Invalid value for `stock_application`, must not be `None`")  # noqa: E501

        self._stock_application = stock_application

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
        if issubclass(SalesOrderCorrectionRequest, dict):
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
        if not isinstance(other, SalesOrderCorrectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
