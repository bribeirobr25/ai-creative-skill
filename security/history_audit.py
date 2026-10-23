"""Read-only audit of Git objects reachable from refs currently fetched locally.

Scans ALL reachable text blob versions (not just HEAD) for recognizable
secret and sharing-link patterns. Summary counts only: NO matched values,
source text, URLs, paths, blob hashes, filenames or snippets are printed.

This is an auxiliary security signal, NOT a certification that all private
information is absent: images, binary payloads, obfuscation, inaccessible
branches, forks, unreachable commits, server logs and linguistic PII remain.
"""
from __future__ import annotations

from collections import Counter
import subprocess
import sys

from publication_guard import BLOCK_RULES, REVIEW_RULES, PRIVATE_FILENAME, REVIEW_FILE_SUFFIXES

MAX_TEXT_BLOB_BYTES = 2_000_000
MAX_BLOB_COUNT = 50000


def git(cmd: list[str], stdin: bytes | None = None) -> bytes:
    try:
        return subprocess.run(
            ["git", *cmd], input=stdin, check=True,
            capture_output=True, timeout=120,
        ).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as exc:
        raise RuntimeError("Cannot inspect local Git object history safely") from exc


def _reachable_blobs() -> tuple[dict[str, str], dict[str, int]]:
    lines = git(["rev-list", "--objects", "--all"]).decode("utf-8", "replace").splitlines()
    items: dict[str, str] = {}
    for line in lines:
        key, _, path = line.partition(" ")
        if key:
            items.setdefault(key, path)
    if len(items) > MAX_BLOB_COUNT:
        raise RuntimeError("Object inventory exceeds review cap; refusing partial green status")
    if not items:
        raise RuntimeError("Empty reachable Git object inventory")
    payload = "".join(key + "\n" for key in items).encode()
    info = git(["cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)"], stdin=payload)
    types = {}
    sizes = {}
    for ln in info.decode("utf-8", "replace").splitlines():
        parts = ln.split()
        if len(parts) == 3 and parts[1] == "blob":
            sizes[parts[0]] = int(parts[2])
            types[parts[0]] = parts[1]
    paths = {oid: path for oid, path in items.items() if oid in types}
    return paths, sizes


def audit_text_blob(text: str, path: str) -> set[str]:
    """Return only rule/category names, never offending text or token."""
    found: set[str] = set()
    for name, pat in BLOCK_RULES:
        if pat.search(text):
            found.add("BLOCK:" + name)
    for name, pat in REVIEW_RULES:
        if pat.search(text):
            found.add("REVIEW:" + name)
    # path classification can be useful, but suppress actual paths in output.
    if PRIVATE_FILENAME.search(path):
        found.add("BLOCK:PRIVATE_FILE_PATH")
    if path.lower().endswith(REVIEW_FILE_SUFFIXES):
        found.add("REVIEW:BINARY_OR_MEDIA_PATH")
    return found


def audit_commit_metadata() -> dict[str, int]:
    """Scan reachable commit messages and author addresses without logging them."""
    out: Counter[str] = Counter()
    raw = git(["log", "--all", "--format=%B%x00"]).decode("utf-8", "replace")
    messages = [s for s in raw.split("\0") if s.strip()]
    out["SCANNED_COMMIT_MESSAGES"] = len(messages)
    for message in messages:
        for category in audit_text_blob(message, ""):
            out["COMMIT_" + category] += 1
    authors = git(["log", "--all", "--format=%ae"]).decode("utf-8", "replace").splitlines()
    emails = {v.strip().casefold() for v in authors if v.strip()}
    # Git commit author email can be personal data even though git hosts
    # display it. Noreply addresses and generic localhost examples are omitted.
    for mail in emails:
        if not (mail.endswith("@users.noreply.github.com") or mail.endswith("@noreply.github.com")
                or mail.endswith("@localhost") or mail.endswith("@example.com")):
            out["REVIEW:COMMIT_AUTHOR_EMAIL"] += 1
    return dict(out)


