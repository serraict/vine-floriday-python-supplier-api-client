# Doing

Issue reference on Github: [Issue #2 - Update to the latest api version](https://github.com/serraict/vine-floriday-python-supplier-api-client/issues/2)

## Goal

Update the Floriday Python Supplier API Client from the current version (v2024.1) to the latest API version (v2024.2).

## Analysis

The Floriday API has been updated from v2024.1 to v2024.2 with several changes to models, endpoints, and enums. The key changes include:

1. New properties added to existing models:
   - `sellerOrganizationId` added to TradeItem and TradeItemSummary
   - `floricodeVrsPackagingId` added to CustomPackage
   - `name` added to DeliveryLocation
   - `isPaid` added to SalesOrder
   - `stickerId` added to OrderedAdditionalService
   - `batchReference` added to SalesOrder
   - `creationDateTime` added to CustomerSticker
   - `additionalPackagingInformationFloricodeVrsPackagingIds` added to TradeItem
   - `floricodeVrsPackagingId` added to PackingConfiguration
   - `shouldReturnPackages` added to AddSalesOrderCorrectionRequest and SalesOrderCorrectionRequest

2. New endpoints:
   - SalesOrders - Assign Additional Services
   - FulfillmentOrders - Assign Missing Carrier Organization
   - AddClockSupplyLines - Define clock strategy

3. New models:
   - CustomerOffer and CustomerOfferLine
   - BatchBaseSupply, BatchBaseSupplyPackingConfiguration, BatchBaseSupplyPriceGroupPrice

4. Enum changes:
   - New value RFH_AFTERPAY added to PaymentProvider
   - New values HALF_YEAR and YEAR added to ContractPeriodKind
   - New types added to LoadCarrierType

5. Property changes:
   - `addedOn` renamed to `creationDateTime` in BatchMutation
   - Type change for `pricePerPiece` in EditClockPresalesSupplyLine from double to decimal
   - Several nullable properties updated to non-nullable in Warehouse, Organization, and Batch models

## Design

To update the client to the latest API version, we need to:

1. Implement API version tagging strategy
   - Add tags to mark which API version each release targets
   - Update release process to maintain these tags
2. Update the Swagger/OpenAPI specification to the latest version
3. Regenerate the client code using swagger-codegen
4. Ensure any custom code in the client is preserved during regeneration
5. Update the base URL to point to the v2024.2 API
6. Update tests to work with the new API version
7. Update documentation to reflect the changes

## Steps

After each step, commit all repository changes.

1. Version Tagging Setup
   - Add tag `floriday_api_v2024.1` to mark the last commit targeting v2024.1
   - Update makefile's release target to manage API version tags
   - Ensure release process creates/moves `floriday_api_v{version}` tag

2. API Version Update
   - Update makefile's api_version to 2024v2
   - Update spec URL in makefile to point to v2024.2
   - Check the current `.swagger-codegen-ignore` file to ensure custom code is preserved
   - Download the latest OpenAPI specification for v2024.2
   - Update the base URL in the client configuration to point to v2024.2

3. Code Generation & Updates
   - Regenerate the client code using swagger-codegen
   - Review the generated code for any issues
   - Update tests to work with the new API version
   - Update documentation to reflect the changes

4. Testing & Release
   - Run unit tests with `make tests`
   - Run integration tests with `make test-integration`
   - Create a new release that will:
     - Tag the release with version number
     - Tag with `floriday_api_v2024.2` to mark API version
     - Push both tags to the repository

## Progress

Version Tagging:
- [x] Add `floriday_api_v2024.1` tag to current version
- [x] Update makefile release target for API version tagging

API Version Update:
- [x] Update makefile api_version and spec URL
- [x] Check `.swagger-codegen-ignore` file
- [ ] Download latest OpenAPI specification
- [ ] Update base URL in configuration

Code Generation & Updates:
- [ ] Regenerate client code
- [ ] Review generated code
- [ ] Update tests
- [ ] Update documentation

Testing & Release:
- [ ] Run unit tests
- [ ] Run integration tests
- [ ] Create release with version and API tags
