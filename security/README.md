# Publication Safety Guard · experimental candidate

**Status:** PR #20 DRAFT. ADR-0003 proposed, not accepted or merged. `main`, V2.5 and PR #17 unchanged.

## The active S0 result

See [S0-STATUS](../docs/security/S0-STATUS.md) for the single sanitized closure statement. Historical working notes are deliberately superseded in HEAD and must not be used as alternative current statuses. S0 ended by owner attestation, not an exhaustive privacy certificate.

## What the scanner does

- `publication_guard.py` scans text **added** by a PR's final diff AND each commit in its range. Thus a token introduced and removed in a later commit is still detectable.
- It does not require a successfully parsed `+++ b/file` header to inspect added hunk lines. Handles accented and whitespace-containing paths, binary-only file names and unusual Unicode line separators; an unparseable destination is BLOCK, not silently skipped.
- Undecodable diff bytes are **operational failure (exit 2)**, distinct from a detected BLOCK (exit 1). No filenames, token values, URLs or source lines are shown in guard findings.
- `BLOCK`: recognizable secrets, signed URLs, private key material and private-file naming. `REVIEW`: ambiguous Drive links, potentially personal email or binary/media provenance needing classification. REVIEW does not automatically mean exposure.
- This is defense in depth, **not** safe handling of all malware, secrets, media frames, encoded payloads or contractual rights. Binary payloads remain a manual review requirement.

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

The global historical scan runs **only on explicit workflow_dispatch/manual use**, not as a blocking dependency of unrelated PRs. Full coverage of unreachable commits, forks, caches, media pixels, historical permissions and rights is not claimed. Private link/media triage remains `private_triage.py`, local only, never GitHub Actions.

## Follow-up required before merging PR #20

1. Independent CC verification of the real-Git accented-path, unusual separators, non-UTF8 and binary path regressions.
2. Review the slim [ADR-0003 candidate](../docs/decisions/ADR-0003-PROPOSED-development-review-and-publication-safety.md) against ADR-0001/0002 and obtain explicit owner approval.
3. Confirm false-positive handling of review-only references and that blocked diffs do not expose values.
4. Treat one stable Drive asset link still distributed in media documentation/registry as a separate **versioned `src/` inventory change**, coordinated with PR #17 and Manifest governance. No silent change to `main`.
5. Merging a public security gate does **not** grant API credentials, source rights, production or release authority.
