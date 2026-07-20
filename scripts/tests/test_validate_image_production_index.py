import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_image_production_index.py"


def load_module():
    if not SCRIPT.exists():
        raise AssertionError("validate_image_production_index.py is missing")
    spec = importlib.util.spec_from_file_location("validate_image_production_index", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def complete_index():
    return {
        "schema_version": 1,
        "project_id": "energy_defense",
        "active_round_id": "round-002",
        "rounds": [
            {
                "round_id": "round-001",
                "round_type": "asset_overview",
                "status": "approved",
                "asset_id": None,
                "screen_id": None,
                "depends_on": [],
                "prompt_path": "design/image-rounds/round-001__asset-overview/prompt.md",
                "negative_prompt_path": "design/image-rounds/round-001__asset-overview/negative-prompt.md",
                "manifest_path": "design/image-rounds/round-001__asset-overview/manifest.json",
                "image_sha256": ["a" * 64],
                "approval_evidence": "用户确认总览范围",
                "next_round": "round-002",
            },
            {
                "round_id": "round-002",
                "round_type": "model_theme",
                "status": "shown",
                "asset_id": "crystal_tower",
                "screen_id": None,
                "depends_on": ["round-001"],
                "prompt_path": "design/image-rounds/round-002__model-theme/prompt.md",
                "negative_prompt_path": "design/image-rounds/round-002__model-theme/negative-prompt.md",
                "manifest_path": "design/image-rounds/round-002__model-theme/manifest.json",
                "image_sha256": ["b" * 64, "c" * 64, "d" * 64],
                "approval_evidence": None,
                "next_round": "round-003",
            },
        ],
    }


class ImageProductionIndexValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_module()

    def test_accepts_complete_ordered_index(self):
        self.assertEqual(self.validator.validate_index(complete_index())["errors"], [])

    def test_rejects_duplicate_or_malformed_round_ids(self):
        payload = complete_index()
        payload["rounds"][1]["round_id"] = "round-001"
        self.assertTrue(any("unique" in error for error in self.validator.validate_index(payload)["errors"]))

        payload = complete_index()
        payload["rounds"][1]["round_id"] = "two"
        self.assertTrue(any("round-NNN" in error for error in self.validator.validate_index(payload)["errors"]))

    def test_rejects_paths_outside_image_rounds(self):
        payload = complete_index()
        payload["rounds"][0]["prompt_path"] = "../prompt.md"
        self.assertTrue(any("design/image-rounds" in error for error in self.validator.validate_index(payload)["errors"]))

    def test_approved_round_requires_hashes_and_approval_evidence(self):
        payload = complete_index()
        payload["rounds"][0]["image_sha256"] = []
        payload["rounds"][0]["approval_evidence"] = None
        joined = "\n".join(self.validator.validate_index(payload)["errors"])
        self.assertIn("image_sha256", joined)
        self.assertIn("approval_evidence", joined)

    def test_rejects_unknown_dependency_and_active_round(self):
        payload = complete_index()
        payload["active_round_id"] = "round-999"
        payload["rounds"][1]["depends_on"] = ["round-888"]
        joined = "\n".join(self.validator.validate_index(payload)["errors"])
        self.assertIn("active_round_id", joined)
        self.assertIn("unknown dependency", joined)

    def test_rejects_unrecognized_status(self):
        payload = complete_index()
        payload["rounds"][1]["status"] = "done"
        self.assertTrue(any("status" in error for error in self.validator.validate_index(payload)["errors"]))


if __name__ == "__main__":
    unittest.main()
