# Publication Safety Guard · experimental candidate

**Scope:** Publication Safety Guard candidate. The acceptance state belongs to the reviewed ADR and repository owner; this README is not an operative merge decision. Historical V2.5 is immutable and Web 2.6 is maintained separately.

## The active S0 result

See [S0-STATUS](../docs/security/S0-STATUS.md) for the single sanitized closure statement. Historical working notes are deliberately superseded in HEAD and must not be used as alternative current statuses. S0 ended by owner attestation, not an exhaustive privacy certificate.

## What the scanner does

- `publication_guard.py` scans text **added** by a PR's final diff AND each commit in its range. Thus a token introduced and removed in a later commit is still detectable.
- It does not require a successfully parsed `+++ b/file` header to inspect added hunk lines. Handles accented and whitespace-containing paths, binary-only file names and unusual Unicode line separators; an unparseable destination is BLOCK, not silently skipped.
- Invalid UTF-8 produces a sanitized **REVIEW** while ASCII token patterns are still inspected. A Git subprocess failure returns **exit 2**; recognized secrets or dangerous diff-hiding attributes/NUL additions return **exit 1**. No token values or raw filenames appear in findings.
- `BLOCK`: recognizable secrets, signed URLs, private key material and private-file naming. `REVIEW`: ambiguous Drive links, potentially personal email or binary/media provenance needing classification. REVIEW does not automatically mean exposure.
- Text diffs use `--text --no-textconv` to prevent Git attributes and NUL bytes from hiding token patterns. Any residual uninspected binary patch is blocked. Media pixels, EXIF, licensing, malformed encodings and hidden source history still require manual review. This is defense in depth, not a security certification.

## Local preflight before committing

```sh
python security/publication_guard.py --staged --fail-on-warning
python -m unittest discover -s security -p 'test_*.py' -v
```

An example hook `security/pre-commit.example` can be integrated into existing local hooks after review. It is not automatically installed on a user's machine. For GitHub connector writes, inspect the *entire* new file before creating the commit; CI runs **after** initial publication.

## Pull request gate

```sh
python security/publication_guard.py \
  --range "origin/main...HEAD" \
  --history-range "origin/main..HEAD"
```

`.github/workflows/publication-guard.yml` executes the PR scan, with `fetch-depth: 0`, `persist-credentials: false` and a timeout. Note that PR code controls its own workflow definition, so the scanner targets accidental disclosure, not a malicious collaborator with write rights. Repository-level protected reviews/check configuration remains separately necessary.

## Independent global history audit

```sh
git fetch --no-tags --prune origin '+refs/heads/*:refs/remotes/origin/*'
python security/history_audit.py
```

The global historical scan runs **only on explicit workflow_dispatch/manual use**, not as a blocking dependency of unrelated PRs. It reports **audit incomplete (exit 2)** when it encounters skipped oversized, binary or non-UTF8 blobs; a zero exit code must not be claimed in that case. Full coverage of unreachable commits, forks, caches, media pixels, historical permissions and rights is not claimed. Private link/media triage remains local only.

## Follow-up required before merging PR #20

1. Independent CC verification of the real-Git accented-path, unusual separators, non-UTF8 and binary path regressions.
2. Review the slim [ADR-0003 candidate](../docs/decisions/ADR-0003-PROPOSED-development-review-and-publication-safety.md) against ADR-0001/0002 and obtain explicit owner approval.
3. Confirm false-positive handling of review-only references and that blocked diffs do not expose values.
4. Treat one stable Drive asset link still distributed in media documentation/registry as a separate **versioned `src/` inventory change**, coordinated with PR #17 and Manifest governance. No silent change to `main`.
5. Merging a public security gate does **not** grant API credentials, source rights, production or release authority.
