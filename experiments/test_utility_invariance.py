from fractions import Fraction as Q
from itertools import product
import unittest
from matching_audit import action
from utility_invariance import (groups, normalize, preserves, is_mixed_ne,
                                mixed_counterexample, binary_scaled_potential,
                                binary_ordinal_only, four_face_cross_difference)


class UtilityInvarianceTests(unittest.TestCase):
    def test_normalizations_and_strict_transitivity(self):
        examples = [binary_scaled_potential(), binary_ordinal_only(),
                    {(a, b): (5, b) for a, b in product(range(2), repeat=2)}]
        for game in examples:
            sizes = (2,) * len(next(iter(game)))
            gs = groups(game, sizes)
            self.assertLessEqual(set(gs['exact']), set(gs['cardinal']))
            self.assertLessEqual(set(gs['cardinal']), set(gs['ordinal']))
            identity = tuple(range(len(sizes)))
            kernels = [{g for g in gs[mode] if g[0] == identity}
                       for mode in ('exact', 'cardinal', 'ordinal')]
            self.assertEqual(kernels[0], kernels[1])
            self.assertEqual(kernels[1], kernels[2])
            levels = [sorted({row[i] for row in game.values()}) for i in range(len(sizes))]
            for g in gs['ordinal']:
                self.assertEqual(g in gs['exact'], all(levels[i] == levels[g[0][i]]
                                                       for i in range(len(sizes))))
                for i in range(len(sizes)):
                    if g[0][i] == i:
                        self.assertTrue(all(game[s][i] == game[action(g, s)][i] for s in game))
            for mode in ('cardinal', 'ordinal'):
                normalized = normalize(game, mode)
                self.assertEqual(set(gs[mode]), set(groups(normalized, sizes)['exact']))
        scaled = groups(examples[0], (2, 2, 2))
        ordinal = groups(examples[1], (2, 2, 2))
        self.assertEqual(len({g[0] for g in scaled['exact']}), 1)
        self.assertEqual(len({g[0] for g in scaled['cardinal']}), 6)
        self.assertEqual(len({g[0] for g in ordinal['cardinal']}), 2)
        self.assertEqual(len({g[0] for g in ordinal['ordinal']}), 6)

    def test_ordinal_automorphism_preserves_pure_but_not_mixed_ne(self):
        game = mixed_counterexample()
        swap = ((1, 0), ((0, 1), (0, 1)))
        self.assertTrue(preserves(game, swap, 'ordinal'))
        self.assertFalse(preserves(game, swap, 'cardinal'))
        laws = ((Q(2, 3), Q(1, 3)), (Q(1, 2), Q(1, 2)))
        self.assertTrue(is_mixed_ne(game, laws))
        self.assertFalse(is_mixed_ne(game, laws[::-1]))
        pure_ne = {s for s in game if all(game[s][i] >= game[s[:i] + (1-s[i],) + s[i+1:]][i]
                                         for i in range(2))}
        self.assertEqual(pure_ne, {(0, 1), (1, 0)})
        self.assertEqual(pure_ne, {action(swap, s) for s in pure_ne})

    def test_potential_strength_separations(self):
        # A weighted potential can fail the exact-potential face identity.
        scaled = binary_scaled_potential()
        self.assertEqual(four_face_cross_difference(scaled, 0, 1, (0, 0, 0)), (2, 4))
        # An ordinal potential need not be a positive weighted exact potential:
        # proportional nonzero cross differences are necessary, but 0 != 2/w.
        ordinal = binary_ordinal_only()
        self.assertEqual(four_face_cross_difference(ordinal, 0, 1, (0, 0, 0)), (0, 2))


if __name__ == '__main__':
    unittest.main()
