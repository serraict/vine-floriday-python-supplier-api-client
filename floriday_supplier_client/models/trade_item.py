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

class TradeItem(object):
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
        'trade_item_id': 'str',
        'supplier_article_code': 'str',
        'article_gtin': 'str',
        'vbn_product_code': 'int',
        'trade_item_name': 'TradeItemName',
        'characteristics': 'list[Characteristic]',
        'customer_organization_ids': 'list[str]',
        'seasonal_periods': 'list[SeasonalPeriod]',
        'photos': 'list[Photo]',
        'packing_configurations': 'list[PackingConfiguration]',
        'botanical_names': 'list[str]',
        'country_of_origin_iso_codes': 'list[str]',
        'is_hidden_in_catalog': 'bool',
        'sequence_number': 'int',
        'is_parent_for_variant': 'bool',
        'parent_id': 'str',
        'trade_item_components': 'list[TradeItemComponent]',
        'trade_item_reference': 'str',
        'trade_item_version': 'int',
        'creation_date_time': 'datetime',
        'last_modified_date_time': 'datetime',
        'is_deleted': 'bool',
        'has_invalid_floricode_data': 'bool'
    }

    attribute_map = {
        'trade_item_id': 'tradeItemId',
        'supplier_article_code': 'supplierArticleCode',
        'article_gtin': 'articleGtin',
        'vbn_product_code': 'vbnProductCode',
        'trade_item_name': 'tradeItemName',
        'characteristics': 'characteristics',
        'customer_organization_ids': 'customerOrganizationIds',
        'seasonal_periods': 'seasonalPeriods',
        'photos': 'photos',
        'packing_configurations': 'packingConfigurations',
        'botanical_names': 'botanicalNames',
        'country_of_origin_iso_codes': 'countryOfOriginIsoCodes',
        'is_hidden_in_catalog': 'isHiddenInCatalog',
        'sequence_number': 'sequenceNumber',
        'is_parent_for_variant': 'isParentForVariant',
        'parent_id': 'parentId',
        'trade_item_components': 'tradeItemComponents',
        'trade_item_reference': 'tradeItemReference',
        'trade_item_version': 'tradeItemVersion',
        'creation_date_time': 'creationDateTime',
        'last_modified_date_time': 'lastModifiedDateTime',
        'is_deleted': 'isDeleted',
        'has_invalid_floricode_data': 'hasInvalidFloricodeData'
    }

    def __init__(self, trade_item_id=None, supplier_article_code=None, article_gtin=None, vbn_product_code=None, trade_item_name=None, characteristics=None, customer_organization_ids=None, seasonal_periods=None, photos=None, packing_configurations=None, botanical_names=None, country_of_origin_iso_codes=None, is_hidden_in_catalog=None, sequence_number=None, is_parent_for_variant=None, parent_id=None, trade_item_components=None, trade_item_reference=None, trade_item_version=None, creation_date_time=None, last_modified_date_time=None, is_deleted=None, has_invalid_floricode_data=None):  # noqa: E501
        """TradeItem - a model defined in Swagger"""  # noqa: E501
        self._trade_item_id = None
        self._supplier_article_code = None
        self._article_gtin = None
        self._vbn_product_code = None
        self._trade_item_name = None
        self._characteristics = None
        self._customer_organization_ids = None
        self._seasonal_periods = None
        self._photos = None
        self._packing_configurations = None
        self._botanical_names = None
        self._country_of_origin_iso_codes = None
        self._is_hidden_in_catalog = None
        self._sequence_number = None
        self._is_parent_for_variant = None
        self._parent_id = None
        self._trade_item_components = None
        self._trade_item_reference = None
        self._trade_item_version = None
        self._creation_date_time = None
        self._last_modified_date_time = None
        self._is_deleted = None
        self._has_invalid_floricode_data = None
        self.discriminator = None
        self.trade_item_id = trade_item_id
        self.supplier_article_code = supplier_article_code
        if article_gtin is not None:
            self.article_gtin = article_gtin
        self.vbn_product_code = vbn_product_code
        self.trade_item_name = trade_item_name
        self.characteristics = characteristics
        if customer_organization_ids is not None:
            self.customer_organization_ids = customer_organization_ids
        if seasonal_periods is not None:
            self.seasonal_periods = seasonal_periods
        self.photos = photos
        self.packing_configurations = packing_configurations
        if botanical_names is not None:
            self.botanical_names = botanical_names
        if country_of_origin_iso_codes is not None:
            self.country_of_origin_iso_codes = country_of_origin_iso_codes
        self.is_hidden_in_catalog = is_hidden_in_catalog
        self.sequence_number = sequence_number
        if is_parent_for_variant is not None:
            self.is_parent_for_variant = is_parent_for_variant
        if parent_id is not None:
            self.parent_id = parent_id
        if trade_item_components is not None:
            self.trade_item_components = trade_item_components
        if trade_item_reference is not None:
            self.trade_item_reference = trade_item_reference
        if trade_item_version is not None:
            self.trade_item_version = trade_item_version
        self.creation_date_time = creation_date_time
        self.last_modified_date_time = last_modified_date_time
        if is_deleted is not None:
            self.is_deleted = is_deleted
        self.has_invalid_floricode_data = has_invalid_floricode_data

    @property
    def trade_item_id(self):
        """Gets the trade_item_id of this TradeItem.  # noqa: E501


        :return: The trade_item_id of this TradeItem.  # noqa: E501
        :rtype: str
        """
        return self._trade_item_id

    @trade_item_id.setter
    def trade_item_id(self, trade_item_id):
        """Sets the trade_item_id of this TradeItem.


        :param trade_item_id: The trade_item_id of this TradeItem.  # noqa: E501
        :type: str
        """
        if trade_item_id is None:
            raise ValueError("Invalid value for `trade_item_id`, must not be `None`")  # noqa: E501

        self._trade_item_id = trade_item_id

    @property
    def supplier_article_code(self):
        """Gets the supplier_article_code of this TradeItem.  # noqa: E501


        :return: The supplier_article_code of this TradeItem.  # noqa: E501
        :rtype: str
        """
        return self._supplier_article_code

    @supplier_article_code.setter
    def supplier_article_code(self, supplier_article_code):
        """Sets the supplier_article_code of this TradeItem.


        :param supplier_article_code: The supplier_article_code of this TradeItem.  # noqa: E501
        :type: str
        """
        if supplier_article_code is None:
            raise ValueError("Invalid value for `supplier_article_code`, must not be `None`")  # noqa: E501

        self._supplier_article_code = supplier_article_code

    @property
    def article_gtin(self):
        """Gets the article_gtin of this TradeItem.  # noqa: E501


        :return: The article_gtin of this TradeItem.  # noqa: E501
        :rtype: str
        """
        return self._article_gtin

    @article_gtin.setter
    def article_gtin(self, article_gtin):
        """Sets the article_gtin of this TradeItem.


        :param article_gtin: The article_gtin of this TradeItem.  # noqa: E501
        :type: str
        """

        self._article_gtin = article_gtin

    @property
    def vbn_product_code(self):
        """Gets the vbn_product_code of this TradeItem.  # noqa: E501


        :return: The vbn_product_code of this TradeItem.  # noqa: E501
        :rtype: int
        """
        return self._vbn_product_code

    @vbn_product_code.setter
    def vbn_product_code(self, vbn_product_code):
        """Sets the vbn_product_code of this TradeItem.


        :param vbn_product_code: The vbn_product_code of this TradeItem.  # noqa: E501
        :type: int
        """
        if vbn_product_code is None:
            raise ValueError("Invalid value for `vbn_product_code`, must not be `None`")  # noqa: E501

        self._vbn_product_code = vbn_product_code

    @property
    def trade_item_name(self):
        """Gets the trade_item_name of this TradeItem.  # noqa: E501


        :return: The trade_item_name of this TradeItem.  # noqa: E501
        :rtype: TradeItemName
        """
        return self._trade_item_name

    @trade_item_name.setter
    def trade_item_name(self, trade_item_name):
        """Sets the trade_item_name of this TradeItem.


        :param trade_item_name: The trade_item_name of this TradeItem.  # noqa: E501
        :type: TradeItemName
        """
        if trade_item_name is None:
            raise ValueError("Invalid value for `trade_item_name`, must not be `None`")  # noqa: E501

        self._trade_item_name = trade_item_name

    @property
    def characteristics(self):
        """Gets the characteristics of this TradeItem.  # noqa: E501


        :return: The characteristics of this TradeItem.  # noqa: E501
        :rtype: list[Characteristic]
        """
        return self._characteristics

    @characteristics.setter
    def characteristics(self, characteristics):
        """Sets the characteristics of this TradeItem.


        :param characteristics: The characteristics of this TradeItem.  # noqa: E501
        :type: list[Characteristic]
        """
        if characteristics is None:
            raise ValueError("Invalid value for `characteristics`, must not be `None`")  # noqa: E501

        self._characteristics = characteristics

    @property
    def customer_organization_ids(self):
        """Gets the customer_organization_ids of this TradeItem.  # noqa: E501


        :return: The customer_organization_ids of this TradeItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._customer_organization_ids

    @customer_organization_ids.setter
    def customer_organization_ids(self, customer_organization_ids):
        """Sets the customer_organization_ids of this TradeItem.


        :param customer_organization_ids: The customer_organization_ids of this TradeItem.  # noqa: E501
        :type: list[str]
        """

        self._customer_organization_ids = customer_organization_ids

    @property
    def seasonal_periods(self):
        """Gets the seasonal_periods of this TradeItem.  # noqa: E501


        :return: The seasonal_periods of this TradeItem.  # noqa: E501
        :rtype: list[SeasonalPeriod]
        """
        return self._seasonal_periods

    @seasonal_periods.setter
    def seasonal_periods(self, seasonal_periods):
        """Sets the seasonal_periods of this TradeItem.


        :param seasonal_periods: The seasonal_periods of this TradeItem.  # noqa: E501
        :type: list[SeasonalPeriod]
        """

        self._seasonal_periods = seasonal_periods

    @property
    def photos(self):
        """Gets the photos of this TradeItem.  # noqa: E501


        :return: The photos of this TradeItem.  # noqa: E501
        :rtype: list[Photo]
        """
        return self._photos

    @photos.setter
    def photos(self, photos):
        """Sets the photos of this TradeItem.


        :param photos: The photos of this TradeItem.  # noqa: E501
        :type: list[Photo]
        """
        if photos is None:
            raise ValueError("Invalid value for `photos`, must not be `None`")  # noqa: E501

        self._photos = photos

    @property
    def packing_configurations(self):
        """Gets the packing_configurations of this TradeItem.  # noqa: E501


        :return: The packing_configurations of this TradeItem.  # noqa: E501
        :rtype: list[PackingConfiguration]
        """
        return self._packing_configurations

    @packing_configurations.setter
    def packing_configurations(self, packing_configurations):
        """Sets the packing_configurations of this TradeItem.


        :param packing_configurations: The packing_configurations of this TradeItem.  # noqa: E501
        :type: list[PackingConfiguration]
        """
        if packing_configurations is None:
            raise ValueError("Invalid value for `packing_configurations`, must not be `None`")  # noqa: E501

        self._packing_configurations = packing_configurations

    @property
    def botanical_names(self):
        """Gets the botanical_names of this TradeItem.  # noqa: E501


        :return: The botanical_names of this TradeItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._botanical_names

    @botanical_names.setter
    def botanical_names(self, botanical_names):
        """Sets the botanical_names of this TradeItem.


        :param botanical_names: The botanical_names of this TradeItem.  # noqa: E501
        :type: list[str]
        """

        self._botanical_names = botanical_names

    @property
    def country_of_origin_iso_codes(self):
        """Gets the country_of_origin_iso_codes of this TradeItem.  # noqa: E501


        :return: The country_of_origin_iso_codes of this TradeItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._country_of_origin_iso_codes

    @country_of_origin_iso_codes.setter
    def country_of_origin_iso_codes(self, country_of_origin_iso_codes):
        """Sets the country_of_origin_iso_codes of this TradeItem.


        :param country_of_origin_iso_codes: The country_of_origin_iso_codes of this TradeItem.  # noqa: E501
        :type: list[str]
        """

        self._country_of_origin_iso_codes = country_of_origin_iso_codes

    @property
    def is_hidden_in_catalog(self):
        """Gets the is_hidden_in_catalog of this TradeItem.  # noqa: E501


        :return: The is_hidden_in_catalog of this TradeItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden_in_catalog

    @is_hidden_in_catalog.setter
    def is_hidden_in_catalog(self, is_hidden_in_catalog):
        """Sets the is_hidden_in_catalog of this TradeItem.


        :param is_hidden_in_catalog: The is_hidden_in_catalog of this TradeItem.  # noqa: E501
        :type: bool
        """
        if is_hidden_in_catalog is None:
            raise ValueError("Invalid value for `is_hidden_in_catalog`, must not be `None`")  # noqa: E501

        self._is_hidden_in_catalog = is_hidden_in_catalog

    @property
    def sequence_number(self):
        """Gets the sequence_number of this TradeItem.  # noqa: E501


        :return: The sequence_number of this TradeItem.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this TradeItem.


        :param sequence_number: The sequence_number of this TradeItem.  # noqa: E501
        :type: int
        """
        if sequence_number is None:
            raise ValueError("Invalid value for `sequence_number`, must not be `None`")  # noqa: E501

        self._sequence_number = sequence_number

    @property
    def is_parent_for_variant(self):
        """Gets the is_parent_for_variant of this TradeItem.  # noqa: E501


        :return: The is_parent_for_variant of this TradeItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_parent_for_variant

    @is_parent_for_variant.setter
    def is_parent_for_variant(self, is_parent_for_variant):
        """Sets the is_parent_for_variant of this TradeItem.


        :param is_parent_for_variant: The is_parent_for_variant of this TradeItem.  # noqa: E501
        :type: bool
        """

        self._is_parent_for_variant = is_parent_for_variant

    @property
    def parent_id(self):
        """Gets the parent_id of this TradeItem.  # noqa: E501


        :return: The parent_id of this TradeItem.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this TradeItem.


        :param parent_id: The parent_id of this TradeItem.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def trade_item_components(self):
        """Gets the trade_item_components of this TradeItem.  # noqa: E501


        :return: The trade_item_components of this TradeItem.  # noqa: E501
        :rtype: list[TradeItemComponent]
        """
        return self._trade_item_components

    @trade_item_components.setter
    def trade_item_components(self, trade_item_components):
        """Sets the trade_item_components of this TradeItem.


        :param trade_item_components: The trade_item_components of this TradeItem.  # noqa: E501
        :type: list[TradeItemComponent]
        """

        self._trade_item_components = trade_item_components

    @property
    def trade_item_reference(self):
        """Gets the trade_item_reference of this TradeItem.  # noqa: E501


        :return: The trade_item_reference of this TradeItem.  # noqa: E501
        :rtype: str
        """
        return self._trade_item_reference

    @trade_item_reference.setter
    def trade_item_reference(self, trade_item_reference):
        """Sets the trade_item_reference of this TradeItem.


        :param trade_item_reference: The trade_item_reference of this TradeItem.  # noqa: E501
        :type: str
        """

        self._trade_item_reference = trade_item_reference

    @property
    def trade_item_version(self):
        """Gets the trade_item_version of this TradeItem.  # noqa: E501


        :return: The trade_item_version of this TradeItem.  # noqa: E501
        :rtype: int
        """
        return self._trade_item_version

    @trade_item_version.setter
    def trade_item_version(self, trade_item_version):
        """Sets the trade_item_version of this TradeItem.


        :param trade_item_version: The trade_item_version of this TradeItem.  # noqa: E501
        :type: int
        """

        self._trade_item_version = trade_item_version

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this TradeItem.  # noqa: E501


        :return: The creation_date_time of this TradeItem.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this TradeItem.


        :param creation_date_time: The creation_date_time of this TradeItem.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this TradeItem.  # noqa: E501


        :return: The last_modified_date_time of this TradeItem.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this TradeItem.


        :param last_modified_date_time: The last_modified_date_time of this TradeItem.  # noqa: E501
        :type: datetime
        """
        if last_modified_date_time is None:
            raise ValueError("Invalid value for `last_modified_date_time`, must not be `None`")  # noqa: E501

        self._last_modified_date_time = last_modified_date_time

    @property
    def is_deleted(self):
        """Gets the is_deleted of this TradeItem.  # noqa: E501


        :return: The is_deleted of this TradeItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this TradeItem.


        :param is_deleted: The is_deleted of this TradeItem.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def has_invalid_floricode_data(self):
        """Gets the has_invalid_floricode_data of this TradeItem.  # noqa: E501


        :return: The has_invalid_floricode_data of this TradeItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_invalid_floricode_data

    @has_invalid_floricode_data.setter
    def has_invalid_floricode_data(self, has_invalid_floricode_data):
        """Sets the has_invalid_floricode_data of this TradeItem.


        :param has_invalid_floricode_data: The has_invalid_floricode_data of this TradeItem.  # noqa: E501
        :type: bool
        """
        if has_invalid_floricode_data is None:
            raise ValueError("Invalid value for `has_invalid_floricode_data`, must not be `None`")  # noqa: E501

        self._has_invalid_floricode_data = has_invalid_floricode_data

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
        if issubclass(TradeItem, dict):
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
        if not isinstance(other, TradeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
