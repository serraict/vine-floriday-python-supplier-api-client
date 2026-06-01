# Update guide: Floriday Supplier API 2025v2 → 2026v1

## Summary

Floriday `2026v1` is the current Main version (deprecates after October 2026, offline after April 2027). This is a mostly additive release: one new API class (`FifoBatchCountersApi`), a scattering of new methods on existing API classes, a new syncable entity (`LogisticMeansInvoiceStatus`), and many new **optional** model fields. The only breaking changes are a batch image field rename (`image_url` → `image_id`) and the removal of `photo_url` from one packing-configuration request model. If you do not create or read batches, this is a one-line `FLORIDAY_BASE_URL` update plus a library version bump.

## Required config changes

- Update `FLORIDAY_BASE_URL` to end in `/suppliers-api-2026v1` (was `/suppliers-api-2025v2`).
- Upgrade this library to the version released alongside this guide.
- No new environment variables.
- No change to the OAuth scopes requested by `ApiFactory` (see the scope note under New capabilities if you adopt the new clock-supply / FIFO endpoints).

## Breaking changes

### Batch image: `image_url` → `image_id`

Batches now reference their image by a Floriday **media ID** instead of a URL string. The attribute is renamed on three models:

- `Batch.image_url` → `Batch.image_id`
- `AddBatch.image_url` → `AddBatch.image_id`
- `AddBatchFromTradeItemProperties.image_url` → `AddBatchFromTradeItemProperties.image_id`

This is both a rename and a semantics change: the value is no longer a `https://image.floriday.io/...` URL but the ID of an uploaded media object. Code that sets `image_url=` will raise `TypeError` (unexpected keyword argument) at call time, and code reading `.image_url` will raise `AttributeError`.

```python
# before (2025v2)
batch = AddBatch(..., image_url="https://image.floriday.io/abc123")

# after (2026v1)
batch = AddBatch(..., image_id="abc123")   # media object ID, not a URL
```

Note: on the read model `Batch`, `image_id` is now optional (the old `image_url` was a required field).

### `TransformBatchRequestPackingConfiguration.photo_url` removed

The `photo_url` field was dropped from `TransformBatchRequestPackingConfiguration` with no replacement on that model. Code passing `photo_url=` to it will raise `TypeError`.

```python
# before (2025v2)
cfg = TransformBatchRequestPackingConfiguration(..., photo_url="https://image.floriday.io/abc123")

# after (2026v1)
cfg = TransformBatchRequestPackingConfiguration(...)   # photo_url no longer accepted
```

No model classes or API methods were removed in this release.

## New capabilities

### New API class

- `FifoBatchCountersApi` — manage FIFO batch counters:
  - `add_fifo_batch_counter(body)`
  - `edit_fifo_batch_counter(body, ...)`
  - `delete_fifo_batch_counter(...)`

  Exposed at the package root (`from floriday_supplier_client import FifoBatchCountersApi`).

### New methods on existing API classes

`AuctionApi`:

- `edit_clock_supply_line(...)`
- `get_fulfillment_request_id_by_daytrade_clock_supply_line_by_id(...)`
- `get_fulfillment_request_id_by_sales_strategy_presales_order_id(...)`

`DirectSalesApi`:

- `set_supply_line_assigned_number_of_pieces(...)`
- `set_supply_line_only_asap_delivery(...)`

`CustomerOffersApi`:

- `set_availability_of_customer_offer_line(...)`

`InvoiceLinesApi`:

- `get_logistic_means_invoice_status_by_sequence_number(sequence_number, limit)`
- `get_logistic_means_invoice_status_max_sequence()`

  These follow the standard sync-endpoint shape — see Sync module notes.

### New optional fields on existing models

All additive and backward-compatible — existing constructor calls keep working:

- **FSI compliance:** `Organization.is_fsi_compliant`, `CustomerTradeSettings.trades_exclusively_with_fsi_compliant_suppliers`
- **ASAP delivery:** `BaseSupply.only_asap_delivery`, `BatchBaseSupply.only_asap_delivery`, `SupplyLine.only_asap_delivery`, `SupplyLineCreate.only_asap_delivery`
- **Supply line:** `SupplyLine.assigned_number_of_pieces`
- **Customer offer availability:** `CustomerOfferLine.is_available`, `AddCustomerOfferLine.is_available`, `EditCustomerOfferLine.is_available`
- **Seller organization:** `SalesOrder.seller_organization_id`, `TradeItemBase.seller_organization_id`, `TradeItemUpdate.seller_organization_id`, `CollectionTradeItem.supplier_organization_id`
- **Daytrade:** `SalesOrder.is_daytrade_from_nursery`
- **Load carrier:** `LoadCarrierItem.alternative_display_name`, `LoadCarrierItem.load_carrier_item_id`, `AddLoadCarrierItem.alternative_display_name`, `AddLoadCarrierItem.load_carrier_item_id`, `AddLoadCarrierItemCorrection.load_carrier_item_id`
- **Sales-order corrections:** `SalesOrderCorrectionRequest.additional_services`, `SalesOrderCorrectionRequest.delivery_price_per_piece`, `SalesOrderCorrectionRequest.reclamation_action_decision`, and the same `additional_services` / `delivery_price_per_piece` on `AddSalesOrderCorrectionRequest`
- **Invoice:** `InvoiceLine.creation_date_time`
- **Media:** `Photo.sort_index`

### New model classes

- `AllocatedBatch`
- `LogisticMeansInvoiceStatus`, `LogisticMeansType`, `SyncResultOfLogisticMeansInvoiceStatus`
- `CorrectionAdditionalService`, `AddSalesOrderCorrectionRequestForAdditionalService`, `SalesOrderReclamationActionDecision`
- `SupplyLineAssignedNumberOfPiecesUpdate`, `SupplyLineOnlyAsapDeliveryUpdate`
- `EditClockSupplyLine`
- `AddFifoBatchCounter`, `EditFifoBatchCounter`

### Scope note

`ApiFactory` requests a fixed scope list and was not regenerated, so requested scopes are unchanged. Some of the new endpoints require scopes the bundled factory does not request — e.g. `edit_clock_supply_line` needs `clock-supply:write`. This is a pre-existing limitation (the factory already omits several scopes), not new to `2026v1`. If you call the new clock-supply or FIFO endpoints with the default factory and get a 403, extend the scope string in `ApiFactory._get_access_token`.

## Removed / deprecated

Nothing beyond the two breaking field changes above. No endpoints or model classes were removed.

## Sync module notes

`floriday_supplier_client.sync.sync_entities` is unaffected:

- No existing `get_*_by_sequence_number` callbacks changed signature, so existing sync wiring continues to work.
- A new sync-endpoint pair is available on `InvoiceLinesApi` for logistic-means invoice status (`get_logistic_means_invoice_status_by_sequence_number` / `..._max_sequence`), with a matching `SyncResultOfLogisticMeansInvoiceStatus` model. Plug them into `sync_entities` only if you want to mirror that new entity locally.
