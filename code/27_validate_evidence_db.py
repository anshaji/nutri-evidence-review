#!/usr/bin/env python3
"""Validate the evidence database against its JSON Schema (accuracy guardrail).

Checks every record in data/evidence_db.json against
schema/evidence_record.schema.json and prints a conformance report. Exits
non-zero if any record violates the schema — handy to run after each extraction
so schema drift (new stray keys, bad enums, wrong types) is caught immediately.

Dependency-free: implements the small subset of JSON Schema the schema uses
(type, enum, pattern, required, properties, additionalProperties, items, $ref,
anyOf), so it needs neither pip nor the `jsonschema` package.

Usage:
    python3 code/27_validate_evidence_db.py
    python3 code/27_validate_evidence_db.py [data/evidence_db.json] [schema.json]
"""

import json
import os
import re
import sys
from collections import Counter

DEFAULT_DB = "./data/evidence_db.json"
DEFAULT_SCHEMA = "./schema/evidence_record.schema.json"


def _type_ok(inst, types) -> bool:
    for t in types:
        if t == "null" and inst is None:
            return True
        if t == "string" and isinstance(inst, str):
            return True
        if t == "boolean" and isinstance(inst, bool):
            return True
        if t == "integer" and isinstance(inst, int) and not isinstance(inst, bool):
            return True
        if t == "number" and isinstance(inst, (int, float)) and not isinstance(inst, bool):
            return True
        if t == "object" and isinstance(inst, dict):
            return True
        if t == "array" and isinstance(inst, list):
            return True
    return False


def _resolve(ref: str, root: dict):
    node = root
    for part in ref.lstrip("#/").split("/"):
        node = node[part]
    return node


def validate(inst, schema: dict, path: str, errs: list, root: dict) -> None:
    if "$ref" in schema:
        return validate(inst, _resolve(schema["$ref"], root), path, errs, root)

    if "anyOf" in schema:
        for sub in schema["anyOf"]:
            branch: list = []
            validate(inst, sub, path, branch, root)
            if not branch:
                return
        errs.append(f"{path}: no anyOf branch matched (value={inst!r})")
        return

    t = schema.get("type")
    if t is not None:
        types = t if isinstance(t, list) else [t]
        if not _type_ok(inst, types):
            errs.append(f"{path}: type {type(inst).__name__} not in {types}")
            return  # further checks are unsafe if the type is wrong

    if "enum" in schema and inst not in schema["enum"]:
        errs.append(f"{path}: {inst!r} not in enum {schema['enum']}")

    if "pattern" in schema and isinstance(inst, str):
        if not re.search(schema["pattern"], inst):
            errs.append(f"{path}: {inst!r} does not match /{schema['pattern']}/")

    if isinstance(inst, dict) and ("properties" in schema or schema.get("type") == "object"):
        props = schema.get("properties", {})
        for k in schema.get("required", []):
            if k not in inst:
                errs.append(f"{path}: missing required '{k}'")
        if schema.get("additionalProperties") is False:
            for k in inst:
                if k not in props:
                    errs.append(f"{path}: unexpected key '{k}'")
        for k, v in inst.items():
            if k in props:
                validate(v, props[k], f"{path}.{k}", errs, root)

    if isinstance(inst, list) and "items" in schema:
        for i, item in enumerate(inst):
            validate(item, schema["items"], f"{path}[{i}]", errs, root)


def main():
    db_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DB
    schema_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_SCHEMA
    schema = json.load(open(schema_path))
    records = json.load(open(db_path))
    if not isinstance(records, list):
        records = [records]

    all_errs = []
    bad_records = 0
    for i, r in enumerate(records):
        errs: list = []
        key = r.get("key", f"#{i}") if isinstance(r, dict) else f"#{i}"
        validate(r, schema, key, errs, schema)
        if errs:
            bad_records += 1
            all_errs.extend(errs)

    print(f"Validated {len(records)} records in {db_path}")
    print(f"  against {schema_path}")
    if not all_errs:
        print(f"  ✓ CONFORMANT — 0 violations across {len(records)} records")
        sys.exit(0)
    # summarise by violation kind (strip the record key / index prefix)
    kinds = Counter(re.sub(r"^[^:]+", "", e, count=1).lstrip(": ") for e in all_errs)
    print(f"  ✗ {len(all_errs)} violations in {bad_records} records:")
    for kind, n in kinds.most_common(20):
        print(f"    {n:>4d}  {kind}")
    print("\n  examples:")
    for e in all_errs[:8]:
        print(f"    {e}")
    sys.exit(1)


if __name__ == "__main__":
    main()
