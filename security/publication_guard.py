"""Conservative pre-publication scan of ADDED Git diff lines.

No third-party dependencies or network. Does NOT audit Git history, GitHub
forks/caches, screenshots or permission status. Human review is still required.
Findings deliberately do not print matched secret values.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import re
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
    return findings


def scan_unified_diff(patch: str) -> list[Finding]:
    """Scan additions only, including new filenames; never echo the match."""
    results: list[Finding] = []
    path: str | None = None
    line_no = 0
    seen_file_checks: set[tuple[str, str]] = set()
    for raw in patch.splitlines():
        m = DIFF_FILE.match(raw)
        if m:
            path = m.group(1)
            line_no = 0
            if PRIVATE_FILENAME.search(path) and (path, "PRIVATE_FILE_PATH") not in seen_file_checks:
                results.append(Finding("BLOCK", "PRIVATE_FILE_PATH", path, 0))
                seen_file_checks.add((path, "PRIVATE_FILE_PATH"))
            if path.lower().endswith(REVIEW_FILE_SUFFIXES) and (path, "BINARY_OR_MEDIA_REVIEW") not in seen_file_checks:
                results.append(Finding("REVIEW", "BINARY_OR_MEDIA_REVIEW", path, 0))
                seen_file_checks.add((path, "BINARY_OR_MEDIA_REVIEW"))
            continue
        if raw.startswith("diff --git "):
            path = None
            continue
        if raw.startswith("+++ ") or raw.startswith("--- ") or raw.startswith("\\ No newline"):
            continue
        if path and raw.startswith("+"):
            line_no += 1
            results.extend(scan_added_line(path, raw[1:], line_no))
    return results


def _get_diff(args: argparse.Namespace) -> str:
    if args.staged:
        cmd = ["git", "diff", "--cached", "--no-ext-diff", "--no-color", "--unified=0", "--"]
    else:
        cmd = ["git", "diff", "--no-ext-diff", "--no-color", "--unified=0", args.range, "--"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=30)
        return result.stdout
    except (subprocess.SubprocessError, OSError) as exc:
        raise RuntimeError("Git diff unavailable; pre-publication scan was NOT performed") from exc


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
        # Neither source line nor matching secret appears in CI or local logs.
        # The path is a path already in the public Git diff; users must still
        # review potentially private filenames before publication.
        print(f"{item.severity}: {item.rule} in {item.path} (added-line {item.added_line})")
    print(f"Publication guard: {blockers} BLOCK, {warnings} REVIEW. "
          "Scan covers added textual diff only; manual review still required.")
    return 1 if blockers or (warnings and ns.fail_on_warning) else 0


if __name__ == "__main__":
    raise SystemExit(main())
