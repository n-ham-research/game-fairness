"""Exact observation matrices for pair-hidden opponent identities.

No third-party packages, sampling, or precomputed dimension formula are used.
"""
from fractions import Fraction
from itertools import permutations, product


def profiles(m, k):
    return list(product(range(k), repeat=m))


def observation_matrix(m, k, edges):
    tuples = profiles(m, k)
    index = {t: j for j, t in enumerate(tuples)}
    rows = []
    for r, s in edges:
        if not 0 <= r < s < m:
            raise ValueError("An edge must have 0 <= r < s < m")
        for t in tuples:
            swapped = list(t)
            swapped[r], swapped[s] = swapped[s], swapped[r]
            row = [0] * len(tuples)
            row[index[t]] += 1
            row[index[tuple(swapped)]] += 1
            rows.append(row)
    return rows


def rational_rank(rows):
    """Sparse incremental exact elimination of an observation matrix."""
    basis = {}
    for row in rows:
        vector = {j: Fraction(x) for j, x in enumerate(row) if x}
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                leading = vector[pivot]
                basis[pivot] = {j: x / leading for j, x in vector.items()}
                break
            scale = vector[pivot]
            for j, x in basis[pivot].items():
                value = vector.get(j, 0) - scale * x
                if value:
                    vector[j] = value
                else:
                    vector.pop(j, None)
    return len(basis)


def alternating(t, selected=None):
    if selected is None:
        selected = tuple(range(len(t)))
    if sorted(t) != list(selected):
        return 0
    inversions = sum(t[i] > t[j] for i in range(len(t)) for j in range(i+1, len(t)))
    return (-1) ** inversions


def signed_game(s):
    return tuple((-1) ** i * alternating(s[:i] + s[i+1:]) for i in range(len(s)))


def permute_profile(s, p):
    out = [None] * len(s)
    for i, image in enumerate(p):
        out[image] = s[i]
    return tuple(out)


def summary():
    cases = [
        (2, 2, [(0, 1)]),
        (3, 2, [(0, 1)]),
        (3, 2, [(0, 1), (1, 2)]),
        (3, 3, [(0, 1), (1, 2)]),
        (4, 3, [(0, 1), (1, 2)]),
        (4, 3, [(0, 1), (1, 2), (2, 3)]),
        (4, 2, [(0, 1), (2, 3)]),
    ]
    return [dict(opponents=m, actions=k, edges=edges,
                 rank=rational_rank(observation_matrix(m, k, edges)),
                 entries=k**m) for m, k, edges in cases]


if __name__ == '__main__':
    import json
    print(json.dumps(summary(), indent=2))
