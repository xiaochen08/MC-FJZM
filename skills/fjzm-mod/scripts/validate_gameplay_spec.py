#!/usr/bin/env python3
"""Validate type-specific Minecraft gameplay attributes before Mod implementation."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


ID = re.compile(r"^[a-z][a-z0-9_\-]{1,63}$")
PROFILE_FIELDS = {
    "entity_pet_boss": (
        "max_health", "armor", "attack_damage", "movement_speed", "follow_range",
        "knockback_resistance", "hitbox", "faction_and_targets", "spawn_rules",
        "drops_and_xp", "persistence_and_despawn", "taming_and_breeding",
    ),
    "item_weapon_tool_armor": (
        "stack_size", "durability_or_uses", "rarity", "use_action", "cooldown",
        "attribute_modifiers", "acquisition", "persistence",
    ),
    "block_machine_turret": (
        "hardness", "blast_resistance", "harvest", "collision", "placement",
        "drops", "redstone", "tick_policy", "persistence", "ownership_and_permissions",
    ),
    "projectile": (
        "owner", "speed", "gravity", "lifetime", "collision", "damage",
        "friendly_fire", "impact", "network_sync", "cleanup",
    ),
    "gui_menu": (
        "open_condition", "slots", "data_fields", "synchronization", "permissions",
        "distance_validity", "close_behavior", "shift_click", "localization",
    ),
    "world_generation_structure": (
        "dimension", "biome_filters", "placement", "frequency", "height",
        "terrain_adaptation", "bounding_box", "seed_determinism", "performance",
    ),
}


def validate_spec(spec: dict[str, Any]) -> dict[str, list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if spec.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    for field in ("project_id", "asset_id"):
        value = spec.get(field)
        if not isinstance(value, str) or not ID.fullmatch(value):
            errors.append(f"{field} must be a stable lowercase ASCII identifier")
    if not isinstance(spec.get("asset_version"), str) or not spec["asset_version"].strip():
        errors.append("asset_version is required")

    asset_type = spec.get("asset_type")
    required = PROFILE_FIELDS.get(asset_type)
    if required is None:
        errors.append(f"asset_type must be one of: {', '.join(PROFILE_FIELDS)}")
        required = ()

    approval = spec.get("approval")
    if not isinstance(approval, dict) or approval.get("status") != "approved" or not approval.get("evidence"):
        errors.append("explicit attribute approval is required; guessed defaults are forbidden")

    attributes = spec.get("attributes")
    evidence = spec.get("attribute_evidence")
    if not isinstance(attributes, dict):
        errors.append("attributes object is required")
        attributes = {}
    if not isinstance(evidence, dict):
        errors.append("attribute_evidence object is required")
        evidence = {}
    for field in required:
        if field not in attributes or attributes[field] is None or attributes[field] == "":
            errors.append(f"attributes.{field} is required for {asset_type}")
        if not isinstance(evidence.get(field), str) or not evidence[field].strip():
            errors.append(f"attribute evidence for {field} is required")

    if asset_type == "entity_pet_boss":
        for field in ("max_health", "armor", "attack_damage", "movement_speed", "follow_range", "knockback_resistance"):
            value = attributes.get(field)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
                errors.append(f"attributes.{field} must be a non-negative number")
        if isinstance(attributes.get("max_health"), (int, float)) and attributes["max_health"] <= 0:
            errors.append("attributes.max_health must be greater than zero")
        hitbox = attributes.get("hitbox")
        if not isinstance(hitbox, dict) or not all(isinstance(hitbox.get(key), (int, float)) and hitbox[key] > 0 for key in ("width", "height")):
            errors.append("attributes.hitbox requires positive width and height")
    return {"errors": errors, "warnings": warnings}


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        payload = json.loads(args.spec.read_text(encoding="utf-8"))
        result = validate_spec(payload)
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
    print(f"PASS: {args.spec}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
