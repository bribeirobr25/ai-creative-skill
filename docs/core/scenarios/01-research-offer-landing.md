# Scenario 1 · Research → offer → landing page (reference playbook)

**Type:** the one detailed reference playbook of v0.1, and a conceptual compatibility check. Fictional: an agency serves an end client, a small tea shop that wants to sell a subscription. No real data, no run.

**Why this flow:** it crosses Research, Sales and Visual & Brand, covers the business half, needs no paid generation (the page is code, rendered locally), and continues after delivery when results arrive.

## Playbook (summary of the `playbook` record)

| Stage | Deliverable | Owner | Required elements (`REQUIRED` unless noted) | Final? | Checkpoint |
|---|---|---|---|---|---|
| Intake | Project record and plan | project-lead | Goal, audience, budget, deadline, what exists, approver | — | Plan shared with the user (no approval needed) |
| Research | Market brief: competitors, pricing, buyer complaints | research | Sources with dates, counterevidence, `review_by`, gaps stated | Intermediate | — |
| Offer | Offer proposal: who, what, price, guarantee | sales | Grounded in findings; claims only from facts | Intermediate | `direction` |
| Brand basics | Use of the existing brand kit | visual-brand | Approved logo and palette versions; mark check if anything new (`CONDITIONAL`) | Intermediate | `authority_change` only if the kit changes |
| Page direction | Structure, copy, look | visual-brand | Hook, offer, call to action, accessibility plan | Intermediate | `direction` |
| Build | Page code and local render | visual-brand (websites pack) | Rendered review on desktop and phone sizes; delivery record | Final | — |
| Review | Independent acceptance | reviewer | Boundary C on the render; required elements | — | — |
| Publish | Live page | visual-brand (act) | Rights, accessibility, AI disclosure, platform terms, consent text for lead capture | — | `outward_action` |
| Measure | Results summary | growth | External results as data; what changed | Intermediate | — |

`continuation`: on `external_result` or `research_due`, start the next iteration at Offer or Page direction; `ends_when`: the user closes the project, or 90 days pass, whichever comes first.

## Walk-through

| # | Step | Owner | Knowledge | Delegation | Records | Authority |
|---|---|---|---|---|---|---|
| 1 | Agency user sends the goal and names the client's marketing lead as approver for `direction` and `outward_action` | project-lead | — | — | project (tenant = client), `designation` approval, plan tasks | User (person_attested) |
| 2 | Research scans competitors' sites and pricing, and public reviews where platform terms allow | research | Research packs (buyer research, evidence synthesis) | Plan assignment, depth 0 | findings with `checked_at`, `review_by`; external refs with snapshots and retention where permitted | Read level only |
| 3 | Sales drafts the offer, with options A and B | sales | Offer pack | — | offer v1 `proposed`; closing check | — |
| 4 | Approver picks option B | — | — | — | `decision` message → host records `direction` approval of offer v1 (option B) | Client approver, within the designation |
| 5 | Visual & Brand writes the page direction from the approved offer and brand kit | visual-brand | Websites pack | Copy drafted locally with the copy pack (no trigger) | direction v1 `proposed` → approval → `approved` | Client approver |
| 6 | Builds the page and renders it locally | visual-brand | Websites pack | — | asset with tool, rights; package (code), no scope needed | None needed: no spend, nothing outward |
| 7 | Independent review on the render; one repair (a hero image collapsed on phone size) | reviewer | Review criteria | `independent_review` | review C `REPAIR` → round 1 → `ACCEPTED` | — |
| 8 | Publication requested and approved; required elements checked at the moment of publishing | visual-brand | — | — | `approval_request` → `outward_action` approval → consumed by the publish record | Client approver |
| 9 | Two weeks later, visits and sign-ups arrive | growth | Measurement pack | — | `external_result` event (the analytics system's own id as key); finding | Read level |
| 10 | Growth proposes a new headline test; pricing research is due | growth, research | — | Event-driven, depth 0 | proposal in `next_actions`; one pending `research_due` refresh | A new `direction` approval before anything changes |

## Gaps found

| Gap | Class | Note |
|---|---|---|
| Whether the host can attest that the user, not an agent, sent the naming | Open question | The naming is evidenced by the user's own `person_attested` message (settled); host attestation is README open question 1 |
| Lead capture stores personal data: consent text, retention and erasure | Accepted limitation | ADR-0004 privacy rules and D8 apply; the concrete policy comes with the private-half layout, before a real project |
| Reading analytics needs credentials and possibly paid data | Accepted limitation | Step-2 secret store, and an execution scope if paid |
| Website structure (sections, components) | Domain extension | Websites pack schema under `extension` |
