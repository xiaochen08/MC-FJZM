import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class ModSkillPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.attributes = (ROOT / "references" / "gameplay-attributes.md").read_text(encoding="utf-8")
        cls.handoff = (ROOT / "references" / "mod-handoff.md").read_text(encoding="utf-8")

    def test_identity_and_attribute_gate(self):
        self.assertIn("name: fjzm-mod", self.skill)
        self.assertIn("validate_gameplay_spec.py", self.skill)
        self.assertIn("Silence and guessed defaults are not approval", self.skill)

    def test_one_question_rule(self):
        self.assertIn("Ask exactly one user-facing question per turn", self.skill)
        self.assertIn("Never dump the complete attribute checklist", self.skill)

    def test_delegated_mode_keeps_main_approval(self):
        self.assertIn("return the next unresolved decision to `$fjzm`", self.skill)
        self.assertIn("`$fjzm` remains the only approval owner", self.skill)

    def test_entity_foundation_and_contract(self):
        for phrase in ("max_health", "attack_damage", "hitbox", "spawn_rules", "taming_and_breeding"):
            self.assertIn(phrase, self.attributes)
        for phrase in ("gameplay_spec_sha256", "allowed_write_roots", "mod-result.json"):
            self.assertIn(phrase, self.handoff)


if __name__ == "__main__":
    unittest.main()
