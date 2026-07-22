import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MOD_SKILL = ROOT / "skills" / "fjzm-mod" / "SKILL.md"
ATTRIBUTES = ROOT / "skills" / "fjzm-mod" / "references" / "gameplay-attributes.md"
HANDOFF = ROOT / "skills" / "fjzm-mod" / "references" / "mod-handoff.md"
LOADERS = ROOT / "skills" / "fjzm-mod" / "references" / "loader-adapters.md"


class ModWorkshopPolicyTests(unittest.TestCase):
    def required_text(self, path):
        self.assertTrue(path.is_file(), f"required Mod workshop file is missing: {path}")
        return path.read_text(encoding="utf-8")

    def test_mod_workshop_has_a_stable_identity(self):
        skill = self.required_text(MOD_SKILL)
        self.assertIn("name: fjzm-mod", skill)
        self.assertIn("方界造模·Mod 工坊", skill)

    def test_no_gameplay_code_is_written_before_validated_attributes(self):
        skill = self.required_text(MOD_SKILL)
        for phrase in (
            "gameplay-spec.json",
            "validate_gameplay_spec.py",
            "Do not write gameplay code before the type-specific attribute gate passes",
            "Silence and guessed defaults are not approval",
        ):
            self.assertIn(phrase, skill)

    def test_user_intake_is_one_plain_question_per_turn(self):
        skill = self.required_text(MOD_SKILL)
        self.assertIn("Ask exactly one user-facing question per turn", skill)
        self.assertIn("plain Chinese", skill)
        self.assertIn("numbered choices", skill)
        self.assertIn("Never dump the complete attribute checklist", skill)

    def test_delegated_mode_keeps_main_as_the_only_approval_owner(self):
        skill = self.required_text(MOD_SKILL)
        self.assertIn("return the next unresolved decision to `$fjzm`", skill)
        self.assertIn("`$fjzm` remains the only approval owner", skill)

    def test_entity_and_pet_foundation_cannot_be_skipped(self):
        attributes = self.required_text(ATTRIBUTES)
        for field in (
            "max_health",
            "armor",
            "attack_damage",
            "movement_speed",
            "follow_range",
            "knockback_resistance",
            "hitbox",
            "faction_and_targets",
            "spawn_rules",
            "drops_and_xp",
            "persistence_and_despawn",
            "taming_and_breeding",
        ):
            self.assertIn(field, attributes)

    def test_each_runtime_asset_type_has_its_own_profile(self):
        attributes = self.required_text(ATTRIBUTES)
        for profile in (
            "entity_pet_boss",
            "item_weapon_tool_armor",
            "block_machine_turret",
            "projectile",
            "gui_menu",
            "world_generation_structure",
        ):
            self.assertIn(profile, attributes)

    def test_loaders_are_internal_adapters_not_separate_skills(self):
        loaders = self.required_text(LOADERS)
        for phrase in ("Forge", "NeoForge", "Fabric", "official primary sources", "Do not silently substitute"):
            self.assertIn(phrase, loaders)
        self.assertIn("one Mod workshop", loaders)

    def test_contract_locks_asset_identity_and_write_scope(self):
        handoff = self.required_text(HANDOFF)
        for field in (
            "project_id",
            "asset_id",
            "asset_version",
            "minecraft_version",
            "loader",
            "gameplay_spec_sha256",
            "model_sha256",
            "rig_signature",
            "allowed_write_roots",
            "approval_evidence",
            "mod-result.json",
        ):
            self.assertIn(field, handoff)


if __name__ == "__main__":
    unittest.main()
