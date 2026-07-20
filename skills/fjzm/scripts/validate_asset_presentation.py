#!/usr/bin/env python3
"""Validate one FJZM Mod asset's player-facing presentation contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
KEY_PATTERN = re.compile(r"^[a-z0-9_.-]+$")
SURFACES = {"tooltip", "gui_info_panel", "hud", "boss_bar", "catalog", "multiple"}
STYLE_MODES = {"themed_serious", "light_chuunibyou", "full_chuunibyou"}
STABLE_RULES = {"stable_per_stack", "stable_per_asset_instance", "stable_per_session"}
LINE_ORDER = ["display_name", "mod_line", "usage", "flavor"]


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _translation_key(value: Any) -> bool:
    return _text(value) and bool(KEY_PATTERN.fullmatch(value))


def _style(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{path} must be an object")
        return {}
    if not _text(value.get("color")):
        errors.append(f"{path}.color is required")
    for flag in ("bold", "italic"):
        if flag in value and not isinstance(value.get(flag), bool):
            errors.append(f"{path}.{flag} must be true or false")
    return value


def _localized_line(payload: dict[str, Any], field: str, errors: list[str]) -> dict[str, Any]:
    value = payload.get(field)
    if not isinstance(value, dict):
        errors.append(f"{field} must be an object")
        return {}
    if not _translation_key(value.get("translation_key")):
        errors.append(f"{field}.translation_key is required and must be a stable localization key")
    _style(value.get("style"), f"{field}.style", errors)
    return value


def validate_manifest(payload: dict[str, Any]) -> dict[str, list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    for field in ("project_id", "asset_id", "mod_id"):
        value = payload.get(field)
        if not _text(value) or not ID_PATTERN.fullmatch(value):
            errors.append(f"{field} must be a lowercase ASCII identifier")

    surfaces = payload.get("presentation_surface")
    if not isinstance(surfaces, list) or not surfaces:
        errors.append("presentation_surface must be a non-empty list")
    elif any(surface not in SURFACES for surface in surfaces):
        errors.append(f"presentation_surface values must be one of: {', '.join(sorted(SURFACES))}")

    display_name = _localized_line(payload, "display_name", errors)
    mod_line = _localized_line(payload, "mod_line", errors)
    _localized_line(payload, "usage", errors)

    display_style = display_name.get("style") if isinstance(display_name.get("style"), dict) else {}
    if display_style.get("bold") is not True:
        warnings.append("display_name.style.bold is recommended for a clear hierarchy")

    mod_style = mod_line.get("style") if isinstance(mod_line.get("style"), dict) else {}
    if mod_style.get("color") != "gray":
        errors.append("mod_line.style.color must be gray")
    if mod_style.get("italic") is not True:
        errors.append("mod_line.style.italic must be true")

    flavor = payload.get("flavor")
    if not isinstance(flavor, dict):
        errors.append("flavor must be an object")
        flavor = {}
    if flavor.get("style_mode") not in STYLE_MODES:
        errors.append(f"flavor.style_mode must be one of: {', '.join(sorted(STYLE_MODES))}")
    if flavor.get("selection_rule") not in STABLE_RULES:
        errors.append("flavor.selection_rule must use a stable non-per-frame rule")
    _style(flavor.get("style"), "flavor.style", errors)

    entries = flavor.get("entries")
    if not isinstance(entries, list) or len(entries) < 4:
        errors.append("flavor.entries must contain at least 4 approved entries")
        entries = entries if isinstance(entries, list) else []
    elif len(entries) > 8:
        warnings.append("flavor.entries normally should contain no more than 8 entries")

    keys: list[str] = []
    texts: list[str] = []
    for index, entry in enumerate(entries):
        path = f"flavor.entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{path} must be an object")
            continue
        key = entry.get("translation_key")
        text_zh = entry.get("text_zh")
        if not _translation_key(key):
            errors.append(f"{path}.translation_key is required")
        else:
            keys.append(key)
        if not _text(text_zh):
            errors.append(f"{path}.text_zh is required")
        else:
            texts.append(text_zh.strip())
            if "§" in text_zh:
                errors.append(f"{path}.text_zh must not contain legacy formatting codes")
    if len(keys) != len(set(keys)) or len(texts) != len(set(texts)):
        errors.append("flavor entries must use unique translation keys and unique text")

    layout = payload.get("layout")
    if not isinstance(layout, dict):
        errors.append("layout must be an object")
        layout = {}
    if layout.get("line_order") != LINE_ORDER:
        errors.append(f"layout.line_order must be exactly {LINE_ORDER}")
    wrap_width = layout.get("wrap_width")
    if not isinstance(wrap_width, int) or isinstance(wrap_width, bool) or wrap_width < 80:
        errors.append("layout.wrap_width must be an integer of at least 80 pixels")
    scales = layout.get("gui_scale_tested")
    if not isinstance(scales, list) or not scales or any(not isinstance(value, int) or isinstance(value, bool) or value < 1 for value in scales):
        errors.append("layout.gui_scale_tested must contain one or more positive integer GUI scales")
    if layout.get("color_only_meaning") is not False:
        errors.append("layout.color_only_meaning must be false")

    return {"errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="Path to asset-presentation.json")
    args = parser.parse_args()

    try:
        with args.manifest.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({"errors": [str(exc)], "warnings": []}, ensure_ascii=False, indent=2))
        return 2

    if not isinstance(payload, dict):
        result = {"errors": ["manifest root must be an object"], "warnings": []}
    else:
        result = validate_manifest(payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
