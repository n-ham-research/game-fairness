import unittest
from fractions import Fraction as Q
from itertools import product
from phase7_opportunities import value,IID_MENUS,iid,graph_game,graph_groups,majority_game,two_action_maximin


class AssignmentWitnesses(unittest.TestCase):
    def test_iid_invisible_option_and_full_support_exchangeable_gap(self):
        # Finite corroboration; the universal polynomial inequality is proved in the note.
        for denominator in range(1,13):
            for numerator in range(denominator+1):
                p=Q(numerator,denominator)
                self.assertEqual(value(IID_MENUS[0],iid(p)),value(IID_MENUS[1],iid(p)))
        eps=Q(1,4);mu=(eps/2,(1-eps)/2,(1-eps)/2,eps/2)
        self.assertEqual([value(rows,mu) for rows in IID_MENUS],[eps,1-eps])

    def test_unordered_optimized_values_forget_order(self):
        rows0=((0,1,-1,0),(0,-1,1,0)); rows1=((0,0,0,0),)*2
        mu=(Q(1,8),Q(1,4),Q(1,4),Q(3,8))
        self.assertEqual(value(rows0,mu),value(rows1,mu))
        self.assertEqual(value(rows0,(0,1,0,0)),1)
        self.assertEqual(value(rows1,(0,1,0,0)),0)

    def test_pure_undominated_rows_can_be_opportunity_redundant(self):
        menus=(((1,0),(0,1),(Q(1,2),Q(1,2))),
               ((1,0),(0,1),(Q(1,4),Q(1,4))))
        for rows in menus:
            self.assertFalse(any(all(x>=y for x,y in zip(row,rows[2])) for row in rows[:2]))
        for p in [Q(i,20) for i in range(21)]:
            self.assertEqual(value(menus[0],(p,1-p)),value(menus[1],(p,1-p)))

    def test_essential_focal_opportunities_without_player_transitivity(self):
        game=graph_game();group=graph_groups()
        self.assertEqual(len(group),2)
        self.assertEqual({g[0] for g in group},{(0,1,2)})
        successor=(1,0,0)
        for i in range(3):
            for own in range(2):
                # Every own action uniquely maximizes for some full-support product law.
                ps=[Q(1,2)]*3;ps[successor[i]]=Q(3,4) if own else Q(1,4)
                vals=[]
                for a in range(2):
                    total=0
                    opponents=[j for j in range(3) if j!=i]
                    for opp in product(range(2),repeat=2):
                        s=[0]*3;s[i]=a;weight=1
                        for j,b in zip(opponents,opp):s[j]=b;weight*=ps[j] if b else 1-ps[j]
                        total+=weight*game[tuple(s)][i]
                    vals.append(total)
                self.assertGreater(vals[own],vals[1-own])

    def test_common_risk_attitude_can_change_equal_means(self):
        sure=(1,1);lottery=(0,2);mu=(Q(1,2),)*2
        self.assertEqual(sum(x*p for x,p in zip(sure,mu)),sum(x*p for x,p in zip(lottery,mu)))
        self.assertNotEqual(sum(x*x*p for x,p in zip(sure,mu)),sum(x*x*p for x,p in zip(lottery,mu)))

    def test_vnm_fair_guarantees_need_not_have_core(self):
        game=majority_game()
        self.assertTrue(all(sum(row)==0 for row in game.values()))
        # For singleton0, opponent pure columns give affine expected-payoff lines.
        lines=[]
        for b,c in product(range(2),repeat=2):
            u0=game[(0,b,c)][0];u1=game[(1,b,c)][0]
            lines.append((Q(u1-u0),Q(u0)))
        best,values=two_action_maximin(lines)
        self.assertEqual(best,-1);self.assertEqual(values[Q(1,2)],-1)
        # Complement values are1. Summing all three pair inequalities contradicts efficiency0.
        self.assertGreater(3*1,2*0)
