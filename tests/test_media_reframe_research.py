"""R1 non-production smoke test for research-only synthetic reframe.
No customer assets, models, provider credentials or paid network calls.
"""
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "docs" / "research" / "media-reframe" / "r1_offline_smoke.py"

class MediaReframeResearchOfflineTests(unittest.TestCase):
    @unittest.skipUnless(importlib.util.find_spec("PIL") is not None, "Pillow not installed")
    def test_synthetic_crops_pad_and_scene_cut_video(self):
        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            self.skipTest("requires ffmpeg and ffprobe; no external install performed")
        with tempfile.TemporaryDirectory(prefix="r1-reframe-") as work:
            run = subprocess.run([sys.executable, str(SCRIPT), "--out", work],
                                 capture_output=True, text=True, timeout=120)
            self.assertEqual(run.returncode, 0, run.stderr)
            report = json.loads((Path(work) / "report.json").read_text())
            self.assertEqual(report["cost_paid_usd"], 0)
            self.assertEqual(report["images"]["status"], "PASS")
            self.assertEqual(report["video"]["status"], "PASS")
            self.assertEqual(report["video"]["output_dimensions"], [360, 640])
            self.assertEqual(report["video"]["fps_before_after"], ["12/1", "12/1"])
            self.assertTrue(report["video"]["audio_preserved"])
            self.assertEqual(report["video"]["tracking"],
                             "manual scene-conditioned trajectory, not vision-based auto tracking")
            self.assertIn("NOT_TESTED", report["video"]["semantic_QA"])

if __name__ == "__main__":
    unittest.main()
