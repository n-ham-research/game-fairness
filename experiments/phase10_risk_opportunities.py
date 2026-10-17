"""Common-risk rank-one probes versus state-dependent preferences."""
from fractions import Fraction as F
from itertools import product
BASE=(F(3,4),F(1,4),F(3,4),F(1,4))
DIRECTIONS=((-1,F(5,2),0,-1),(-1,0,F(5,2),-1),(1,0,0,-4),(-4,0,0,1))

def menus():return tuple(tuple(BASE[i]+F(1,20)*h[i] for i in range(4)) for h in DIRECTIONS)
def weights(p,d):return tuple(q*x for q in (p,1-p) for x in d)
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def value(menu,p,d):return max(dot(row,weights(p,d)) for row in menu)

def rankone_certificate(w):
    x,y,z,t=w
    assert min(w)>0 and x*t==y*z
    if x>=4*t:return 2
    if t>=4*x:return 3
    assert 4*(x+t)**2<=25*x*t
    assert max(y,z)**2>=x*t
    j=0 if y>=z else 1
    assert dot(DIRECTIONS[j],w)>=0
    return j

def unique_witnesses():
    out={}
    for j,k,l in product(range(1,16),repeat=3):
        p,d=F(j,16),(F(k,4),F(l,4))
        scores=[dot(row,weights(p,d)) for row in menus()]
        winners=[i for i,s in enumerate(scores) if s==max(scores)]
        if len(winners)==1:out.setdefault(winners[0],(p,d))
        if len(out)==4:break
    return out
