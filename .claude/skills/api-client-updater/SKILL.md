---
name: api-client-updater
description: Update the Floriday Supplier API Python client to a newer Floriday API version and produce a consumer-facing update guide. Use this whenever the user asks to update/bump/upgrade the Floriday client, regenerate against a new Floriday release, "move to 2025v2" (or any new `NNNNvN` version), or prepare a release for a new Floriday API version. Trigger even when the user doesn't explicitly say "skill" — phrasings like "new Floriday API is out", "regenerate the swagger client", or "bump to the latest supplier API" should all invoke this. Only applies inside the vine-floriday-python-supplier-api-client repo (or repos with the same Makefile/ApiFactory layout).
---

# Floriday API Client Updater

This skill walks a maintainer through bumping this library to a new Floriday Supplier API version and writing the update notes consumers need. It is a release workflow, not a consumer feature.

## What you are producing

1. A regenerated `floriday_supplier_client/` and `test/` against the new spec.
2. Three version bumps committed in step with the regeneration.
3. `about/update_guides/UPDATE_GUIDE_<new_version>.md` — a consumer-facing migration note focused on the public surface (API classes, model fields, method signatures, config/env, auth scopes).
4. A short maintainer punch list of anything that needs human attention before cutting a release (failing tests, codegen warnings, suspicious diffs).

Do **not** commit or tag a release on your own initiative — leave that to the maintainer, unless they explicitly direct you through it (see step 8).

## The public surface that matters to consumers

Consumers of this library depend on a narrow set of things. Diff with these in mind — changes inside generated plumbing (internal helpers, serialization internals, docstring rewording) are noise, not migration items.

- `ApiFactory` (floriday_supplier_client/api_factory.py) — constructor, `get_api_client`, `get_api_instance`, `EXPECTED_API_VERSION`.
- Per-endpoint API classes exposed at the package root: `TradeItemsApi`, `SalesOrdersApi`, `BatchesApi`, `ContractsApi`, and the rest. Specifically: which classes exist, which methods each has, and each method's parameters and return type.
- Models under `floriday_supplier_client/models/` — which classes exist and which attributes they expose.
- `floriday_supplier_client.sync` — `sync_entities`, `EntitySyncResult`. This module is preserved via `.swagger-codegen-ignore`, so it shouldn't change from regeneration — but callbacks like `get_*_by_sequence_number` *can* change signature, which breaks sync callers.
- `ApiException` from `floriday_supplier_client.rest`.
- OAuth scopes requested in `ApiFactory._get_access_token` — if Floriday adds/removes scopes for the new version, consumers with restricted credentials may need updates.
- Environment variables: `FLORIDAY_CLIENT_ID`, `FLORIDAY_CLIENT_SECRET`, `FLORIDAY_API_KEY`, `FLORIDAY_AUTH_URL`, `FLORIDAY_BASE_URL`.

## Workflow

### 1. Find the target version and confirm with the maintainer

Run `make versions` to print the API version recorded everywhere that matters — `Makefile` `api_version`, `api_factory.py` `EXPECTED_API_VERSION`, `.env.example`, the local `.env`, and the spec's `info.version` — and to flag disagreements automatically.

The two committed sources that must agree are `Makefile` `api_version` and `api_factory.py` `EXPECTED_API_VERSION`; `make versions` exits non-zero if they disagree. If it does, stop and tell the maintainer — that's a pre-existing bug and you shouldn't paper over it with a bump.

Then discover what Floriday currently offers. Check these sources in order and cross-reference them — any single page can lag, so corroborate before committing to a target version:

1. **Welcome / changelog**: https://developer.floriday.io/docs/welcome — usually lists the current and upcoming API versions with release dates and deprecation timelines.
2. **Release notes / versioning pages**: follow links from the welcome page (typically "API versioning", "Release notes", or a "What's new in YYYYvN" article). The changelog often names the version that is *currently recommended* vs. versions that are still available but deprecated.
3. **The live swagger endpoint**: run `make remote-version V=<candidate>` (e.g. `make remote-version V=2026v1`) to probe staging. A `200` or `401` confirms the version exists and the URL shape is unchanged (`401` just means the endpoint needs auth — that still confirms it resolves); a `404` means either the version is wrong or Floriday changed the URL template (the latter is a bigger problem and needs maintainer attention).
4. **Spec `info.version`**: if you can pull the spec (step 4 fetches it), the spec's own `info.version` field is ground truth for what you're about to generate against. If it disagrees with what the docs advertised, trust the spec and flag the mismatch.

