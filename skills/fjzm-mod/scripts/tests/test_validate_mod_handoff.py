import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_mod_handoff.py"
SPEC = importlib.util.spec_from_file_location("validate_mod_handoff", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ModHandoffValidatorTests(unittest.TestCase):
    def valid_contract(self, root):
        source = root / "src"
        source.mkdir()
        return {
            "schema_version": 1,
            "protocol_version": "1.0",
            "message_type": "handoff",
            "from_skill": "fjzm",
            "to_skill": "fjzm-mod",
            "stage": "gameplay_design",
            "identity": {"project_id": "cat-mod", "asset_id": "cat", "asset_version": "1.0.0"},
            "project_root": str(root),
            "allowed_write_roots": [str(source)],
            "minecraft_version": "1.20.1",
            "loader": "forge",
            "gameplay_spec_sha256": "a" * 64,
            "approval_evidence": {"status": "approved", "evidence": "user-message-42"},
        }

    def test_valid_gameplay_handoff_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            MODULE.validate(self.valid_contract(Path(temp).resolve()))

    def test_wrong_route_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            data = self.valid_contract(Path(temp).resolve())
            data["to_skill"] = "fjzm-animation"
            with self.assertRaisesRegex(ValueError, "fjzm-mod"):
                MODULE.validate(data)

    def test_write_root_outside_project_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            data = self.valid_contract(Path(temp).resolve())
            data["allowed_write_roots"] = [str(Path(outside).resolve())]
            with self.assertRaisesRegex(ValueError, "outside project_root"):
                MODULE.validate(data)

    def test_runtime_integration_requires_frozen_asset_interface(self):
        with tempfile.TemporaryDirectory() as temp:
            data = self.valid_contract(Path(temp).resolve())
            data["stage"] = "runtime_integration"
            with self.assertRaisesRegex(ValueError, "model_sha256"):
                MODULE.validate(data)

    def test_project_bootstrap_does_not_require_gameplay_hash(self):
        with tempfile.TemporaryDirectory() as temp:
            data = self.valid_contract(Path(temp).resolve())
            data["stage"] = "project_bootstrap"
            data.pop("gameplay_spec_sha256")
            MODULE.validate(data)


if __name__ == "__main__":
    unittest.main()
