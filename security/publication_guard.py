"""Conservative pre-publication scan of ADDED Git diff lines.

No third-party dependencies or network. Does NOT audit Git history, GitHub
forks/caches, screenshots or permission status. Human review is still required.
Findings deliberately do not print matched secret values.
"""
from __future__ import annotations

import argparse
import base64
import binascii
import hashlib
from dataclasses import dataclass
import re
import shlex
import subprocess
import sys
from pathlib import PurePosixPath


@dataclass(frozen=True)
class Finding:
    severity: str  # BLOCK or REVIEW
    rule: str
    path: str
    added_line: int


BLOCK_RULES = (
    ("GITHUB_TOKEN", re.compile(r"(?<![A-Za-z0-9])(?:ghp_|gho_|ghu_|ghs_|ghr_)[A-Za-z0-9]{30,}(?![A-Za-z0-9])|(?<![A-Za-z0-9])github_pat_[A-Za-z0-9_]{40,}(?![A-Za-z0-9])")),
    ("SECRET_KEY", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b|\bsk_(?!live_)[A-Za-z0-9_]{24,}\b")),
    ("GOOGLE_API_KEY", re.compile(r"\bAIza[A-Za-z0-9_-]{35}\b")),
    ("STRIPE_LIVE_KEY", re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{20,}\b")),
    ("SLACK_TOKEN", re.compile(r"\bxox(?:b|p|s|a|r)-[A-Za-z0-9-]{24,}\b")),
    ("HUGGINGFACE_TOKEN", re.compile(r"\bhf_[A-Za-z0-9]{30,}\b")),
    ("NPM_TOKEN", re.compile(r"\bnpm_[A-Za-z0-9]{30,}\b")),

    ("GOOGLE_OAUTH_CLIENT_SECRET", re.compile(r"(?<![A-Za-z0-9])GOCSPX-[A-Za-z0-9_-]{20,}")),
    ("GOOGLE_OAUTH_ACCESS_TOKEN", re.compile(r"(?<![A-Za-z0-9])ya29\.[A-Za-z0-9._~-]{30,}")),
    ("GOOGLE_OAUTH_REFRESH_TOKEN", re.compile(r"(?<![A-Za-z0-9])1//[A-Za-z0-9._~-]{35,}")),
    ("META_ACCESS_TOKEN", re.compile(r"(?<![A-Za-z0-9])EAA[A-Za-z0-9]{45,}")),
    # Also common key names (api_key, x-api-key, token, secret) in env, JSON or header form (2026-10-30 audit).
    ("GENERIC_SECRET_ASSIGNMENT", re.compile(r"(?i)(?:client_secret|api_secret|refresh_token|access_token|password|api[_-]?key|x-api-key|secret[_-]?key|auth[_-]?token|(?<![a-z0-9_])token|(?<![a-z0-9_])secret)['\"]?\s*[:=]\s*['\\\"]?[A-Za-z0-9._/+~-]{24,}")),
    ("AWS_ACCESS_ID", re.compile(r"(?<![A-Za-z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Za-z0-9])")),
    # Also matches JSON/YAML quoting, e.g. "Authorization": "Bearer ..." (finding PR20-P2-4).
    ("BEARER_CREDENTIAL", re.compile(r"(?i)\bauthorization['\"]?\s*[:=]\s*['\"]?bearer\s+[A-Za-z0-9._~+/-]{24,}")),
    ("PRIVATE_KEY_PEM", re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----")),
    ("PGP_PRIVATE_KEY", re.compile(r"-----BEGIN PGP PRIVATE KEY[ ]BLOCK-----")),
    ("JWT", re.compile(r"(?<![A-Za-z0-9_-])eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    # user:password@host in any URL scheme; obvious placeholders are not credentials.
    ("CREDENTIALS_IN_URL", re.compile(
        r"(?i)\b[a-z][a-z0-9+.-]{1,20}://[^\s/:@'\"<>]{1,64}:"
        r"(?!(?:password|passwd|pass|secret|changeme|example|placeholder|x+|\*+)@)(?![<$%{])[^\s/@'\"<>]{6,}@[^\s/'\"<>]+")),
    ("SIGNED_ACCESS_URL", re.compile(r"(?i)(?:X-Amz-Signature|X-Goog-Signature)=[A-Za-z0-9%]{32,}")),
    ("SIGNED_QUERY_TOKEN", re.compile(r"(?i)(?:https?://[^\s<>'\"]{1,900}[?&](?:token|access_token|signature|sig|auth)=)[A-Za-z0-9%._~-]{24,}")),
)
REVIEW_RULES = (
    ("DRIVE_REFERENCE", re.compile(r"https?://(?:drive|docs)\.google\.com/(?:(?:file(?:/u/\d+)?/d|drive(?:(?:/u/\d+|/mobile))?/folders|document(?:/u/\d+)?/d|spreadsheets(?:/u/\d+)?/d|presentation(?:/u/\d+)?/d)/[A-Za-z0-9_-]{18,}|(?:open|uc)\?id=[A-Za-z0-9_-]{18,})", re.I)),
    ("SHAREABLE_STORAGE_LINK", re.compile(r"https?://[^\s<>'\"]{1,300}/(?:share|sharing|download)/[^\s<>'\"]{10,}", re.I)),
    # A local home folder names the owner's account and machine layout (owner-environment detail).
    ("LOCAL_HOME_PATH", re.compile(r"(?<![A-Za-z0-9])(?:/Users|/home)/(?!(?:you|user|username|name|me|runner|someone|example)[/\s])[A-Za-z][A-Za-z0-9._-]{1,30}/")),
)

EMAIL_CANDIDATE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
_RESERVED_SAMPLE_DOMAINS = frozenset({"example.com", "example.net", "example.org"})


def has_reviewable_email(text: str) -> bool:
    """Report possible personal emails but ignore documentation-only domains."""
    for match in EMAIL_CANDIDATE.finditer(text):
        domain = match.group(0).rsplit("@", 1)[1].lower()
        if domain in _RESERVED_SAMPLE_DOMAINS:
            continue
        if domain.endswith((".invalid", ".example", ".test", ".localhost", ".noreply.github.com")):
            continue
        if domain.endswith("@users.noreply.github.com"):
            continue
        return True
    return False


PRIVATE_FILENAME = re.compile(
    r"(?i)(?:^|/)(?:\.env(?:\.(?!example$|sample$|template$|dist$)[\w-]+)?|"
    r"\.npmrc|\.netrc|\.git-credentials|id_(?:rsa|ed25519|ecdsa)|token\.(?:json|pickle)|(?:\.aws/)?credentials|"
    r"(?:client_secret[^/]*|credentials?)\.(?:json|ya?ml)|"
    r"[^/]+\.tfstate(?:\.backup)?|"
    r"(?:secrets?|private|credentials?)/[^/]+\.(?:p12|pfx|pem|key|db|sqlite)|"
    r"[^/]*(?:private|secret|credential|token)[^/]*\.(?:p12|pfx|pem|key|db|sqlite)|"
    r"[^/]+\.(?:p12|pfx))$"
)
REVIEW_FILE_SUFFIXES = (".zip", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".heic", ".heif", ".mov", ".mp4", ".key", ".pem", ".db", ".sqlite",
                        ".tif", ".tiff", ".webm", ".docx", ".xlsx", ".pptx")
DIFF_FILE = re.compile(r"^\+\+\+ b/(.+)$")
# The suffix alone is never enough to exempt NUL-containing content.
RECOGNIZED_MEDIA_SUFFIXES = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".mp4", ".mov", ".heic", ".tif", ".tiff", ".webm")


def _has_valid_media_magic(path: str, data: bytes) -> bool:
    suffix = PurePosixPath(path.lower()).suffix
    if suffix == ".png":
        return data.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in (".jpg", ".jpeg"):
        return data.startswith(b"\xff\xd8\xff")
    if suffix == ".gif":
        return data.startswith((b"GIF87a", b"GIF89a"))
    if suffix == ".webp":
        return data.startswith(b"RIFF") and data[8:12] == b"WEBP"
    if suffix == ".pdf":
        return data.startswith(b"%PDF-")
    if suffix in (".tif", ".tiff"):
        return data.startswith((b"II*\x00", b"MM\x00*"))
    if suffix == ".webm":
        return data.startswith(b"\x1a\x45\xdf\xa3")
    if suffix in (".mp4", ".mov", ".heic"):
        return len(data) >= 12 and data[4:8] == b"ftyp" and (
            suffix != ".heic" or data[8:12] in (b"heic", b"heix", b"hevc", b"mif1"))
    return False


def _verified_media_paths(ns: argparse.Namespace, metadata: list[Finding] | None = None) -> set[str]:
    # Read the actual staged/HEAD blob, not a filename or a Git diff rendering.
    command = ["git", "diff"]
    if ns.staged:
        command.append("--cached")
    command += ["--name-only", "-z"]
    if ns.range:
        command.append(ns.range)
    command.append("--")
    names = _run_git(command)
    valid = set()
    for raw in names.split(b"\x00"):
        if not raw:
            continue
        name = raw.decode("utf-8", errors="replace")
        if PurePosixPath(name.lower()).suffix not in RECOGNIZED_MEDIA_SUFFIXES:
            continue
        blobref = ":" + name if ns.staged else "HEAD:" + name
        try:
            content = _run_git(["git", "show", blobref])
        except RuntimeError:
            # A claimed media filename without inspectable bytes gets NO exception.
            continue
        if _has_valid_media_magic(name, content):
            valid.add(name)
            if metadata is not None:
                metadata.extend(media_metadata_findings(name, content))
    return valid


def _verified_media_paths_at_commit(commit: str) -> frozenset[str]:
    """Media exemptions in history belong to the exact historical blob.

    HEAD's current signature does not validate an older version of a file.
    A missing or undecodable historical blob gets no NUL exemption.
    """
    names = _run_git([
        "git", "-c", "core.quotePath=false", "show", "--format=",
        "--name-only", "-z", "--diff-merges=remerge", commit, "--",
    ])
    valid: set[str] = set()
    for raw in names.split(b"\x00"):
        if not raw:
            continue
        try:
            name = raw.decode("utf-8").strip("\n")
        except UnicodeDecodeError:
            continue
        if PurePosixPath(name.lower()).suffix not in RECOGNIZED_MEDIA_SUFFIXES:
            continue
        try:
            blob = _run_git(["git", "show", commit + ":" + name])
        except RuntimeError:
            # Deleted files or inaccessible blobs never acquire exemptions.
            continue
        if _has_valid_media_magic(name, blob):
            valid.add(name)
    return frozenset(valid)


def _scan_commit_history(range_ref: str) -> list[Finding]:
    """Inspect every commit patch with media verified at that commit, not HEAD."""
    commits = _run_git(["git", "rev-list", "--reverse", range_ref, "--"])
    findings: list[Finding] = []
    for raw in commits.splitlines():
        try:
            commit = raw.decode("ascii")
        except UnicodeDecodeError as exc:
            raise RuntimeError("Invalid Git commit identifier; inspection incomplete") from exc
        if re.fullmatch(r"[0-9a-f]{40,64}", commit) is None:
            raise RuntimeError("Invalid Git commit identifier; inspection incomplete")
        patch_bytes = _run_git([
            "git", "-c", "core.quotePath=false", "show", "--format=",
            "--diff-merges=remerge", "--text", "--no-textconv",
            "--no-ext-diff", "--no-color", "--unified=0", commit, "--",
        ])
        patch, issues = _decode_inspected_bytes(patch_bytes, "<git-commits>")
        findings.extend(issues)
        findings.extend(scan_unified_diff(
            patch, verified_media_paths=_verified_media_paths_at_commit(commit)
        ))
    return findings


BASE64_RUN = re.compile(r"[A-Za-z0-9+/_-]{40,4096}={0,2}")


def _base64_hidden_secrets(path: str, line: str, line_number: int) -> list[Finding]:
    """Finding PR20-P2-2: a token encoded as base64 (standard or URL-safe) is still a token."""
    found = []
    for match in BASE64_RUN.finditer(line):
        raw = match.group(0).rstrip("=").replace("-", "+").replace("_", "/")
        try:
            decoded = base64.b64decode(raw + "=" * (-len(raw) % 4)).decode("ascii")
        except (binascii.Error, ValueError, UnicodeDecodeError):
            continue
        for name, rx in BLOCK_RULES:
            if rx.search(decoded):
                found.append(Finding("BLOCK", "BASE64_" + name, path, line_number))
                break
    return found


def scan_added_line(path: str, line: str, line_number: int, *, verified_media: bool = False) -> list[Finding]:
    findings = []
    # Git --text exposes UTF-16-style data as interleaved NUL bytes. Treat
    # these as suspicious and also inspect the de-NUL'd ASCII token stream.
    if "\x00" in line:
        if not verified_media:
            findings.append(Finding("BLOCK", "NUL_IN_ADDED_CONTENT", path, line_number))
        line = line.replace("\x00", "").replace("\ufffd", "").replace("\ufeff", "")
    # A Git attribute can hide arbitrary text from the diff renderer. This
    # should not be published without a separate explicit review.
    if path.endswith("/.gitattributes") or path == ".gitattributes":
        rule = re.search(r"(?i)(?:^|\s)(?:-diff|binary|diff=[^\s]+)(?:\s|$)", line)
        if rule:
            findings.append(Finding("BLOCK", "DIFF_ATTRIBUTE_HIDES_CONTENT", path, line_number))
    for name, rx in BLOCK_RULES:
        if rx.search(line):
            findings.append(Finding("BLOCK", name, path, line_number))
    findings += _base64_hidden_secrets(path, line, line_number)
    for name, rx in REVIEW_RULES:
        # Check every matched resource: a harmless fixture must not hide
        # a real Drive link later on the same added line.
        for match in rx.finditer(line):
            if name == "DRIVE_REFERENCE":
                # Only the matched identifier may qualify as a placeholder.
                identifier_match = re.search(
                    r"(?i)(?:/(?:d|folders)/|[?&]id=)([A-Za-z0-9_-]+)",
                    match.group(0),
                )
                identifier = identifier_match.group(1) if identifier_match else ""
                is_placeholder = re.fullmatch(
                    r"(?i)(?:EXAMPLE|PLACEHOLDER|FILE_ID|FOLDER_ID|YOUR|FAKE)"
                    r"(?:[_-][A-Z0-9_-]+)?", identifier,
                ) is not None
                if is_placeholder:
                    findings.append(Finding("REVIEW", "LINK_INCOMPLETE_OR_PLACEHOLDER_IDENTIFIER", path, line_number))
                else:
                    findings.append(Finding("BLOCK", "DRIVE_RESOURCE_REFERENCE", path, line_number))
            else:
                findings.append(Finding("REVIEW", name, path, line_number))
    if has_reviewable_email(line):
        findings.append(Finding("REVIEW", "EMAIL_ADDRESS", path, line_number))
    return findings


def _destination_from_git_header(line: str) -> str | None:
    """Read the destination even for binary-only diffs with no +++ header.

    Git quotes unusual paths in diff headers. If parsing is ambiguous, the
    scanner must report REVIEW rather than silently skip the entire file.
    """
    try:
        words = shlex.split(line)
    except ValueError:
        return None
    if (len(words) == 4 and words[:2] == ["diff", "--git"]
            and words[2].startswith("a/") and words[3].startswith("b/")):
        return words[3][2:]
    # Git with core.quotePath=false may emit an *unquoted* path with spaces.
    # Only recover an unambiguous single a/ ... b/ pair. Ambiguity is BLOCK
    # at the call site and added hunk lines are still inspected.
    prefix = "diff --git a/"
    if line.startswith(prefix) and line.count(" b/") == 1:
        return line.split(" b/", 1)[1]
    return None


_JOIN_TAIL = " \t\\\"'+,"
_JOIN_HEAD = " \t\"'+"


def _join(parts: list[str]) -> str:
    out = parts[0]
    for part in parts[1:]:
        out = out.rstrip(_JOIN_TAIL) + part.lstrip(_JOIN_HEAD)
    return out


def _split_token_findings(path: str, window: list[str], line_number: int) -> list[Finding]:
    """Finding PR20-P2-2: a token split across two or three consecutive added lines
    (string concatenation or line continuation) is still a token. A rule is reported
    only if it matches the whole window and no shorter run of it, so nothing is counted twice."""
    joined = _join(window)
    shorter = [window[i:j] for i in range(len(window)) for j in range(i + 1, len(window) + 1) if j - i < len(window)]
    found = []
    for name, rx in BLOCK_RULES:
        if rx.search(joined) and not any(rx.search(_join(run)) for run in shorter):
            found.append(Finding("BLOCK", "SPLIT_" + name, path, line_number))
    return found


def media_metadata_findings(path: str, content: bytes) -> list[Finding]:
    """Finding PR20-P1-5: added media with EXIF or text metadata needs review before
    publication (location, device or identifying values). Labels only; no values."""
    from history_audit import classify_binary_metadata
    kinds = classify_binary_metadata(content)
    risky = sorted(k for k in kinds if "EXIF" in k or "PNG_METADATA" in k or "LINK" in k)
    return [Finding("REVIEW", "MEDIA_METADATA_REVIEW", path, 0)] if risky else []


def scan_unified_diff(patch: str, *, verified_media_paths: frozenset[str] = frozenset()) -> list[Finding]:
    """Scan every added hunk line, even if a filename cannot be decoded.

    Git textual diffs quote unusual paths, sometimes using octal byte escapes.
    Never make scanning the *content* contingent on decoding a +++ filename.
    An ambiguous path is BLOCK, not an ignored warning.
    """
    results: list[Finding] = []
    destination: str | None = None
    deleted = False
    in_hunk = False
    line_no = 0
    previous_added: list[str] = []
    seen_file_checks: set[tuple[str, str]] = set()

    def check_destination(value: str) -> None:
        if PRIVATE_FILENAME.search(value) and (value, "PRIVATE_FILE_PATH") not in seen_file_checks:
            results.append(Finding("BLOCK", "PRIVATE_FILE_PATH", value, 0))
            seen_file_checks.add((value, "PRIVATE_FILE_PATH"))
        if value.lower().endswith(REVIEW_FILE_SUFFIXES) and (value, "BINARY_OR_MEDIA_REVIEW") not in seen_file_checks:
            results.append(Finding("REVIEW", "BINARY_OR_MEDIA_REVIEW", value, 0))
            seen_file_checks.add((value, "BINARY_OR_MEDIA_REVIEW"))

    for raw in patch.split("\n"):
        # Splitting only at LF is essential: str.splitlines() would silently
        # skip a token following form feed, vertical tab or U+2028.
        line = raw.removesuffix("\r")
        if line.startswith("diff --git "):
            if destination is not None and not deleted:
                check_destination(destination)
            destination = _destination_from_git_header(line)
            if destination is None:
                destination = "<unparsed-git-path>"
                results.append(Finding("BLOCK", "UNPARSEABLE_DIFF_HEADER", destination, 0))
            deleted = False
            in_hunk = False
            line_no = 0
            continue
        # An added literal '+++ /dev/null' inside an active hunk is data.
        # Check it before interpreting file headers; do not let an attacker
        # suppress the rest of the hunk with a crafted added line.
        if in_hunk and line.startswith("+"):
            line_no += 1
            results.extend(scan_added_line(destination or "<unknown-file>", line[1:], line_no,
                                           verified_media=destination in verified_media_paths))
            for size in (1, 2):
                if len(previous_added) >= size:
                    results.extend(_split_token_findings(destination or "<unknown-file>", previous_added[-size:] + [line[1:]], line_no))
            previous_added = (previous_added + [line[1:]])[-2:]
            continue
        previous_added = []
        if line.startswith("deleted file mode ") or line == "+++ /dev/null":
            deleted = True
            in_hunk = False
            continue
        if line.startswith("+++ "):
            quoted = line[4:]
            if quoted.startswith('"'):
                try:
                    fields = shlex.split(quoted)
                    if len(fields) == 1 and fields[0].startswith("b/"):
                        destination = fields[0][2:]
                    else:
                        results.append(Finding("BLOCK", "UNPARSEABLE_DESTINATION", "<unparsed-git-path>", 0))
                except ValueError:
                    results.append(Finding("BLOCK", "UNPARSEABLE_DESTINATION", "<unparsed-git-path>", 0))
            elif quoted.startswith("b/"):
                destination = quoted[2:]
            elif quoted != "/dev/null":
                results.append(Finding("BLOCK", "UNPARSEABLE_DESTINATION", "<unparsed-git-path>", 0))
            continue
        if line.startswith("@@ "):
            in_hunk = True
            continue
        if (line.startswith("Binary files ") or line.startswith("GIT binary patch")
                or line.startswith("literal ") or line.startswith("delta ")):
            results.append(Finding("BLOCK", "UNINSPECTED_BINARY_DIFF",
                                   destination or "<binary-file>", 0))
            continue
    if destination is not None and not deleted:
        check_destination(destination)
    return results


def _run_git(command: list[str]) -> bytes:
    """Execute a bounded Git read without exposing stdout/stderr on failure."""
    try:
        return subprocess.run(
            command, capture_output=True, check=True, timeout=30
        ).stdout
    except (subprocess.SubprocessError, OSError) as exc:
        raise RuntimeError("Git inspection unavailable; scan NOT performed") from exc


def _decode_inspected_bytes(raw: bytes, scope: str) -> tuple[str, list[Finding]]:
    """Recover ASCII secret patterns in mixed-encoding text without skipping scan.

    Invalid UTF-8 is an explicit REVIEW, not a silently successful scan or a
    subprocess failure. Replacement cannot erase ordinary ASCII token bytes.
    """
    decoded = raw.decode("utf-8", errors="replace")
    issues = [Finding("REVIEW", "NON_UTF8_CONTENT", scope, 0)] if "\ufffd" in decoded else []
    return decoded, issues


def _diff_args(*, staged: bool = False, range_ref: str | None = None) -> list[str]:
    command = ["git", "-c", "core.quotePath=false", "diff"]
    if staged:
        command.append("--cached")
    command += ["--text", "--no-textconv", "--no-ext-diff", "--no-color", "--unified=0"]
    if range_ref:
        command.append(range_ref)
    return command + ["--"]


def _get_diff(args: argparse.Namespace) -> str:
    # Kept independently callable for local pre-commit hooks and tests.
    return _decode_inspected_bytes(
        _run_git(_diff_args(staged=args.staged, range_ref=args.range)),
        "<git-diff>"
    )[0]


def _scan_path_list(raw: bytes, scope: str) -> list[Finding]:
    decoded, issues = _decode_inspected_bytes(raw, scope)
    out = list(issues)
    for path in decoded.split("\x00"):
        path = path.strip("\n")
        if not path:
            continue
        out.extend(scan_added_line(scope, path, 0))
        if PRIVATE_FILENAME.search(path):
            out.append(Finding("BLOCK", "PRIVATE_FILE_PATH", scope, 0))
    return out


def _octopus_findings(range_ref: str) -> list[Finding]:
    commits = _run_git(["git", "rev-list", "--min-parents=3", range_ref, "--"])
    return ([Finding("BLOCK", "OCTOPUS_MERGE_UNINSPECTED", "<git-history>", 0)]
            if commits.strip() else [])


def _metadata_findings(range_ref: str) -> list[Finding]:
    """Review PR commit messages and new filenames, never echoing raw values."""
    results: list[Finding] = []
    base = ["git", "-c", "core.quotePath=false"]
    messages = _run_git(base + [
        "log", "--no-patch", "--format=%B%x00", range_ref, "--"
    ])
    text, issues = _decode_inspected_bytes(messages, "<git-commit-metadata>")
    results.extend(issues)
    for message in text.split("\x00"):
        if message:
            results.extend(scan_added_line("<git-commit-metadata>", message, 0))

    # Both final state and each individual commit are scanned. The -z format
    # makes path handling unambiguous even with tabs and embedded newlines.
    for command in (
        base + ["diff", "--name-only", "-z", range_ref.replace("..", "...", 1) if "..." not in range_ref else range_ref, "--"],
        base + ["log", "--format=", "--name-only", "-z", range_ref, "--"],
    ):
        raw = _run_git(command)
        text, issues = _decode_inspected_bytes(raw, "<git-path-metadata>")
        results.extend(issues)
        for path in text.split("\x00"):
            path = path.strip("\n")
            if not path:
                continue
            results.extend(scan_added_line("<git-path-metadata>", path, 0))
            if PRIVATE_FILENAME.search(path):
                results.append(Finding("BLOCK", "PRIVATE_FILE_PATH", "<git-path-metadata>", 0))
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Scan publication changes without printing values")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true")
    mode.add_argument("--range", metavar="BASE...HEAD")
    ap.add_argument("--history-range", metavar="BASE..HEAD")
    ap.add_argument("--fail-on-warning", action="store_true")
    ns = ap.parse_args(argv)
    try:
        # IMPORTANT: these are two different Git operations. A history range
        # must never replace the final-tree diff. Merge-only additions are
        # included by git diff even when log misses them.
        final_text = _get_diff(ns)
        findings = ([Finding("REVIEW", "NON_UTF8_CONTENT", "<git-diff>", 0)]
                    if "\ufffd" in final_text else [])
        media_metadata: list[Finding] = []
        verified_media_paths = frozenset(_verified_media_paths(ns, media_metadata))
        findings.extend(scan_unified_diff(final_text, verified_media_paths=verified_media_paths))
        findings.extend(media_metadata)
        if ns.staged:
            # Staged paths are not necessarily present in a text hunk.
            findings.extend(_scan_path_list(_run_git([
                "git", "diff", "--cached", "--name-only", "-z", "--"
            ]), "<staged-git-paths>"))
        if ns.history_range:
            if _octopus_findings(ns.history_range):
                # An uninspectable merge is incomplete, not proof of a leaked secret.
                print("OCTOPUS_MERGE_UNINSPECTED: Git history inspection incomplete", file=sys.stderr)
                return 2
            # Never re-use HEAD's media signature to exempt historical NUL.
            findings.extend(_scan_commit_history(ns.history_range))
            findings.extend(_metadata_findings(ns.history_range))
        elif ns.range:
            findings.extend(_metadata_findings(ns.range.replace("...", "..", 1)))
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    blockers = sum(f.severity == "BLOCK" for f in findings)
    warnings = sum(f.severity == "REVIEW" for f in findings)
    for item in findings:
        # Never reveal the path or matching value in CI.
        path_ref = hashlib.sha256(item.path.encode("utf-8")).hexdigest()[:12]
        print(f"{item.severity}: {item.rule} path_ref={path_ref} (added-line {item.added_line})")
    print(f"Publication guard: {blockers} BLOCK, {warnings} REVIEW. "
          "Final diff, commit patches and metadata scanned when requested; manual media review still required.")
    return 1 if blockers or (warnings and ns.fail_on_warning) else 0


if __name__ == "__main__":
    raise SystemExit(main())
