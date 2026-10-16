"""Exact candidate-symmetry and mask-design evidence."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from phase8_observations import rational_rank, subset_mask

def displacement(permutation, table):
    return tuple(table[permutation[i]]-table[i] for i in range(len(table)))

def matrix_rank(rows): return rational_rank(rows)

def defect(permutation,table):
    return max(map(abs,displacement(permutation,table)),default=0)

def optimal_value(rows,law):
    return max(sum(a*b for a,b in zip(row,law)) for row in rows)

def mask_design_rank(triples):
    return rational_rank([row for t in triples for row in subset_mask(5,2,t)])

def unselected_graph_is_odd_unicyclic(triples):
    vertices=set(range(5)); E={tuple(sorted(vertices-set(t))) for t in triples}
    F_edges=set(combinations(range(5),2))-E
    adj={i:set() for i in range(5)}
    for i,j in F_edges:adj[i].add(j);adj[j].add(i)
    seen={0};stack=[0];color={0:0};odd=False
    while stack:
        i=stack.pop()
        for j in adj[i]:
            if j not in seen: seen.add(j);stack.append(j);color[j]=1-color[i]
            elif color[j]==color[i]:odd=True
    return len(seen)==5 and len(F_edges)==5 and odd
