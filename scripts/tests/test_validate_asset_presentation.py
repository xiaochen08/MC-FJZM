import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_asset_presentation.py"


def load_module():
    if not SCRIPT.exists():
        raise AssertionError("validate_asset_presentation.py is missing")
    spec = importlib.util.spec_from_file_location("validate_asset_presentation", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def complete_manifest():
    return {
        "schema_version": 1,
        "project_id": "energy_defense",
        "asset_id": "rift_core",
        "mod_id": "fjzm_energy",
        "presentation_surface": ["tooltip", "gui_info_panel"],
        "display_name": {
            "translation_key": "item.fjzm_energy.rift_core",
            "style": {"color": "aqua", "bold": True, "italic": False},
        },
        "mod_line": {
            "translation_key": "tooltip.fjzm_energy.rift_core.mod",
            "style": {"color": "gray", "bold": False, "italic": True},
        },
        "usage": {
            "translation_key": "tooltip.fjzm_energy.rift_core.use",
            "style": {"color": "yellow", "bold": False, "italic": False},
        },
        "flavor": {
            "style_mode": "light_chuunibyou",
            "selection_rule": "stable_per_stack",
            "style": {"color": "dark_purple", "bold": False, "italic": True},
            "entries": [
                {"translation_key": f"tooltip.fjzm_energy.rift_core.flavor.{index:02d}", "text_zh": text}
                for index, text in enumerate(
                    ["第七码环正在低语。", "别盯着核心看太久。", "沉默也会成为武器。", "权限不足，但命运已批准。"],
                    start=1,
                )
            ],
        },
        "layout": {
            "line_order": ["display_name", "mod_line", "usage", "flavor"],
            "wrap_width": 220,
            "gui_scale_tested": [2, 3, 4],
            "color_only_meaning": False,
        },
    }


class AssetPresentationValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_module()

    def test_accepts_a_complete_localizable_manifest(self):
        self.assertEqual(self.validator.validate_manifest(complete_manifest())["errors"], [])

    def test_requires_gray_italic_mod_line(self):
        payload = complete_manifest()
        payload["mod_line"]["style"] = {"color": "white", "italic": False}
        joined = "\n".join(self.validator.validate_manifest(payload)["errors"])
        self.assertIn("gray", joined)
        self.assertIn("italic", joined)

    def test_requires_usage_text_and_colored_style(self):
        payload = complete_manifest()
        payload["usage"] = {"translation_key": "", "style": {"color": ""}}
        joined = "\n".join(self.validator.validate_manifest(payload)["errors"])
        self.assertIn("usage.translation_key", joined)
        self.assertIn("usage.style.color", joined)

    def test_requires_four_unique_flavor_lines(self):
        payload = complete_manifest()
        payload["flavor"]["entries"] = payload["flavor"]["entries"][:2]
        self.assertTrue(any("at least 4" in error for error in self.validator.validate_manifest(payload)["errors"]))

        payload = complete_manifest()
        payload["flavor"]["entries"][1] = deepcopy(payload["flavor"]["entries"][0])
        self.assertTrue(any("unique" in error for error in self.validator.validate_manifest(payload)["errors"]))

    def test_rejects_per_frame_randomization(self):
        payload = complete_manifest()
        payload["flavor"]["selection_rule"] = "per_frame"
        self.assertTrue(any("stable" in error for error in self.validator.validate_manifest(payload)["errors"]))

    def test_rejects_hardcoded_legacy_formatting_codes(self):
        payload = complete_manifest()
        payload["flavor"]["entries"][0]["text_zh"] = "§5第七码环正在低语。"
        self.assertTrue(any("formatting codes" in error for error in self.validator.validate_manifest(payload)["errors"]))

    def test_requires_accessible_layout_and_exact_line_order(self):
        payload = complete_manifest()
        payload["layout"]["color_only_meaning"] = True
        payload["layout"]["line_order"] = ["display_name", "usage", "flavor"]
        joined = "\n".join(self.validator.validate_manifest(payload)["errors"])
        self.assertIn("line_order", joined)
        self.assertIn("color_only_meaning", joined)


if __name__ == "__main__":
    unittest.main()
