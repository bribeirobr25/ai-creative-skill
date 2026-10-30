"""Tests for the reusable prepublication scanner.

Synthetic token examples are assembled at runtime so no secrets are committed.
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from publication_guard import scan_added_line, scan_unified_diff, main, media_metadata_findings
from history_audit import audit_text_blob, _exif_value_risk_categories, _verified_branch_coverage, classify_binary_metadata, _scope_bucket, classify_link_metadata, _reachable_blobs, _link_fingerprints, _generic_share_host_types, audit_commit_metadata


def fake_patch(line: str, path: str = "docs/example.md") -> str:
    return (
        f"diff --git a/{path} b/{path}\n"
        "new file mode 100644\n"
        f"+++ b/{path}\n"
        "@@ -0,0 +1 @@\n"
        f"+{line}\n"
    )


def rules(patch_text):
    return [(x.severity, x.rule) for x in scan_unified_diff(patch_text)]


class SecretRulesTests(unittest.TestCase):
    def test_binary_only_new_image_without_plus_header_is_reviewed(self):
        diff = (
            "diff --git a/assets/new.jpg b/assets/new.jpg\\n"
            "new file mode 100644\\n"
            "index 0000000..123abcd\\n"
            "Binary files /dev/null and b/assets/new.jpg differ\\n"
        ).replace("\\n", "\n")
        self.assertIn(("REVIEW", "BINARY_OR_MEDIA_REVIEW"), rules(diff))

    def test_binary_only_private_filename_without_plus_header_is_blocked(self):
        diff = (
            "diff --git a/config/.env.prod b/config/.env.prod\\n"
            "new file mode 100644\\n"
            "Binary files /dev/null and b/config/.env.prod differ\\n"
        ).replace("\\n", "\n")
        self.assertIn(("BLOCK", "PRIVATE_FILE_PATH"), rules(diff))

    def test_renamed_image_without_text_hunk_is_reviewed(self):
        diff = (
            "diff --git a/assets/old.jpg b/assets/new.jpg\\n"
            "similarity index 100%\\n"
            "rename from assets/old.jpg\\n"
            "rename to assets/new.jpg\\n"
        ).replace("\\n", "\n")
        self.assertIn(("REVIEW", "BINARY_OR_MEDIA_REVIEW"), rules(diff))

    def test_binary_deletion_does_not_flag_new_publication(self):
        diff = (
            "diff --git a/assets/old.jpg b/assets/old.jpg\\n"
            "deleted file mode 100644\\n"
            "Binary files a/assets/old.jpg and /dev/null differ\\n"
        ).replace("\\n", "\n")
        self.assertNotIn(("REVIEW", "BINARY_OR_MEDIA_REVIEW"), rules(diff))

    def test_quoted_binary_path_with_spaces_is_reviewed(self):
        diff = (
            'diff --git "a/assets/my image.jpeg" "b/assets/my image.jpeg"\\n'
            "new file mode 100644\\n"
            "Binary files /dev/null and b/assets/my image.jpeg differ\\n"
        ).replace("\\n", "\n")
        self.assertIn(("REVIEW", "BINARY_OR_MEDIA_REVIEW"), rules(diff))

    def test_unparseable_diff_header_fails_open_to_manual_review_not_silence(self):
        diff = "diff --git a/incomplete\\nBinary files differ\\n".replace("\\n", "\n")
        self.assertIn(("BLOCK", "UNPARSEABLE_DIFF_HEADER"), rules(diff))

    def test_two_binary_files_reviewed_separately(self):
        diff = (
            "diff --git a/one.jpg b/one.jpg\\n"
            "Binary files /dev/null and b/one.jpg differ\\n"
            "diff --git a/two.png b/two.png\\n"
            "Binary files /dev/null and b/two.png differ\\n"
        ).replace("\\n", "\n")
        self.assertEqual(2, sum(rule == "BINARY_OR_MEDIA_REVIEW" for _, rule in rules(diff)))

    def test_token_after_formfeed_is_scanned(self):
        synthetic = "ghp_" + "A" * 32
        self.assertIn(("BLOCK", "GITHUB_TOKEN"),
                      rules(fake_patch("safe" + "\f" + synthetic)))

    def test_token_after_unicode_line_separator_is_scanned(self):
        synthetic = "ghp_" + "B" * 32
        self.assertIn(("BLOCK", "GITHUB_TOKEN"),
                      rules(fake_patch("safe" + "\u2028" + synthetic)))

    def test_quoted_plus_header_with_spaces_is_scanned(self):
        synthetic = "ghp_" + "B" * 32
        patch_text = (
            'diff --git "a/my file.txt" "b/my file.txt"\n'
            'new file mode 100644\n'
            '--- /dev/null\n'
            '+++ "b/my file.txt"\n'
            '@@ -0,0 +1 @@\n'
            '+' + synthetic + '\n'
        )
        self.assertIn(("BLOCK", "GITHUB_TOKEN"), rules(patch_text))

    def test_nonutf8_git_diff_is_operational_failure_not_clean(self):
        from types import SimpleNamespace
        with patch("publication_guard.subprocess.run",
                   return_value=SimpleNamespace(stdout=b"\\xffbroken".replace(b"\\xff", b"\xff"))):
            from publication_guard import _get_diff
            from argparse import Namespace
            decoded = _get_diff(Namespace(staged=True, range=None))
            self.assertIn("\ufffd", decoded)
            # Undecodable bytes are reviewable content, not an operational
            # Git failure or a silently dropped entire patch.

    def test_real_git_accented_path_and_binary_name(self):
        import tempfile
        import subprocess
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            def git(*args):
                return subprocess.run(["git", "-C", d, *args],
                                      capture_output=True, check=True).stdout
            git("init", "-q")
            (Path(d) / "relatório.txt").write_text(
                "token=" + "ghp_" + "Q" * 32 + "\n", encoding="utf-8")
            (Path(d) / "secrets").mkdir()
            (Path(d) / "secrets" / ".env").write_bytes(b"\x00\xff\x00")
            git("add", ".")
            patch_bytes = git("-c", "core.quotePath=false", "diff", "--cached",
                              "--no-ext-diff", "--no-color", "--unified=0", "--")
            result = rules(patch_bytes.decode("utf-8"))
            self.assertIn(("BLOCK", "GITHUB_TOKEN"), result)
            self.assertIn(("BLOCK", "PRIVATE_FILE_PATH"), result)

    def test_real_git_quoted_binary_secret_path_with_spaces(self):
        import tempfile
        import subprocess
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            def git(*args):
                return subprocess.run(["git", "-C", d, *args],
                                      capture_output=True, check=True).stdout
            git("init", "-q")
            (Path(d) / "internal files").mkdir()
            (Path(d) / "internal files" / ".env").write_bytes(b"\\x00\\xff".replace(b"\\x00", b"\x00").replace(b"\\xff", b"\xff"))
            git("add", ".")
            patch_bytes = git("-c", "core.quotePath=false", "diff",
                              "--cached", "--no-ext-diff", "--no-color", "--unified=0")
            self.assertIn(("BLOCK", "PRIVATE_FILE_PATH"), rules(patch_bytes.decode("utf-8")))

    def test_git_commit_history_detects_token_removed_before_final_diff(self):
        import tempfile
        import subprocess
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            def git(*args):
                return subprocess.run(["git", "-C", d, *args],
                                      capture_output=True, check=True).stdout
            git("init", "-q")
            git("config", "user.email", "test@example.invalid")
            git("config", "user.name", "Synthetic Test")
            target=Path(d) / "test.txt"
            target.write_text("ordinary\n")
            git("add", ".")
            git("commit", "-qm", "base")
            base=git("rev-parse", "HEAD").decode().strip()
            target.write_text("token=" + "ghp_" + "Y" * 32 + "\n")
            git("add", ".")
            git("commit", "-qm", "introduce synthetic secret")
            target.write_text("ordinary\n")
            git("add", ".")
            git("commit", "-qm", "remove synthetic secret")
            final_patch=git("diff", base + "...HEAD").decode()
            self.assertNotIn(("BLOCK", "GITHUB_TOKEN"), rules(final_patch))
            history=git("-c", "core.quotePath=false", "log", "--patch", "--format=",
                        "--no-ext-diff", "--no-color", "--unified=0", base + "..HEAD").decode()
            self.assertIn(("BLOCK", "GITHUB_TOKEN"), rules(history))

    def test_new_common_token_families_block_without_logging_values(self):
        examples = (
            ("STRIPE_LIVE_KEY", "sk_live_" + "S" * 32),
            ("SLACK_TOKEN", "xoxb-" + "1" * 12 + "-" + "A" * 30),
            ("HUGGINGFACE_TOKEN", "hf_" + "H" * 40),
            ("NPM_TOKEN", "npm_" + "N" * 40),
        )
        for rule, token in examples:
            with self.subTest(rule=rule):
                self.assertIn(("BLOCK", rule), rules(fake_patch("value=" + token)))

    def test_ambiguous_certificate_and_database_extensions_are_review_not_block(self):
        for filename in ("lecture.key", "public-cert.pem", "offline.db"):
            with self.subTest(filename=filename):
                matches = rules(fake_patch("ordinary", filename))
                self.assertIn(("REVIEW", "BINARY_OR_MEDIA_REVIEW"), matches)
                self.assertFalse(any(severity == "BLOCK" for severity, _ in matches))

    def test_drive_open_and_uc_share_routes_need_review(self):
        for route in ("open?id=", "uc?id="):
            with self.subTest(route=route):
                url="https://" + "drive.google.com/" + route + "D" * 30
                self.assertIn(("BLOCK", "DRIVE_RESOURCE_REFERENCE"), rules(fake_patch(url)))

    def test_ci_cli_blocks_merge_only_added_token(self):
        import tempfile
        import subprocess
        from pathlib import Path

        with tempfile.TemporaryDirectory() as root:
            def git(*args):
                return subprocess.run(["git", "-C", root, *args],
                                      capture_output=True, check=True).stdout
            git("init", "-q")
            git("config", "user.email", "test@example.invalid")
            git("config", "user.name", "Synthetic Reviewer")
            (Path(root) / "baseline.txt").write_text("base\n")
            git("add", ".")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD").decode().strip()
            git("checkout", "-qb", "other")
            (Path(root) / "feature.txt").write_text("safe\n")
            git("add", ".")
            git("commit", "-qm", "feature")
            git("checkout", "-qb", "review", base)
            (Path(root) / "main-side.txt").write_text("also safe\n")
            git("add", ".")
            git("commit", "-qm", "base side")
            git("merge", "--no-ff", "--no-commit", "other")
            (Path(root) / "merged-only.txt").write_text("ghp_" + "M" * 35 + "\n")
            git("add", ".")
            git("commit", "-qm", "merge with synthetic token")
            import publication_guard
            def git_scoped(cmd):
                return subprocess.run(["git", "-C", root, *cmd[1:]],
                                      capture_output=True, check=True).stdout
            with patch("publication_guard._run_git", side_effect=git_scoped):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(1, main([
                        "--range", base + "...HEAD",
                        "--history-range", base + "..HEAD"
                    ]))

    def test_ci_cli_checks_commit_message_and_path_metadata(self):
        import tempfile
        import subprocess
        from pathlib import Path
        with tempfile.TemporaryDirectory() as root:
            def git(*args):
                return subprocess.run(["git", "-C", root, *args],
                                      capture_output=True, check=True).stdout
            git("init", "-q")
            git("config", "user.email", "test@example.invalid")
            git("config", "user.name", "Synthetic Reviewer")
            (Path(root) / "base.txt").write_text("base\n")
            git("add", ".")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD").decode().strip()
            (Path(root) / "safe.txt").write_text("no secret\n")
            git("add", ".")
            git("commit", "-qm", "ghp_" + "C" * 35)
            def git_scoped(cmd):
                return subprocess.run(["git", "-C", root, *cmd[1:]],
                                      capture_output=True, check=True).stdout
            with patch("publication_guard._run_git", side_effect=git_scoped):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(1, main([
                        "--range", base + "...HEAD",
                        "--history-range", base + "..HEAD"
                    ]))
            # Name-only metadata check when text content is innocuous.
            git("checkout", "-qb", "path-test", base)
            (Path(root) / ("ghp_" + "P" * 35 + ".txt")).write_text("safe\n")
            git("add", ".")
            git("commit", "-qm", "plain commit")
            with patch("publication_guard._run_git", side_effect=git_scoped):
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(1, main([
                        "--range", base + "...HEAD",
                        "--history-range", base + "..HEAD"
                    ]))

    def test_literal_added_dev_null_line_cannot_hide_token(self):
        token = "ghp_" + "T" * 34
        payload = fake_patch("++ /dev/null\n+" + token)
        self.assertIn(("BLOCK", "GITHUB_TOKEN"), rules(payload))

    def test_binary_hidden_text_with_gitattributes_real_cli(self):
        """End-to-end: a committed -diff attribute cannot make a token invisible."""
        import subprocess
        import tempfile
        from pathlib import Path
        from publication_guard import __file__ as guard
        with tempfile.TemporaryDirectory() as d:
            def git(*args):
                return subprocess.run(["git", "-C", d, *args],
                                      capture_output=True, check=True).stdout
            git("init", "-q")
            git("config", "user.email", "test@example.invalid")
            git("config", "user.name", "Synthetic")
            (Path(d) / "base.txt").write_text("baseline\n")
            git("add", ".")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD").decode().strip()
            (Path(d) / ".gitattributes").write_text("*.md -diff\n")
            (Path(d) / "notes.md").write_text("ghp_" + "D" * 38 + "\n")
            git("add", ".")
            git("commit", "-qm", "hidden token test")
            cmd = [
                "python", str(Path(guard).resolve()),
                "--range", base + "...HEAD",
                "--history-range", base + "..HEAD",
            ]
            result = subprocess.run(cmd, cwd=d, capture_output=True, text=True)
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("GITHUB_TOKEN", result.stdout)
            self.assertIn("DIFF_ATTRIBUTE_HIDES_CONTENT", result.stdout)
            self.assertNotIn("ghp_" + "D" * 38, result.stdout)

    def test_null_byte_text_is_scanned_not_ignored(self):
        import tempfile
        import subprocess
        from pathlib import Path
        from publication_guard import __file__ as guard
        with tempfile.TemporaryDirectory() as d:
            def git(*args):
                return subprocess.run(["git", "-C", d, *args],
                                      capture_output=True, check=True).stdout
            git("init", "-q")
            git("config", "user.email", "test@example.invalid")
            git("config", "user.name", "Synthetic")
            (Path(d) / "base.txt").write_text("base\n")
            git("add", ".")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD").decode().strip()
            (Path(d) / "notes.txt").write_bytes(b"\x00ghp_" + b"F" * 36 + b"\n")
            git("add", ".")
            git("commit", "-qm", "NUL token test")
            result = subprocess.run(
                ["python", str(Path(guard).resolve()), "--range", base + "...HEAD",
                 "--history-range", base + "..HEAD"],
                cwd=d, capture_output=True, text=True,
            )
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("GITHUB_TOKEN", result.stdout)

    def test_gitattributes_binary_marker_alone_blocks(self):
        self.assertIn(("BLOCK", "DIFF_ATTRIBUTE_HIDES_CONTENT"),
                      rules(fake_patch("*.json binary", ".gitattributes")))
        self.assertIn(("BLOCK", "UNINSPECTED_BINARY_DIFF"),
                      rules("diff --git a/data.json b/data.json\n"
                            "Binary files a/data.json and b/data.json differ\n"))

    def test_utf16_nul_obfuscation_blocks_and_detects_synthetic_token(self):
        import tempfile
        import subprocess
        from pathlib import Path
        from publication_guard import __file__ as guard
        with tempfile.TemporaryDirectory() as d:
            def git(*args):
                return subprocess.run(["git", "-C", d, *args],
                                      capture_output=True, check=True).stdout
            git("init", "-q")
            git("config", "user.email", "test@example.invalid")
            git("config", "user.name", "Synthetic")
            (Path(d) / "base.txt").write_text("base\n")
            git("add", ".")
            git("commit", "-qm", "base")
            base = git("rev-parse", "HEAD").decode().strip()
            synthetic = "ghp_" + "U" * 36
            (Path(d) / "notes.txt").write_bytes((synthetic + "\n").encode("utf-16le"))
            git("add", ".")
            git("commit", "-qm", "UTF16-style binary text")
            result = subprocess.run(
                ["python", str(Path(guard).resolve()), "--range", base + "...HEAD",
                 "--history-range", base + "..HEAD"],
                cwd=d, capture_output=True, text=True,
            )
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("NUL_IN_ADDED_CONTENT", result.stdout)
            self.assertIn("GITHUB_TOKEN", result.stdout)
            self.assertNotIn(synthetic, result.stdout)

    def test_env_example_not_blocked_as_private_env(self):
        out = rules(fake_patch("DOCUMENTED=PLACEHOLDER", ".env.example"))
        self.assertNotIn(("BLOCK", "PRIVATE_FILE_PATH"), out)
        self.assertIn(("BLOCK", "PRIVATE_FILE_PATH"),
                      rules(fake_patch("LIVE=1", ".env.production")))

    def test_credential_file_names_block(self):
        # Finding PR20-P2-3: these names were in the rule but untested.
        for path in (".npmrc", "config/.netrc", "secrets/token.json", "token.pickle", ".git-credentials"):
            self.assertIn(("BLOCK", "PRIVATE_FILE_PATH"), rules(fake_patch("x=1", path)), path)

    def test_jwt_blocks(self):
        # Finding PR20-P2-4. Built at runtime so this file holds no token-shaped literal.
        seg = lambda c: "eyJ" + c * 20
        self.assertIn(("BLOCK", "JWT"), rules(fake_patch("t = " + seg("A") + "." + seg("B") + "." + "S" * 30)))
        self.assertNotIn(("BLOCK", "JWT"), rules(fake_patch("eyJ is how a JWT header starts")))

    def test_private_key_block_variants(self):
        for label, rule in (("ENCRYPTED PRIVATE KEY", "PRIVATE_KEY_PEM"), ("PGP PRIVATE KEY BLOCK", "PGP_PRIVATE_KEY")):
            self.assertIn(("BLOCK", rule), rules(fake_patch("-----BEGIN " + label + "-----")), label)
        self.assertNotIn(("BLOCK", "PGP_PRIVATE_KEY"), rules(fake_patch("-----BEGIN PGP PUBLIC KEY BLOCK-----")))

    def test_bearer_inside_json_blocks(self):
        line = '{"Authorization": "Bearer ' + "q" * 30 + '"}'
        self.assertIn(("BLOCK", "BEARER_CREDENTIAL"), rules(fake_patch(line)))

    def test_credentials_in_url(self):
        self.assertIn(("BLOCK", "CREDENTIALS_IN_URL"),
                      rules(fake_patch("DATABASE_URL=postgres://admin:" + "S3cr3tValue9" + "@db.internal:5432/app")))
        for benign in ("postgres://user:password@localhost/db", "https://user:${DB_PASS}@host/x",
                       "https://user:<password>@host/x", "see https://example.com/a:b@c"):
            self.assertNotIn(("BLOCK", "CREDENTIALS_IN_URL"), rules(fake_patch(benign)), benign)

    def test_base64_encoded_token_blocks(self):
        import base64
        token = ("ghp_" + "X" * 32).encode()
        for enc in (base64.b64encode(token), base64.urlsafe_b64encode(token)):
            self.assertIn(("BLOCK", "BASE64_GITHUB_TOKEN"), rules(fake_patch("blob: " + enc.decode())))
        self.assertFalse([r for r in rules(fake_patch("hash " + "a1b2c3d4" * 8)) if r[1].startswith("BASE64_")])

    def test_office_tiff_and_webm_files_reviewed(self):
        # Finding PR20-P1-5 (partly): these formats are routed to review.
        for path in ("assets/scan.tiff", "assets/clip.webm", "docs/brief.docx", "docs/sheet.xlsx"):
            self.assertIn(("REVIEW", "BINARY_OR_MEDIA_REVIEW"), rules(fake_patch("x", path)), path)

    def test_token_split_across_two_added_lines_blocks(self):
        # Finding PR20-P2-2: concatenation or line continuation must not hide a token.
        head, tail = "ghp_" + "X" * 12, "X" * 20
        for first, second in ((f'TOKEN = "{head}" +', f'    "{tail}"'), (f"TOKEN={head}\\", tail)):
            patch = ("diff --git a/a.py b/a.py\nnew file mode 100644\n+++ b/a.py\n@@ -0,0 +2 @@\n"
                     f"+{first}\n+{second}\n")
            self.assertIn(("BLOCK", "SPLIT_GITHUB_TOKEN"), rules(patch), first)
        unrelated = ("diff --git a/a.md b/a.md\nnew file mode 100644\n+++ b/a.md\n@@ -0,0 +2 @@\n"
                     "+The ghp_ prefix marks a classic token.\n+It is followed by 36 characters.\n")
        self.assertFalse([r for r in rules(unrelated) if r[1].startswith("SPLIT_")])

    def test_token_split_across_three_added_lines_blocks(self):
        # 2026-10-30 audit: a third line must not hide a split token either.
        parts = ('TOKEN = "ghp_' + "X" * 10 + '" +', '    "' + "X" * 10 + '" +', '    "' + "X" * 12 + '"')
        patch = ("diff --git a/a.py b/a.py\nnew file mode 100644\n+++ b/a.py\n@@ -0,0 +3 @@\n"
                 + "".join("+%s\n" % p for p in parts))
        found = [r for r in rules(patch) if r[1] == "SPLIT_GITHUB_TOKEN"]
        self.assertEqual(found, [("BLOCK", "SPLIT_GITHUB_TOKEN")])

    def test_common_key_names_block(self):
        # 2026-10-30 audit: api_key, x-api-key, token and secret assignments with key-like values.
        value = "Q7" + "w" * 30
        for line in ("API_KEY=" + value, '"api_key": "%s"' % value, "x-api-key: " + value,
                     "TOKEN=" + value, "SECRET = '%s'" % value):
            self.assertIn(("BLOCK", "GENERIC_SECRET_ASSIGNMENT"), rules(fake_patch(line)), line)
        for line in ("API_KEY=<your key>", "token: ${{ secrets.GITHUB_TOKEN }}", "the token is short", "api_key=abc"):
            self.assertNotIn(("BLOCK", "GENERIC_SECRET_ASSIGNMENT"), rules(fake_patch(line)), line)

    def test_underscore_secret_key_blocks(self):
        self.assertIn(("BLOCK", "SECRET_KEY"), rules(fake_patch("key " + "sk_" + "t" * 30)))

    def test_local_home_path_is_reviewed(self):
        # 2026-10-30 audit: a home folder names the owner's account and machine layout.
        self.assertIn(("REVIEW", "LOCAL_HOME_PATH"), rules(fake_patch("see /Users/" + "jdoe/Desktop/notes")))
        self.assertIn(("REVIEW", "LOCAL_HOME_PATH"), rules(fake_patch("cd /home/" + "jdoe/work/")))
        for line in ("/Users/you/project/", "/home/runner/work/", "C:/Users/someone/a.js"):
            self.assertNotIn(("REVIEW", "LOCAL_HOME_PATH"), rules(fake_patch(line)), line)

    def test_media_with_exif_needs_review(self):
        # Finding PR20-P1-5: EXIF in added media is routed to review (labels only, no values).
        jpeg = b"\xff\xd8\xff\xe1\x00\x10" + b"Exif\x00\x00" + b"II*\x00\x08\x00\x00\x00" + b"\x00\x00"
        self.assertEqual([(f.severity, f.rule) for f in media_metadata_findings("p.jpg", jpeg)], [("REVIEW", "MEDIA_METADATA_REVIEW")])
        plain_png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
        self.assertEqual(media_metadata_findings("p.png", plain_png), [])

    def test_google_refresh_token_blocks(self):
        # Killed a surviving mutant in security/mutation_check.py.
        self.assertIn(("BLOCK", "GOOGLE_OAUTH_REFRESH_TOKEN"), rules(fake_patch("refresh: 1//" + "R" * 40)))

    def test_shareable_storage_link_is_reviewed(self):
        # Killed a surviving mutant in security/mutation_check.py.
        line = "https://files.example.net/share/" + "a1b2c3d4e5f6"
        self.assertIn(("REVIEW", "SHAREABLE_STORAGE_LINK"), rules(fake_patch(line)))
        self.assertNotIn(("REVIEW", "SHAREABLE_STORAGE_LINK"), rules(fake_patch("https://example.net/share/x")))

    def test_github_classic_token(self):
        token = "ghp_" + "X" * 32
        self.assertIn(("BLOCK", "GITHUB_TOKEN"), rules(fake_patch("token=" + token)))

    def test_github_fine_grained_token(self):
        tok = "github_pat_" + "T" * 50
        self.assertIn(("BLOCK", "GITHUB_TOKEN"), rules(fake_patch(tok)))

    def test_openai_key(self):
        token = "sk-" + "z" * 31
        self.assertIn(("BLOCK", "SECRET_KEY"), rules(fake_patch(token)))

    def test_google_api_key(self):
        key = "AIza" + "a" * 35
        self.assertIn(("BLOCK", "GOOGLE_API_KEY"), rules(fake_patch(key)))

    def test_aws_access_identifier(self):
        key = "AKIA" + "A" * 16
        self.assertIn(("BLOCK", "AWS_ACCESS_ID"), rules(fake_patch(key)))

    def test_bearer_header(self):
        tok = "authorization: bearer " + "T" * 36
        self.assertIn(("BLOCK", "BEARER_CREDENTIAL"), rules(fake_patch(tok)))

    def test_private_key_pem_header(self):
        key = "-----BEGIN " + "RSA PRIVATE KEY-----"
        self.assertIn(("BLOCK", "PRIVATE_KEY_PEM"), rules(fake_patch(key)))

    def test_amz_signed_url(self):
        url = "https://example.org/file?X-Amz-Signature=" + "abcdef" * 12
        self.assertIn(("BLOCK", "SIGNED_ACCESS_URL"), rules(fake_patch(url)))

    def test_generic_query_access_token(self):
        url = "https://example.org/download?token=" + "A" * 32
        self.assertIn(("BLOCK", "SIGNED_QUERY_TOKEN"), rules(fake_patch(url)))

    def test_nonsecret_documentation_is_clear(self):
        self.assertEqual([], rules(fake_patch("The GitHub provider requires tokens.")))

    def test_drive_resource_link_blocks_by_default(self):
        link = "https://" + "drive.google.com/file/d/" + "1" * 30 + "/view"
        self.assertIn(("BLOCK", "DRIVE_RESOURCE_REFERENCE"), rules(fake_patch(link)))

    def test_docs_link_requires_block(self):
        link = "https://" + "docs.google.com/document/d/" + "a" * 30 + "/edit"
        self.assertIn(("BLOCK", "DRIVE_RESOURCE_REFERENCE"), rules(fake_patch(link)))

    def test_email_in_public_text_requires_review_but_not_autoblock(self):
        candidate = "person@" + "company.org"
        result = rules(fake_patch("Contact: " + candidate))
        self.assertIn(("REVIEW", "EMAIL_ADDRESS"), result)
        self.assertFalse(any(severity == "BLOCK" for severity, _ in result))

    def test_reserved_example_email_does_not_raise_review(self):
        candidate = "documentation@" + "example.invalid"
        self.assertNotIn(("REVIEW", "EMAIL_ADDRESS"), rules(fake_patch(candidate)))

    def test_commit_coauthor_email_separated_from_other_message_content(self):
        address = "contributor@" + "company.org"
        data = ("Subject\n\nCo-authored-by: Tester <" + address + ">\n").encode()
        def fake_git(args, stdin=None):
            if args == ["log", "--all", "HEAD", "--format=%B%x00"]:
                return data + b"\x00"
            if args == ["log", "--all", "HEAD", "--format=%ae"]:
                return b"bot@users.noreply.github.com\n"
            raise AssertionError("Unexpected Git request")
        with patch("history_audit.git", side_effect=fake_git):
            report = audit_commit_metadata()
        self.assertEqual(1, report["REVIEW:COAUTHORSHIP_TRAILER_EMAIL_LINES"])
        self.assertEqual(1, report["UNIQUE_COMMIT_MESSAGE_EMAILS_REVIEW"])
        self.assertEqual(0, report.get("REVIEW:OTHER_COMMIT_MESSAGE_EMAIL_LINES", 0))
        self.assertNotIn(address, repr(report))

    def test_repeated_commit_message_email_counts_as_one_unique_candidate(self):
        email = "person@" + "company.org"
        messages = (("first " + email) + "\x00" + ("second " + email)
                    + "\x00" + "test test@example.invalid" + "\x00").encode()
        def fake_git(args, stdin=None):
            if args == ["log", "--all", "HEAD", "--format=%B%x00"]:
                return messages
            if args == ["log", "--all", "HEAD", "--format=%ae"]:
                return b"bot@users.noreply.github.com\n"
            raise AssertionError("Unexpected git request")
        with patch("history_audit.git", side_effect=fake_git):
            result = audit_commit_metadata()
        self.assertEqual(1, result["UNIQUE_COMMIT_MESSAGE_EMAILS_REVIEW"])
        self.assertEqual(2, result["COMMIT_REVIEW:EMAIL_ADDRESS"])
        self.assertNotIn(email, repr(result))

    def test_detached_checkout_head_is_included_in_commit_metadata_scan(self):
        requested = []
        def fake_git(args, stdin=None):
            requested.append(args)
            if args == ["log", "--all", "HEAD", "--format=%B%x00"]:
                return b"example subject\x00"
            if args == ["log", "--all", "HEAD", "--format=%ae"]:
                return b"bot@users.noreply.github.com\n"
            raise AssertionError("Unexpected Git query")
        with patch("history_audit.git", side_effect=fake_git):
            report = audit_commit_metadata()
        self.assertEqual(1, report["SCANNED_COMMIT_MESSAGES"])
        self.assertEqual(2, len(requested))
        self.assertTrue(all("HEAD" in query for query in requested))

    def test_historical_email_is_reviewed_without_value_disclosure(self):
        address = "user@" + "privatecompany.de"
        result = audit_text_blob("Contact is " + address, "docs/review.md")
        self.assertIn("REVIEW:EMAIL_ADDRESS", result)
        self.assertNotIn(address, repr(result))

    def test_public_github_reference_does_not_warn(self):
        link = "https://github.com/bribeirobr25/ai-creative-skill/pull/18"
        self.assertEqual([], rules(fake_patch(link)))

    def test_private_filename_block(self):
        x = rules(fake_patch("PRIVATE=1", ".env.production"))
        self.assertIn(("BLOCK", "PRIVATE_FILE_PATH"), x)

    def test_private_key_filename_block(self):
        self.assertIn(("BLOCK", "PRIVATE_FILE_PATH"), rules(fake_patch("x", "secrets/keys.pem")))

    def test_binary_file_review(self):
        self.assertIn(("REVIEW", "BINARY_OR_MEDIA_REVIEW"), rules(fake_patch("x", "assets/photo.jpg")))

    def test_deleted_content_not_scanned(self):
        key = "ghp_" + "Y" * 34
        diff = (
            "diff --git a/file b/file\n+++ b/file\n"
            "@@ -1 +1 @@\n-" + key + "\n+safe replacement\n"
        )
        self.assertEqual([], scan_unified_diff(diff))

    def test_git_header_not_content(self):
        self.assertEqual([], rules("diff --git a/x b/x\n+++ b/x\n@@ -0,0 +1 @@\n+harmless\n"))

    def test_both_added_files_scanned(self):
        a = fake_patch("sk-" + "A" * 29, "a.md")
        b = fake_patch("ghp_" + "B" * 40, "b.txt")
        x = scan_unified_diff(a + b)
        self.assertEqual(2, sum(y.severity == "BLOCK" for y in x))

    def test_output_never_prints_secret(self):
        secret = "ghp_" + "C" * 41
        with patch("publication_guard._get_diff", return_value=fake_patch(secret)):
            buf = io.StringIO()
            with redirect_stdout(buf):
                status = main(["--staged"])
            self.assertEqual(1, status)
            self.assertNotIn(secret, buf.getvalue())
            self.assertIn("GITHUB_TOKEN", buf.getvalue())

    def test_scanner_never_logs_sensitive_filename(self):
        secret_in_path = "private/" + "user@example.com" + "/.env"
        patch_text = fake_patch("api_token=" + "ghp_" + "P" * 40, secret_in_path)
        with patch("publication_guard._get_diff", return_value=patch_text):
            buf = io.StringIO()
            with redirect_stdout(buf):
                result = main(["--staged"])
            self.assertEqual(1, result)
            self.assertNotIn(secret_in_path, buf.getvalue())
            self.assertNotIn("user@example.com", buf.getvalue())
            self.assertIn("path_ref=", buf.getvalue())

    def test_warning_default_does_not_break(self):
        link = "https://" + "docs.google.com/document/d/EXAMPLE_DOCUMENT_ID/edit"
        with patch("publication_guard._get_diff", return_value=fake_patch(link)):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(0, main(["--staged"]))

    def test_warning_can_be_strict(self):
        link = "https://" + "docs.google.com/document/d/EXAMPLE_DOCUMENT_ID/edit"
        with patch("publication_guard._get_diff", return_value=fake_patch(link)):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(1, main(["--staged", "--fail-on-warning"]))

    def test_remote_branch_coverage_exact_match(self):
        def fake_git(args, stdin=None):
            if args[:2] == ["ls-remote", "--heads"]:
                return b"a" * 40 + b"\trefs/heads/main\n" + b"b" * 40 + b"\trefs/heads/feature/example\n"
            if args and args[0] == "for-each-ref":
                return b"main " + b"a" * 40 + b"\nfeature/example " + b"b" * 40 + b"\n"
            raise AssertionError("Unexpected git command")
        with patch("history_audit.git", side_effect=fake_git):
            self.assertEqual(2, _verified_branch_coverage())

    def test_remote_branch_missing_blocks_audit(self):
        def fake_git(args, stdin=None):
            if args[:2] == ["ls-remote", "--heads"]:
                return b"a" * 40 + b"\trefs/heads/main\n" + b"b" * 40 + b"\trefs/heads/secret-branch\n"
            if args and args[0] == "for-each-ref":
                return b"main " + b"a" * 40 + b"\n"
            raise AssertionError("Unexpected git command")
        with patch("history_audit.git", side_effect=fake_git):
            with self.assertRaisesRegex(RuntimeError, "incomplete"):
                _verified_branch_coverage()

    def test_stale_branch_head_blocks_audit(self):
        def fake_git(args, stdin=None):
            if args[:2] == ["ls-remote", "--heads"]:
                return b"a" * 40 + b"\trefs/heads/main\n"
            if args and args[0] == "for-each-ref":
                return b"main " + b"b" * 40 + b"\n"
            raise AssertionError("Unexpected git command")
        with patch("history_audit.git", side_effect=fake_git):
            with self.assertRaisesRegex(RuntimeError, "incomplete"):
                _verified_branch_coverage()

    @staticmethod
    def _synthetic_exif_text(value: bytes, tag: int = 0x013B) -> bytes:
        import struct
        offset = 26
        entry = struct.pack("<HHII", tag, 2, len(value), offset)
        return (
            b"\xff\xd8\xffExif\x00\x00"
            + b"II\x2a\x00"
            + struct.pack("<I", 8)
            + struct.pack("<H", 1)
            + entry + b"\x00" * 4 + value
        )

    def test_exif_real_value_flags_email_without_emitting_it(self):
        private_example = b"person@example.invalid\x00"
        raw = self._synthetic_exif_text(private_example)
        flags = classify_binary_metadata(raw)
        self.assertIn("BINARY_EXIF_IDENTIFYING_VALUE_PRESENT", flags)
        self.assertIn("BINARY_EXIF_EMAIL_LIKE_VALUE_NEEDS_REVIEW", flags)
        self.assertNotIn("person@example.invalid", repr(flags))

    def test_exif_benign_text_is_still_marked_present_not_certified(self):
        flags = classify_binary_metadata(self._synthetic_exif_text(b"Generic Creator\x00"))
        self.assertIn("BINARY_EXIF_IDENTIFYING_VALUE_PRESENT", flags)
        self.assertNotIn("BINARY_EXIF_EMAIL_LIKE_VALUE_NEEDS_REVIEW", flags)

    def test_exif_text_url_flag(self):
        flags = classify_binary_metadata(
            self._synthetic_exif_text(b"https://" + b"example.invalid/private\x00", tag=0x010E)
        )
        self.assertIn("BINARY_EXIF_URL_LIKE_VALUE_NEEDS_REVIEW", flags)

    def test_exif_invalid_value_offset_returns_incomplete(self):
        raw = (
            b"Exif\x00\x00II\x2a\x00"
            + (8).to_bytes(4, "little")
            + (1).to_bytes(2, "little")
            + (0x013B).to_bytes(2, "little")
            + (2).to_bytes(2, "little")
            + (30).to_bytes(4, "little")
            + (4000).to_bytes(4, "little")
            + (0).to_bytes(4, "little")
        )
        self.assertIn(
            "BINARY_EXIF_VALUE_INSPECTION_INCOMPLETE",
            _exif_value_risk_categories(raw),
        )

    def test_exif_gps_and_author_tags_are_classified_without_values(self):
        # Small synthetic TIFF IFD: GPSInfo tag and Artist tag.
        exif = (
            b"Exif\x00\x00" + b"II\x2a\x00" + (8).to_bytes(4, "little")
            + (2).to_bytes(2, "little")
            + (0x8825).to_bytes(2, "little") + (4).to_bytes(2, "little")
            + (1).to_bytes(4, "little") + (40).to_bytes(4, "little")
            + (0x013B).to_bytes(2, "little") + (2).to_bytes(2, "little")
            + (1).to_bytes(4, "little") + (88).to_bytes(4, "little")
            + (0).to_bytes(4, "little")
        )
        flags = classify_binary_metadata(b"\xff\xd8\xff" + exif)
        self.assertIn("BINARY_EXIF_GPS_POINTER", flags)
        self.assertIn("BINARY_EXIF_POTENTIAL_IDENTIFYING_TAG", flags)
        self.assertIn("BINARY_EXIF_ARTIST_TAG", flags)
        self.assertTrue(all("88" not in f for f in flags))

    def test_exif_image_description_separates_from_serial_and_owner(self):
        tiff = (
            b"Exif\x00\x00" + b"II\x2a\x00" + (8).to_bytes(4, "little")
            + (1).to_bytes(2, "little")
            + (0x010E).to_bytes(2, "little") + (2).to_bytes(2, "little")
            + (1).to_bytes(4, "little") + (88).to_bytes(4, "little")
            + (0).to_bytes(4, "little")
        )
        flags = classify_binary_metadata(b"\xff\xd8\xff" + tiff)
        self.assertIn("BINARY_EXIF_IMAGE_DESCRIPTION_TAG", flags)
        self.assertNotIn("BINARY_EXIF_CAMERA_SERIAL_TAG", flags)
        self.assertNotIn("BINARY_EXIF_CAMERA_OWNER_TAG", flags)

    def test_malformed_exif_gets_review_classification(self):
        flags = classify_binary_metadata(b"\xff\xd8\xff" + b"Exif\x00\x00" + b"broken")
        self.assertIn("BINARY_EXIF_UNPARSEABLE", flags)

    def test_standard_metadata_namespace_is_separate_from_link_review(self):
        flags = classify_binary_metadata(
            b"\xff\xd8\xff" + b'http://ns.adobe.com/xap/1.0/'
        )
        self.assertIn("BINARY_STANDARD_METADATA_NAMESPACE", flags)
        self.assertNotIn("BINARY_OTHER_EMBEDDED_URL_NEEDS_REVIEW", flags)

    def test_drive_uri_in_jpeg_metadata_requires_review(self):
        url = b"https://" + b"drive.google.com/file/d/" + b"X" * 32
        flags = classify_binary_metadata(b"\xff\xd8\xff" + url)
        self.assertIn("BINARY_DRIVE_REFERENCE_NEEDS_REVIEW", flags)

    def test_jpeg_exif_flag_without_publishing_metadata(self):
        raw = b"\xff\xd8\xff" + b"\x00" * 8 + b"Exif\x00\x00" + b"GPS private"
        result = classify_binary_metadata(raw)
        self.assertIn("BINARY_JPEG", result)
        self.assertIn("BINARY_EXIF_PRESENT", result)
        self.assertTrue(all("GPS private" not in flag for flag in result))

    def test_png_metadata_flag(self):
        raw = b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\x05iTXt" + b"example"
        self.assertIn("BINARY_PNG_METADATA_PRESENT", classify_binary_metadata(raw))

    def test_pdf_embedded_url_marker(self):
        raw = b"%PDF-1.7\n" + b" /URI " + b"ignored-private-link"
        kinds = classify_binary_metadata(raw)
        self.assertIn("BINARY_PDF", kinds)
        self.assertIn("BINARY_PDF_LINK_OR_SCRIPT_MARKER", kinds)

    def test_zip_requires_private_manual_review(self):
        kinds = classify_binary_metadata(b"PK\x03\x04\x00\x00")
        self.assertIn("BINARY_ZIP", kinds)

    def test_webp_exif_and_xmp_categories_are_detected_without_raw_values(self):
        blob = b"RIFF" + b"\x00" * 4 + b"WEBP" + b"EXIF" + b"xmpmeta"
        kinds = classify_binary_metadata(blob)
        self.assertIn("BINARY_WEBP", kinds)
        self.assertIn("BINARY_WEBP_METADATA_PRESENT", kinds)
        self.assertIn("BINARY_POSSIBLE_XMP_METADATA", kinds)

    def test_heic_container_gets_manual_media_review_class(self):
        blob = b"\x00\x00\x00\x18ftypheic" + b"\x00" * 12
        kinds = classify_binary_metadata(blob)
        self.assertIn("BINARY_HEIF_OR_HEIC_NEEDS_MEDIA_REVIEW", kinds)

    def test_unrecognized_binary_type(self):
        self.assertIn("BINARY_UNKNOWN_OR_OTHER", classify_binary_metadata(b"\x00\x01\x02"))

    def test_history_preserves_all_paths_for_identical_blob_versions(self):
        sha = b"c" * 40
        commit1 = b"a" * 40
        commit2 = b"b" * 40

        def fake_git(args, stdin=None):
            if args == ["rev-list", "--all", "HEAD"]:
                return commit1 + b"\n" + commit2 + b"\n"
            if args[:3] == ["ls-tree", "-r", "-z"]:
                path = b"docs/research/public-reference.md" if args[3] == commit1.decode() else b"src/references/old-path.md"
                return b"100644 blob " + sha + b"\t" + path + b"\x00"
            if args and args[0] == "cat-file":
                self.assertEqual(sha + b"\n", stdin)
                return sha + b" blob 12\n"
            raise AssertionError("Unexpected Git command")

        with patch("history_audit.git", side_effect=fake_git):
            paths, sizes = _reachable_blobs()
        self.assertEqual(12, sizes[sha.decode()])
        self.assertEqual({
            "docs/research/public-reference.md",
            "src/references/old-path.md"
        }, paths[sha.decode()])

    def test_history_rejects_empty_commit_list(self):
        with patch("history_audit.git", return_value=b""):
            with self.assertRaises(RuntimeError):
                _reachable_blobs()

    def test_classify_github_download_without_exposing_url(self):
        url = "https://" + "github.com/public/example/releases/download/v1.0/asset.zip"
        flags = _generic_share_host_types(url)
        self.assertEqual(1, len(flags["PUBLIC_GITHUB"]))
        self.assertEqual(0, len(flags["OTHER"]))
        self.assertNotIn(url, str(flags))

    def test_classify_unknown_download_service_as_reviewable(self):
        url = "https://" + "files.example.invalid/download/" + "abcdef1234567890"
        flags = _generic_share_host_types(url)
        self.assertEqual(1, len(flags["OTHER"]))
        self.assertEqual(0, len(flags["PUBLIC_GITHUB"]))

    def test_distinct_link_fingerprints_deduplicate_repeated_url(self):
        a = "https://" + "drive.google.com/drive/folders/" + "D" * 32
        b = "https://" + "drive.google.com/drive/folders/" + "E" * 32
        first = _link_fingerprints(a + "\n" + a)["DRIVE"]
        second = _link_fingerprints(a + "\n" + b)["DRIVE"]
        self.assertEqual(1, len(first))
        self.assertEqual(2, len(second))
        self.assertTrue(all(a not in x and b not in x for x in second))

    def test_distinct_share_link_is_not_drive_count(self):
        u = "https://" + "github.com/public/project/releases/download/" + "test-data"
        result = _link_fingerprints(u)
        self.assertEqual(0, len(result["DRIVE"]))
        self.assertEqual(1, len(result["GENERIC_SHARE"]))

    def test_incomplete_file_and_document_url_prefixes_are_not_real_resources(self):
        f = "https://" + "drive.google.com/file/d/"
        d = "https://" + "docs.google.com/document/d/"
        self.assertIn("LINK_INCOMPLETE_OR_PLACEHOLDER_IDENTIFIER", classify_link_metadata(f))
        self.assertIn("LINK_INCOMPLETE_OR_PLACEHOLDER_IDENTIFIER", classify_link_metadata(d))

    def test_plausible_complete_folder_id_not_flagged_as_placeholder(self):
        u = "https://" + "drive.google.com/drive/folders/" + "A" * 33
        flags = classify_link_metadata(u)
        self.assertIn("LINK_DRIVE_FOLDER", flags)
        self.assertNotIn("LINK_INCOMPLETE_OR_PLACEHOLDER_IDENTIFIER", flags)

    def test_drive_link_classification_redacts_identifier(self):
        u = "https://" + "drive.google.com/drive/folders/" + "F" * 33
        flags = classify_link_metadata(u)
        self.assertIn("LINK_DRIVE_FOLDER", flags)
        self.assertNotIn(u, repr(flags))
        self.assertTrue(all("F" * 33 not in tag for tag in flags))

    def test_docs_link_classification(self):
        u = "https://" + "docs.google.com/document/d/" + "D" * 28 + "/edit"
        self.assertIn("LINK_DRIVE_NATIVE_DOCUMENT", classify_link_metadata(u))

    def test_drive_resource_key_is_reviewed_not_granted(self):
        u = "https://" + "drive.google.com/file/d/" + "X" * 30 + "/view?resourcekey=" + "Y" * 31
        flags = classify_link_metadata(u)
        self.assertIn("LINK_DRIVE_FILE", flags)
        self.assertIn("LINK_WITH_ACCESS_HINT_NEEDS_PRIVATE_REVIEW", flags)

    def test_example_file_ref_may_be_placeholder(self):
        u = "https://" + "drive.google.com/file/d/FILE_ID/view"
        flags = classify_link_metadata(u)
        self.assertIn("LINK_POSSIBLE_PLACEHOLDER", flags)

    def test_no_drive_links(self):
        flags = classify_link_metadata("https://github.com/public/project")
        self.assertEqual(set(), flags)

    def test_origin_scope_buckets_do_not_reveal_private_paths(self):
        self.assertEqual("RESEARCH", _scope_bucket("docs/research/brand-private/report.md"))
        self.assertEqual("MIGRATION", _scope_bucket("docs/migration/client-folder.md"))
        self.assertEqual("VALIDATION", _scope_bucket("validation/fixtures/test.json"))
        self.assertEqual("OTHER", _scope_bucket("unknown/secret-resource.txt"))

    def test_history_scan_detects_categories_without_content(self):
        synthetic = "https://" + "drive.google.com/file/d/" + "1" * 32 + "/view"
        token = "ghp_" + "Q" * 40
        found = audit_text_blob("reference: " + synthetic + " token=" + token, "docs/example.md")
        self.assertIn("REVIEW:DRIVE_REFERENCE", found)
        self.assertIn("BLOCK:GITHUB_TOKEN", found)
        self.assertTrue(all(synthetic not in item and token not in item for item in found))

    def test_history_scan_flags_binary_and_private_names_without_exposing_path(self):
        found = audit_text_blob("nothing secret here", "internal/.env")
        self.assertIn("BLOCK:PRIVATE_FILE_PATH", found)
        self.assertNotIn("internal/.env", str(found))
        other = audit_text_blob("", "assets/brand-photo.jpg")
        self.assertIn("REVIEW:BINARY_OR_MEDIA_PATH", other)

    def test_history_scan_allows_safe_text(self):
        self.assertEqual(set(), audit_text_blob("ordinary public method", "docs/safe.md"))

    def test_history_audit_incomplete_is_not_reported_as_success(self):
        from history_audit import main as history_main
        with patch("history_audit.scan_history",
                   return_value={"SKIPPED_BINARY_BLOB": 2,
                                 "SCANNED_TEXT_BLOB": 11}):
            with redirect_stdout(io.StringIO()):
                with patch("sys.stderr", new_callable=io.StringIO):
                    self.assertEqual(2, history_main())
        with patch("history_audit.scan_history",
                   return_value={"SCANNED_TEXT_BLOB": 11}):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(0, history_main())

    def test_git_error_not_success(self):
        with patch("publication_guard._get_diff", side_effect=RuntimeError("Git diff unavailable")):
            with patch("sys.stderr", new_callable=io.StringIO):
                self.assertEqual(2, main(["--staged"]))


if __name__ == "__main__":
    unittest.main()


class ClosedScopeCliRegressions(unittest.TestCase):
    """Real-Git CLI tests: guard behavior, not isolated rules()."""

    def _repo(self):
        import tempfile
        import pathlib
        import subprocess
        tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(tmp.name)
        def git(*args):
            return subprocess.run(["git", "-C", str(root), *args], check=True,
                                  capture_output=True).stdout
        git("init", "-q")
        git("config", "user.email", "review@example.invalid")
        git("config", "user.name", "Fixture reviewer")
        git("commit", "-qm", "base", "--allow-empty")
        base = git("rev-parse", "HEAD").decode().strip()
        return tmp, root, git, base

    def _cli(self, root, *args):
        import subprocess
        from pathlib import Path
        from publication_guard import __file__ as guard_file
        return subprocess.run(["python", str(Path(guard_file).resolve()), *args],
                              cwd=root, capture_output=True, text=True)

    def test_history_added_then_removed_is_not_clean(self):
        tmp, root, git, base = self._repo()
        with tmp:
            p = root / "once.md"
            p.write_text("ghp_" + "Q" * 36)
            git("add", "-A"); git("commit", "-qm", "add")
            p.unlink(); git("add", "-A"); git("commit", "-qm", "remove")
            result = self._cli(root, "--range", base + "...HEAD",
                               "--history-range", base + "..HEAD")
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("GITHUB_TOKEN", result.stdout)

    def test_two_parent_merge_added_then_removed_is_caught_by_cli(self):
        """Removing --diff-merges=remerge must break this real-Git regression."""
        tmp, root, git, base = self._repo()
        with tmp:
            git("checkout", "-qb", "side", base)
            (root / "side.md").write_text("ordinary side\n")
            git("add", "-A"); git("commit", "-qm", "side")
            git("checkout", "-qb", "review", base)
            (root / "review.md").write_text("ordinary review\n")
            git("add", "-A"); git("commit", "-qm", "review")
            git("merge", "--no-ff", "--no-commit", "side")
            injected = root / "merged_only.md"
            injected.write_text("ghp_" + "K" * 36 + "\n")
            git("add", "-A"); git("commit", "-qm", "merge-only addition")
            injected.unlink()
            git("add", "-A"); git("commit", "-qm", "remove merge-only addition")
            result = self._cli(root, "--range", base + "...HEAD",
                               "--history-range", base + "..HEAD")
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("GITHUB_TOKEN", result.stdout)

    def test_invalid_base_ref_exits_incomplete(self):
        tmp, root, git, base = self._repo()
        with tmp:
            result = self._cli(root, "--range", "does-not-exist...HEAD",
                               "--history-range", "does-not-exist..HEAD")
            self.assertEqual(2, result.returncode)

    def test_staged_path_must_be_scanned(self):
        tmp, root, git, base = self._repo()
        with tmp:
            filename = "ghp_" + "M" * 35 + ".md"
            (root / filename).write_text("ordinary text")
            git("add", "-A")
            result = self._cli(root, "--staged")
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("GITHUB_TOKEN", result.stdout)

    def test_octopus_history_fails_closed(self):
        tmp, root, git, base = self._repo()
        with tmp:
            for b in ("b1", "b2", "b3"):
                git("checkout", "-qb", b, base)
                (root / (b + ".md")).write_text(b)
                git("add", "-A"); git("commit", "-qm", b)
            git("checkout", "-qb", "review", base)
            git("merge", "--no-ff", "--no-commit", "b1", "b2", "b3")
            (root / "evil.md").write_text("ghp_" + "E" * 36)
            git("add", "-A"); git("commit", "-qm", "octopus")
            git("rm", "-q", "evil.md"); git("commit", "-qm", "remove")
            result = self._cli(root, "--range", base + "...HEAD",
                               "--history-range", base + "..HEAD")
            self.assertEqual(2, result.returncode, result.stderr)
            self.assertIn("OCTOPUS_MERGE_UNINSPECTED", result.stderr)

    def test_provider_families_and_placeholder(self):
        import publication_guard as guard
        for token in ("GOCSPX-" + "A" * 28, "ya29." + "a0B" * 30,
                      "EAA" + "Bw" * 40,
                      'client_secret = "' + "q7" * 16 + '"'):
            with self.subTest(family=token[:4]):
                self.assertTrue(any(x.severity == "BLOCK" for x in guard.scan_added_line("fixture.md", token, 1)))
        self.assertFalse(any(x.severity == "BLOCK" for x in guard.scan_added_line(
            "fixture.md", "https://drive.google.com/file/d/FILE_ID", 1)))


class RecognizedMediaRegressionTests(unittest.TestCase):
    def test_magic_and_extension_both_required(self):
        import publication_guard as guard
        good = b"\x89PNG\r\n\x1a\n" + bytes(range(256))
        self.assertTrue(guard._has_valid_media_magic("fixture.png", good))
        self.assertFalse(guard._has_valid_media_magic("fixture.md", good))
        self.assertFalse(guard._has_valid_media_magic("fixture.png", b"\xff\xfe" + b"secret"))
        self.assertIn(("BLOCK", "NUL_IN_ADDED_CONTENT"),
                      [(v.severity, v.rule) for v in guard.scan_added_line("fixture.md", "x\x00y", 1)])
        self.assertNotIn(("BLOCK", "NUL_IN_ADDED_CONTENT"),
                         [(v.severity, v.rule) for v in guard.scan_added_line(
                             "fixture.png", "x\x00y", 1, verified_media=True)])
        token = "ghp_" + "X" * 36
        rules = guard.scan_added_line("fixture.png", "\x00" + token, 1, verified_media=True)
        self.assertTrue(any(v.rule == "GITHUB_TOKEN" and v.severity == "BLOCK" for v in rules))

    def test_staged_real_png_review_but_disguised_utf16_blocks(self):
        tmp, root, git, base = ClosedScopeCliRegressions()._repo()
        with tmp:
            # A structurally identified PNG is a review item, not a fake text exception.
            (root / "image.png").write_bytes(b"\x89PNG\r\n\x1a\n" + bytes(range(256)))
            git("add", "-A")
            result = ClosedScopeCliRegressions()._cli(root, "--staged")
            self.assertEqual(0, result.returncode, result.stdout)
            self.assertIn("BINARY_OR_MEDIA_REVIEW", result.stdout)
            git("reset", "-q")
            (root / "image.png").write_bytes(("ghp_" + "Z" * 36).encode("utf-16"))
            git("add", "-A")
            result = ClosedScopeCliRegressions()._cli(root, "--staged")
            self.assertEqual(1, result.returncode, result.stdout)


class HistoricalMediaAndDriveAcceptance(unittest.TestCase):
    def test_a_placeholder_word_outside_real_drive_identifier_cannot_exempt_link(self):
        from publication_guard import scan_added_line
        real = "https://drive.google.com/drive/folders/" + "Ab3" * 11
        findings = scan_added_line("notes.md", "EXAMPLE: " + real, 1)
        self.assertIn(("BLOCK", "DRIVE_RESOURCE_REFERENCE"),
                      [(finding.severity, finding.rule) for finding in findings])
        placeholder = "https://drive.google.com/drive/folders/EXAMPLE_" + "A" * 25
        findings = scan_added_line("notes.md", placeholder, 1)
        self.assertFalse(any(finding.severity == "BLOCK" for finding in findings))
        self.assertIn("LINK_INCOMPLETE_OR_PLACEHOLDER_IDENTIFIER",
                      [finding.rule for finding in findings])

    def test_historical_media_exemption_uses_each_commit_blob(self):
        test = ClosedScopeCliRegressions()
        tmp, root, git, base = test._repo()
        with tmp:
            image_path = root / "history.png"
            authentic = b"\x89PNG\r\n\x1a\n" + bytes(range(256))
            image_path.write_bytes(authentic)
            git("add", "-A"); git("commit", "-qm", "valid synthetic image")
            image_path.write_bytes("ordinary synthetic text".encode("utf-16"))
            git("add", "-A"); git("commit", "-qm", "disguised synthetic text")
            image_path.write_bytes(authentic)
            git("add", "-A"); git("commit", "-qm", "restore valid synthetic image")
            run = test._cli(root, "--range", base + "...HEAD",
                            "--history-range", base + "..HEAD")
            self.assertEqual(1, run.returncode, run.stdout)
            self.assertIn("NUL_IN_ADDED_CONTENT", run.stdout)

    def test_valid_historical_png_requires_review_without_false_nul_block(self):
        test = ClosedScopeCliRegressions()
        tmp, root, git, base = test._repo()
        with tmp:
            (root / "original.png").write_bytes(
                b"\x89PNG\r\n\x1a\n" + bytes(range(256)))
            git("add", "-A"); git("commit", "-qm", "add valid synthetic image")
            run = test._cli(root, "--range", base + "...HEAD",
                            "--history-range", base + "..HEAD")
            self.assertEqual(0, run.returncode, run.stdout)
            self.assertIn("BINARY_OR_MEDIA_REVIEW", run.stdout)
            self.assertNotIn("NUL_IN_ADDED_CONTENT", run.stdout)


class AccountScopedDriveAndGifAcceptance(unittest.TestCase):
    """Closed S-A6/S-A7 acceptance, with synthetic identifiers only."""

    def test_drive_resource_paths_require_block(self):
        root = "https://" + "drive.google.com/"
        docs = "https://" + "docs.google.com/"
        paths = (
            (root, "drive/folders/"),
            (root, "drive/u/0/folders/"),
            (root, "drive/u/1/folders/"),
            (root, "drive/mobile/folders/"),
            (root, "file/d/"),
            (root, "file/u/0/d/"),
            (docs, "document/d/"),
            (docs, "document/u/0/d/"),
            (docs, "spreadsheets/d/"),
            (docs, "spreadsheets/u/0/d/"),
            (docs, "presentation/d/"),
            (docs, "presentation/u/0/d/"),
            (root, "open?id="),
            (root, "uc?id="),
        )
        for host, route in paths:
            with self.subTest(route=route):
                link = host + route + "Ab3" * 11
                self.assertIn(
                    ("BLOCK", "DRIVE_RESOURCE_REFERENCE"),
                    rules(fake_patch(link)),
                )

    def test_short_and_long_placeholder_identifiers_stay_nonblocking(self):
        from publication_guard import scan_added_line
        host = "https://" + "drive.google.com/"
        examples = (
            host + "drive/u/0/folders/EXAMPLE_" + "A" * 24,
            host + "file/u/0/d/FILE_ID",
            host + "drive/mobile/folders/PLACEHOLDER_" + "B" * 20,
        )
        for link in examples:
            with self.subTest(route=link.split(host)[1][:28]):
                findings = scan_added_line("fixture.md", link, 1)
                self.assertFalse(any(f.severity == "BLOCK" for f in findings))

    def test_real_resource_after_placeholder_on_same_line_blocks(self):
        from publication_guard import scan_added_line
        host = "https://" + "drive.google.com/"
        placeholder = host + "file/d/EXAMPLE_" + "A" * 23
        real = host + "drive/u/0/folders/" + "Ab3" * 11
        matches = scan_added_line("fixture.md", placeholder + " and " + real, 1)
        self.assertIn(
            ("BLOCK", "DRIVE_RESOURCE_REFERENCE"),
            [(m.severity, m.rule) for m in matches],
        )
        self.assertIn(
            ("REVIEW", "LINK_INCOMPLETE_OR_PLACEHOLDER_IDENTIFIER"),
            [(m.severity, m.rule) for m in matches],
        )

    def test_account_scoped_drive_url_blocks_in_real_git_cli(self):
        test = ClosedScopeCliRegressions()
        tmp, root, git, base = test._repo()
        with tmp:
            link = ("https://" + "drive.google.com/drive/u/0/folders/"
                    + "Ab3" * 11)
            (root / "note.md").write_text(link)
            git("add", "-A")
            git("commit", "-qm", "synthetic resource reference")
            result = test._cli(root, "--range", base + "...HEAD",
                               "--history-range", base + "..HEAD")
            self.assertEqual(1, result.returncode, result.stdout)
            self.assertIn("DRIVE_RESOURCE_REFERENCE", result.stdout)
            self.assertNotIn(link, result.stdout)

    def test_recognized_gif_is_reviewed_without_nul_block(self):
        import publication_guard as guard
        self.assertTrue(guard._has_valid_media_magic(
            "synthetic.gif", b"GIF89a" + bytes(range(256))))
        test = ClosedScopeCliRegressions()
        tmp, root, git, base = test._repo()
        with tmp:
            path = root / "synthetic.gif"
            path.write_bytes(b"GIF89a" + bytes(range(256)))
            git("add", "-A")
            clean = test._cli(root, "--staged")
            self.assertEqual(0, clean.returncode, clean.stdout)
            self.assertIn("BINARY_OR_MEDIA_REVIEW", clean.stdout)
            self.assertNotIn("NUL_IN_ADDED_CONTENT", clean.stdout)

            path.write_bytes(("ghp_" + "S" * 36).encode("utf-16"))
            git("add", "-A")
            disguised = test._cli(root, "--staged")
            self.assertEqual(1, disguised.returncode, disguised.stdout)
            self.assertIn("NUL_IN_ADDED_CONTENT", disguised.stdout)

            path.write_bytes(b"GIF89a\n" + b"ghp_" + b"R" * 36)
            git("add", "-A")
            inside = test._cli(root, "--staged")
            self.assertEqual(1, inside.returncode, inside.stdout)
            self.assertIn("GITHUB_TOKEN", inside.stdout)
