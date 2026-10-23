"""LOCAL-ONLY private triage of historical links and reviewable media.

Never runs in CI. Writes raw link candidates ONLY to a restrictive temporary
directory outside the repository. The JSON is NOT safe to upload to GitHub,
a chat, or a public artifact. It does not evaluate Google Drive permissions.
Requires a local Git clone with all current public heads fetched.

CLI: python security/private_triage.py
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import tempfile

from history_audit import (
    MAX_TEXT_BLOB_BYTES, _reachable_blobs, _verified_branch_coverage,
    classify_binary_metadata, classify_link_metadata, git,
)

_DRIVE_URL = re.compile(r"""https?://(?:drive|docs)\.google\.com/[^\s<>"')]{1,1200}""", re.I)
_ALL_URL = re.compile(r"""https?://[^\s<>"')]{4,1200}""", re.I)
_SHARE_SHAPE = re.compile(r"/(?:share|sharing|download)/.{10,}", re.I)


def _inside_repo(target: Path, repo_root: Path) -> bool:
    try:
        target.resolve().relative_to(repo_root.resolve())
        return True
    except ValueError:
        return False


def link_candidates_from_text(content: str) -> set[str]:
    """Return candidates for PRIVATE review. Never call this in CI logs."""
    links = set(_DRIVE_URL.findall(content))
    for match in _ALL_URL.findall(content):
        if _SHARE_SHAPE.search(match):
            links.add(match)
    return links


def produce_private_triage() -> dict:
    if os.environ.get("CI") or os.environ.get("GITHUB_ACTIONS"):
        raise RuntimeError("Private triage is forbidden in CI/public runners")
    repo_root = Path(git(["rev-parse", "--show-toplevel"]).decode().strip())
    _verified_branch_coverage()
    paths_by_sha, sizes = _reachable_blobs()
    links: dict[str, dict] = {}
    media: list[dict] = []
    for blob_sha, aliases in paths_by_sha.items():
        if sizes[blob_sha] > MAX_TEXT_BLOB_BYTES:
            media.append({"category": "OVERSIZED", "paths": sorted(aliases)})
            continue
        raw = git(["cat-file", "blob", blob_sha])
        if b"\0" in raw:
            media.append({
                "category": "BINARY",
                "paths": sorted(aliases),
                "flags": sorted(classify_binary_metadata(raw)),
            })
            continue
        try:
            plain = raw.decode("utf-8")
        except UnicodeDecodeError:
            media.append({"category": "NON_UTF8", "paths": sorted(aliases)})
            continue
        for url in link_candidates_from_text(plain):
            item = links.setdefault(url, {
                "url": url,
                "risk_categories": sorted(classify_link_metadata(url)),
                "paths": set(),
            })
            item["paths"].update(aliases)
    # Do not stringify absolute paths/URL data in public CI or PR review.
    clean_links = [
        {"url": url, "risk_categories": row["risk_categories"], "paths": sorted(row["paths"])}
        for url, row in sorted(links.items())
    ]
    raw_emails = git(["log", "--all", "--format=%ae"]).decode("utf-8", "replace").splitlines()
    candidate_emails = sorted({
        addr.strip() for addr in raw_emails
        if addr.strip() and not (
            addr.endswith("@users.noreply.github.com")
            or addr.endswith("@noreply.github.com")
            or addr.endswith("@example.com")
            or addr.endswith("@localhost")
        )
    })
    return {
        "status": "PRIVATE_REVIEW_REQUIRED",
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "source": "LOCAL_GIT_REACHABLE_REFS",
        "raw_links": clean_links,
        "candidate_commit_author_addresses": candidate_emails,
        "binary_objects_needing_manual_review": media,
        "note": "This is a confidential local review input, not a publication-safe report.",
    }


def write_private_file(data: dict, destination: Path | None = None) -> Path:
    if os.environ.get("CI") or os.environ.get("GITHUB_ACTIONS"):
        raise RuntimeError("Refusing to write private findings in CI")
    repo_root = Path(git(["rev-parse", "--show-toplevel"]).decode().strip()).resolve()
    if destination is None:
        safe_dir = Path(tempfile.mkdtemp(prefix="acs-security-private-"))
        os.chmod(safe_dir, 0o700)
        target = safe_dir / "review.json"
    else:
        target = destination.expanduser().resolve()
        if _inside_repo(target, repo_root):
            raise RuntimeError("Destination inside Git repository is forbidden")
        # Never chmod an existing directory such as /tmp or the user's home.
        # Require a private destination directory; create it when absent.
        if not target.parent.exists():
            target.parent.mkdir(mode=0o700, parents=True)
            os.chmod(target.parent, 0o700)
        elif os.stat(target.parent).st_mode & 0o077:
            raise RuntimeError("Destination directory is not private (mode 0700 required)")
    fd = os.open(str(target), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    except BaseException:
        target.unlink(missing_ok=True)
        raise
    return target


def main() -> int:
    if os.environ.get("CI") or os.environ.get("GITHUB_ACTIONS"):
        print("Private review is deliberately disabled in CI")
        return 2
    try:
        result = produce_private_triage()
        output = write_private_file(result)
    except (RuntimeError, OSError, ValueError) as exc:
        # Avoid including underlying exception text: it could contain private data.
        print("Private review could not be generated; no success claimed")
        return 2
    # Local output only: never run this command in GitHub Actions or log upload.
    print(f"Local private review written to: {output}")
    print(f"Link candidates: {len(result['raw_links'])}; "
          f"binary objects: {len(result['binary_objects_needing_manual_review'])}; "
          f"possible author emails: {len(result['candidate_commit_author_addresses'])}")
    print("Do NOT upload the file to GitHub, public CI, chat, or shared storage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
