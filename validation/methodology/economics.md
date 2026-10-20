# Illustrative economic stress model

This model is **not calibrated**, contains no actual provider pricing or observed acceptance rates, and does not rank Higgsfield or any other vendor. No model or payment API is called. It compares hypothetical strategies to expose which measurements matter before investment.

Implementation: [economics.py](../simulations/economics.py). Seed: `20261020`; 2,000 independent trials per strategy per sensitivity setting. Three strategies × six settings = 36,000 simulated jobs. Each job has at most three route opportunities:

- `local_only`: local, local, local.
- `commercial_only`: commercial, commercial, commercial; the cash cap permits at most two paid attempts under base assumptions.
- `local_first_hybrid`: local, commercial, commercial.

Unavailable opportunities are skipped without waiting or spending. Available attempts reserve cash before execution. An uncertain outcome immediately stops for reconciliation; it never triggers a duplicate retry. Technical failure consumes the reserved attempt and permits the next opportunity. Successful technical outputs can require human time and then be creatively accepted or rejected. Cash is reserved conservatively even for failures/uncertain outcomes; it is not verified billed cash.

| Assumption | Fictional base value |
|---|---:|
| Budget per job | $3.00 |
| Commercial attempt reservation | $1.50 |
| Local incremental reservation | $0.00 |
| Availability per opportunity | 95% |
| Technical success per attempt | 95% |
| Unknown outcome | 3% |
| Local creative acceptance, after technical success | 45% |
| Commercial creative acceptance, after technical success | 75% |
| Human intervention | 10%, adding 8 minutes |
| Local/commercial attempt time | 4 / 1 minutes |

Bernoulli draws are independent. Sensitivity changes one input at a time: local acceptance 20% or 75%, commercial acceptance 45%, availability 65%, or uncertainty 15%. This is sensitivity analysis, not a confidence interval or causal result. Fixed-seed repeated output proves reproducibility, not accuracy of assumptions. Strategies consume random draws differently; their outcomes are not a matched empirical experiment.

Reports include acceptance rate, mean attempts/reserved cash, total reserved cash divided by accepted assets (including failed-job costs), median/p90/p95 costs, elapsed time for all outcomes, conditional time to acceptance and stop reasons. Conditional time percentiles exclude rejected jobs and must be read with acceptance rate. Zero accepted assets yield null cost/time metrics, not false zero efficiency.

Budget overruns are zero by construction under the implemented reservation policy. This validates the toy policy's arithmetic, not real-world billing safety. Correlated failures, queueing, delayed billing, refunds, learning, subscriptions, labor price, local energy/hardware and long-duration render time are excluded. All monetary totals are illustrative USD. Local zero incremental cash must not be called zero total cost.

The follow-up is to measure accepted deliveries, manual repair time, failure/unknown outcomes and actual spend by capability and route. Calibrate separately for task difficulty and human quality criteria before making commercial or scalability decisions.
