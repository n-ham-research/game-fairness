import unittest
from fractions import Fraction as F
from itertools import permutations, product, combinations
from experiments.phase10_opportunity_symmetry import graph,rigid_graph,automorphisms,receipt,is_typed,lift

class OpportunitySymmetryTests(unittest.TestCase):
    def test_rigid_regular_witness(self):
        adj=rigid_graph()
        self.assertEqual({len(v) for v in adj},{3})
        self.assertEqual(automorphisms(adj),[tuple(range(12))])
        colors=[sum(j in adj[k] for j,k in combinations(adj[i],2)) for i in range(12)]
        expected=([3,2,1,2,2,3,3,3,2,1,0,2],[5,3,1,3,3,5,6,6,4,1,0,2],
                  [7,4,1,5,5,8,9,9,6,2,0,3],[8,4,1,5,6,9,11,10,7,2,0,3])
        for row in expected:
            signatures=[(colors[i],tuple(sorted(colors[j] for j in adj[i]))) for i in range(12)]
            palette={s:k for k,s in enumerate(sorted(set(signatures)))}
            colors=[palette[s] for s in signatures]
            self.assertEqual(colors,row)
        self.assertEqual(len(set(colors)),12)
        # Spanning traversal also checks connectivity.
        self.assertEqual(lift(adj,tuple(range(12))),(0,)*12)

    def test_all_focal_tables(self):
        adj=rigid_graph()
        for t in product((0,1),repeat=11):
            for own in (0,1):
                expected=F(sum(own==x for x in t[:3]),3)
                for i in range(12):
                    order=sorted(adj[i])+sorted(set(range(12))-{i}-set(adj[i]))
                    a=[0]*12;a[i]=own
                    for j,x in zip(order,t):a[j]=x
                    self.assertEqual(receipt(adj,a,i),expected)

    def test_full_support_essentiality(self):
        for d in range(1,5):
            for label in (0,1):
                values=[F(0),F(0)]
                for t in product((0,1),repeat=d):
                    prob=F(1)
                    for x in t:prob*=F(3,4) if x==label else F(1,4)
                    for own in (0,1):values[own]+=prob*F(sum(own==x for x in t),d)
                self.assertEqual(values[label],F(3,4));self.assertEqual(values[1-label],F(1,4))

    def test_small_typed_groups(self):
        for n,edges in ((2,[(0,1)]),(3,list(combinations(range(3),2))),(4,[(0,1),(1,2),(2,3),(3,0)])):
            adj=graph(n,edges);autos=set(automorphisms(adj))
            actual={(p,f) for p in permutations(range(n)) for f in product((0,1),repeat=n) if is_typed(adj,p,f)}
            self.assertEqual(actual,{(p,(bit,)*n) for p in autos for bit in (0,1)})

    def test_unfolding_is_not_actual_ball(self):
        adj=rigid_graph()
        triangle_counts={sum(j in adj[k] for j,k in combinations(adj[i],2)) for i in range(12)}
        self.assertGreater(len(triangle_counts),1)
        # Nonbacktracking universal-cover levels have sizes 1,3,6,12,... at every root.
        for root in range(12):
            paths=[(root,)];levels=[1]
            for depth in range(1,7):
                paths=[p+(j,) for p in paths for j in adj[p[-1]] if len(p)==1 or j!=p[-2]]
                levels.append(len(paths))
            self.assertEqual(levels,[1]+[3*2**(k-1) for k in range(1,7)])

    def test_signed_cycle_obstruction(self):
        adj=graph(4,combinations(range(4),2));signs=frozenset({(0,1)})
        actual=set()
        for p in permutations(range(4)):
            eps=lift(adj,p,signs)
            lifts={f for f in product((0,1),repeat=4) if is_typed(adj,p,f,signs)}
            expected=set() if eps is None else {eps,tuple(1-x for x in eps)}
            self.assertEqual(lifts,expected)
            if lifts:actual.add(p)
        self.assertEqual(actual,{p for p in permutations(range(4)) if {p[0],p[1]}=={0,1}})
        self.assertEqual(len(actual),4)

if __name__=='__main__':unittest.main()
