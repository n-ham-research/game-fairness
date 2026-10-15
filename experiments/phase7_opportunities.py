"""Exact witnesses for assignment choice, information and cooperative limits."""
from fractions import Fraction as Q
from itertools import product
from matching_audit import bijections, action


def value(rows, belief):
    return max(sum(Q(x)*Q(p) for x,p in zip(row,belief)) for row in rows)


IID_MENUS=(((2,0,0,0),(0,0,0,2),(0,0,0,0)),
           ((2,0,0,0),(0,0,0,2),(0,1,1,0)))


def iid(p):
    return ((1-p)**2,(1-p)*p,p*(1-p),p*p)


def graph_game():
    successor=(1,0,0)
    return {s:tuple(int(s[i]==s[successor[i]]) for i in range(3))
            for s in product(range(2),repeat=3)}


def graph_groups():
    """Pure order on a two-valued table fixes 0/1, so all three groups agree."""
    game=graph_game()
    return {g for g in bijections((2,2,2))
            if all(game[action(g,s)][g[0][i]]==game[s][i]
                   for s in game for i in range(3))}


def majority_game():
    out={}
    for s in product(range(2),repeat=3):
        if len(set(s))==1:out[s]=(0,0,0)
        else:
            majority=int(sum(s)>=2)
            out[s]=tuple(1 if a==majority else -2 for a in s)
    return out


def two_action_maximin(lines):
    """Maximize min affine(p) using all exact intersections and endpoints."""
    candidates={Q(0),Q(1)}
    for a,b in lines:
        for c,d in lines:
            if a!=c:
                p=Q(d-b,a-c)
                if 0<=p<=1:candidates.add(p)
    values={p:min(a*p+b for a,b in lines) for p in candidates}
    return max(values.values()),values
