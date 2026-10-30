# Decision/state record contract v0.1

This is the one record contract from [ADR-0005](../docs/decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md) D5. The Project Brain is its first instance. `python -m brain validate` enforces this file; if the two disagree, fix the validator or this file in the same PR.

## Record

There is one JSON object per line in `brain/records/*.jsonl`.

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique and stable, e.g. `DEC-2026-10-29-container`. Never reused. |
| `kind` | yes | `OBSERVED` (a fact seen), `CHANGE_REQUESTED` (someone asked for something) or `DECISION_RECORDED` (the owner decided). |
| `subject` | yes | What the record is about, e.g. `container` or `license`. At most one current decision per subject. |
| `statement` | yes | One or two plain sentences. |
| `authority_ref` | for decisions | The owner act that makes it a decision: `pr:#N` (a PR merged by the repository owner). |
| `evidence_refs` | yes, may be empty | Repo paths, `pr:#N`, `issue:#N` or `commit:<sha>`. |
| `supersedes` | no | The `id` of an earlier record this one replaces. |
| `scope` | no | Host, model, route or version it is valid for. |
| `occurred_at` | yes | Date it happened (`YYYY-MM-DD`). |
| `recorded_at` | yes | Date it was written down. |
| `review_by` | no | Date to look at it again. `status` lists it once due. |
| `privacy_class` | yes | Must be `public` here. Anything else belongs in the private half, outside this repository (invariant 8). |

**Findings** (`brain/records/findings.jsonl`) use the same fields with `kind: OBSERVED`, plus:
- `finding_status`: `OPEN`, `FIXED`, `ACCEPTED-RISK` or `UNKNOWN`;
- `test_ref`: the test that catches the problem again (`path` or `path::Class[.method]`; the file must exist), or `paper` until a test exists;
- `source`: where the finding was raised.

## Rules

1. **The emitter is not the persister.** Agents and people propose records in a PR. A record counts only once the owner merges that PR. For a decision, `authority_ref` names the PR whose merge was the owner's act. `python -m brain validate --verify-authority` checks that on GitHub.
2. **Superseded is never current.** A record named in another record's `supersedes` is history.
3. **Contradictions fail closed.** Two current decisions on the same subject make `validate` fail. Supersede one; don't edit both.
4. **No automatic promotion.** An observation or a benchmark result never becomes a decision by itself (ADR-0004 I5, Calibration §1.2).
5. **Add, don't rewrite.** To correct a record, add a new one that supersedes it. Typos may be fixed in place in the same PR that added the record, before merge.
6. **Public only.** The private half (pilot canon, client brands, account state, off-repo decisions) lives where the owner chooses, outside the repository.
