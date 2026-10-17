import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase10_risk_opportunities import BASE,DIRECTIONS,menus,weights,dot,value,rankone_certificate,unique_witnesses

class RiskOpportunityTests(unittest.TestCase):
    def test_physical_lotteries(self):
        for row in (*menus(),BASE):
            for k in (0,2):
                first,second=row[k:k+2];probs=(1-first,first-second,second)
                self.assertEqual(sum(probs),1);self.assertTrue(all(p>=0 for p in probs))

    def test_rankone_certificate(self):
        for j,k,l in product(range(1,12),range(1,8),range(1,8)):
            p=F(j,12);d=(F(k,3),F(l,3));w=weights(p,d)
            self.assertGreaterEqual(dot(DIRECTIONS[rankone_certificate(w)],w),0)
            self.assertEqual(value(menus(),p,d),value((*menus(),BASE),p,d))

    def test_state_dependent_separator_and_essential_rows(self):
        w=(F(1),F(1,10),F(1,10),F(1))
        self.assertTrue(all(dot(h,w)<0 for h in DIRECTIONS))
        self.assertGreater(dot(BASE,w),max(dot(row,w) for row in menus()))
        self.assertEqual(len(unique_witnesses()),4)

    def test_variable_risk_essentiality(self):
        rows=((F(9,10),F(1,10)),(F(3,5),F(2,5)))
        self.assertEqual(sum(rows[0]),sum(rows[1]))
        self.assertGreater(dot(rows[0],(2,1)),dot(rows[1],(2,1)))
        self.assertLess(dot(rows[0],(1,2)),dot(rows[1],(1,2)))

if __name__=='__main__':unittest.main()
