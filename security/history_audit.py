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


def _exif_tag_categories(payload: bytes) -> set[str]:
    """Read only IFD tag IDs, never their values, from a bounded TIFF block."""
    results: set[str] = set()
    exif_pos = payload.find(b"Exif\x00\x00")
    if exif_pos < 0:
        return results
    tiff = payload[exif_pos + 6:]
    if len(tiff) < 8 or tiff[:2] not in (b"II", b"MM"):
        return {"BINARY_EXIF_UNPARSEABLE"}
    order = "little" if tiff[:2] == b"II" else "big"

    def number(a: bytes) -> int:
        return int.from_bytes(a, order)

    if number(tiff[2:4]) != 42:
        return {"BINARY_EXIF_UNPARSEABLE"}
    pointers = [number(tiff[4:8])]
    visited: set[int] = set()
    while pointers:
        offset = pointers.pop()
        if offset in visited:
            continue
        visited.add(offset)
        if offset < 8 or offset + 2 > len(tiff):
            results.add("BINARY_EXIF_UNPARSEABLE")
            continue
        entries = number(tiff[offset:offset + 2])
        if entries > 512 or offset + 2 + entries * 12 > len(tiff):
            results.add("BINARY_EXIF_UNPARSEABLE")
            continue
        for idx in range(entries):
            item = tiff[offset + 2 + idx * 12:offset + 14 + idx * 12]
            tag = number(item[:2])
            if tag == 0x8825:
                results.add("BINARY_EXIF_GPS_POINTER")
            if tag in (0x013B, 0x8298, 0xA430, 0xA431, 0x9286, 0x010E):
                results.add("BINARY_EXIF_POTENTIAL_IDENTIFYING_TAG")
            if tag == 0x8769 and number(item[2:4]) == 4 and number(item[4:8]) == 1:
                pointers.append(number(item[8:12]))
    return results


def _embedded_link_categories(payload: bytes) -> set[str]:
    """Classify URI hosts in metadata without emitting URIs or identifiers."""
    import re
    from urllib.parse import urlsplit
    found: set[str] = set()
    raw_urls = re.findall(rb"https?://[^\x00-\x20'\"<>]{4,320}", payload[:262144])
    for raw in raw_urls:
        try:
            hostname = urlsplit(raw.decode("ascii", "ignore")).hostname or ""
        except ValueError:
            hostname = ""
        if hostname in ("ns.adobe.com", "www.w3.org", "purl.org"):
            found.add("BINARY_STANDARD_METADATA_NAMESPACE")
        elif hostname in ("drive.google.com", "docs.google.com"):
            found.add("BINARY_DRIVE_REFERENCE_NEEDS_REVIEW")
        else:
            found.add("BINARY_OTHER_EMBEDDED_URL_NEEDS_REVIEW")
    return found


def classify_binary_metadata(raw: bytes) -> set[str]:
    """Categorize signatures/metadata only; no pixel analysis or extraction."""
    kinds: set[str] = set()
    head = raw[:262144]
    if raw.startswith(b"\xff\xd8\xff"):
        kinds.add("BINARY_JPEG")
        if b"Exif\x00\x00" in head:
            kinds.add("BINARY_EXIF_PRESENT")
            kinds.update(_exif_tag_categories(head))
        kinds.update(_embedded_link_categories(head))
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


def classify_link_metadata(text: str) -> set[str]:
    """Classify public-repository links by *shape*; never reveal URL or ID.

    This is a lexical pre-screen. It does NOT determine Google Drive sharing
    permissions, whether a link is valid, or whether it confers access.
    """
    import re
    from urllib.parse import urlsplit, parse_qsl
    kinds: set[str] = set()
    matches = re.findall(
        r"""https?://(?:drive|docs)\.google\.com/[^\s<>"')]{1,1200}""",
        text, flags=re.I,
    )
    for candidate in matches:
        try:
            url = urlsplit(candidate)
            path = url.path.casefold()
            params = {key.casefold() for key, _ in parse_qsl(url.query)}
        except ValueError:
            kinds.add("LINK_DRIVE_PARSE_REVIEW")
            continue
        if "/folders/" in path:
            kinds.add("LINK_DRIVE_FOLDER")
        elif "/document/d/" in path or "/spreadsheets/d/" in path or "/presentation/d/" in path:
            kinds.add("LINK_DRIVE_NATIVE_DOCUMENT")
        elif "/file/d/" in path:
            kinds.add("LINK_DRIVE_FILE")
        else:
            kinds.add("LINK_DRIVE_OTHER")
        if "resourcekey" in params or "key" in params:
            kinds.add("LINK_WITH_ACCESS_HINT_NEEDS_PRIVATE_REVIEW")
        if {"token", "access_token", "signature", "sig"} & params:
            kinds.add("LINK_WITH_AUTH_QUERY_NEEDS_PRIVATE_REVIEW")
        if any(x in path for x in ("/file_id", "/folder_id", "/document_id", "/example/")):
            kinds.add("LINK_POSSIBLE_PLACEHOLDER")
    return kinds


def _scope_bucket(path: str) -> str:
    """Broad, non-identifying origin bucket for manual review planning."""
    if path.startswith("docs/research/"):
        return "RESEARCH"
    if path.startswith("docs/migration/"):
        return "MIGRATION"
    if path.startswith("validation/"):
        return "VALIDATION"
    if path.startswith(("security/", "tests/")):
        return "TESTS"
    if path.startswith("src/"):
        return "SOURCE"
    return "OTHER"


def scan_history() -> dict:
    """Conservative scan: every readable reachable blob version within cap."""
    branch_count = _verified_branch_coverage()
    paths, sizes = _reachable_blobs()
    summary = Counter()
    summary["VERIFIED_REMOTE_BRANCH_HEADS"] = branch_count
    exif_sensitive_paths: set[str] = set()
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
            flags = classify_binary_metadata(raw)
            for kind in flags:
                summary[kind] += 1
            if "BINARY_EXIF_POTENTIAL_IDENTIFYING_TAG" in flags:
                exif_sensitive_paths.add(path)
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
        link_flags = classify_link_metadata(value)
        for flag in link_flags:
            summary[flag] += 1
        for category in audit_text_blob(value, path):
            summary[category] += 1
            if category in ("REVIEW:DRIVE_REFERENCE", "REVIEW:SHAREABLE_STORAGE_LINK"):
                summary["LINK_SCOPE:" + _scope_bucket(path)] += 1
    summary["REACHABLE_BLOB_VERSIONS"] = len(paths)
    summary["UNIQUE_PATHS_WITH_EXIF_IDENTIFYING_TAG"] = len(exif_sensitive_paths)
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
