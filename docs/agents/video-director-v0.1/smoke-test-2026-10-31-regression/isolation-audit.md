# Isolation audit of the regression run (2026-10-31)

One row per agent call. "Files read" lists every file the agent opened, from its tool log (each call is recorded twice in the log; duplicates are merged). Allowed: the Director reads `bundle.md` and its scenario's `conversation.md`; the user reads its `user-sheet.md` and `conversation.md`. The raw logs contain the injected harness context, so they are kept privately, not published.

The Director bundle `bundle.md` has SHA-256 `a9686fde1f9da598ed2ff5d7be08448a747b4704122b9ab6ea20aa10069326f9`; its composition is in [post-approval-test-2026-11-03.md](../post-approval-test-2026-11-03.md).

| # | Scenario | Role | Turn | Files read | Other tool use | Within allowed |
|---|---|---|---|---|---|---|
| 1 | S1 | Director | 1 | `S1/conversation.md`, `bundle.md` | none | yes |
| 2 | S2 | Director | 1 | `S2/conversation.md`, `bundle.md` | none | yes |
| 3 | S1 | User | 2 | `S1/conversation.md`, `S1/user-sheet.md` | none | yes |
| 4 | S4 | Director | 1 | `S4/conversation.md`, `bundle.md` | none | yes |
| 5 | S3 | Director | 1 | `S3/conversation.md`, `bundle.md` | none | yes |
| 6 | S2 | User | 2 | `S2/conversation.md`, `S2/user-sheet.md` | none | yes |
| 7 | S5 | Director | 1 | `S5/conversation.md`, `bundle.md` | none | yes |
| 8 | S4 | User | 2 | `S4/conversation.md`, `S4/user-sheet.md` | none | yes |
| 9 | S3 | User | 2 | `S3/conversation.md`, `S3/user-sheet.md` | none | yes |
| 10 | S1 | Director | 2 | `S1/conversation.md`, `bundle.md` | none | yes |
| 11 | S5 | User | 2 | `S5/conversation.md`, `S5/user-sheet.md` | none | yes |
| 12 | S2 | Director | 2 | `S2/conversation.md`, `bundle.md` | none | yes |
| 13 | S4 | Director | 2 | `S4/conversation.md`, `bundle.md` | none | yes |
| 14 | S3 | Director | 2 | `S3/conversation.md`, `bundle.md` | none | yes |
| 15 | S5 | Director | 2 | `S5/conversation.md`, `bundle.md` | none | yes |
| 16 | S1 | User | 3 | `S1/conversation.md`, `S1/user-sheet.md` | none | yes |
| 17 | S1 | Director | 3 | `S1/conversation.md`, `bundle.md` | none | yes |
| 18 | S3 | User | 3 | `S3/conversation.md`, `S3/user-sheet.md` | none | yes |
| 19 | S2 | User | 3 | `S2/conversation.md`, `S2/user-sheet.md` | none | yes |
| 20 | S4 | User | 3 | `S4/conversation.md`, `S4/user-sheet.md` | none | yes |
| 21 | S5 | User | 3 | `S5/conversation.md`, `S5/user-sheet.md` | none | yes |
| 22 | S3 | Director | 3 | `S3/conversation.md`, `bundle.md` | none | yes |
| 23 | S2 | Director | 3 | `S2/conversation.md`, `bundle.md` | none | yes |
| 24 | S1 | User | 4 | `S1/conversation.md`, `S1/user-sheet.md` | none | yes |
| 25 | S4 | Director | 3 | `S4/conversation.md`, `bundle.md` | none | yes |
| 26 | S5 | Director | 3 | `S5/conversation.md`, `bundle.md` | none | yes |
| 27 | S2 | User | 4 | `S2/conversation.md`, `S2/user-sheet.md` | none | yes |
| 28 | S3 | User | 4 | `S3/conversation.md`, `S3/user-sheet.md` | none | yes |
| 29 | S4 | User | 4 | `S4/conversation.md`, `S4/user-sheet.md` | none | yes |
| 30 | S3 | Director | 4 | `S3/conversation.md`, `bundle.md` | none | yes |
| 31 | S5 | User | 4 | `S5/conversation.md`, `S5/user-sheet.md` | none | yes |
| 32 | S4 | Director | 4 | `S4/conversation.md`, `bundle.md` | none | yes |
| 33 | S5 | Director | 4 | `S5/conversation.md`, `bundle.md` | none | yes |
| 34 | S3 | User | 5 | `S3/conversation.md`, `S3/user-sheet.md` | none | yes |
| 35 | S5 | User | 5 | `S5/conversation.md`, `S5/user-sheet.md` | none | yes |
| 36 | S4 | User | 5 | `S4/conversation.md`, `S4/user-sheet.md` | none | yes |