def classify_binary_metadata(raw: bytes) -> set[str]:
    """Categorize signatures/metadata only; no pixel analysis or extraction."""
    kinds: set[str] = set()
    head = raw[:262144]
    if raw.startswith(b"\xff\xd8\xff"):
        kinds.add("BINARY_JPEG")
        if b"Exif\x00\x00" in head:
            kinds.add("BINARY_EXIF_PRESENT")
        if b"http://" in head or b"https://" in head:
            kinds.add("BINARY_TEXT_URL_PRESENT")
    elif raw.startswith(b"\x89PNG\r\n\x1a\n"):
        kinds.add("BINARY_PNG")
        if any(label in head for label in (b"tEXt", b"zTXt", b"iTXt", b"eXIf")):
            kinds.add("BINARY_PNG_METADATA_PRESENT")
    elif raw.startswith(b"%PDF"):
        kinds.add("BINARY_PDF")
        if b"/URI" in head or b"/JavaScript" in head:
            kinds.add("BINARY_PDF_LINK_OR_SCRIPT_MARKER")
    elif raw.startswith((b"PK\x03\x04", b"PK\x05\x06")):
        kinds.add("BINARY_ZIP")
    elif len(head) >= 12 and head[4:8] == b"ftyp":
        kinds.add("BINARY_ISOBMFF_MP4_OR_MOV")
    elif raw.startswith(b"GIF8"):
        kinds.add("BINARY_GIF")
    elif raw.startswith(b"RIFF"):
        kinds.add("BINARY_RIFF")
    else:
        kinds.add("BINARY_UNKNOWN_OR_OTHER")
    return kinds


def _verified_branch_coverage() -> int:
    """Require every current remote public branch tip to be fetched.

    The CI fetches all refs/heads first. If refs are missing or stale, fail
    closed rather than reporting an incomplete history as clean.
    """
    remote_raw = git(["ls-remote", "--heads", "origin"]).decode("utf-8", "replace")
    local_raw = git([
        "for-each-ref",
        "--format=%(refname:strip=3) %(objectname)",
        "refs/remotes/origin",
    ]).decode("utf-8", "replace")
    remote: dict[str, str] = {}
    for item in remote_raw.splitlines():
        bits = item.split()
        if len(bits) != 2 or not bits[1].startswith("refs/heads/"):
            raise RuntimeError("Invalid remote branch listing")
        remote[bits[1][len("refs/heads/"):]] = bits[0]
    local: dict[str, str] = {}
    for item in local_raw.splitlines():
        bits = item.split()
        if len(bits) == 2:
            local[bits[0]] = bits[1]
    if not remote or any(local.get(key) != sha for key, sha in remote.items()):
        raise RuntimeError("Historical scan incomplete: public branch heads not all fetched")
    return len(remote)


def scan_history() -> dict:
    """Conservative scan: every readable reachable blob version within cap."""
    branch_count = _verified_branch_coverage()
    paths, sizes = _reachable_blobs()
    summary = Counter()
    summary["VERIFIED_REMOTE_BRANCH_HEADS"] = branch_count
    for oid, path in paths.items():
        size = sizes[oid]
        if size > MAX_TEXT_BLOB_BYTES:
            summary["SKIPPED_OVERSIZED_BLOB"] += 1
            if PRIVATE_FILENAME.search(path):
                summary["BLOCK:PRIVATE_FILE_PATH"] += 1
            if path.lower().endswith(REVIEW_FILE_SUFFIXES):
                summary["REVIEW:BINARY_OR_MEDIA_PATH"] += 1
            continue
        raw = git(["cat-file", "blob", oid])
        if b"\0" in raw:
            summary["SKIPPED_BINARY_BLOB"] += 1
            for kind in classify_binary_metadata(raw):
                summary[kind] += 1
            if PRIVATE_FILENAME.search(path):
                summary["BLOCK:PRIVATE_FILE_PATH"] += 1
            if path.lower().endswith(REVIEW_FILE_SUFFIXES):
                summary["REVIEW:BINARY_OR_MEDIA_PATH"] += 1
            continue
        try:
            value = raw.decode("utf-8")
        except UnicodeDecodeError:
            summary["SKIPPED_NON_UTF8_BLOB"] += 1
            continue
        summary["SCANNED_TEXT_BLOB"] += 1
        for category in audit_text_blob(value, path):
            summary[category] += 1
    summary["REACHABLE_BLOB_VERSIONS"] = len(paths)
    summary.update(audit_commit_metadata())
    return dict(sorted(summary.items()))


def main() -> int:
    try:
        counts = scan_history()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print("Read-only Git history audit (reachable refs; sanitized counts only):")
    for label, value in counts.items():
        print(f"  {label}: {value}")
    print("Not a complete privacy certification: manual binary/rights/history review required.")
    blockers = sum(v for k, v in counts.items() if k.startswith("BLOCK:") or k.startswith("COMMIT_BLOCK:"))
    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
