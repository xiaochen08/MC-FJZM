import argparse
import json
import re
import sys
from pathlib import Path


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
STAGES = {"project_bootstrap", "gameplay_design", "runtime_integration"}


def require(data, keys, label="contract"):
    missing = [key for key in keys if key not in data]
    if missing:
        raise ValueError(f"{label} missing fields: {', '.join(missing)}")


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate_sha(value, label):
    if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
        raise ValueError(f"{label} must be 64 lowercase hex characters")


def validate(data):
    require(data, [
        "schema_version", "protocol_version", "message_type", "from_skill", "to_skill",
        "stage", "identity", "project_root", "allowed_write_roots", "minecraft_version",
        "loader", "approval_evidence",
    ])
    if data["schema_version"] != 1 or data["protocol_version"] != "1.0" or data["message_type"] != "handoff":
        raise ValueError("mod handoff requires schema 1 and ContractFlow 1.0 handoff")
    if data["from_skill"] != "fjzm" or data["to_skill"] != "fjzm-mod":
        raise ValueError("mod handoff must route centrally from fjzm to fjzm-mod")
    if data["stage"] not in STAGES:
        raise ValueError("stage must be project_bootstrap, gameplay_design, or runtime_integration")

    identity = data["identity"]
    if not isinstance(identity, dict):
        raise ValueError("identity must be an object")
    require(identity, ["project_id", "asset_id", "asset_version"], "identity")
    if not all(nonempty(identity[key]) for key in identity):
        raise ValueError("identity values must be non-empty strings")

    if not nonempty(data["minecraft_version"]) or data["loader"] not in {"forge", "neoforge", "fabric"}:
        raise ValueError("minecraft_version and supported loader are required")
    approval = data["approval_evidence"]
    if not isinstance(approval, dict) or approval.get("status") != "approved" or not nonempty(approval.get("evidence")):
        raise ValueError("explicit approval_evidence is required")

    root = Path(data["project_root"])
    if not root.is_absolute():
        raise ValueError("project_root must be absolute")
    root = root.resolve()
    roots = data["allowed_write_roots"]
    if not isinstance(roots, list) or not roots:
        raise ValueError("allowed_write_roots must be a non-empty list")
    for value in roots:
        candidate = Path(value)
        if not candidate.is_absolute():
            raise ValueError("allowed_write_roots must be absolute")
        try:
            candidate.resolve().relative_to(root)
        except ValueError as exc:
            raise ValueError("allowed_write_root is outside project_root") from exc

    if data["stage"] in {"gameplay_design", "runtime_integration"}:
        require(data, ["gameplay_spec_sha256"])
        validate_sha(data["gameplay_spec_sha256"], "gameplay_spec_sha256")
    if data["stage"] == "runtime_integration":
        require(data, ["model_sha256", "rig_signature", "event_mapping"])
        validate_sha(data["model_sha256"], "model_sha256")
        if not nonempty(data["rig_signature"]):
            raise ValueError("rig_signature must be non-empty")
        if not isinstance(data["event_mapping"], dict) or not data["event_mapping"]:
            raise ValueError("event_mapping must be a non-empty object")


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid UTF-8 JSON: {exc}") from exc


def main():
    parser = argparse.ArgumentParser(description="Validate an FJZM Mod workshop handoff")
    parser.add_argument("contract", type=Path)
    args = parser.parse_args()
    try:
        validate(load_json(args.contract))
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("OK: Mod handoff is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
