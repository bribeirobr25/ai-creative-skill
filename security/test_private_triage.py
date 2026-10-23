"""Local-only private review utility tests; all inputs are synthetic."""
from __future__ import annotations

import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch

from private_triage import _inside_repo, link_candidates_from_text, write_private_file, main


class PrivateReviewGuardTests(unittest.TestCase):
    def test_drive_shape_candidate_without_literal_private_url(self):
        u = "https://" + "drive.google.com/drive/folders/" + "X" * 28
        self.assertIn(u, link_candidates_from_text("This is " + u))

    def test_generic_share_is_candidate(self):
        u = "https://" + "assets.example.invalid/download/" + "y" * 30
        self.assertIn(u, link_candidates_from_text(u))

    def test_normal_public_page_is_not_candidate(self):
        self.assertEqual(set(), link_candidates_from_text("https://www.python.org/"))

    def test_repository_output_is_forbidden(self):
        root = Path("/tmp/test-acsskill-gitroot")
        self.assertTrue(_inside_repo(root / "security" / "findings.json", root))
        self.assertFalse(_inside_repo(Path("/tmp/local-user-review.json"), root))

    def test_ci_refuses_to_write(self):
        with patch.dict(os.environ, {"CI": "true"}):
            with self.assertRaisesRegex(RuntimeError, "CI"):
                write_private_file({"raw_links": []})

    def test_default_tmpdir_inside_repo_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="test-repo-temp-") as d:
            folder = Path(d) / "generated-private-dir"
            folder.mkdir()
            with patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}):
                with patch("private_triage.git", return_value=(str(Path(d)) + "\n").encode()):
                    with patch("private_triage.tempfile.mkdtemp", return_value=str(folder)):
                        with self.assertRaisesRegex(RuntimeError, "inside Git repository"):
                            write_private_file({"raw_links": []})
            self.assertFalse(folder.exists())

    def test_private_review_cannot_write_under_repo(self):
        root = "/tmp/test-acsskill-repository"
        with patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}):
            with patch("private_triage.git", return_value=(root + "\n").encode()):
                with self.assertRaisesRegex(RuntimeError, "inside Git repository"):
                    write_private_file({"raw_links": []}, Path(root) / "findings.json")

    def test_writes_restricted_local_file_only(self):
        with tempfile.TemporaryDirectory(prefix="test-private-safety-") as dirname:
            out = Path(dirname) / "restricted" / "findings.json"
            sample = {
                "raw_links": [{"url": "https://" + "drive.google.com/file/d/FILE_ID/view"}],
                "status": "PRIVATE_REVIEW_REQUIRED",
            }
            with patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}):
                with patch("private_triage.git", return_value=b"/not/the/temp/directory\n"):
                    p = write_private_file(sample, out)
            self.assertEqual(sample, json.loads(p.read_text()))
            if os.name == "posix":
                self.assertEqual(stat.S_IMODE(p.stat().st_mode), 0o600)
                self.assertEqual(stat.S_IMODE(p.parent.stat().st_mode), 0o700)

    def test_world_readable_destination_is_rejected_without_chmod(self):
        if os.name != "posix":
            self.skipTest("POSIX mode check")
        with tempfile.TemporaryDirectory(prefix="test-review-unsafe-") as d:
            previous = stat.S_IMODE(Path(d).stat().st_mode)
            os.chmod(d, 0o755)
            with patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}):
                with patch("private_triage.git", return_value=b"/unrelated/repository\n"):
                    with self.assertRaisesRegex(RuntimeError, "not private"):
                        write_private_file({"status": "test"}, Path(d) / "review.json")
            self.assertEqual(0o755, stat.S_IMODE(Path(d).stat().st_mode))
            os.chmod(d, previous)

    def test_existing_target_refused_without_overwriting(self):
        with tempfile.TemporaryDirectory(prefix="test-review-existing-") as d:
            out = Path(d) / "review.json"
            out.write_text("keep this content", encoding="utf-8")
            with patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}):
                with patch("private_triage.git", return_value=b"/another/dir\n"):
                    with self.assertRaises(FileExistsError):
                        write_private_file({"status": "test"}, out)
            self.assertEqual("keep this content", out.read_text())

    def test_cli_refuses_ci_even_if_git_available(self):
        with patch.dict(os.environ, {"GITHUB_ACTIONS": "true"}):
            self.assertEqual(2, main())


if __name__ == "__main__":
    unittest.main()