Produce a short report for the maintainer before touching any files:

- Current client version (from Makefile + api_factory.py)
- Latest version advertised in Floriday docs, with the URL you found it at
- Any other still-supported versions and their deprecation dates, if the docs say
- Recommended target and why (usually "latest non-deprecated stable")
- Any red flags: docs don't list versions clearly, welcome page 404s, URL template looks different, versions disagree between sources

Format the recommendation as: "Currently on `<old>`. Floriday's latest is `<new>` (source: `<url>`). Recommend bumping to `<new>`. Proceed?" — then wait for explicit confirmation before continuing. Picking the wrong version wastes a full regeneration cycle and muddies the git history, so the extra round-trip is worth it.

If the maintainer names a specific version (e.g. "bump to 2025v2"), still do the doc check and confirm the named version actually exists and isn't already deprecated before proceeding.

### 2. Make sure the working tree is clean

No `/tmp` snapshot is needed — `make surface-diff` (step 6) diffs the committed code at `HEAD` against the regenerated working tree, *including untracked files*. For that to give a true before/after, `HEAD` must hold the current (pre-bump) generated client, so start from a clean tree:

```bash
git status --porcelain   # expect no output
```

If there are unrelated uncommitted changes, stop and check with the maintainer rather than mixing them into the regeneration diff.

### 3. Apply the three version bumps

- `Makefile`: `api_version := <new_version>`
- `floriday_supplier_client/api_factory.py`: `EXPECTED_API_VERSION = "<new_version>"`
- `.env.example`: update the version segment in `FLORIDAY_BASE_URL` (e.g. `suppliers-api-2025v1` → `suppliers-api-<new_version>`)

Grep the repo for the old version string after you're done to make sure nothing else references it (docs, example code, CI config). Flag stragglers to the maintainer rather than silently rewriting docs — some references may be intentional historical notes.

### 4. Regenerate

```bash
make local_specs   # fetches new swagger spec to ./specs/
make client        # runs swagger-codegen
```

`make client` depends on the spec file path, which includes the version — so `local_specs` must succeed first. If `local_specs` fails (404, auth), the spec URL format may have changed; check Floriday docs before patching the Makefile URL template.

Capture and surface any codegen warnings. Swagger-codegen warnings about unmapped types, missing `operationId`s, or discriminator issues often map directly to fields/methods that end up missing or broken in the generated code — they belong in the maintainer punch list.

### 5. Run the tests

```bash
make tests         # unit tests (not integration)
```

Report failures with their context. Do **not** run `make test-integration` unless the maintainer asks — it hits the live Floriday API and calls `example.py`.

If the maintainer does ask you to run it, it (and `example.py`) requires `FLORIDAY_BASE_URL` to point at `suppliers-api-<new_version>`, matching `EXPECTED_API_VERSION`, or `ApiFactory` raises a version-mismatch `ValueError` before any request goes out. Update the version segment in the local `.env` (gitignored), and on this harness *also* pass it inline because the shell's direnv-exported value can be stale after editing `.env`:

```bash
FLORIDAY_BASE_URL="https://api.staging.floriday.io/suppliers-api-<new_version>" make test-integration
```

### 6. Diff the public surface

Run `make surface-diff` (defaults to comparing `HEAD` against the working tree). It reports, grouped into **BREAKING** and **ADDITIVE**, every item in "The public surface that matters to consumers" above:

- added/removed API class files — *including untracked ones*, which `git diff` hides (this masked a whole new API class during the 2026v1 bump)
- added/removed methods per API class
- changed `get_*_by_sequence_number` / `*_max_sequence` signatures (sync-callback breakages)
- added/removed model classes
- added/removed/renamed model attributes (a rename shows as a removed **and** an added attribute on the same model — read those pairs as renames)
- OAuth scopes the spec references but `ApiFactory` does not request (informational)

