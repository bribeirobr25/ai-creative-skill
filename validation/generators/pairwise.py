"""Deterministic greedy pair coverage over a deliberately small, bounded domain."""
from itertools import combinations, product

def pairs(row):
    return {(a, row[a], b, row[b]) for a, b in combinations(sorted(row), 2)}

def generate(domains):
    keys = sorted(domains)
    candidates = [dict(zip(keys, values)) for values in product(*(domains[k] for k in keys))]
    uncovered = set().union(*(pairs(row) for row in candidates))
    selected = []
    while uncovered:
        best = max(candidates, key=lambda row: len(pairs(row) & uncovered))
        selected.append(best)
        uncovered -= pairs(best)
        candidates.remove(best)
    return selected

def coverage(domains, rows):
    keys = sorted(domains)
    required = {(a, x, b, y) for a, b in combinations(keys, 2)
                for x in domains[a] for y in domains[b]}
    seen = set().union(*(pairs(row) for row in rows))
    return {'required_pairs': len(required), 'covered_pairs': len(required & seen),
            'missing_pairs': len(required - seen), 'rows': len(rows)}
