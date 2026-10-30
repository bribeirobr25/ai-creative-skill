# Privacy redaction v1 — review candidate, not a release

**Status:** active source candidate. Parent: [web-runtime-2.6-v2](../web-runtime-2.6-v2/README.md), whose records stay
byte-identical to the commit that reviewed them (`ce20a59`, on `main`). Release approval: **false**.

**Why:** [ADR-0005](../../../docs/decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md) D4. The skill
package is frozen with no new release line (D1). This candidate is the one planned `src/` change: it replaces public
references to the owner's private storage and operator environment with neutral wording. It changes no method, rule,
runtime code or schema, adds or removes no file, generates no media and calls no provider.

## Scope added over v2 (cumulative)

| Change | Files | Before → after |
|---|---|---|
| Drive folder link (3 occurrences, same folder) | `media/README_PTBR.md`, `media/registry/provider_capabilities_v0.2.json`, `media/registry/provider_capabilities_v0.3.json` | Google Drive folder URL → `private-archive://media-evidence/realesrgan-mps-video-v0.2` |
| Drive path prefix (143 occurrences) | Calibration and Experience Memory, External Skill Analysis Ledger, Method Provenance Map, AI Media Provider Registry | `/Google Drive/ai/influencer/` → `private-archive://influencer/`. File names are kept, so provenance stays traceable. |
| Operator-environment statements (16 lines) | Current Design Manifest, External Skill Analysis Ledger, Method Provenance Map, Project Profile Pilot01 | "installed in the operator's account" / "disables it in the account" → "if present in the operator's environment" / "disables it where present". The rule itself is unchanged: the skill stays disabled during Pilot work, and re-enabling it is an operator decision. |

`private-archive://` is a logical ID in the sense of ADR-0001: the location resolves outside the public repository.

## Known limits

- Git history, forks and caches still hold the old text; this candidate does not rewrite history.
- `MANIFEST_SHA256.json` stays pinned to the V2.5 release, so these files differ from it, as the v2 files already do.
- Out of scope, recorded for a separate owner decision: Pilot project names, the voice-lock preset and Provider
  Registry spend records, which are project details rather than storage or account details.
- Google Drive is still named as a service where the text describes an event (Ledger §29: a malware flag), not a
  location.
