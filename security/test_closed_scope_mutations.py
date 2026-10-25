"""One-off mutation replay of S-A5 on temporary integration PR #25 only.

Each test mutates a sandbox copy of security/publication_guard.py and reruns
the existing real-Git CLI tests. No production file or original PR is mutated.
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class ClosedScopeMutationAcceptance(unittest.TestCase):
    def test_seven_security_boundary_mutants_are_killed(self):
        source_dir = Path(__file__).resolve().parent
        original = (source_dir / "publication_guard.py").read_text(encoding="utf-8")
        changes = {
            "history_patch_scan_removed": (
                "            findings.extend(_scan_commit_history(ns.history_range))",
                "            pass",
            ),
            "remerge_diff_switched_off": (
                '"--diff-merges=remerge", "--text", "--no-textconv"',
                '"--diff-merges=off", "--text", "--no-textconv"',
            ),
            "git_errors_suppressed": (
                "command, capture_output=True, check=True, timeout=30",
                "command, capture_output=True, check=False, timeout=30",
            ),
            "octopus_detection_removed": (
                "if _octopus_findings(ns.history_range):",
                "if False and _octopus_findings(ns.history_range):",
            ),
            "google_oauth_rule_removed": (
                '("GOOGLE_OAUTH_CLIENT_SECRET", re.compile(',
                '("GOOGLE_OAUTH_CLIENT_SECRET_DISABLED", re.compile(',
            ),
            "generic_secret_rule_removed": (
                '("GENERIC_SECRET_ASSIGNMENT", re.compile(',
                '("GENERIC_SECRET_ASSIGNMENT_DISABLED", re.compile(',
            ),
            "staged_filename_scan_removed": (
                "            findings.extend(_scan_path_list(_run_git([",
                "            findings.extend([] if True else _scan_path_list(_run_git([",
            ),
        }
        for name, (target, replacement) in changes.items():
            with self.subTest(mutation=name):
                self.assertEqual(1, original.count(target), name)
                modified = original.replace(target, replacement, 1)
                with tempfile.TemporaryDirectory(prefix="guard-mutation-") as scratch:
                    root = Path(scratch)
                    for basename in ("test_publication_guard.py", "history_audit.py"):
                        (root / basename).write_text(
                            (source_dir / basename).read_text(encoding="utf-8"),
                            encoding="utf-8",
                        )
                    (root / "publication_guard.py").write_text(
                        modified, encoding="utf-8")
                    result = subprocess.run(
                        [sys.executable, "-m", "unittest", "discover",
                         "-s", str(root), "-p", "test_publication_guard.py"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        timeout=120,
                        check=False,
                    )
                    self.assertNotEqual(0, result.returncode,
                                        "Mutation escaped tests: " + name)
