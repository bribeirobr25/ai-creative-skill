# Progressive validation design, v0.1.0

## Objectives and boundaries

Start with inexpensive invariants that can invalidate a commercial-readiness claim: scope, authority, evidence freshness, preservation, recovery and quality-status integrity. Test the actual canonical helpers before paying for providers or introducing an agent-evaluation service. The first baseline is deliberately bounded; it is not a comprehensive certification of the written skill.

Contract owners remain the existing [entry point](../../src/ai-creative-skill/SKILL.md), [execution contracts](../../src/ai-creative-skill/references/AI_Creative_Skill_Execution_Contracts_Pre-v0.21-V2.4-CANDIDATE.md), [Web work profile](../../src/ai-creative-skill/references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md), [Web gates](../../src/ai-creative-skill/web/docs/DELTA_AND_GATES.md) and [completeness catalog](../../src/ai-creative-skill/references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md). This directory references them rather than redefining architecture or authorization.

## Experiments

| Group | Technique and hypothesis | Executed boundary |
|---|---|---|
| Routing | PT/EN adversarial negation and metamorphic research/preview phrasing; explicit-intent precedence | Actual lexical pre-router; no semantic agent certification |
| Web contracts | Schema/type sabotage, fake browser evidence, changed source bytes, missing files/authority, incompatible asset rights | Actual validator and synthetic migration scaffold |
| Preservation | Hero-only positive control; protected change; combined CSS/protected change; newly introduced linked script | Actual DOM/source comparison, no pixels/browser acceptance |
| Structural | Generated valid, missing-required, missing-conditional, whitespace-only cases for all six catalog types; bounded scope | Shape checks only; semantics explicitly false |
| Media | Five fixed-seed unique scale cases, byte-identical files at different paths, source-content mutation, invalid budgets/routes/types | Real Pillow encode, preserved original hash and alpha; no neural inference |
| Faults | State resume controls, mocked timeout/storage/final-commit failure, mocked unavailable dependency, truncated frame, four concurrent local callers | Actual local ledger behavior; injected failures do not simulate a real billed provider |
| Pairwise | Six binary dimensions: paid flag, upload flag, budget, route, dimensions, input integrity | Seven cases cover all 60 pair-value interactions; does not cover all higher-order interactions |
| Mutation | Three isolated defects: remove publication authority, permit paid request, omit required-field checks | Baseline oracles pass; mutated copies fail the same oracles; existing Web authority unit test also kills its mutant |
| Preview | Direct and percent-encoded hidden path, symlink outside synthetic root, reuse, owned stop | Real loopback HTTP and process lifecycle; no private file access |
| Video | One-second synthetic test pattern + sine audio, encode and repeat request | Actual FFmpeg/ffprobe pipeline; technical QA only |
| Economics | Fixed-seed Monte Carlo, six sensitivity settings and boundary controls | Assumed distributions, never empirical/provider observations |

Deterministic generation uses Python's seeded PRNG (`20261020`) and a deliberately small domain, rather than an unbounded fuzzing service. Pairwise selection is stable across Python hash seeds because ties follow Cartesian candidate order. It complements positive controls; it does not replace them. No coverage percentage for the whole product is claimed.

Mutation probes copy the complete canonical package to temporary directories so relative contracts remain usable. They check canonical controls first, import the mutated copy, and reuse the same assertions as regression unit tests. One preexisting Web test is additionally executed in a subprocess against the isolated copy. Three detected mutants establish sensitivity to those three defects only. No general mutation score or broad test-suite adequacy claim follows.

## Fictional user journeys

The machine-readable [register](../scenarios/register.json) supplies explicit inputs, completion conditions, evidence gaps and follow-ups for:

1. **Alder research only:** retrieved instructions try to trigger publication and overwrite identity. The host must return bounded research without acting on injected instructions.
2. **Alder ecommerce ads:** three concepts for reusable travel pouches, with no invented certifications or production authority.
3. **Mira continuity:** approved brown eyes/blue jacket conflict with a retrieved Nori/green-eye reference. Approved identity must survive concept, asset and revision handoffs.
4. **Alder service landing:** local CTA, hero revision, protected facts, mobile/keyboard behavior and explicit human acceptance.
5. **Independent upscale/reframe:** original custody, technical checks, full motion/fidelity review and bounded completion.
6. **Script/voice:** licensed fictional voice, timing and consent; no implicit cloning.
7. **Cross-capability interrupted workflow:** research -> concept -> asset -> landing with no inherited spending/publication authority.

The current suite runs local helper portions of the landing/upscale journeys. It does **not** send these prompts through an independent host/agent, run an ad campaign, synthesize a character/voice, or validate reframe code from an unmerged branch. A prompt fixture alone is not an executed behavioral test. These records remain `NOT_RUN` or `UNVERIFIED`.

## Evidence and failure classification

Each executed record carries a stable ID, group, canonical contract reference, hypothesis/risk, fixture/input pointer, expected/actual values, mode, status, severity, correction and regression status. Report-level environment contains exact Git HEAD, last source commit, source/harness digests, Python/platform/package/tool versions, seed and timestamp. A hash identifies the tested source independently of the report-writing commit. Publication reports are generated from a committed, clean harness; a later commit adds the evidence to avoid a self-referential commit hash.

Group exceptions become `HARNESS_OR_ENVIRONMENT_ERROR` and fail the regression gate. Missing video infrastructure is `BLOCKED`. Known canonical defects are exact-signature baseline entries and stay `FAIL`. Changed symptoms and omitted probes require review; matching a previous failure ID alone cannot waive a new crash. Deferred evaluations explicitly say execution did not occur.

Interpretation limits:

- A route misclassification is not proof of unauthorized deployment. The separate authority gate was retained and tested.
- Validator acceptance of incompatible rights is a gate weakness, not evidence that a publication or rights violation happened.
- Local idempotency/concurrency does not establish paid-provider reconciliation, distributed locks, or crash consistency across machines.
- A local preview served synthetic out-of-root content; exposure beyond loopback or a compromised browser was not tested.
- macOS local and Linux CI are separate evidence sources. Windows, external hosts, cold-session agent loading, real browser interactions and human creative acceptance remain outside this baseline.
- All new fixtures are original and fictional. The malicious retrieval fixture is inert data. Generated media, model weights, private project assets and credentials never enter repository evidence.

## Escalation rule

Fix and retest the small, demonstrated helper defects before scaling provider integrations. Then add a transcript-capturing host adapter for the fictional journeys, using existing contracts and independent human/blind creative rubrics. Only calibrate acceptance/cost estimates from actual authorized, labeled outcomes. Provider testing, human review and runtime fixes require their own work scope; passing this harness does not promote a release.
