# Scenario 4 · Story, world and character → scene

**Type:** conceptual compatibility check for long-running creative work. Fictional animated series. The Story, Character and World roles do not exist yet; they are assumed only for this check.

**Question:** can shared context, asset identity, versions, canon and continuity be represented without story-specific rules in the core?

| # | Step | Owner | Knowledge | Delegation | Records | Authority |
|---|---|---|---|---|---|---|
| 1 | Goal: a 10-episode season. The plan assigns Story, Character and World in parallel | project-lead | — | Plan assignments, all depth 0 | tasks; project | User sees the plan |
| 2 | Story drafts the story bible: premise, rules, cast list | story | Story pack | — | entity `kind: story-bible`, v1 `proposed`; `extension` story.bible.v0 | — |
| 3 | User approves the bible v1; it becomes canon | — | — | — | `authority_change` approval; listed in `authorities` | User |
| 4 | Character designer defines the lead character | character | Character pack | — | entity `kind: character`, v1, `relations: appears_in` → bible | — |
| 5 | Moodboard: real references from Research, generated variants from Production | character | — | `context` → Research (depth 1); `permission` → Production (depth 1, under an approved scope) | findings with rights; generated assets with tool | Scope for the generated variants |
| 6 | Character sheet v1 approved as canon | — | — | — | approval; asset dependencies recorded | User |
| 7 | World builder defines the city and two locations | world | World pack | — | entities `kind: location`, `relations: located_in` | User approves canon |
| 8 | Episode 1, scene 3: the Director plans from approved versions | video-director | — | Plan assignment | deliverable with dependency refs: character v1, location v1 | — |
| 9 | Later, the user approves a costume change: character v2 | character | — | — | `authority_change`; v1 `superseded` | User |
| 10 | Only scenes that depend on character v1 become `invalidated`; others stay accepted | project-lead | — | Event `authority_changed` resumes the affected scene tasks | lifecycle projection; tasks `active` again | Re-approval before reuse |
| 11 | A generator keeps adding a scarf; it is not canon until promoted | character | — | — | repeated choice ≠ canon; the owner may propose character v3 `proposed`; on approval a `canon_promotion_ref` is recorded | User decides |

## What the core needed, and what it did not

- **Used from the core:** entities with stable ids and free `kind`; versions with lifecycle; `relations`; canon as approved authority; dependency-based invalidation; events; parallel assignment versus delegation depth.
- **Not in the core:** what a character sheet, a bible or a location contains; episode timelines; continuity ledgers. These are the Story area's extensions.

## Gaps found

| Gap | Class | Note |
|---|---|---|
| Timeline and continuity across episodes ("what happened in episode 3") | Domain extension | Story's schema; the core supplies entities, relations and versions it is built from |
| Voices and consent for recurring characters | Accepted limitation | Rights and consent records exist; voice routes are Production's |
| Many dependent scenes invalidated at once: cost of re-review | Accepted limitation | Selective invalidation limits it; batching the re-review is a playbook choice |

No blocking gap.
