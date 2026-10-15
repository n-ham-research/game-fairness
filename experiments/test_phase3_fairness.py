"""Exact separating examples for assignment, information and preference tests."""
from fractions import Fraction
from itertools import combinations, product
import unittest
from matching_audit import action, bijections


def automorphism_images(game, sizes):
    return {g[0] for g in bijections(sizes)
            if all(row[i] == game[action(g, s)][g[0][i]]
                   for s, row in game.items() for i in range(len(sizes)))}


class AssignmentExamples(unittest.TestCase):
    def test_focal_opportunities_without_simultaneous_role_transport(self):
        successor = (1, 0, 0)
        game = {s: tuple(2*s[i]+s[successor[i]] for i in range(3))
                for s in product(range(2), repeat=3)}
        self.assertEqual(automorphism_images(game, (2, 2, 2)), {(0, 1, 2)})
        for i in range(3):
            other = next(j for j in range(3) if j not in (i, successor[i]))
            table = {(s[i], s[successor[i]], s[other]): row[i]
                     for s, row in game.items()}
            self.assertEqual(table, {s: 2*s[0]+s[1] for s in game})

    def test_equal_optimal_values_without_equal_payoff_menus(self):
        game = {s: (1-s[0], 1-2*s[1]) for s in product(range(2), repeat=2)}
        self.assertEqual(automorphism_images(game, (2, 2)), {(0, 1)})
        self.assertEqual([max(row[i] for row in game.values()) for i in range(2)], [1, 1])
        self.assertNotEqual({row[0] for row in game.values()}, {row[1] for row in game.values()})

    def test_aggregate_tests_hide_ordered_opponent_effects(self):
        game = {s: tuple(s[i]+s[(i+1)%3]-s[(i+2)%3] for i in range(3))
                for s in product(range(2), repeat=3)}
        for i in range(3):
            for a in range(2):
                for count in range(3):
                    values = [row[i] for s, row in game.items()
                              if s[i] == a and sum(s)-a == count]
                    self.assertEqual(Fraction(sum(values), len(values)), a)
        self.assertNotEqual(game[(0, 1, 0)][0], game[(0, 0, 1)][0])

    def test_uniform_equality_and_noninvariant_selection_separations(self):
        game = {s: (2*s[0]+s[1], 3-2*s[0]-s[1]) for s in product(range(2), repeat=2)}
        self.assertEqual([Fraction(sum(row[i] for row in game.values()), 4)
                          for i in range(2)], [Fraction(3, 2)]*2)
        self.assertEqual(automorphism_images(game, (2, 2)), {(0, 1)})
        symmetric = {s: s for s in product(range(2), repeat=2)}
        self.assertIn((1, 0), automorphism_images(symmetric, (2, 2)))
        self.assertNotEqual(*symmetric[(0, 1)])

    def test_zero_coalition_values_do_not_force_transitive_roles(self):
        game = {s: (s[0]-s[1], s[1]-s[0], 0) for s in product(range(2), repeat=3)}
        images = automorphism_images(game, (2, 2, 2))
        self.assertEqual({p[2] for p in images}, {2})
        for size in range(4):
            for coalition in combinations(range(3), size):
                outsiders = tuple(i for i in range(3) if i not in coalition)
                matrix = []
                for a in product(range(2), repeat=size):
                    row = []
                    for b in product(range(2), repeat=len(outsiders)):
                        profile = [0]*3
                        for i, value in zip(coalition, a): profile[i] = value
                        for i, value in zip(outsiders, b): profile[i] = value
                        row.append(sum(game[tuple(profile)][i] for i in coalition))
                    matrix.append(row)
                self.assertEqual(max(map(min, matrix)), 0)
                self.assertEqual(min(max(row[j] for row in matrix)
                                     for j in range(len(matrix[0]))), 0)

    def test_ordinal_and_mixed_preference_tests_are_different(self):
        u = (0, 1, 2)
        v = (0, 1, 4)
        self.assertTrue(all((u[a] <= u[b]) == (v[a] <= v[b])
                            for a in range(3) for b in range(3)))
        certain = (Fraction(0), Fraction(1), Fraction(0))
        lottery = (Fraction(1, 2), Fraction(0), Fraction(1, 2))
        expectation = lambda payoffs, law: sum(a*p for a, p in zip(payoffs, law))
        self.assertEqual(expectation(u, certain), expectation(u, lottery))
        self.assertLess(expectation(v, certain), expectation(v, lottery))


if __name__ == '__main__':
    unittest.main()
