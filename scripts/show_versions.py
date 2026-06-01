#!/usr/bin/env python3
"""Print the Floriday API version recorded in every place that matters and
flag disagreements.

Usage: python3 scripts/show_versions.py

Sources checked:
  - Makefile           api_version
  - api_factory.py     EXPECTED_API_VERSION
  - .env.example       FLORIDAY_BASE_URL version segment
  - .env (if present)  FLORIDAY_BASE_URL version segment  (integration-test guard)
  - specs/             info.version of the spec for the Makefile's api_version

Exit code 1 if the two committed sources (Makefile vs api_factory) disagree,
since that is a real bug a version bump must not paper over. Other mismatches
print a warning but do not fail. Stdlib only.
"""
import json
import os
import re
import sys

VER_RE = r"suppliers-api-(\d{4}v\d+)"


def find(path, pattern):
    try:
        with open(path) as f:
            m = re.search(pattern, f.read())
            return m.group(1) if m else None
    except FileNotFoundError:
        return None


def main():
    makefile = find("makefile", r"api_version\s*:=\s*(\S+)") \
        or find("Makefile", r"api_version\s*:=\s*(\S+)")
    factory = find("floriday_supplier_client/api_factory.py",
                   r'EXPECTED_API_VERSION\s*=\s*"([^"]+)"')
    env_example = find(".env.example", VER_RE)
    env_local = find(".env", VER_RE)

    spec_ver = None
    if makefile:
        spec_path = f"specs/floriday-suppliers-api-{makefile}-swagger-UUID.json"
        if os.path.exists(spec_path):
            with open(spec_path) as f:
                spec_ver = json.load(f).get("info", {}).get("version")

    rows = [
        ("Makefile api_version", makefile),
        ("api_factory EXPECTED_API_VERSION", factory),
        (".env.example base URL", env_example),
        (".env base URL (local)", env_local),
        (f"spec info.version ({makefile})", spec_ver),
    ]
    width = max(len(r[0]) for r in rows)
    for label, val in rows:
        print(f"  {label:<{width}} : {val or '(not found)'}")

    print()
    ok = True
    if makefile and factory and makefile != factory:
        print(f"ERROR: Makefile ({makefile}) and api_factory ({factory}) DISAGREE "
              f"- fix this before bumping.")
        ok = False
    if env_local and factory and env_local != factory:
        print(f"WARN: local .env points to {env_local} but client expects {factory} "
              f"- integration tests will fail the version guard. Update .env (and on "
              f"this harness pass FLORIDAY_BASE_URL inline to make test-integration).")
    if spec_ver and makefile and spec_ver != makefile:
        print(f"WARN: spec info.version ({spec_ver}) != Makefile api_version "
              f"({makefile}) - trust the spec, re-fetch with make local_specs.")
    if ok and not any(
        v and v != factory for v in (env_local, spec_ver) if v
    ):
        print("All version sources agree.")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