To review what a specific commit changed instead of the working tree, pass a base ref: `make surface-diff BASE=<ref>`.

Treat everything under BREAKING as a migration item and verify each by hand — open the model/API file to confirm the rename or removed method, since the tool reports symbol changes, not intent. The ADDITIVE list feeds the "New capabilities" section of the guide. If a major release produces a long ADDITIVE list, group it by theme — e.g. "all `*Batch*` models gained `lot_code`", "`SalesOrdersApi` gained 3 amendment methods" — and enumerate only the breakages precisely.

### 7. Write the update guide

Write to `about/update_guides/UPDATE_GUIDE_<new_version>.md` (create the directory if it does not exist). Structure:

```markdown
# Update guide: Floriday Supplier API <old_version> → <new_version>

## Summary
One paragraph: what's the headline of this Floriday release, and what's the bottom-line impact for consumers of this library (e.g. "no breaking changes, two new endpoints" or "breaking: `SalesOrderLine.price` renamed to `unit_price`").

## Required config changes
- Update `FLORIDAY_BASE_URL` to `.../suppliers-api-<new_version>`
- Upgrade this library to version `<library-version-that-will-ship>`
- (Any new env vars, scope changes, etc.)

## Breaking changes
Only list things that will cause existing consumer code to fail at import, at call time, or to silently return wrong data. For each:
- What broke
- How to migrate (concrete before/after snippet where it helps)

## New capabilities
New API classes, new methods on existing classes, new models worth knowing about. Keep it skimmable — consumers will read Floriday's own changelog for depth.

## Removed / deprecated
Endpoints or models that disappeared. If Floriday documented a deprecation path, link it.

## Sync module notes
If any `get_*_by_sequence_number` method changed signature, call it out — `sync_entities` callers bind these as callbacks and will break.
```

Keep breaking changes precise and everything else skimmable. A consumer reading this guide wants to know in 30 seconds whether their upgrade is a one-line bump or a real migration.

### 8. Maintainer punch list

End your final message with a short checklist of things the maintainer still needs to do — typically:

- Review the update guide
- Decide on library version number
- Run `make test-integration` against staging
- Follow the release steps in `about/readme.md` (tag, push)
- Resolve any test failures or codegen warnings you surfaced

By default, do not run the release steps yourself — leave them to the maintainer. But if the maintainer explicitly directs you to commit and release, here is the mechanism (learned the hard way):

- **The shipped version is driven by the git tag, not a file.** `make release` auto-tags `v$(python -m setuptools_scm --strip-dev)`, which is always a **patch** bump from the last tag. For a **minor or major** bump, do NOT run `make release` verbatim — tag `vX.Y.0` explicitly, then push the tags the same way the target does.
- **Pushing any `v*` tag triggers `.github/workflows/python-publish.yml`, which publishes to PyPI** — irreversible (a version can be yanked but never reused). Confirm the exact version with the maintainer before pushing the tag.
- The `release` target's preconditions are: clean tree, `main` checked out, and `origin/main == HEAD`. So commit, then `git push origin main`, *then* tag and push tags.
- Run git commands one at a time (not chained with `&&`) so each matches its permission allowlist entry and doesn't trigger a prompt.

## Things to avoid

- Don't edit files under `floriday_supplier_client/` or `test/` by hand to "fix" codegen output — that work is lost on the next regeneration. If generated code is wrong, the fix goes in `.swagger-codegen-ignore` (to protect a hand-written file) or upstream in the spec.
- Don't commit. The maintainer reviews the diff before committing. If the regeneration pulls in changes you don't understand, flag them rather than burying them in a commit.
- Don't treat the volume of the generated diff as meaningful. Swagger-codegen routinely reshuffles formatting, docstrings, and import order between runs. Focus only on the public-surface diff from step 6.
- Don't guess the Floriday version from recent commits or the current Makefile — always cross-check against Floriday's docs, because "latest" drifts.
