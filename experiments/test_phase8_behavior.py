"""Exact counterexample and operational checks, not proofs of general claims."""
import unittest
from fractions import Fraction as F
from itertools import product
from phase8_observations import apply

class BehaviorTests(unittest.TestCase):
    def test_announced_mixture_changes_opportunity(self):
        def row(p): return p,1-p*p
        value=lambda x: sum(x,F(0))/2
        self.assertEqual(value(row(F(1,2))),F(5,8))
        self.assertEqual(max(value(row(F(0))),value(row(F(1)))),F(1,2))
        # Exact completed square certifies the global optimum on [0,1].
        for p in map(lambda n:F(n,20),range(21)):
            self.assertEqual(F(5,8)-value(row(p)),(p-F(1,2))**2/2)

    def test_shared_controller_observes_invisible_real_difference(self):
        K=[[F(1,2),F(1,2)]]; d=[F(1),F(-1)]
        self.assertEqual(apply(K,d),[0])
        # Two singleton candidate players swap; a binary opponent is fixed.
        u=lambda i,t: d[t] if i==1 else F(0)
        for i in [0,1]:
            discrepancy=[u(1-i,t)-u(i,t) for t in range(2)]
            self.assertEqual(apply(K,discrepancy),[0])
            self.assertTrue(any(discrepancy))

    def test_equilibrium_selection_vs_invariant_recommendation(self):
        payoff=lambda a,b: (2,1) if (a,b)==(0,0) else ((1,2) if (a,b)==(1,1) else (0,0))
        for a,b in product(range(2),repeat=2):
            self.assertEqual(payoff(1-b,1-a),payoff(a,b)[::-1])
        p,q=F(2,3),F(1,3)
        self.assertEqual(2*q,1-q)
        self.assertEqual(p,2*(1-p))
        self.assertEqual(2*q,F(2,3))
        law={(0,0):F(1,2),(1,1):F(1,2)}
        receipts=tuple(sum(w*payoff(*s)[i] for s,w in law.items()) for i in range(2))
        self.assertEqual(receipts,(F(3,2),F(3,2)))
        # Every correlated-recommendation deviation inequality is checked.
        for i,a,b in product(range(2),repeat=3):
            diff=F(0)
            for s,w in law.items():
                if s[i]==a:
                    t=list(s);t[i]=b
                    diff+=w*(payoff(*s)[i]-payoff(*t)[i])
            self.assertGreaterEqual(diff,0)

    def test_observable_coherence_quotient(self):
        # C4 -> C2: every odd lift squares to a nonzero kernel element.
        for lift in [1,3]:
            defect=(lift+lift)%4
            self.assertEqual(defect,2)
            self.assertEqual(defect%2,0)
        # Full-label observation distinguishes that defect at every state.
        self.assertTrue(all((x+2)%4!=x for x in range(4)))

    def test_calibration_and_risk_are_different(self):
        x=[0,2]; y=[1,1]; w=[F(1,2),F(1,2)]
        mean=lambda a:sum(p*z for p,z in zip(w,a))
        self.assertEqual(mean(x),mean(y))
        self.assertNotEqual(mean([z*z for z in x]),mean([z*z for z in y]))
        self.assertNotEqual(mean([z+1 for z in x]),mean(y))
        # Rolewise minmax removes affine freedom but changes the physical test.
        norm=lambda a:tuple((z-min(a))/(max(a)-min(a)) for z in a)
        self.assertEqual(norm([F(0),F(2)]),norm([F(7),F(13)]))

    def test_equal_security_unequal_opportunities(self):
        rows=[(F(0),F(0)),(F(1),F(-1))]
        # Any mixture has worst coordinate -p; max at p=0 has value0.
        for p in [F(0),F(1,3),F(1)]:
            self.assertEqual(min(p,-p),-p)
        self.assertEqual(max(r[0] for r in rows),1)
        self.assertEqual(max(r[0] for r in [(0,0)]),0)

if __name__=='__main__':unittest.main()
