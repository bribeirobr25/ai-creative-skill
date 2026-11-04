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

The global historical scan runs **only on explicit manual use** (the `history-audit` job in `.github/workflows/history-audit.yml`), not as a blocking dependency of unrelated PRs; the `brain-records` and `scan-publication-diff` required checks run only on pull requests, so a manual run can never report them (the V2.5 integrity and boundary-hardening checks in `validate.yml` can also run manually or on push). It reports **audit incomplete (exit 2)** when it encounters skipped oversized, binary or non-UTF8 blobs; a zero exit code must not be claimed in that case. Full coverage of unreachable commits, forks, caches, media pixels, historical permissions and rights is not claimed. Private link/media triage remains local only.

## Follow-up items from PR #20 (status 2026-10-30)

1. Real-Git regressions for accented paths, unusual separators, non-UTF8 and binary paths: done (finding ADR3-1).
2. [ADR-0003](../docs/decisions/ADR-0003-PROPOSED-development-review-and-publication-safety.md): accepted by the owner on 2026-10-30.
3. False-positive handling of review-only references, and blocked diffs not exposing values: covered by the guard tests.
4. The stable Drive asset link in `src/` media documentation and registry: replaced by candidate `privacy-redaction-v1` (#35).
5. Merging a public security gate does **not** grant API credentials, source rights, production or release authority.

## Local hook and mutation check (2026-10-30)

- `python3 security/install_hooks.py` installs a pre-push hook that runs the guard on every commit being pushed and stops the push on BLOCK. `--check` reports whether it is installed. GitHub API and connector writes bypass local hooks; the required CI check covers them.
- `python3 security/mutation_check.py --report security/mutation-report.md` disables each rule in turn and requires the test suite to fail. Current score: 29 of 29 killed (`security/mutation-report.md`).
- A PR that adds media or binary files fails `scan-publication-diff` unless its description has a line `Media reviewed: ...`.

## Workflow supply chain and meaning-level privacy (2026-10-30)

- The repository setting "require SHA pinning" is on: a workflow that uses an Action by tag or branch fails to start. `python3 -m brain status` re-checks the setting. `.github/dependabot.yml` opens weekly PRs that move the pins to newer releases; the owner merges them.
- Meaning-level privacy (account, environment, client or personal details written in prose) has no automated check. The owner accepted this as a known risk: the PR template checklist is the control.

## 2026-10-30 audit fixes

- The base-branch scan runs with `shell: bash` (pipefail), so a BLOCK fails the step instead of being lost in `| tee`. It runs before any PR code and uses the base commit SHA from the event.
- `brain-records` also validates the PR's records with the base commit's `brain/` code, for the same reason.
- New detection: common key names (`api_key`, `x-api-key`, `token`, `secret`) with key-like values, `sk_` keys, tokens split across three lines, and local home-folder paths (REVIEW).
- Known limits: a PR can still edit the workflow files themselves (the control is owner-only merges); PR bodies and comments are not scanned. See `FND-AUDIT-WORKFLOW-EDIT` and `FND-AUDIT-DETECTION-REST` in the Brain.

## 2026-11-03 audit and 2026-11-04 review fixes (PR #58)

- `brain-records` judges rule 5 (no merged record changed or removed) with the base commit's validator, not only the PR's: the base-copy step runs `validate --base-ref` over the checkout's git history, so a PR that edits its own validator to hide a rewritten record still fails. The records it judges are the PR's git blobs, and the step fails unless `brain/records` is a plain folder of plainly named `.jsonl` files, read without trimming (a symlink plus `export-subst`, or a look-alike name such as `decisions.jsonl<TAB>`, could otherwise show it an unchanged copy). Reading no base records fails the check. `tests/test_findings.py::TrustedRuleFive` runs the step's own script against that attack.
- Bootstrap limit: `main` before PR #58 has no `--base-ref`, so for PR #58 itself rule 5 is checked only by the PR's own code. Base enforcement starts with the first PR after #58 merges. The fall-back for a base without the flag should then be removed in a follow-up (`FND-AUDIT3-BOOTSTRAP-FALLBACK`), so a later rename of the flag cannot silently re-open it.
- Separate, still open: a PR that edits the workflow files can remove the base-copy step (`FND-AUDIT-WORKFLOW-EDIT`). The fix above does not close it; the control is still owner-only merges and reading workflow diffs.
- `sk_` keys block as Stripe test keys or as one unbroken run containing a digit (ElevenLabs-style hex), so `sk_snake_case` identifiers do not; `sk_` keys with an underscore after the prefix or no digit are a known gap (`FND-AUDIT-DETECTION-REST-r2`). A 40-hex value under a credential name (`client_secret`, `password`, `access_token`, `*_TOKEN`, `*_SECRET`) blocks; a commit SHA under another name does not.
- Rule 5 compares parsed records, and a line that repeats a key is malformed, so a second `"statement"` cannot hide a change from the check. A record supersedes only a record on its own subject, and a record carrying `finding_status` follows the finding rules in any file.
- Rule 5 is checked against the event's base commit. If the base branch moves after the event, records merged in between are covered only when the PR is updated; the "require branches to be up to date" setting forces that update before a merge.
- `GENERIC_SECRET_ASSIGNMENT` bounds the key name (an unbounded one backtracked quadratically, so one long line could stall the scan) and skips dotted lookups such as `process.env.GITHUB_TOKEN`.
