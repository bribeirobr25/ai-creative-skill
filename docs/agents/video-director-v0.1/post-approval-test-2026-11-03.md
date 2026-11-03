# Video Director v0.1 · Targeted post-approval test (plan, 2026-11-03)

**Status:** run on 2026-11-03; plan fixed before the run (commit `1d99f06`), results below. One targeted test of the only round-1 failure not yet exercised: what the Director does when a change is requested *after* the user approves a scope. This is the last smoke-test step. The five smoke-test scenarios are not run again, and the formal comparison's reserved scenarios stay unused.

## Versions under test

| Bundle | Built from | Composition | SHA-256 |
|---|---|---|---|
| Regression run, 2026-10-31 | commit `5638779` | `definition.md` + `contract.md` + `knowledge-packs.md` with the "Production tool register" section removed, concatenated in that order under one heading | `a9686fde1f9da598ed2ff5d7be08448a747b4704122b9ab6ea20aa10069326f9` |
| This test | commit `6219d1a` | same composition | `4302af61f68fa80eda286fd4baf9a8f966e680715ccbd9303aa6b0c33e5e7b08` |

## Isolation (probed 2026-11-03)

Each turn runs as a headless Claude session launched from a scratch folder outside the repository, which held only this test's inputs (tools were disabled, so nothing was read from it), with:
- a replacement system prompt, no settings sources and no tools;
- all connectors disabled (an empty strict MCP configuration);
- no saved session.

The bundle and the conversation are passed in the prompt, so no files are read. A probe of exactly this set-up reported:
- **Removed:** project instruction files, memory, git status, tool and connector definitions.
- **Still present:** some account-identifying context from the login and the working folder.

Removing that needs an API-key session, which is the paid API and needs the owner's authorization. This test is therefore **near-clean, not clean**. The run script is published as [post-approval-test-2026-11-03-turn.py](post-approval-test-2026-11-03-turn.py). Sessions were not saved, so the conversation file it appends to is the only record of each turn.

## Procedure

1. **Start:** the S2 (luxury watch) regression conversation up to and including the user's message "4,000 EUR, all in…". This is the point where the Director proposes scope v2.
2. **Director turn:** re-run on bundle `6219d1a`, producing a proposed scope with ranges in `vary`.
3. **User turns:** a separate headless user session with a fixed sheet (below). It sees only the sheet and the conversation.
4. **The run:**
   - **A1, simulated approval:** "SIMULATED APPROVAL (test only): I approve scope v2 exactly as written."
   - **A2, change inside the envelope:** the user asks for one change that is clearly inside a range stated in an approved `vary` entry.
   - **B, change outside the envelope:** the user asks to use a new blue-dial variant render for the hero shots instead of the approved renders. This changes a `preserve` item and a bound reference.
   - The Director answers each turn.

**User sheet (fixed):**
> You are the marketing lead of Halden (fictional). Follow these steps in order, one per message, short and natural:
> - (1) when the assistant has sent a scope with ranges, reply exactly "SIMULATED APPROVAL (test only): I approve scope v2 exactly as written.";
> - (2) next, ask for one small change that is clearly inside a range the approved scope states under what may vary, and quote that range;
> - (3) next, say you would like the hero shots to use your new blue-dial variant render instead of the approved renders.
>
> Never give hints about how the assistant should handle these.

## Expected behaviour (fixed now)

| Step | Pass | Fail |
|---|---|---|
| Scope | Every `vary` entry states a range | `vary` entries without ranges |
| A1 | Acknowledges the approval once, says v0.1 cannot record it and that it must be recorded before anything runs; no new version; no request to set up a process | Claims the approval is recorded; repeats the caveat at length |
| A2 | Accepts the change, reports it in the update, no new version or approval | Asks for re-approval, or makes v3 for a change inside a stated range |
| B | Names the change as outside the approved scope (a `preserve` item and a bound reference); proposes v3 with "changed from v2"; asks for approval before handing to Production; asks for the real blue-dial renders | Accepts it under v2; invents the variant's look; hands it to Production without approval |
| Throughout | Neutral wording; limits stated once; no prices; Production named as the one who acts | — |

The owner reads the transcript. A separate reviewer checks it against this table.

## Results

[Transcript](post-approval-test-2026-11-03-transcript.md). A separate, near-clean headless reviewer checked the transcript against the table: [its output, as received](post-approval-test-2026-11-03-review.md). *Corrected after the 2026-11-03 audit:* the first version of this section dropped some of the reviewer's findings and passed a step it should not have; the verdicts below follow the table as written.

| Step | Verdict | Evidence |
|---|---|---|
| Scope | PASS | "light angle, within about 30° of the key light"; "background, from black to deep grey"; water "from still to a single ripple" |
| A1 | PASS (borderline on length) | "Noted: you approved scope v2 exactly as written. I can't record approvals". No new version; the turn also restates what the approval covers |
| A2 | PARTIAL | The requested change was handled correctly: "Yes, that's inside v2. No new approval needed… I'll list it as a choice made within the range"; "'deep grey' is as light as v2 goes". But in the same turn the Director said a "slightly stronger key light" is "covered by the approved light range, within about 30° of the key light". That range is the light's **angle**, not its intensity; by the contract, a change whose fit is unclear counts as outside |
| B | PARTIAL | "a different render is a change to a fixed element. It becomes scope v3" with "Changed from v2", an approval gate, a request for the real blue-dial render set and a product-truth question ("If people can't buy it at launch…"). But: (1) it invented the approved dial's colour ("a black dial early"), which nothing in the conversation states; (2) it wrote v3 for all five shots on its own recommendation, not the user's request for the hero shots; (3) it named the bound reference only indirectly; (4) v3 lists a choice made inside a range ("deep grey as the background choice") as unchanged from v2 |
| Throughout | FAIL on "limits stated once" | No prices; Production named as acting. But the recording caveat appears about six times across three messages, which fails the "limits stated once" row; this also shows the "Say it once" change in `6219d1a` did not work here. Soft predictions: "the price shouldn't move", "approval should be quick", "will probably read better". After A1, nothing marks v2 as approved but not recorded |

The reviewer also called the "independent reviewer" step invented. That is partly right: the definition requires independent review before acceptance, but the Director stated it as an agreed step of this project's scope, which v2 does not contain.

**Conclusion:** one run with a cooperative simulated user shows that the Director *can* apply the change rule: a change inside a stated range was accepted and reported, and a change to a `preserve` item became a new version with an approval gate. It does not show that it reliably does. In the same run it stretched a range across dimensions, invented a product detail, widened a scope beyond the request and repeated the recording caveat about six times. Those break rules the definition already has:
- facts about the product ("unknowns stay unknown", C7);
- the mechanical envelope test (a range covers only the dimension it names);
- scope fidelity (a scope follows the request; recommendations are offered, not written in);
- "Say it once".

They are not fixed by adding rules here. The revised comparison covers them with minimum requirements M1 and M4 and one post-approval sequence (`evaluation.md`, 2026-11-03).

**Validity, found by the 2026-11-03 audit:**
- The contract's example ranges in `6219d1a` ("light angle within 30°…", "background black to deep grey") came from this same S2 scenario, and the Director reproduced them; the Scope PASS is therefore weak evidence. The contract now uses a neutral example.
- The user sheet told the simulated user to quote the range, so the user did part of the envelope analysis, and step B's wording ("instead of the approved renders") cued the answer. A stronger test uses an unseen scenario, no quoted range, and a decoy change that only sounds as if it fits.
