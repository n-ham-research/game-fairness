"""Finite rational certificates of information recovery and its failure."""
import unittest
from itertools import combinations, permutations

from phase7_independent_information import (
    alternating, observation_matrix, permute_profile, profiles, rational_rank,
    signed_game,
)


class InformationExperiments(unittest.TestCase):
    def test_binary_three_opponents_two_overlapping_masks_recover(self):
        self.assertEqual(rational_rank(observation_matrix(3, 2, [(0, 1), (1, 2)])), 8)
        for edge in combinations(range(3), 2):
            self.assertEqual(rational_rank(observation_matrix(3, 2, [edge])), 6)

    def test_ternary_cutoff_and_minimality(self):
        self.assertEqual(rational_rank(observation_matrix(3, 3, [(0, 1), (1, 2)])), 26)
        self.assertEqual(rational_rank(observation_matrix(4, 3, [(0, 1), (1, 2), (2, 3)])), 81)
        for edges in combinations(list(combinations(range(4), 2)), 2):
            self.assertLess(rational_rank(observation_matrix(4, 3, edges)), 81)

    def test_disconnected_components_leave_product_ambiguity(self):
        # Two binary alternating matrices can be multiplied: one undetectable direction.
        self.assertEqual(rational_rank(observation_matrix(4, 2, [(0, 1), (2, 3)])), 15)
        self.assertEqual(rational_rank(observation_matrix(4, 3, [(0, 1), (1, 2)])), 78)

    def test_orientation_is_nonzero_but_invisible(self):
        for m, k in [(2, 2), (2, 3), (3, 3)]:
            vector = [alternating(t) for t in profiles(m, k)]
            self.assertTrue(any(vector))
            for row in observation_matrix(m, k, list(combinations(range(m), 2))):
                self.assertEqual(sum(a*b for a, b in zip(row, vector)), 0)

    def test_ordinal_robustness_uses_distributions_not_means(self):
        self.assertEqual(sum((0, 2)), sum((1, 1)))
        self.assertNotEqual(sum(x*x for x in (0, 2)), sum(x*x for x in (1, 1)))
        for m in (2, 3):
            for t in profiles(m, m):
                for r, q in combinations(range(m), 2):
                    swapped = list(t)
                    swapped[r], swapped[q] = swapped[q], swapped[r]
                    x = (alternating(t), alternating(tuple(swapped)))
                    self.assertEqual(sorted(x), sorted(-v for v in x))
                    # Every increasing three-level calibration has identical sums.
                    for phi in ({-1: 0, 0: 1, 1: 7}, {-1: -8, 0: 2, 1: 3}):
                        self.assertEqual(sum(phi[v] for v in x), sum(phi[-v] for v in x))

    def test_simultaneous_game_transport_counterexample(self):
        for n in (3, 4):
            m = n-1
            p = tuple([1, 0] + list(range(2, n)))
            discrepancies = set()
            for s in profiles(n, m):
                original = signed_game(s)
                transported = signed_game(permute_profile(s, p))
                for i in range(n):
                    self.assertEqual(transported[p[i]], -original[i])
                    discrepancies.add(transported[p[i]]-original[i])
            self.assertNotEqual(discrepancies, {0})
            for i in range(n):
                for a in range(m):
                    vector = []
                    for t in profiles(m, m):
                        s = t[:i] + (a,) + t[i:]
                        target = signed_game(permute_profile(s, p))[p[i]]
                        vector.append(target-signed_game(s)[i])
                    for row in observation_matrix(m, m, list(combinations(range(m), 2))):
                        self.assertEqual(sum(x*y for x, y in zip(row, vector)), 0)


if __name__ == '__main__':
    unittest.main()
