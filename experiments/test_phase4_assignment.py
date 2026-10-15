"""Concrete history and utility-group consequences, with exact witnesses."""
import unittest
from matching_audit import action, multiply
from phase3_splitting import binary_payoff_code, game, predicted_group
from utility_invariance import groups
# Migration adaptation: local explicit witness avoids importing the companion
# project's unrelated restriction/classification stack. Original test source is
# recorded in the migration manifest.
from itertools import product

def orientation_game():
    def value(s):
        if len(set(s)) != 3:
            return 0
        return (-1) ** sum(s[i] > s[j] for i in range(3) for j in range(i + 1, 3))
    return {s: (value(s),) * 3 for s in product(range(3), repeat=3)}


class CalibratedAssignmentTests(unittest.TestCase):
    def test_individual_transports_and_repeated_exchange_kernel(self):
        payoffs = game(binary_payoff_code)
        group = predicted_group()
        swap = next(g for g in group if g[0] == (1, 0, 2))
        twice = multiply(swap, swap)
        self.assertEqual(twice[0], (0, 1, 2))
        self.assertNotEqual(action(twice, (0, 0, 0)), (0, 0, 0))
        for s, row in payoffs.items():
            self.assertEqual(payoffs[action(twice, s)], row)
            for i in range(3):
                transport = next(g for g in group if g[0][0] == i)
                self.assertEqual(payoffs[action(transport, s)][i], row[0])

    def test_orientation_obstruction_persists_for_all_utility_groups(self):
        found = groups(orientation_game(), (3, 3, 3))
        self.assertEqual(len(found['exact']), 18)
        self.assertEqual(set(found['exact']), set(found['cardinal']))
        self.assertEqual(set(found['cardinal']), set(found['ordinal']))


if __name__ == '__main__':
    unittest.main()
