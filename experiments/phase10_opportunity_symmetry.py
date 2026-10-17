"""Exact graph-opportunity and switching checks; no graph-library oracle."""
from fractions import Fraction as F
from itertools import permutations, product, combinations


def graph(n, edges):
    adj=[set() for _ in range(n)]
    for i,j in edges:
        adj[i].add(j); adj[j].add(i)
    return tuple(frozenset(v) for v in adj)


def rigid_graph():
    return graph(12,[(i,(i+1)%12) for i in range(12)]+[(0,7),(1,11),(2,10),(3,5),(4,9),(6,8)])


def automorphisms(adj):
    """Complete backtracking search checking edges AND nonedges."""
    n=len(adj); assigned={};used=set(); result=[]
    def search():
        if len(assigned)==n:
            result.append(tuple(assigned[i] for i in range(n)));return
        i=max((i for i in range(n) if i not in assigned),key=lambda i:sum(j in assigned for j in adj[i]))
        for j in range(n):
            if j in used or len(adj[i])!=len(adj[j]):continue
            if all((k in adj[i])==(assigned[k] in adj[j]) for k in assigned):
                assigned[i]=j;used.add(j);search();used.remove(j);del assigned[i]
    search();return result


def receipt(adj, action, i, signs=frozenset()):
    return F(sum((action[i]^action[j])==int(tuple(sorted((i,j))) in signs) for j in adj[i]),len(adj[i]))


def transformed(action,p,flips):
    out=[0]*len(action)
    for i,j in enumerate(p):out[j]=action[i]^flips[i]
    return tuple(out)


def is_typed(adj,p,flips,signs=frozenset()):
    return all(receipt(adj,transformed(a,p,flips),p[i],signs)==receipt(adj,a,i,signs)
               for a in product((0,1),repeat=len(adj)) for i in range(len(adj)))


def lift(adj,p,signs=frozenset()):
    if any({p[j] for j in adj[i]}!=set(adj[p[i]]) for i in range(len(adj))):return None
    eps={0:0};todo=[0]
    while todo:
        i=todo.pop()
        for j in adj[i]:
            h=int(tuple(sorted((i,j))) in signs)^int(tuple(sorted((p[i],p[j]))) in signs)
            val=eps[i]^h
            if j in eps:
                if eps[j]!=val:return None
            else:eps[j]=val;todo.append(j)
    if len(eps)!=len(adj):raise ValueError('connected graph required')
    return tuple(eps[i] for i in range(len(adj)))
