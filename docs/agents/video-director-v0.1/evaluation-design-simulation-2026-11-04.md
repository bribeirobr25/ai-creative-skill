# Evaluation design simulation (2026-11-04)

**Status:** offline simulation under DEC-2026-10-30-evaluation-method. No model was called and nothing was spent. It sizes the automated evaluation in `evaluation.md`; it says nothing about how good the Director is.

**Question:** for plausible specialization effects, judge noise and judge bias, how often would each design (scenarios × runs per arm) give a clear reading of whether the Director beats a generalist, and how often a clear but wrong one?

**Reproduce:** `python3 evaluation-design-simulation.py --n 4000 --boot 1000 --seed 20261104` (numpy, already in `validation/requirements.txt`; about 90 seconds). The full output is [evaluation-design-simulation-2026-11-04-results.md](evaluation-design-simulation-2026-11-04-results.md).

## Model

- Each scenario has a true effect of the Director's guidance. It varies between scenarios when the effect depends on conditions (`tau`).
- Each run pair (one Director run, one generalist run, same scenario) differs by that effect plus run-to-run noise. Runs of one scenario share its effect, so they are correlated.
- Each pair is judged twice with positions swapped. A judge has its own noise (`sigma_j`), a position bias (cancelled by the swap) and possibly a lean toward the Director (`bias`: same model family, recognisable format, length). The swap does not cancel that lean.
- The estimate is the mean preference over scenarios. Its 95% interval comes from a bootstrap that resamples whole scenarios, so repeated runs are not counted as independent.
- "Clear" means the interval excludes no difference. This measures how informative a design is. It is **not** the readiness rule.

## Inputs: observed and assumed

| Input | Value used | Source |
|---|---|---|
| Effect size `mu` | 0, 0.25, 0.5, 1.0 (a Director run beats a generalist run 50%, 57%, 64%, 76% of the time) | **Assumed.** BL-2026-10-29-01 found no owner-visible difference between its arms, which makes small effects plausible, but it tested a different question |
| Effect varies by scenario `tau` | 0 or 0.5 | **Assumed** |
| Judge noise `sigma_j` | 0.5 or 1.5 (two independent judges agree on 86% or 67% of pairs) | **Informed, not estimated:** in BL-2026-10-29-01 two same-family LLM judges agreed on 15 of 17 untied pairwise orderings across 6 triplets (about 88%). Small sample, other tasks; agreement between same-family judges cannot reveal a bias they share |
| Lean toward the Director `bias` | 0 or 0.3 | **Assumed.** Not measurable from recorded evidence. In BL-2026-10-29-01 the LLM judges guessed the long-skill arm in 2 of 13 guesses (chance about 1 in 3), but the Director's format is far more recognisable |
| Position bias | 0.3 | **Assumed**; cancelled by swapping |

## Results (percent of simulated evaluations with a clear reading for the Director)

Selected cells; every condition is in the results file. Monte Carlo error is at most ±1.5 points.

| Design | Transcripts | No effect, no lean | No effect, lean 0.3 | `mu` 0.5, noisy judge | `mu` 1.0, noisy judge |
|---|---|---|---|---|---|
| 3 scenarios × 2 runs (the 2026-11-03 plan) | 12 | 3–4 | 7–8 | 11 | 22–23 |
| 6 × 1 | 12 | 4–6 | 8–11 | 15–17 | 29–31 |
| 12 × 1 | 24 | 3 | 8–9 | 12–14 | 35–37 |
| 24 × 1 | 48 | 3 | 10–13 | 19–20 | 59–62 |
| 12 × 2 | 48 | 3–4 | 12–17 | 21–24 | 61–65 |

Ranges span `tau` 0 and 0.5. "Noisy judge" is `sigma_j` 1.5 with no lean.

**Robustness checks** (closed form): with 12 Director runs facing a check, a failure that happens 10% of the time is seen at least once with 72% probability; with 24 runs, 92%. If 24 runs show no failure, the rate is below 11% at 95%.

## What it means for the design

1. **No affordable design proves superiority unless the effect is large.** At a moderate effect (`mu` 0.5), even 48 transcripts give a clear reading only about one time in five with a noisy judge. An inconclusive comparison is the expected outcome, which is why readiness for an owner trial cannot rest on a win rate.
2. **A judge's lean grows into false confidence with size.** With no real effect and a lean of 0.3, larger designs declare the Director clearly better more often (8–9% at 12 × 1, up to 17% at 12 × 2). More runs do not fix a biased judge; controls do: rule-based checks where possible, a format control, swapped positions, and the owner's trial as the real test.
3. **Scenarios beat repeats.** At equal transcripts, more scenarios with one run each give about the same clarity as fewer scenarios with repeats, and they cover more conditions. Three scenarios are too few for a scenario bootstrap.
4. **Robustness is where runs pay off.** About 24 Director runs facing the binding checks (main scenarios plus targeted probes) make a 10% failure rate very likely to show.

**Chosen design** (`evaluation.md`): a held-out pass of 13 scenarios × 1 run per arm, the smallest set that covers every pair of the scenario factors, plus 12 targeted probes per arm, so about 25 Director runs face the binding checks. It was simulated as 12 × 1. A 48-transcript design would add about 5–25 points of clarity at about twice the cost, and with more risk of confident bias. That is not worth it for a decision whose real test is the owner's trial.

## Limits

- Every effect and bias parameter is an assumption. The only recorded inputs are from another study with other tasks.
- Quality is one latent number per transcript; a real judge weighs several criteria.
- Judge calls on one pair share a lean but have independent noise; real calls may be more correlated.
- It does not model leakage, scenario-writing quality or a judge's preference for length.
