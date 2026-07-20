import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_encoding_preflight.py"


def load_module():
    if not SCRIPT.exists():
        raise AssertionError("validate_encoding_preflight.py is missing")
    spec = importlib.util.spec_from_file_location("validate_encoding_preflight", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class EncodingPreflightValidatorTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_module()
        self.host = {
            "schema_version": 1,
            "severity": "red",
            "status": "host_passed",
            "host_checks": {
                "powershell7": "passed",
                "console_input_encoding": "utf-8",
                "console_output_encoding": "utf-8",
                "default_text_write": "utf-8-no-bom",
                "line_endings": "lf",
                "chinese_sentinel_round_trip": "passed",
                "strict_utf8_decode_scan": "passed",
                "bom_violations": 0,
                "invalid_utf8_files": 0,
            },
        }

    def test_accepts_complete_host_phase(self):
        self.assertEqual(self.validator.validate_report(self.host, "host")["errors"], [])

    def test_rejects_bom_or_console_encoding_regression(self):
        report = deepcopy(self.host)
        report["host_checks"]["console_output_encoding"] = "gbk"
        report["host_checks"]["bom_violations"] = 1
        errors = self.validator.validate_report(report, "host")["errors"]
        self.assertTrue(any("console_output_encoding" in error for error in errors))
        self.assertTrue(any("bom_violations" in error for error in errors))

    def test_project_phase_requires_gradle_java_and_localized_build_checks(self):
        report = deepcopy(self.host)
        report["status"] = "project_passed"
        report["project_checks"] = {
            "java_process_file_encoding": "utf-8",
            "gradle_daemon_file_encoding": "utf-8",
            "java_compile_encoding": "utf-8",
            "localized_resource_round_trip": "passed",
            "localized_build": "passed",
            "strict_utf8_decode_scan": "passed",
        }
        self.assertEqual(self.validator.validate_report(report, "project")["errors"], [])
        report["project_checks"].pop("localized_build")
        errors = self.validator.validate_report(report, "project")["errors"]
        self.assertTrue(any("project_checks.localized_build" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
