"""Conservative pre-publication scan of ADDED Git diff lines.

No third-party dependencies or network. Does NOT audit Git history, GitHub
forks/caches, screenshots or permission status. Human review is still required.
Findings deliberately do not print matched secret values.
"""
from __future__ import annotations

import argparse
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
    ("GITHUB_TOKEN", re.compile(r"\b(?:ghp_|gho_|ghu_|ghs_|ghr_)[A-Za-z0-9]{30,}\b|\bgithub_pat_[A-Za-z0-9_]{40,}\b")),
    ("SECRET_KEY", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b")),
    ("GOOGLE_API_KEY", re.compile(r"\bAIza[A-Za-z0-9_-]{35}\b")),
    ("STRIPE_LIVE_KEY", re.compile(r"\b(?:sk|rk)_live_[A-Za-z0-9]{20,}\b")),
    ("SLACK_TOKEN", re.compile(r"\bxox(?:b|p|s|a|r)-[A-Za-z0-9-]{24,}\b")),
    ("HUGGINGFACE_TOKEN", re.compile(r"\bhf_[A-Za-z0-9]{30,}\b")),
    ("NPM_TOKEN", re.compile(r"\bnpm_[A-Za-z0-9]{30,}\b")),

    ("AWS_ACCESS_ID", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("BEARER_CREDENTIAL", re.compile(r"(?i)\bauthorization\s*[:=]\s*bearer\s+[A-Za-z0-9._~+/-]{24,}")),
    ("PRIVATE_KEY_PEM", re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----")),
    ("SIGNED_ACCESS_URL", re.compile(r"(?i)(?:X-Amz-Signature|X-Goog-Signature)=[A-Za-z0-9%]{32,}")),
    ("SIGNED_QUERY_TOKEN", re.compile(r"(?i)(?:https?://[^\s<>'\"]{1,900}[?&](?:token|access_token|signature|sig|auth)=)[A-Za-z0-9%._~-]{24,}")),
)
REVIEW_RULES = (
    ("DRIVE_REFERENCE", re.compile(r"https?://(?:drive|docs)\.google\.com/(?:(?:file|drive|document|spreadsheets|presentation|u)/|(?:open|uc)\?id=)", re.I)),
    ("SHAREABLE_STORAGE_LINK", re.compile(r"https?://[^\s<>'\"]{1,300}/(?:share|sharing|download)/[^\s<>'\"]{10,}", re.I)),
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
    r"(?i)(?:^|/)(?:\.env(?:\.[\w-]+)?|id_(?:rsa|ed25519)|credentials?\.(?:json|ya?ml)|"
    r"(?:secrets?|private|credentials?)/[^/]+\.(?:p12|pfx|pem|key|db|sqlite)|"
    r"[^/]*(?:private|secret|credential|token)[^/]*\.(?:p12|pfx|pem|key|db|sqlite)|"
    r"[^/]+\.(?:p12|pfx))$"
)
REVIEW_FILE_SUFFIXES = (".zip", ".pdf", ".png", ".jpg", ".jpeg", ".webp", ".heic", ".heif", ".mov", ".mp4", ".key", ".pem", ".db", ".sqlite")
DIFF_FILE = re.compile(r"^\+\+\+ b/(.+)$")


def scan_added_line(path: str, line: str, line_number: int) -> list[Finding]:
    findings = []
    for name, rx in BLOCK_RULES:
        if rx.search(line):
            findings.append(Finding("BLOCK", name, path, line_number))
    for name, rx in REVIEW_RULES:
        if rx.search(line):
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


def scan_unified_diff(patch: str) -> list[Finding]:
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
            results.extend(scan_added_line(destination or "<unknown-file>", line[1:], line_no))
            continue
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
    command += ["--no-ext-diff", "--no-color", "--unified=0"]
    if range_ref:
        command.append(range_ref)
    return command + ["--"]


def _get_diff(args: argparse.Namespace) -> str:
    # Kept independently callable for local pre-commit hooks and tests.
    return _decode_inspected_bytes(
        _run_git(_diff_args(staged=args.staged, range_ref=args.range)),
        "<git-diff>"
    )[0]


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
        final_bytes = _run_git(_diff_args(staged=ns.staged, range_ref=ns.range))
        final_text, findings = _decode_inspected_bytes(final_bytes, "<git-diff>")
        findings.extend(scan_unified_diff(final_text))
        if ns.history_range:
            historical_bytes = _run_git([
                "git", "-c", "core.quotePath=false", "log", "--patch",
                "--diff-merges=first-parent", "--format=", "--no-ext-diff",
                "--no-color", "--unified=0", ns.history_range, "--"
            ])
            history_text, decode_issues = _decode_inspected_bytes(historical_bytes, "<git-commits>")
            findings.extend(decode_issues)
            findings.extend(scan_unified_diff(history_text))
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
