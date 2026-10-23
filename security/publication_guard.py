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
    ("AWS_ACCESS_ID", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("BEARER_CREDENTIAL", re.compile(r"(?i)\bauthorization\s*[:=]\s*bearer\s+[A-Za-z0-9._~+/-]{24,}")),
    ("PRIVATE_KEY_PEM", re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----")),
    ("SIGNED_ACCESS_URL", re.compile(r"(?i)(?:X-Amz-Signature|X-Goog-Signature)=[A-Za-z0-9%]{32,}")),
    ("SIGNED_QUERY_TOKEN", re.compile(r"(?i)(?:https?://[^\s<>'\"]{1,900}[?&](?:token|access_token|signature|sig|auth)=)[A-Za-z0-9%._~-]{24,}")),
)
REVIEW_RULES = (
    ("DRIVE_REFERENCE", re.compile(r"https?://(?:drive|docs)\.google\.com/(?:file|drive|document|spreadsheets|presentation)/", re.I)),
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
    r"[^/]+\.(?:p12|pfx|key|pem|sqlite|db))$"
)
REVIEW_FILE_SUFFIXES = (".zip", ".pdf", ".png", ".jpg", ".jpeg", ".webp", ".mov", ".mp4")
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
    if (len(words) != 4 or words[:2] != ["diff", "--git"]
            or not words[2].startswith("a/") or not words[3].startswith("b/")):
        return None
    return words[3][2:]


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
        if in_hunk and line.startswith("+"):
            line_no += 1
            results.extend(scan_added_line(destination or "<unknown-file>", line[1:], line_no))
    if destination is not None and not deleted:
        check_destination(destination)
    return results


def _get_diff(args: argparse.Namespace) -> str:
    # core.quotePath=false avoids octal UTF-8 escapes for ordinary accented
    # names. Quoted names with spaces still require explicit parsing.
    cmd = ["git", "-c", "core.quotePath=false", "diff"]
    if args.staged:
        cmd += ["--cached"]
    cmd += ["--no-ext-diff", "--no-color", "--unified=0"]
    if args.range:
        cmd += [args.range]
    cmd += ["--"]
    try:
        raw = subprocess.run(cmd, capture_output=True, check=True, timeout=30).stdout
        return raw.decode("utf-8", "strict")
    except (UnicodeDecodeError, subprocess.SubprocessError, OSError) as exc:
        # Exit 2 is an operational failure. Never report this as a BLOCK scan,
        # and never echo undecodable bytes from exceptions.
        raise RuntimeError("Git diff unavailable or not UTF-8; scan NOT performed") from exc


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Scan added Git diff lines without revealing matched secret values")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="Pre-commit check staged additions")
    mode.add_argument("--range", metavar="BASE...HEAD", help="Check all additions in branch compared to base")
    ap.add_argument("--fail-on-warning", action="store_true", help="Manually opt to fail also for REVIEW items")
    ns = ap.parse_args(argv)
    try:
        findings = scan_unified_diff(_get_diff(ns))
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    blockers = sum(f.severity == "BLOCK" for f in findings)
    warnings = sum(f.severity == "REVIEW" for f in findings)
    for item in findings:
        # Never echo source line, matched secret OR raw filename: a filename
        # can contain an email, project identifier or a secret of its own.
        # Reconcile path_ref against the local diff in a private review.
        path_ref = hashlib.sha256(item.path.encode("utf-8")).hexdigest()[:12]
        print(f"{item.severity}: {item.rule} path_ref={path_ref} (added-line {item.added_line})")
    print(f"Publication guard: {blockers} BLOCK, {warnings} REVIEW. "
          "Scan covers added textual diff only; manual review still required.")
    return 1 if blockers or (warnings and ns.fail_on_warning) else 0


if __name__ == "__main__":
    raise SystemExit(main())
