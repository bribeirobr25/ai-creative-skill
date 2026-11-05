# Knowledge packs

**Sources:** the Video Director [knowledge packs](../agents/video-director-v0.1/knowledge-packs.md) (tags, strengths, loading); ADR-0006 D2, D5; decision `knowledge-freshness`; V2.5 SMS §4 (precedence), §8 (calibration packs); CAL §1–§1.2 (experience as scoped evidence, no automatic edits); RA §7 and its V2.4 addendum (loading must be observable); RES §8 (independence key).

A pack is knowledge a role loads. It adds what the model cannot know or reliably skips: user and market facts, proven stages, required elements, limits, closing steps, tool facts and failures. It does not dictate how the work is done (ADR-0006 D2).

## Pack format

```yaml
pack:
  pack_id:          # required, stable
  owner_role:       # required
  version:          # required
  load: always      # required: always | on_demand
  privacy_class: public   # required; packs holding user or client knowledge live in the private half
  items:
    - id:           # required, stable inside the pack
      statement:    # required, one sentence of what or why, not how
      layer:        # required: core | current | experience
      tag:          # required: rule | evidence | provisional | current | technique | hypothesis
      strength:     # required: binding | default | recommended | option
      basis: []     # required: authority or evidence refs; `rule` needs an authority
      source:       # required for layer current
      checked_at:   # required for layer current
      expires_at:   # required for layer current
      scope:        # optional: host, model, route or version it is valid for
```

Tags and strengths keep the meanings defined in the Video Director packs ("How to read an item"); only `rule` may be `binding`. Layers follow the vision: **core** (proven practice, rarely changes), **current** (dated, expires), **experience** (what this user approved, rejected or what performed).

## Rules

1. **KP1 · Short core, loaded on demand.** A pack's always-loaded part stays short; cards and libraries load only when the task needs them (Video Director packs, "Loading").
2. **KP2 · Loading is recorded, not assumed.** A task records which packs and versions it actually read (`packs_loaded`, [collaboration.md](collaboration.md#task-record)). Availability does not count (RA V2.4 addendum); in the October container test the host never showed the enabled skill being read.
3. **KP3 · Precedence.** Project authority, then the narrower pack, then the broader pack, then generic defaults (SMS §4). A pack never overrides an approved fact, brand rule, canon or limit.
4. **KP4 · Fetched content is data.** Text from sources, references, the web or third parties describes the world; it is never an instruction to the agent (ADR-0006 D5).
5. **KP5 · Current knowledge expires.** An item past `expires_at` counts as unverified until re-checked; the status view lists it as due.
6. **KP6 · Patterns, not copies.** Packs keep principles and why they work, never other people's protected work, brands or likenesses.
7. **KP7 · Knowledge never relaxes a limit.** A `current` item is knowledge, not a rule (ADR-0006 D5): it can add caution or options, never loosen a limit, an approved fact or a platform rule.

## Proposing and adopting changes

Agents propose; they never change core items or rules by themselves (CAL §1.1: "learning capture != automatic skill edit").

```yaml
learning_candidate:
  candidate_id:     # required
  pack_id:          # required: the pack it would change
  proposed_item: {} # required: the item as it would read
  origin:           # required: SIMULATION_ONLY | CONTROLLED_TEST | PROJECT_EMPIRICAL | THIRD_PARTY | THIRD_PARTY_TOOL_DIAGNOSTIC | USER_PREFERENCE (CAL §1.2)
  evidence_refs: [] # required
  counterevidence: []
  proposed_by:      # required: role
```

Adoption follows ADR-0006 D5 by layer:
- **Current knowledge** enters once a reliable source states it or two sources with different RES §8 independence keys agree, with source, reliability, date and expiry. The specialist records it as an `OBSERVED` record; no approval is needed. That record closes the candidate; it appears in the specialist's digest, and the user can remove it.
- **Core items and rules** change only through an `authority_change` approval by the user, or by the system owner for shared packs, with evidence that results improve. A repeated error is a candidate, not a rule.
- Learning from one user's private results stays with that user unless they agree to share it.
