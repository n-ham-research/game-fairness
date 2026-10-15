"""Exact counterexample to the converse of Ham 5.6; no dependencies beyond stdlib.

Strategy labels are residues modulo 4. All three player sets are explicitly
identified with Z/4, and typed maps retain their player projection.
"""
from itertools import permutations, product
import json
from pathlib import Path
from matching_audit import action, bijections, multiply, strategy_trivial, transitive


def payoff_code(d, e):
    if d == e:
        return 0 if d == 0 else 1 if d == 1 else 2
    return 2 if (d, e) == (0, 1) else 1


def binary_payoff_code(d, e):
    return int(d < e and d <= 1)


def game(code=payoff_code):
    result = {}
    for s in product(range(4), repeat=3):
        row = []
        for i in range(3):
            d = (s[(i + 1) % 3] - s[i]) % 4
            e = (s[(i + 2) % 3] - s[i]) % 4
            row.append(code(d, e) if s[i] % 2 == 0 else code(e, d))
        result[s] = tuple(row)
    return result


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def predicted_group():
    return tuple((p, (tuple((a + k) % 4 for a in range(4)),) * 3)
                 for p in permutations(range(3)) for k in range(4)
                 if parity(p) == k % 2)


def verify(binary_payoffs=False):
    payoffs = game(binary_payoff_code if binary_payoffs else payoff_code)
    actual = tuple(g for g in bijections((4, 4, 4))
                   if all(payoffs[s][i] == payoffs[action(g, s)][g[0][i]]
                          for s in payoffs for i in range(3)))
    predicted = predicted_group()
    assert set(actual) == set(predicted)
    identity = (tuple(range(3)), (tuple(range(4)),) * 3)
    kernel = tuple(g for g in actual if g[0] == tuple(range(3)))
    bare_cycles = tuple(g for g in actual if all(f == tuple(range(4)) for f in g[1]))
    assert len(actual) == 12 and len(kernel) == 2
    assert len({g[0] for g in actual}) == 6
    assert len(bare_cycles) == 3 and strategy_trivial(bare_cycles) and transitive(bare_cycles, 3)
    odd_lifts = tuple(g for g in actual if parity(g[0]))
    assert len(odd_lifts) == 6
    assert all(multiply(g, g) != identity and
               multiply(multiply(g, g), multiply(g, g)) == identity for g in odd_lifts)
    assert all(all(v == 0 for v in row) == (len(set(s)) == 1)
               for s, row in payoffs.items())
    # Full subgroup enumeration is tiny here and independently excludes complements.
    from matching_audit import subgroups
    sub = subgroups(actual)
    complements = [h for h in sub if len(h) == 6 and len({g[0] for g in h}) == 6]
    assert not complements
    return {
        'players': 3, 'strategies_per_player': 4, 'profiles': 64,
        'ambient_typed_bijections': 82944, 'payoff_values': sorted({v for row in payoffs.values() for v in row}),
        'automorphism_order': len(actual), 'kernel_order': len(kernel),
        'player_image_order': 6, 'strategy_trivial_transitive_subgroup_order': 3,
        'transposition_lift_orders': [4] * len(odd_lifts),
        'complements': 0, 'subgroups_checked': len(sub),
        'payoffs': [{'profile': s, 'utilities': row} for s, row in payoffs.items()],
    }


if __name__ == '__main__':
    import sys
    binary_payoffs = '--binary-payoffs' in sys.argv
    result = verify(binary_payoffs)
    filename = 'phase3-splitting-binary-results.json' if binary_payoffs else 'phase3-splitting-results.json'
    path = Path(__file__).with_name(filename)
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'payoffs'}, indent=2))
