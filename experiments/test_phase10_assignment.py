import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase10_assignment import values,common_maximizers,reversal

class AssignmentTimingTests(unittest.TestCase):
    def test_all_small_matrices_characterization(self):
        laws=((F(1),F(0)),(F(0),F(1)),(F(1,2),F(1,2)),(F(1,3),F(2,3)))
        for entries in product((-1,0,1),repeat=6):
            rows=(entries[:3],entries[3:])
            blind=[values(rows,law)[0] for law in laws]
            condition=max(rows[0])==max(rows[1]) and bool(common_maximizers(rows))
            self.assertEqual(len(set(blind))==1,condition)

    def test_no_role_information_iff_common_maximizer(self):
        for entries in product((-1,0,1),repeat=6):
            rows=(entries[:3],entries[3:])
            b,i=values(rows,(F(2,7),F(5,7)))
            self.assertLessEqual(b,i)
            self.assertEqual(b==i,bool(common_maximizers(rows)))

    def test_reversal_all_full_support_priors(self):
        for k in range(1,20):
            p=F(k,20);rows=reversal(p)
            self.assertEqual(max(rows[0]),max(rows[1]))
            b,i=values(rows,(F(1,2),F(1,2)))
            self.assertEqual(b,F(1,2));self.assertEqual(i-b,abs(p-F(1,2)))
            scaled=tuple(tuple(3*v+2 for v in r) for r in rows)
            self.assertEqual(values(scaled,(F(1,2),F(1,2))),(3*b+2,3*i+2))

    def test_aligned_stochastic_consequences(self):
        tails=(((F(3,4),F(1,4)),(F(1,2),F(1,3))),((F(1,2),F(1,3)),(F(3,4),F(1,4))))
        for p in (F(1,4),F(3,4)):
            for d in ((1,2),(3,1)):
                r=tuple(sum(w*sum(x*y for x,y in zip(t,d)) for w,t in zip((p,1-p),action)) for action in tails)
                self.assertEqual(values((r,r),(F(2,7),F(5,7))),(max(r),max(r)))

    def test_unused_commitment_counterexample(self):
        rows=((1,0),(1,-1))
        self.assertNotEqual(rows[0],rows[1])
        for k in range(11):self.assertEqual(values(rows,(F(k,10),1-F(k,10))),(1,1))

if __name__=='__main__':unittest.main()
