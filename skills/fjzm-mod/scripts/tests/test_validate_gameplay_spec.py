import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_gameplay_spec.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_gameplay_spec", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GameplaySpecValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()
        fields = {
            "max_health": 20.0, "armor": 2.0, "attack_damage": 3.0,
            "movement_speed": 0.3, "follow_range": 24.0, "knockback_resistance": 0.0,
            "hitbox": {"width": 0.6, "height": 0.7},
            "faction_and_targets": {"faction": "player_pet", "targets": ["hostile_mobs"]},
            "spawn_rules": {"mode": "tamed_only"}, "drops_and_xp": {"drops": [], "xp": 0},
            "persistence_and_despawn": {"persistent_when_tamed": True},
            "taming_and_breeding": {"tameable": True, "breedable": True},
        }
        self.cat = {
            "schema_version": 1, "project_id": "cat_mod", "asset_id": "companion_cat",
            "asset_version": "1.0.0", "asset_type": "entity_pet_boss",
            "approval": {"status": "approved", "evidence": "用户逐项确认"},
            "attributes": fields,
            "attribute_evidence": {key: f"用户确认 {key}" for key in fields},
        }

    def test_complete_entity_profile_passes(self):
        self.assertEqual(self.validator.validate_spec(self.cat)["errors"], [])

    def test_missing_attribute_and_evidence_fail(self):
        payload = deepcopy(self.cat)
        payload["attributes"].pop("max_health")
        payload["attribute_evidence"].pop("movement_speed")
        output = "\n".join(self.validator.validate_spec(payload)["errors"])
        self.assertIn("max_health", output)
        self.assertIn("movement_speed", output)

    def test_assumed_approval_fails(self):
        payload = deepcopy(self.cat)
        payload["approval"]["status"] = "assumed"
        self.assertTrue(any("explicit attribute approval" in error for error in self.validator.validate_spec(payload)["errors"]))


if __name__ == "__main__":
    unittest.main()
