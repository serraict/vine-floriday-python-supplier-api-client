#!/usr/bin/env python3
"""Report public-surface changes between a git base ref and the working tree.

Usage:
    python3 scripts/surface_diff.py [BASE_REF]   # default BASE_REF=HEAD

Compares the API classes, their methods, the model classes and their
attributes as they exist in BASE_REF against the current files on disk
(INCLUDING untracked files, which `git diff` hides). Intended to be run
after regenerating the client but before committing, to surface the
consumer-facing diff for the update guide.

Output is grouped into BREAKING (things that remove or change existing
public surface) and ADDITIVE (new classes/methods/attributes). Exits 0
regardless of findings; this is a report, not a gate. Stdlib only.
"""
import glob
import os
import re
import subprocess
import sys

API_DIR = "floriday_supplier_client/api"
MODELS_DIR = "floriday_supplier_client/models"
FACTORY = "floriday_supplier_client/api_factory.py"
SEQ_RE = r"get_[a-z0-9_]*(?:by_sequence_number|max_sequence)"


def git_show(ref, path):
    r = subprocess.run(["git", "show", f"{ref}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def git_ls(ref, path):
    r = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return set()
    return {os.path.basename(l) for l in r.stdout.splitlines()
            if l.endswith(".py") and os.path.basename(l) != "__init__.py"}


def disk_ls(d):
    return {os.path.basename(p) for p in glob.glob(f"{d}/*.py")
            if os.path.basename(p) != "__init__.py"}


def read_disk(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return None


def methods(text):
    if not text:
        return set()
    out = set()
    for m in re.findall(r"^\s*def ([a-z0-9_]+)\(", text, re.M):
        if not m.endswith("_with_http_info") and m != "__init__":
            out.add(m)
    return out


def seq_sigs(text):
    """Map sync-callback method name -> normalized parameter list."""
    if not text:
        return {}
    sigs = {}
    for m in re.finditer(rf"def ({SEQ_RE})\(self([^)]*)\)", text):
        sigs[m.group(1)] = re.sub(r"\s+", " ", m.group(2)).strip(", ").strip()
    return sigs


def attrs(text):
    if not text:
        return set()
    return set(re.findall(r"'([a-zA-Z0-9_]+)': '", text))


def scopes_in(text):
    if not text:
        return set()
    return set(re.findall(r"(?:role:app|[a-z][a-z-]+:(?:read|write))", text))


def fmt(items):
    return ", ".join(sorted(items))


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    breaking, additive, notes = [], [], []

    # ---- API classes ----
    base_api, disk_api = git_ls(base, API_DIR), disk_ls(API_DIR)
    for f in sorted(disk_api - base_api):
        additive.append(f"NEW API class file: {f}")
    for f in sorted(base_api - disk_api):
        breaking.append(f"REMOVED API class file: {f}")
    for f in sorted(base_api & disk_api):
        old, new = git_show(base, f"{API_DIR}/{f}"), read_disk(f"{API_DIR}/{f}")
        rm, add = methods(old) - methods(new), methods(new) - methods(old)
        for m in sorted(rm):
            breaking.append(f"{f}: removed method {m}()")
        for m in sorted(add):
            additive.append(f"{f}: new method {m}()")
        os_, ns = seq_sigs(old), seq_sigs(new)
        for m in sorted(set(os_) & set(ns)):
            if os_[m] != ns[m]:
                breaking.append(f"{f}: SYNC CALLBACK signature changed {m}"
                                f"({os_[m]}) -> ({ns[m]})")

    # ---- Models ----
    base_m, disk_m = git_ls(base, MODELS_DIR), disk_ls(MODELS_DIR)
    for f in sorted(disk_m - base_m):
        additive.append(f"NEW model: {f}")
    for f in sorted(base_m - disk_m):
        breaking.append(f"REMOVED model: {f}")
    for f in sorted(base_m & disk_m):
        old, new = git_show(base, f"{MODELS_DIR}/{f}"), read_disk(f"{MODELS_DIR}/{f}")
        rm, add = attrs(old) - attrs(new), attrs(new) - attrs(old)
        if rm:
            breaking.append(f"{f}: removed/renamed attribute(s): {fmt(rm)}")
        if add:
            additive.append(f"{f}: new attribute(s): {fmt(add)}")

    # ---- OAuth scopes (informational) ----
    requested = scopes_in(read_disk(FACTORY))
    spec = sorted(glob.glob("specs/*-swagger-UUID.json"))
    if spec and requested:
        used = scopes_in(read_disk(spec[-1]))
        missing = used - requested
        if missing:
            notes.append(f"Spec references scopes ApiFactory does NOT request: "
                         f"{fmt(missing)} (pre-existing curation; only matters if "
                         f"consumers call those endpoints with the bundled factory)")

    # ---- Report ----
    print(f"Public-surface diff: {base} -> working tree\n")
    print(f"BREAKING ({len(breaking)}):")
    print("\n".join(f"  - {x}" for x in breaking) if breaking else "  (none)")
    print(f"\nADDITIVE ({len(additive)}):")
    print("\n".join(f"  - {x}" for x in additive) if additive else "  (none)")
    if notes:
        print("\nNOTES:")
        print("\n".join(f"  - {x}" for x in notes))


if __name__ == "__main__":
    main()
