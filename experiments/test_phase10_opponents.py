import unittest
from fractions import Fraction as F
from itertools import product
from experiments.phase10_opponents import hidden_value_two_actions,reactive_value,common_minimizers,hidden_plan,reactive_plan

class OpponentTimingTests(unittest.TestCase):
    def test_binary_matrices_timing_bound(self):
        for data in product((F(0),F(1,2),F(1)),repeat=4):
            matrix=(data[:2],data[2:]);s,_=hidden_value_two_actions((matrix,),(1,));r=reactive_value((matrix,),(1,))
            self.assertGreaterEqual(s,r);self.assertLessEqual(s-r,(1-r)/2)

    def test_sharp_family_all_action_counts(self):
        for n in range(1,7):
            for c in (F(0),F(1,4),F(1)):
                matrix=tuple(tuple(c+(1-c)*(a!=t) for t in range(n)) for a in range(n))
                self.assertEqual(reactive_value((matrix,),(1,)),c)
                self.assertEqual(hidden_plan(matrix,(F(1,n),)*n),c+(1-c)*(1-F(1,n)))

    def test_planwise_criterion(self):
        for data in product((0,1,2),repeat=4):
            matrix=(data[:2],data[2:]);sigma=(F(1,3),F(2,3))
            self.assertEqual(hidden_plan(matrix,sigma)==reactive_plan(matrix,sigma),bool(common_minimizers(matrix)))

    def test_optimized_equality_can_hide_plan_gap(self):
        matrix=((1,0),(0,1),(1,1))
        self.assertFalse(common_minimizers(matrix))
        self.assertEqual(reactive_value((matrix,),(1,)),1)
        self.assertEqual(hidden_plan(matrix,(0,0,1)),1)
        self.assertGreater(hidden_plan(matrix,(F(1,2),F(1,2),0)),reactive_plan(matrix,(F(1,2),F(1,2),0)))

    def test_role_preference_reversal(self):
        risky=((1,0),(0,1));safe=((F(1,4),)*2,)*2
        s,_=hidden_value_two_actions((risky,),(1,));r=reactive_value((risky,),(1,))
        self.assertEqual(s,F(1,2));self.assertEqual(r,0)
        self.assertGreater(s,F(1,4));self.assertLess(r,F(1,4))
        self.assertEqual(hidden_value_two_actions((safe,),(1,))[0],F(1,4))

    def test_observation_does_not_uniformize(self):
        self.assertGreater(F(0+1,2),F(1,4));self.assertLess(min(0,1),F(1,4))

    def test_multiple_classes_one_common_action(self):
        classes=(((1,0),(0,1)),((0,0),(1,1)))
        prior=(F(1,2),F(1,2));s,p=hidden_value_two_actions(classes,prior)
        self.assertEqual(s,F(1,2));self.assertGreaterEqual(s,reactive_value(classes,prior))
        # Observing the class before action would instead give 3/4.
        self.assertLess(s,F(3,4))

    def test_affine_calibration(self):
        matrix=((1,0),(0,1));scaled=tuple(tuple(3*x+2 for x in row) for row in matrix)
        self.assertEqual(hidden_value_two_actions((scaled,),(1,))[0],F(7,2))
        self.assertEqual(reactive_value((scaled,),(1,)),2)

    def test_four_player_embedding(self):
        for own in (0,1):
            values=[int(own==opp2) for opp2,opp3 in ((0,1),(1,0))]
            self.assertEqual(values,([1,0] if own==0 else [0,1]))
            self.assertEqual(min(values),0)

if __name__=='__main__':unittest.main()
