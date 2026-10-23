"""Tests for the reusable prepublication scanner.

Synthetic token examples are assembled at runtime so no secrets are committed.
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from publication_guard import scan_added_line, scan_unified_diff, main
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
        self.assertIn(("REVIEW", "UNPARSEABLE_DIFF_HEADER"), rules(diff))

    def test_two_binary_files_reviewed_separately(self):
        diff = (
            "diff --git a/one.jpg b/one.jpg\\n"
            "Binary files /dev/null and b/one.jpg differ\\n"
            "diff --git a/two.png b/two.png\\n"
            "Binary files /dev/null and b/two.png differ\\n"
        ).replace("\\n", "\n")
        self.assertEqual(2, sum(rule == "BINARY_OR_MEDIA_REVIEW" for _, rule in rules(diff)))

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
                return b"example subject\\x00"
            if args == ["log", "--all", "HEAD", "--format=%ae"]:
                return b"bot@users.noreply.github.com\\n"
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
        link = "https://" + "docs.google.com/document/d/" + "D" * 31 + "/edit"
        with patch("publication_guard._get_diff", return_value=fake_patch(link)):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(0, main(["--staged"]))

    def test_warning_can_be_strict(self):
        link = "https://" + "docs.google.com/document/d/" + "D" * 31 + "/edit"
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

    def test_git_error_not_success(self):
        with patch("publication_guard._get_diff", side_effect=RuntimeError("Git diff unavailable")):
            with patch("sys.stderr", new_callable=io.StringIO):
                self.assertEqual(2, main(["--staged"]))


if __name__ == "__main__":
    unittest.main()
