"""Small regression checks for research privacy and source-preservation boundaries."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("quality_report", HERE / "report.py")
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)


class AdapterBoundaries(unittest.TestCase):
    def test_private_observations_are_not_exported(self):
        for key in ("images-loaded", "script-errors", "resource-errors", "external-network"):
            self.assertEqual(report.public_observation({
                "id": key, "expected": [], "actual": ["private://example-secret"],
                "outcome": "FAIL",
            }), (0, 1))
        self.assertEqual(report.public_observation({
            "id": "gallery-next", "actual": "/private-product.png", "outcome": "PASS"
        }), ("different photo", "different photo"))

    def test_only_css_changes_and_original_and_existing_output_survive(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original, output = root / "original", root / "experiment"
            original.mkdir()
            (original / "styles.css").write_text("body { color: black; }\n")
            (original / "index.html").write_text("<h1>Fictional fixture</h1>")
            args = [sys.executable, str(HERE / "prepare.py"), str(original), str(output)]
            subprocess.run(args, check=True, capture_output=True)
            for candidate in ("B", "C"):
                self.assertEqual((output / candidate / "index.html").read_bytes(),
                                 (original / "index.html").read_bytes())
                self.assertNotEqual((output / candidate / "styles.css").read_bytes(),
                                    (original / "styles.css").read_bytes())
            before = (output / "C" / "styles.css").read_bytes()
            self.assertNotEqual(subprocess.run(args, capture_output=True).returncode, 0)
            self.assertEqual((output / "C" / "styles.css").read_bytes(), before)
            self.assertEqual((original / "styles.css").read_text(), "body { color: black; }\n")

    def test_nested_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result = subprocess.run([sys.executable, str(HERE / "prepare.py"),
                                     str(root), str(root / "nested")], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((root / "nested").exists())


if __name__ == "__main__":
    unittest.main()
