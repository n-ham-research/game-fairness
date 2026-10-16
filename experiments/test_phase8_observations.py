import unittest
from fractions import Fraction as F
from itertools import product
from phase8_observations import (all_subset_masks, subset_mask, biased_pair,
                                rational_rank, ternary_kernel, consequence_law)

class ObservationTests(unittest.TestCase):
    def test_larger_masks_threshold(self):
        # Independent matrix ranks on both sides of m > k(r-1).
        for m,k,r,rank in [(3,2,3,4),(4,2,3,14),(5,2,3,32),
                           (3,2,2,8),(3,3,2,26),(4,2,4,5)]:
            self.assertEqual(rational_rank(all_subset_masks(m,k,r)),rank)

    def test_biased_pair_discontinuity(self):
        self.assertEqual(rational_rank(biased_pair(3,2,(0,1),F(1,2))),6)
        for q in [F(0), F(1,3), F(5001,10000), F(1)]:
            self.assertEqual(rational_rank(biased_pair(3,2,(0,1),q)),8)

    def test_incomplete_subset_collection(self):
        one = subset_mask(5,2,(0,1,2))
        self.assertEqual(rational_rank(one),16)
        self.assertEqual(rational_rank(all_subset_masks(5,2,3)),32)

    def test_distribution_recovery_without_mean_recovery(self):
        rows = [[F(1,3),F(2,3)]]
        self.assertEqual(rational_rank(rows),1)
        self.assertEqual(ternary_kernel(rows,2),[])
        # All labelled deterministic tables on three consequences have distinct laws.
        tables = list(product(range(3),repeat=2))
        laws = [consequence_law(rows[0],t) for t in tables]
        self.assertEqual(len({tuple(sorted(x.items())) for x in laws}),len(tables))

    def test_binary_obstruction_criterion(self):
        rows = [[F(1,2),F(1,2)]]
        self.assertEqual(len(ternary_kernel(rows,2)),2)
        self.assertEqual(consequence_law(rows[0],(0,1)),
                         consequence_law(rows[0],(1,0)))

if __name__ == '__main__':
    unittest.main()
