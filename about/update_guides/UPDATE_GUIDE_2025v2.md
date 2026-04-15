# Update guide: Floriday Supplier API 2025v1 → 2025v2

## Summary

Floriday `2025v2` is the current Main version (deprecates after April 2026, offline October 2026). For most consumers this is a low-risk bump: a handful of new endpoints, several new model classes, and one targeted breaking change in `CustomerOffersApi` where the v1/v2 endpoint split was consolidated. If you do not call `CustomerOffersApi`, this should be a one-line `FLORIDAY_BASE_URL` update plus a library version bump.

## Required config changes

- Update `FLORIDAY_BASE_URL` to end in `/suppliers-api-2025v2` (was `/suppliers-api-2025v1`).
- Upgrade this library to the version released alongside this guide.
- No new environment variables, no OAuth scope changes.

## Breaking changes

### `CustomerOffersApi` — v1/v2 endpoints consolidated

The pre-existing `*_v2` variants and the second `delete_customer_offer2` have been collapsed into the primary methods, and the primary methods now take `customer_offer_id` instead of `supply_line_id`. Callers that pass a `supply_line_id` will compile and call the API but send the wrong identifier — this is a silent breakage, not an import error.

| 2025v1 (removed)                                              | 2025v2 (use instead)                                  |
| ------------------------------------------------------------- | ----------------------------------------------------- |
| `add_customer_offer_v2(body)`                                 | (no direct replacement — see Floriday changelog)      |
| `delete_customer_offer(supply_line_id)`                       | `delete_customer_offer(customer_offer_id)`            |
| `delete_customer_offer2(customer_offer_id)`                   | `delete_customer_offer(customer_offer_id)`            |
| `edit_customer_offer(body, supply_line_id)`                   | `edit_customer_offer(body, customer_offer_id)`        |
| `edit_customer_offer_v2(body, customer_offer_id)`             | `edit_customer_offer(body, customer_offer_id)`        |

Migration:

```python
# before (2025v1)
api.delete_customer_offer(supply_line_id=sl_id)
api.edit_customer_offer(body=payload, supply_line_id=sl_id)
api.edit_customer_offer_v2(body=payload, customer_offer_id=co_id)

# after (2025v2)
api.delete_customer_offer(customer_offer_id=co_id)
api.edit_customer_offer(body=payload, customer_offer_id=co_id)
```

If you previously used `add_customer_offer_v2`, you will need to consult the Floriday changelog for the replacement workflow — it has no drop-in successor in this client.

### Removed model classes

These model classes no longer exist in `floriday_supplier_client.models`:

- `AddCustomerOfferV2`
- `EditCustomerOfferV2`
- `Availability`
- `DeliveryCost`

Imports referencing them will fail. The first two relate to the customer-offer consolidation above. `Availability` and `DeliveryCost` were removed as standalone shapes — check the new `TradeItemAvailabilityPerWeek` and `DeliveryConditionAdditionalCosts*` types listed below.

## New capabilities

### New API class

- `AdminApi` — sync-endpoint cache management:
  - `get_sync_endpoint_cache_max_sequences()`
  - `get_sync_endpoint_cache_sequences_of_endpoint(model_name)`
  - `clear_cache_entries_of_sync_endpoint(model_name)`

  Operational tooling, not part of normal data flows.

### New methods on existing API classes

`CatalogPricesApi`:

- `edit_trade_item_availability_for_customer_offers(trade_item_id, is_available_for_customer_offers)`
- `edit_trade_item_availability_per_week(body)`
- `get_trade_item_availabilities_per_week_by_sequence_number(sequence_number, limit)`
- `get_trade_item_availabilities_per_week_max_sequence()`

The last two follow the standard sync-endpoint shape and can be wired into `sync_entities` if you want to mirror weekly trade-item availability locally.

### New model classes

- `AddDeliveryLocation`, `CorrectionDeliveryLocation`
- `DeliveryConditionAdditionalCosts`, `DeliveryConditionAdditionalCostsPerCurrency`
- `EditTradeItemAvailabilityPerWeek`, `TradeItemAvailabilityPerWeek`, `SyncResultOfTradeItemAvailabilityPerWeek`
- `WeekOfYear`
- `CacheNameAndMaxSequence` (used by `AdminApi`)

## Removed / deprecated

Nothing beyond the `CustomerOffersApi` consolidation and the four removed models listed above. No endpoints disappeared from other API classes.

## Sync module notes

`floriday_supplier_client.sync.sync_entities` is unaffected:

- No existing `get_*_by_sequence_number` callbacks changed signature, so existing sync wiring will continue to work.
- A new sync-endpoint pair is available on `CatalogPricesApi` for trade-item-availability-per-week (`get_trade_item_availabilities_per_week_by_sequence_number` / `..._max_sequence`); plug them into `sync_entities` only if you want to consume that new entity type.
