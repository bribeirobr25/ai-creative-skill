"""Illustrative cost-to-accepted-asset model, NOT empirical provider performance."""
import argparse, json, math, random
from dataclasses import asdict, dataclass, replace

@dataclass(frozen=True)
class Assumptions:
    trials: int = 2000
    seed: int = 20261020
    budget_cents: int = 300
    commercial_attempt_cents: int = 150
    local_acceptance: float = .45
    commercial_acceptance: float = .75
    availability: float = .95
    technical_success: float = .95
    uncertain_outcome: float = .03
    human_intervention: float = .10
    local_minutes: float = 4
    commercial_minutes: float = 1
    human_minutes: float = 8

STRATEGIES = {'local_only': ('local',)*3,
              'commercial_only': ('commercial',)*3,
              'local_first_hybrid': ('local', 'commercial', 'commercial')}

def percentile(values, q):
    if not values: return None
    return sorted(values)[max(0, math.ceil(len(values)*q)-1)]

def simulate(a, strategy):
    if strategy not in STRATEGIES: raise ValueError('Unknown strategy')
    if a.trials <= 0 or a.budget_cents < 0 or a.commercial_attempt_cents < 0: raise ValueError('Invalid counts/cost')
    for p in (a.local_acceptance, a.commercial_acceptance, a.availability,
              a.technical_success, a.uncertain_outcome, a.human_intervention):
        if not 0 <= p <= 1: raise ValueError('Invalid probability')
    rng = random.Random(a.seed); records = []
    for _ in range(a.trials):
        spent = 0; minutes = 0; accepted = False; stop = 'ATTEMPT_CAP'; attempts = 0
        for route in STRATEGIES[strategy]:
            if rng.random() > a.availability: continue
            cost = a.commercial_attempt_cents if route == 'commercial' else 0
            if spent + cost > a.budget_cents: stop = 'BUDGET_CAP'; break
            spent += cost  # conservative reservation includes uncertain submission
            attempts += 1
            minutes += a.commercial_minutes if route == 'commercial' else a.local_minutes
            if rng.random() < a.uncertain_outcome:
                stop = 'UNKNOWN_RECONCILE'; break  # never retry uncertain jobs
            if rng.random() > a.technical_success: continue
            if rng.random() < a.human_intervention: minutes += a.human_minutes
            p = a.commercial_acceptance if route == 'commercial' else a.local_acceptance
            if rng.random() < p: accepted = True; stop = 'ACCEPTED'; break
        records.append((spent, minutes, accepted, stop, attempts))
    costs = [r[0]/100 for r in records]; elapsed = [r[1] for r in records]
    accepted_times = [r[1] for r in records if r[2]]; n = len(accepted_times)
    return {'strategy': strategy, 'trials': a.trials, 'accepted': n,
            'acceptance_rate': n/a.trials,
            'mean_reserved_cash_usd': sum(costs)/a.trials,
            'cash_per_accepted_asset_including_failed_jobs_usd': sum(costs)/n if n else None,
            'cash_quantiles_usd': {str(q): percentile(costs,q) for q in (.5,.9,.95)},
            'elapsed_all_outcomes_minutes': {str(q):percentile(elapsed,q) for q in (.5,.9,.95)},
            'time_to_acceptance_minutes_conditional_on_acceptance': {str(q):percentile(accepted_times,q) for q in (.5,.9,.95)},
            'budget_overrun_count':sum(r[0]>a.budget_cents for r in records),
            'stops':{s:sum(r[3]==s for r in records) for s in ('ACCEPTED','BUDGET_CAP','UNKNOWN_RECONCILE','ATTEMPT_CAP')},
            'mean_attempts':sum(r[4] for r in records)/a.trials}

def sensitivity(a=None):
    a = a or Assumptions()
    variants = {'base':a, 'local_quality_low':replace(a,local_acceptance=.20),
                'local_quality_high':replace(a,local_acceptance=.75),
                'commercial_quality_low':replace(a,commercial_acceptance=.45),
                'availability_low':replace(a,availability=.65),
                'uncertainty_high':replace(a,uncertain_outcome=.15)}
    return {'classification':'ILLUSTRATIVE_ASSUMPTIONS_NOT_EMPIRICAL',
            'limits':['Fictional prices and independent Bernoulli draws; no provider calibration',
                      'No campaign correlations, queueing, learning, refunds or monetary labor/energy cost',
                      'Cost is conservative reserved cash, not verified billed cash',
                      'Conditional acceptance times exclude failures; inspect acceptance rate too',
                      'Three attempts maximum; strategies have intentionally different route mixes'],
            'experiments':{name:{'assumptions':asdict(v),'results':[simulate(v,s) for s in STRATEGIES]} for name,v in variants.items()}}

if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    from pathlib import Path
    Path(a.output).write_text(json.dumps(sensitivity(),indent=2)+'\n')
