import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[2] / "skills" / "fjzm-mod" / "scripts" / "validate_gameplay_spec.py"


def load_validator():
    if not SCRIPT.is_file():
        raise AssertionError(f"validator is missing: {SCRIPT}")
    spec = importlib.util.spec_from_file_location("validate_gameplay_spec", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GameplaySpecValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()
        self.cat = {
            "schema_version": 1,
            "project_id": "cat_mod",
            "asset_id": "companion_cat",
            "asset_version": "1.0.0",
            "asset_type": "entity_pet_boss",
            "approval": {"status": "approved", "evidence": "用户逐项确认小猫基础属性"},
            "attributes": {
                "max_health": 20.0,
                "armor": 2.0,
                "attack_damage": 3.0,
                "movement_speed": 0.3,
                "follow_range": 24.0,
                "knockback_resistance": 0.0,
                "hitbox": {"width": 0.6, "height": 0.7},
                "faction_and_targets": {"faction": "player_pet", "targets": ["hostile_mobs"]},
                "spawn_rules": {"mode": "tamed_only"},
                "drops_and_xp": {"drops": [], "xp": 0},
                "persistence_and_despawn": {"persistent_when_tamed": True, "despawn": "vanilla_when_wild"},
                "taming_and_breeding": {"tameable": True, "breedable": True},
            },
            "attribute_evidence": {
                "max_health": "用户确认 20",
                "armor": "用户确认 2",
                "attack_damage": "用户确认 3",
                "movement_speed": "用户确认 0.3",
                "follow_range": "用户确认 24",
                "knockback_resistance": "用户确认 0",
                "hitbox": "用户确认 0.6x0.7",
                "faction_and_targets": "用户确认玩家宠物并攻击敌对生物",
                "spawn_rules": "用户确认只通过驯服获得",
                "drops_and_xp": "用户确认不掉落经验与物品",
                "persistence_and_despawn": "用户确认驯服后永久保留",
                "taming_and_breeding": "用户确认可驯服、可繁殖",
            },
        }

    def test_complete_cat_attributes_pass(self):
        self.assertEqual(self.validator.validate_spec(self.cat)["errors"], [])

    def test_cat_missing_health_or_hitbox_is_rejected(self):
        payload = deepcopy(self.cat)
        payload["attributes"].pop("max_health")
        payload["attributes"].pop("hitbox")
        errors = self.validator.validate_spec(payload)["errors"]
        self.assertTrue(any("max_health" in error for error in errors))
        self.assertTrue(any("hitbox" in error for error in errors))

    def test_unapproved_or_guessed_defaults_are_rejected(self):
        payload = deepcopy(self.cat)
        payload["approval"] = {"status": "assumed", "evidence": "used defaults"}
        errors = self.validator.validate_spec(payload)["errors"]
        self.assertTrue(any("explicit attribute approval" in error for error in errors))

    def test_missing_field_level_evidence_is_rejected(self):
        payload = deepcopy(self.cat)
        payload["attribute_evidence"].pop("movement_speed")
        errors = self.validator.validate_spec(payload)["errors"]
        self.assertTrue(any("movement_speed" in error and "evidence" in error for error in errors))

    def test_wrong_profile_fields_do_not_satisfy_entity_gate(self):
        payload = deepcopy(self.cat)
        payload["attributes"] = {"durability": 100, "stack_size": 1}
        errors = self.validator.validate_spec(payload)["errors"]
        self.assertTrue(any("max_health" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
