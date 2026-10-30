# Project Brain (skeleton v0.1)

One place to answer "where are we, what was decided, what is next" at the start of any session, in any tool. It is a guide to **what** and **in what order**, not a rulebook. Methods and techniques are not kept here: under [ADR-0005](../docs/decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md) D1 they are dated observations in the [benchmark log](../docs/benchmarks/benchmark-log.md).

## Start of a session

```
python3 -m brain status       # current decisions, due reviews, live checks, open PRs and issues
python3 -m brain validate     # records follow the contract
```

`status` is **derived on read**: it reads the records, the benchmark log and, if `gh` is available, GitHub. It is never committed, so it cannot go stale.

## What lives where

| Need | Where |
|---|---|
| A decision the owner made | `brain/records/decisions.jsonl`, one record per decision ([contract](CONTRACT.md)) |
| A review or audit finding, and the test that guards it | `brain/records/findings.jsonl` (empty until the first finding is carried over) |
| Which principles are enforced, and by what | `brain/gates.json` (live, or still on paper) |
| What current models do well or badly | `docs/benchmarks/benchmark-log.md` |
| Why a decision was made | The ADR in `docs/decisions/` |
| Anything private | Not here. Use the owner's private store. |

## Order of work

These are suggestions; change them when the situation changes.

1. Run `status`. Read the current decisions before proposing anything that touches them.
2. Work on a branch and open a PR. Nothing merges without the owner.
3. If the work settles a question, add a `DECISION_RECORDED` record with `authority_ref` set to that PR. The owner's merge is the decision.
4. If a review finds a problem, add a finding with the test that would catch it again. A finding with no test is marked `paper`.
5. If a new principle matters, add it to `gates.json` with the check that enforces it, or mark it `paper` until one exists.
6. When a record is wrong or outdated, supersede it; don't edit history.
