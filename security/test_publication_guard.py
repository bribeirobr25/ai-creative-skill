"""Tests for the reusable prepublication scanner.

Synthetic token examples are assembled at runtime so no secrets are committed.
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from publication_guard import scan_added_line, scan_unified_diff, main
from history_audit import audit_text_blob


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

    def test_drive_link_requires_review_not_automatic_block(self):
        link = "https://" + "drive.google.com/file/d/" + "1" * 30 + "/view"
        self.assertIn(("REVIEW", "DRIVE_REFERENCE"), rules(fake_patch(link)))
        self.assertFalse(any(x[0] == "BLOCK" for x in rules(fake_patch(link))))

    def test_docs_link_requires_review(self):
        link = "https://" + "docs.google.com/document/d/" + "a" * 30 + "/edit"
        self.assertIn(("REVIEW", "DRIVE_REFERENCE"), rules(fake_patch(link)))

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
        link = "https://" + "docs.google.com/document/d/" + "D" * 31 + "/edit"
        with patch("publication_guard._get_diff", return_value=fake_patch(link)):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(0, main(["--staged"]))

    def test_warning_can_be_strict(self):
        link = "https://" + "docs.google.com/document/d/" + "D" * 31 + "/edit"
        with patch("publication_guard._get_diff", return_value=fake_patch(link)):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(1, main(["--staged", "--fail-on-warning"]))

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

    def test_git_error_not_success(self):
        with patch("publication_guard._get_diff", side_effect=RuntimeError("Git diff unavailable")):
            with patch("sys.stderr", new_callable=io.StringIO):
                self.assertEqual(2, main(["--staged"]))


if __name__ == "__main__":
    unittest.main()
