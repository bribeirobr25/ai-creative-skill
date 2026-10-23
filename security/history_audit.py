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


def _reachable_blobs() -> tuple[dict[str, set[str]], dict[str, int]]:
    """Map every reachable blob to ALL its paths in reachable commit trees.

    git rev-list --objects --all reports only one path hint per object. That is
    insufficient for privacy triage if the same content occurs under multiple
    paths. Inspect every reachable commit tree instead, de-duplicate by SHA.
    """
    commits = git(["rev-list", "--all"]).decode("ascii", "strict").splitlines()
    if not commits or len(commits) > 10000:
        raise RuntimeError("Commit inventory empty or beyond review cap")
    item_paths: dict[str, set[str]] = {}
    for commit in commits:
        entries = git(["ls-tree", "-r", "-z", commit])
        for row in entries.split(b"\x00"):
            if not row:
                continue
            try:
                meta, raw_path = row.split(b"\t", 1)
                parts = meta.split()
                if len(parts) != 3:
                    raise ValueError
                kind = parts[1]
                blob_sha = parts[2].decode("ascii")
                file_path = raw_path.decode("utf-8", "replace")
            except (ValueError, UnicodeDecodeError) as exc:
                raise RuntimeError("Unexpected commit-tree entry format") from exc
            if kind != b"blob":
                continue
            item_paths.setdefault(blob_sha, set()).add(file_path)
            if len(item_paths) > MAX_BLOB_COUNT:
                raise RuntimeError("Blob history exceeds review cap")
    if not item_paths:
        raise RuntimeError("Empty reachable Git blob inventory")
    payload = "".join(key + "\n" for key in item_paths).encode()
    info = git(["cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)"], stdin=payload)
    sizes = {}
    for ln in info.decode("utf-8", "replace").splitlines():
        parts = ln.split()
        if len(parts) != 3 or parts[1] != "blob":
            raise RuntimeError("A reachable blob could not be verified")
        sizes[parts[0]] = int(parts[2])
    if len(sizes) != len(item_paths):
        raise RuntimeError("Blob inventory size mismatch")
    return item_paths, sizes

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
        expected_id = None
        if "/folders/" in path:
            kinds.add("LINK_DRIVE_FOLDER")
            expected_id = path.split("/folders/", 1)[-1].split("/", 1)[0]
        elif "/document/d/" in path or "/spreadsheets/d/" in path or "/presentation/d/" in path:
            kinds.add("LINK_DRIVE_NATIVE_DOCUMENT")
            expected_id = path.split("/d/", 1)[-1].split("/", 1)[0]
        elif "/file/d/" in path:
            kinds.add("LINK_DRIVE_FILE")
            expected_id = path.split("/file/d/", 1)[-1].split("/", 1)[0]
        else:
            kinds.add("LINK_DRIVE_OTHER")
        # A literal tutorial prefix like /file/d/ is not a resolvable
        # resource. Plausible ID shape is NOT permission verification.
        if expected_id is not None and (
            len(expected_id) < 12 or not re.fullmatch(r"[a-z0-9_-]+", expected_id)
        ):
            kinds.add("LINK_INCOMPLETE_OR_PLACEHOLDER_IDENTIFIER")
        if "resourcekey" in params or "key" in params:
            kinds.add("LINK_WITH_ACCESS_HINT_NEEDS_PRIVATE_REVIEW")
        if {"token", "access_token", "signature", "sig"} & params:
            kinds.add("LINK_WITH_AUTH_QUERY_NEEDS_PRIVATE_REVIEW")
        if any(x in path for x in ("/file_id", "/folder_id", "/document_id", "/example/")):
            kinds.add("LINK_POSSIBLE_PLACEHOLDER")
    return kinds


def _link_fingerprints(text: str) -> dict[str, set[str]]:
    """Return in-memory fingerprints for counting distinct URLs only.

    Never persist or print fingerprints: even digests of guessable URLs may
    reveal information through a dictionary attack. No actual URL is logged.
    """
    import hashlib
    import re
    result: dict[str, set[str]] = {"DRIVE": set(), "GENERIC_SHARE": set()}
    drive = re.findall(
        r"""https?://(?:drive|docs)\.google\.com/[^\s<>"')]{1,1200}""",
        text, flags=re.I,
    )
    shared = re.findall(
        r"""https?://[^\s<>"')]{1,1200}/(?:share|sharing|download)/[^\s<>"')]{1,1200}""",
        text, flags=re.I,
    )
    for category, urls in (("DRIVE", drive), ("GENERIC_SHARE", shared)):
        for url in urls:
            normalized = url.rstrip(".,;")
            result[category].add(hashlib.sha256(normalized.encode("utf-8")).hexdigest())
    return result


