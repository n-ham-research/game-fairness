"""Counterexamples separating assignment, conditional choice and selection."""
from fractions import Fraction
from itertools import permutations, product
import unittest
from utility_invariance import groups


class AssignmentRuleExamples(unittest.TestCase):
    def test_affine_offsets_change_assignment_values_not_conditional_structure(self):
        profiles = tuple(product(range(2), repeat=2))
        game = {s: s for s in profiles}
        changed = {s: (s[0], s[1]+3) for s in profiles}
        before, after = groups(game, (2, 2)), groups(changed, (2, 2))
        self.assertEqual(set(before['cardinal']), set(after['cardinal']))
        self.assertEqual(set(before['ordinal']), set(after['ordinal']))
        self.assertNotEqual(set(before['exact']), set(after['exact']))
        self.assertEqual([Fraction(sum(row[i] for row in game.values()), 4)
                          for i in range(2)], [Fraction(1, 2)]*2)
        self.assertEqual([Fraction(sum(row[i] for row in changed.values()), 4)
                          for i in range(2)], [Fraction(1, 2), Fraction(7, 2)])

    def test_uniform_assignment_equalizes_people_not_roles(self):
        role_values = (0, 2, 7)
        assignments = tuple(permutations(range(3)))
        expected = [Fraction(sum(role_values[a[i]] for a in assignments), len(assignments))
                    for i in range(3)]
        self.assertEqual(expected, [Fraction(3)]*3)
        self.assertNotEqual(role_values[0], role_values[1])

    def test_invariant_equilibrium_lottery_is_not_its_independent_product(self):
        profiles = tuple(product(range(2), repeat=2))
        game = {s: (int(s[0] != s[1]),)*2 for s in profiles}
        equilibria = [s for s in profiles if all(
            game[s][i] >= game[s[:i]+(1-s[i],)+s[i+1:]][i] for i in range(2))]
        self.assertEqual(equilibria, [(0, 1), (1, 0)])
        self.assertTrue(all(s != s[::-1] for s in equilibria))
        law = {s: Fraction(int(s in equilibria), 2) for s in profiles}
        self.assertTrue(all(law[s] == law[s[::-1]] for s in profiles))
        # Each recommendation's obedience inequality, using the original game.
        for i in range(2):
            for a in range(2):
                incentive = sum(law[s]*(game[s][i]-game[s[:i]+(1-a,)+s[i+1:]][i])
                                for s in profiles if s[i] == a)
                self.assertGreaterEqual(incentive, 0)
        expected_joint = sum(law[s]*game[s][0] for s in profiles)
        expected_product = Fraction(sum(game[s][0] for s in profiles), 4)
        self.assertEqual(expected_joint, 1)
        self.assertEqual(expected_product, Fraction(1, 2))

    def test_vnm_coalition_fairness_changes_under_zero_sum_fixed_payments(self):
        for utilities, fair in [((0, 0), True), ((1, -1), False)]:
            game = {(0, 0): utilities}
            cardinal = groups(game, (1, 1))['cardinal']
            self.assertEqual({g[0] for g in cardinal}, {(0, 1), (1, 0)})
            self.assertEqual(utilities[0] == utilities[1], fair)
            self.assertEqual(sum(utilities), 0)


if __name__ == '__main__':
    unittest.main()
