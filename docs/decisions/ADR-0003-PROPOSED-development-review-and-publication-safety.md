# ADR-0003 · Segurança de publicação no repositório público

**Data:** 2026-10-24
**Status:** ACCEPTED by the owner on 2026-10-30. The acceptance is recorded in the Project Brain (`DEC-2026-10-30-adr-0003`). The filename keeps `-PROPOSED` so existing links stay stable.

> **Acceptance note (2026-10-30).** The items under "Required before acceptance" were met:
> - real-Git tests (finding ADR3-1);
> - the guard run on the Web 2.6 candidate diff (ADR3-2);
> - the cross-check with ADR-0001/0002 (no conflict: this ADR adds publication checks and supersedes neither).
>
> The Drive locator in `src/` mentioned below was replaced by candidate `privacy-redaction-v1` (#35). The text below is otherwise unchanged from the proposal.
**Decision owner:** repository maintainer (owner acceptance required; no automatic approval).
**Authority:** complements ADR-0001 (separation of public source and private assets) and ADR-0002 (minimum sufficient bounded path). Neither is superseded.

## Proposed decision

1. **Before every public write**, including local Git pushes and GitHub connector writes, check the complete proposed content and affected filenames for secrets, personal information, private projects, signed URLs and media distribution rights. CI cannot undo a secret leaked by the first push.
2. Classify as **PUBLIC_OK**, **REVIEW_REQUIRED**, or **NEVER_PUBLIC**. A public brand name does not automatically make a document confidential; a link to a private resource does not automatically grant access. Unknown rights require targeted review, not invented certainty.
3. Provide a local preflight and a second-layer PR scanner. Any recognized credential or safely unparseable file/patch must **BLOCK**. Ambiguous public Drive links, media or non-secret personal indicators produce **REVIEW** to be handled explicitly. The scanner never emits sensitive values or raw filenames.
4. Check **the PR's final diff and all its commits** for material added and later removed. A global, all-branch historical audit is a separate **manual/advisory** process, never a required status check of unrelated PRs.
5. In any confirmed disclosure of access-granting material, **revoke/rotate at its source first**, review scope and logs, and consider Git history/forks/caches cleanup only with separate explicit owner approval. Public reports contain sanitized categories and status, never raw values.
6. PR and release approval remain governed by their established owners, acceptance criteria, context-specific QA and user authorization. Passing the publication scanner **does not** authorize API access, source reuse, paid operations, merging or release.

## Boundaries

This ADR governs publication safety, **not a universal project-management lifecycle**. Proportional testing and learning follow ADR-0002 and the existing implementation methodology. No new Work Profile, policy adjudicator, expense ledger or security override is introduced.

The S0 historical triage was **administratively closed by owner attestation**, with limited automated coverage and residual uncertainties. This does not certify AI-tool/media licenses, likenesses, external third-party elements, EXIF text, current/historical ACLs or unreachable forks. Investigate a newly evidenced exposure as a bounded case, not by reopening the entire S0 survey.

A current stable Drive folder locator remains embedded in three current media documentation/registry files under `src/`; current ACL was previously reported restricted, not a guarantee of prior access. Replace those public locators with approved logical asset references in a **separate versioned candidate**, respecting the protected source inventory and the PR #17 owner. Do not alter protected `src/` files under this ADR proposal.

## Required before acceptance

- Cross-check with ADR-0001/ADR-0002.
- Real-Git tests covering UTF-8/accented filenames, whitespace, non-UTF-8 patches, binary paths and unusual line separators.
- PR guard testing against the independent Web 2.6 candidate diff, without changing its branch.
- Explicit owner approval of this ADR and merge; status remains PROPOSED until then.
