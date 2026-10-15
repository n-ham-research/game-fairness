"""Finite exact/cardinal/ordinal groups and rational witness checks.

Min-max normalization uses Fraction; rank normalization counts distinct levels,
so ties are retained. Pure-order tests are independent of the normalizers.
"""
from fractions import Fraction
from itertools import product
from matching_audit import action, bijections


def normalize(game, mode):
    n = len(next(iter(game)))
    levels = [sorted({row[i] for row in game.values()}) for i in range(n)]
    if mode == 'cardinal':
        def code(i, x):
            lo, hi = levels[i][0], levels[i][-1]
            return Fraction(x - lo, hi - lo) if hi != lo else Fraction(0)
    elif mode == 'ordinal':
        ranks = [{x: k for k, x in enumerate(values)} for values in levels]
        def code(i, x):
            return ranks[i][x]
    else:
        raise ValueError(mode)
    return {s: tuple(code(i, row[i]) for i in range(n)) for s, row in game.items()}


def preserves(game, g, mode):
    n = len(next(iter(game)))
    profiles = tuple(game)
    for i in range(n):
        pairs = [(game[s][i], game[action(g, s)][g[0][i]]) for s in profiles]
        if mode == 'exact':
            if any(x != y for x, y in pairs):
                return False
        elif mode == 'ordinal':
            if any((x <= z) != (y <= w) for x, y in pairs for z, w in pairs):
                return False
        elif mode == 'cardinal':
            lo, ylo = min(pairs)
            hi, yhi = max(pairs)
            if lo == hi:
                if any(y != ylo for x, y in pairs):
                    return False
            else:
                a = Fraction(yhi - ylo, hi - lo)
                if a <= 0 or any(y - ylo != a * (x - lo) for x, y in pairs):
                    return False
        else:
            raise ValueError(mode)
    return True


def groups(game, sizes):
    return {mode: tuple(g for g in bijections(sizes) if preserves(game, g, mode))
            for mode in ('exact', 'cardinal', 'ordinal')}


def expected_action(game, i, a, opponent_laws):
    """Opponent laws indexed by player, excluding i; all entries rational."""
    result = Fraction(0)
    for s, row in game.items():
        if s[i] != a:
            continue
        weight = Fraction(1)
        for j, law in opponent_laws.items():
            weight *= law[s[j]]
        result += weight * row[i]
    return result


def is_mixed_ne(game, laws):
    for i, law in enumerate(laws):
        vals = [expected_action(game, i, a, {j: q for j, q in enumerate(laws) if j != i})
                for a in range(len(law))]
        best = max(vals)
        if any(p > 0 and vals[a] != best for a, p in enumerate(law)):
            return False
    return True


def mixed_counterexample():
    first = ((0, 3), (2, 1))
    second = ((0, 4), (9, 1))
    return {(a, b): (first[a][b], second[a][b]) for a, b in product(range(2), repeat=2)}


def binary_scaled_potential():
    return {s: tuple((i + 1) * sum(s) ** 2 for i in range(3))
            for s in product(range(2), repeat=3)}


def binary_ordinal_only():
    return {s: (sum(s), sum(s) ** 2, sum(s)) for s in product(range(2), repeat=3)}


def four_face_cross_difference(game, i, j, fixed):
    def utility(a, b, player):
        s = list(fixed)
        s[i], s[j] = a, b
        return game[tuple(s)][player]
    return tuple(utility(1, 1, player) - utility(0, 1, player)
                 - utility(1, 0, player) + utility(0, 0, player)
                 for player in (i, j))
