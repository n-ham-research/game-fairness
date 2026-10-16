"""Exact finite observation-channel checks; no representation formulas in matrices."""
from fractions import Fraction
from itertools import combinations, permutations, product
from phase7_independent_information import rational_rank


def subset_mask(m, k, subset):
    states = list(product(range(k), repeat=m))
    index = {t: j for j, t in enumerate(states)}
    orders = list(permutations(subset))
    rows = []
    for t in states:
        row = [Fraction(0)] * len(states)
        for order in orders:
            out = list(t)
            for target, source in zip(subset, order):
                out[target] = t[source]
            row[index[tuple(out)]] += Fraction(1, len(orders))
        rows.append(row)
    return rows


def all_subset_masks(m, k, r):
    return [row for subset in combinations(range(m), r)
            for row in subset_mask(m, k, subset)]


def biased_pair(m, k, pair, q):
    states = list(product(range(k), repeat=m))
    index = {t: j for j, t in enumerate(states)}
    rows = []
    for t in states:
        out = list(t)
        out[pair[0]], out[pair[1]] = out[pair[1]], out[pair[0]]
        row = [Fraction(0)] * len(states)
        row[index[t]] += q
        row[index[tuple(out)]] += 1-q
        rows.append(row)
    return rows


def apply(rows, vector):
    return [sum(a*b for a,b in zip(row, vector)) for row in rows]


def ternary_kernel(rows, n):
    return [v for v in product((-1, 0, 1), repeat=n)
            if any(v) and not any(apply(rows, v))]


def consequence_law(weights, table):
    out = {}
    for weight, consequence in zip(weights, table):
        out[consequence] = out.get(consequence, 0) + weight
    return {c: p for c,p in out.items() if p}