def _generic_share_host_types(text: str) -> dict[str, set[str]]:
    """Group link hashes into host classes without logging URLs or identifiers."""
    import re
    import hashlib
    from urllib.parse import urlsplit
    result: dict[str, set[str]] = {"PUBLIC_GITHUB": set(), "GOOGLE_STORAGE": set(), "OTHER": set()}
    links = re.findall(
        r"""https?://[^\s<>"')]{1,1200}/(?:share|sharing|download)/[^\s<>"')]{1,1200}""",
        text, flags=re.I,
    )
    for url in links:
        try:
            host = (urlsplit(url).hostname or "").lower()
        except ValueError:
            host = ""
        bucket = (
            "PUBLIC_GITHUB" if host in ("github.com", "www.github.com")
            else "GOOGLE_STORAGE" if host in ("drive.google.com", "docs.google.com")
            else "OTHER"
        )
        result[bucket].add(hashlib.sha256(url.rstrip(".,;").encode("utf-8")).hexdigest())
    return result


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
    distinct_links: dict[str, set[str]] = {"DRIVE": set(), "GENERIC_SHARE": set()}
    generic_host_classes: dict[str, set[str]] = {"PUBLIC_GITHUB": set(), "GOOGLE_STORAGE": set(), "OTHER": set()}
    summary["MULTIPATH_BLOB_VERSIONS"] = sum(len(aliases) > 1 for aliases in paths.values())
    summary["REACHABLE_PATH_ALIASES"] = sum(len(aliases) for aliases in paths.values())
    for oid, aliases in paths.items():
        size = sizes[oid]
        if any(PRIVATE_FILENAME.search(path) for path in aliases):
            summary["BLOCK:PRIVATE_FILE_PATH"] += 1
        if any(path.lower().endswith(REVIEW_FILE_SUFFIXES) for path in aliases):
            summary["REVIEW:BINARY_OR_MEDIA_PATH"] += 1
        if size > MAX_TEXT_BLOB_BYTES:
            summary["SKIPPED_OVERSIZED_BLOB"] += 1
            continue
        raw = git(["cat-file", "blob", oid])
        if b"\0" in raw:
            summary["SKIPPED_BINARY_BLOB"] += 1
            flags = classify_binary_metadata(raw)
            for kind in flags:
                summary[kind] += 1
            if "BINARY_EXIF_POTENTIAL_IDENTIFYING_TAG" in flags:
                exif_sensitive_paths.update(aliases)
            continue
        try:
            value = raw.decode("utf-8")
        except UnicodeDecodeError:
            summary["SKIPPED_NON_UTF8_BLOB"] += 1
            continue
        summary["SCANNED_TEXT_BLOB"] += 1
        fingerprints = _link_fingerprints(value)
        for category, hashes in fingerprints.items():
            distinct_links[category].update(hashes)
        for category, hashes in _generic_share_host_types(value).items():
            generic_host_classes[category].update(hashes)
        for flag in classify_link_metadata(value):
            summary[flag] += 1
        for category in audit_text_blob(value, ""):
            summary[category] += 1
            if category in ("REVIEW:DRIVE_REFERENCE", "REVIEW:SHAREABLE_STORAGE_LINK"):
                for scope in {_scope_bucket(path) for path in aliases}:
                    summary["LINK_SCOPE:" + scope] += 1
    summary["REACHABLE_BLOB_VERSIONS"] = len(paths)
    summary["UNIQUE_PATHS_WITH_EXIF_IDENTIFYING_TAG"] = len(exif_sensitive_paths)
    summary["UNIQUE_DRIVE_URL_STRINGS"] = len(distinct_links["DRIVE"])
    summary["UNIQUE_GENERIC_SHARE_URL_STRINGS"] = len(distinct_links["GENERIC_SHARE"])
    for host_class, hashes in generic_host_classes.items():
        summary["GENERIC_SHARE_HOST:" + host_class] = len(hashes)
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
