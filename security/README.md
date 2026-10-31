# Publication Safety Guard

**Scope:** the publication safety guard of [ADR-0003](../docs/decisions/ADR-0003-PROPOSED-development-review-and-publication-safety.md), accepted by the owner on 2026-10-30 (PR #42). This README is not an operative merge decision. Historical V2.5 is immutable and Web 2.6 is maintained separately.

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

## Follow-up items from PR #20 (status 2026-10-30)

1. Real-Git regressions for accented paths, unusual separators, non-UTF8 and binary paths: done (finding ADR3-1).
2. [ADR-0003](../docs/decisions/ADR-0003-PROPOSED-development-review-and-publication-safety.md): accepted by the owner on 2026-10-30.
3. False-positive handling of review-only references, and blocked diffs not exposing values: covered by the guard tests.
4. The stable Drive asset link in `src/` media documentation and registry: replaced by candidate `privacy-redaction-v1` (#35).
5. Merging a public security gate does **not** grant API credentials, source rights, production or release authority.

## Local hook and mutation check (2026-10-30)

- `python3 security/install_hooks.py` installs a pre-push hook that runs the guard on every commit being pushed and stops the push on BLOCK. `--check` reports whether it is installed. GitHub API and connector writes bypass local hooks; the required CI check covers them.
- `python3 security/mutation_check.py --report security/mutation-report.md` disables each rule in turn and requires the test suite to fail. Current score: 28 of 28 killed.
- A PR that adds media or binary files fails `scan-publication-diff` unless its description has a line `Media reviewed: ...`.

## Workflow supply chain and meaning-level privacy (2026-10-30)

- The repository setting "require SHA pinning" is on: a workflow that uses an Action by tag or branch fails to start. `python3 -m brain status` re-checks the setting. `.github/dependabot.yml` opens weekly PRs that move the pins to newer releases; the owner merges them.
- Meaning-level privacy (account, environment, client or personal details written in prose) has no automated check. The owner accepted this as a known risk: the PR template checklist is the control.

## 2026-10-30 audit fixes

- The base-branch scan runs with `shell: bash` (pipefail), so a BLOCK fails the step instead of being lost in `| tee`. It runs before any PR code and uses the base commit SHA from the event.
- `brain-records` also validates the PR's records with the base commit's `brain/` code, for the same reason.
- New detection: common key names (`api_key`, `x-api-key`, `token`, `secret`) with key-like values, `sk_` keys, tokens split across three lines, and local home-folder paths (REVIEW).
- Known limits: a PR can still edit the workflow files themselves (the control is owner-only merges); PR bodies and comments are not scanned. See `FND-AUDIT-WORKFLOW-EDIT` and `FND-AUDIT-DETECTION-REST` in the Brain.
