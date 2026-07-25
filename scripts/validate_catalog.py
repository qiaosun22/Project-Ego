#!/usr/bin/env python3
"""Dependency-free structural checks for ProjectEgo catalog records."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ROOT / "data" / "datasets"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_TOP_LEVEL = {
    "schema_version",
    "record_id",
    "identity",
    "classification",
    "access",
    "content",
    "provenance",
    "curation",
}


def is_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_record(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"invalid JSON: {exc}"]

    missing = REQUIRED_TOP_LEVEL - record.keys()
    if missing:
        errors.append(f"missing top-level fields: {', '.join(sorted(missing))}")

    record_id = record.get("record_id")
    if not isinstance(record_id, str) or not SLUG.fullmatch(record_id):
        errors.append("record_id must be a lowercase kebab-case slug")
    elif path.stem != record_id.rsplit("-v", 1)[0] and path.stem != record_id:
        errors.append("filename must match record_id or its dataset stem")

    if record.get("schema_version") != "0.1.0":
        errors.append("unsupported schema_version")

    provenance = record.get("provenance", [])
    if not isinstance(provenance, list) or not provenance:
        errors.append("provenance must contain at least one source")
        provenance = []
    source_ids = {source.get("source_id") for source in provenance if isinstance(source, dict)}
    if None in source_ids:
        errors.append("every provenance entry requires source_id")
    if len(source_ids) != len(provenance):
        errors.append("provenance source_id values must be unique")

    for index, source in enumerate(provenance):
        if not isinstance(source, dict):
            errors.append(f"provenance[{index}] must be an object")
            continue
        if not is_url(source.get("url")):
            errors.append(f"provenance[{index}].url must be an HTTP(S) URL")
        level = source.get("evidence_level")
        if not isinstance(level, int) or not 1 <= level <= 5:
            errors.append(f"provenance[{index}].evidence_level must be 1..5")

    referenced: set[str] = set(record.get("access", {}).get("source_ids", []))
    for group in ("modalities", "annotations"):
        for item in record.get("content", {}).get(group, []):
            referenced.update(item.get("source_ids", []))
    for quantity in record.get("content", {}).get("scale", {}).values():
        referenced.update(quantity.get("source_ids", []))
    for observation in record.get("quality_observations", []):
        referenced.update(observation.get("source_ids", []))
    dangling = referenced - source_ids
    if dangling:
        errors.append(f"unknown source references: {', '.join(sorted(dangling))}")

    return errors


def main() -> int:
    files = sorted(DATASET_DIR.glob("*.json"))
    if not files:
        print("No dataset records found.", file=sys.stderr)
        return 1

    failed = False
    for path in files:
        errors = validate_record(path)
        if errors:
            failed = True
            print(f"FAIL {path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path.relative_to(ROOT)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
