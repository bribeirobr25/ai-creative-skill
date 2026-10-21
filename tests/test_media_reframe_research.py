"""R1 research tests: one portable image geometry test, one optional FFmpeg video integration.
Both use exclusively generated synthetic media; not a production media route.
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


@unittest.skipUnless(importlib.util.find_spec("PIL") is not None, "Pillow unavailable")
class MediaReframeResearchOfflineTests(unittest.TestCase):
    def test_image_roi_geometry_and_safe_pad_fallback(self):
        module_spec = importlib.util.spec_from_file_location("r1_offline_smoke", SCRIPT)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory(prefix="r1-reframe-image-") as work:
            report = module.test_images(Path(work))
            self.assertEqual(report["status"], "PASS")
            self.assertTrue(module.protected_inside((475, 85, 610, 315), (438, 0, 202, 360)))
            self.assertFalse(module.protected_inside((50, 85, 610, 315), (438, 0, 202, 360)))

    def test_video_reframe_scene_cut_fps_audio_and_frames(self):
        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            self.skipTest("requires FFmpeg/ffprobe; no automatic external dependency installation")
        with tempfile.TemporaryDirectory(prefix="r1-reframe-video-") as work:
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
