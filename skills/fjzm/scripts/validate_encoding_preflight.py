#!/usr/bin/env python3
"""Validate the red Windows UTF-8 preflight report before FJZM production."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable


HOST_EXPECTED = {
    "powershell7": "passed",
    "console_input_encoding": "utf-8",
    "console_output_encoding": "utf-8",
    "default_text_write": "utf-8-no-bom",
    "line_endings": "lf",
    "chinese_sentinel_round_trip": "passed",
    "strict_utf8_decode_scan": "passed",
    "bom_violations": 0,
    "invalid_utf8_files": 0,
}

PROJECT_EXPECTED = {
    "java_process_file_encoding": "utf-8",
    "gradle_daemon_file_encoding": "utf-8",
    "java_compile_encoding": "utf-8",
    "localized_resource_round_trip": "passed",
    "localized_build": "passed",
    "strict_utf8_decode_scan": "passed",
}


def _check_fields(data: Any, prefix: str, expected: dict[str, Any], errors: list[str]) -> None:
    if not isinstance(data, dict):
        errors.append(f"{prefix} must be an object")
        return
    for key, value in expected.items():
        if data.get(key) != value:
            errors.append(f"{prefix}.{key} must be {value!r}")


def validate_report(report: dict[str, Any], required_phase: str) -> dict[str, list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if report.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if report.get("severity") != "red":
        errors.append("severity must be red")
    if required_phase not in {"host", "project"}:
        errors.append("required_phase must be host or project")
        return {"errors": errors, "warnings": warnings}

    allowed_status = {"host_passed", "project_passed"} if required_phase == "host" else {"project_passed"}
    if report.get("status") not in allowed_status:
        errors.append(f"status does not satisfy required {required_phase} phase")
    _check_fields(report.get("host_checks"), "host_checks", HOST_EXPECTED, errors)
    if required_phase == "project":
        _check_fields(report.get("project_checks"), "project_checks", PROJECT_EXPECTED, errors)
    return {"errors": errors, "warnings": warnings}


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--required-phase", choices=("host", "project"), required=True)
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        payload = json.loads(args.report.read_text(encoding="utf-8"))
        result = validate_report(payload, args.required_phase)
    except (OSError, UnicodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    for warning in result["warnings"]:
        print(f"WARNING: {warning}")
    for error in result["errors"]:
        print(f"ERROR: {error}")
    if result["errors"]:
        print(f"FAIL: {len(result['errors'])} error(s)")
        return 1
    print(f"PASS: {args.report} ({args.required_phase})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
