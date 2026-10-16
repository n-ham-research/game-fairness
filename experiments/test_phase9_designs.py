import unittest
from fractions import Fraction as F
from itertools import combinations,product
from phase9_designs import (displacement,defect,optimal_value,mask_design_rank,
                            unselected_graph_is_odd_unicyclic)
from phase8_observations import rational_rank,apply

class MinimalAndStableTests(unittest.TestCase):
    def test_cycle_discrepancy_recovery(self):
        g=(1,2,0,4,3,5);u=tuple(map(F,[2,5,1,7,-1,20]))
        d=displacement(g,u)
        # One omitted coordinate per cycle is determined; last cycle fixed.
        reconstructed=(d[0],d[1],-d[0]-d[1],d[3],-d[3],F(0))
        self.assertEqual(reconstructed,d)
        # Cycle averages lose every nonzero candidate discrepancy.
        self.assertEqual(sum(d[:3]),0);self.assertEqual(sum(d[3:5]),0)
        self.assertTrue(any(d))

    def test_approximate_maps_not_group(self):
        u=(F(0),F(3,4),F(3,2));g=(1,0,2);h=(0,2,1)
        gh=tuple(g[h[i]] for i in range(3))
        self.assertLessEqual(defect(g,u),1);self.assertLessEqual(defect(h,u),1)
        self.assertGreater(defect(gh,u),1)
        self.assertLessEqual(defect(gh,u),defect(g,u)+defect(h,u))

    def test_noise_overlap_at_margin(self):
        alpha,eps,eta=F(1,5),F(2),F(1,5)
        center=alpha*eps
        shared=center/2
        self.assertEqual(abs(shared),eta)
        self.assertEqual(abs(shared-center),eta)
        # Near uniform bias hides a fixed antisymmetric discrepancy.
        for q in [F(51,100),F(5001,10000)]:
            d=(F(1),F(-1)); y=(q*d[0]+(1-q)*d[1],q*d[1]+(1-q)*d[0])
            self.assertEqual(max(map(abs,y)),abs(2*q-1))

    def test_linear_class_need_not_recover_utilities(self):
        # D for a swap has rank1; contrast alone decides status in R2.
        self.assertEqual(rational_rank([[1,-1]]),1)
        for a,b in product(range(3),repeat=2):
            self.assertEqual(a==b,(a-b)==0)
        # Invariant mean direction is unnecessary for membership.
        self.assertEqual(apply([[1,-1]],[7,7]),[0])

    def test_value_bound_all_small_menus(self):
        eps=F(1,4)
        for values in product(range(3),repeat=4):
            rows=[tuple(map(F,values[:2])),tuple(map(F,values[2:]))]
            target=[(r[0]+eps,r[1]-eps) for r in rows]
            for p in [F(0),F(1,3),F(1)]:
                self.assertLessEqual(abs(optimal_value(rows,(p,1-p))-
                                         optimal_value(target,(p,1-p))),eps)

    def test_five_context_graph_criterion_exhaustive(self):
        triples=list(combinations(range(5),3))
        # Independent actual matrix ranks for all 252 five-context choices.
        for design in combinations(triples,5):
            self.assertEqual(mask_design_rank(design)==32,
                             unselected_graph_is_odd_unicyclic(design),design)

    def test_no_four_context_design_recovers(self):
        triples=list(combinations(range(5),3))
        best=max(mask_design_rank(design) for design in combinations(triples,4))
        self.assertEqual(best,30)
        self.assertEqual(mask_design_rank([(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4)]),32)

if __name__=='__main__':unittest.main()
