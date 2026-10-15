"""Exact finite-game utilities. Exhaustive algorithms for small games only."""
from itertools import permutations, product


def compose(tau, pi):
    """tau after pi; permutations use zero-based player indices."""
    return tuple(tau[pi[i]] for i in range(len(pi)))


def inverse(pi):
    result = [0] * len(pi)
    for i, j in enumerate(pi):
        result[j] = i
    return tuple(result)


def permute(pi, profile):
    """Left coordinate action: result[pi[i]]=profile[i]."""
    result = [None] * len(pi)
    for i, j in enumerate(pi):
        result[j] = profile[i]
    return tuple(result)


def symmetries(payoffs, n):
    """All label-preserving symmetries of a common-action game."""
    return tuple(pi for pi in permutations(range(n)) if all(
        payoffs[s][i] == payoffs[permute(pi, s)][pi[i]]
        for s in payoffs for i in range(n)))


def inverse_condition(payoffs, n):
    return all(payoffs[s][i] == payoffs[permute(inverse(pi), s)][pi[i]]
               for pi in permutations(range(n)) for s in payoffs for i in range(n))


def common_payoffs(payoffs):
    return all(len(set(row)) == 1 for row in payoffs.values())


def automorphisms(payoffs, sizes):
    """Enumerate exact player/strategy automorphisms; labels are local integers.

    A component maps the action of player i to the action of player pi[i].
    Unequal cardinalities forbid that player mapping. This is intentionally
    factorial, for small-game counterexamples rather than large classification.
    """
    n = len(sizes)
    for pi in permutations(range(n)):
        if any(sizes[i] != sizes[pi[i]] for i in range(n)):
            continue
        for maps in product(*(tuple(permutations(range(m))) for m in sizes)):
            good = True
            for s, row in payoffs.items():
                t = [None] * n
                for i in range(n):
                    t[pi[i]] = maps[i][s[i]]
                if any(row[i] != payoffs[tuple(t)][pi[i]] for i in range(n)):
                    good = False
                    break
            if good:
                yield pi, maps


def player_transitive(player_permutations, n):
    perms = tuple(player_permutations)
    return all({pi[i] for pi in perms} == set(range(n)) for i in range(n))


def binary_game(n, payoff):
    return {s: tuple(payoff(s, i) for i in range(n)) for s in product(range(2), repeat=n)}
