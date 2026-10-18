"""Offline regression tests for V2.5 source import and deterministic packaging."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "packaging"))
import build as package_build

class PackageTests(unittest.TestCase):
    def test_original_source_identity(self):
        source, descriptor = package_build.payloads()
        self.assertEqual(len(source), 74)
        self.assertIn("SKILL.md", source)
        self.assertIn('"version": "0.3.0"', descriptor.decode())
        self.assertEqual(len(package_build.entries("agent")), 74)
        self.assertEqual(len(package_build.entries("plugin")), 75)

    def test_deterministic_builds(self):
        with tempfile.TemporaryDirectory() as base:
            a, b = Path(base)/"first", Path(base)/"second"
            x, y = package_build.build(a), package_build.build(b)
            self.assertEqual(x, y)
            for kind, info in x["artifacts"].items():
                one, two = a/info["filename"], b/info["filename"]
                self.assertEqual(one.read_bytes(), two.read_bytes())
                self.assertEqual(hashlib.sha256(one.read_bytes()).hexdigest(), info["sha256"])
                package_build.verify_zip(one, package_build.entries(kind))

    def test_import_not_product_certification(self):
        a = json.loads(package_build.ATTESTATION.read_text())
        self.assertEqual(a["release"], "2.5.0")
        self.assertEqual(a["source_file_count"], 74)
        self.assertEqual(len(a["files_sha256"]), 74)

if __name__ == "__main__":
    unittest.main()
