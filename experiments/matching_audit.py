"""Exact typed-bijection/matching audit; no floating point or sampling."""
from itertools import permutations, product
import json
from pathlib import Path
from finite_games import compose, inverse


def bijections(sizes):
    n = len(sizes)
    return tuple((p, f) for p in permutations(range(n))
                 if all(sizes[i] == sizes[p[i]] for i in range(n))
                 for f in product(*(tuple(permutations(range(m))) for m in sizes)))


def multiply(g, h):
    p, f = g
    q, k = h
    return compose(p, q), tuple(tuple(f[q[i]][k[i][a]] for a in range(len(k[i]))) for i in range(len(p)))


def action(g, s):
    p, f = g
    t = [None] * len(p)
    for i in range(len(p)):
        t[p[i]] = f[i][s[i]]
    return tuple(t)


def weakly_anonymous(payoffs, sizes):
    """Label-dependent weak anonymity, defined only for common action sets."""
    if len(set(sizes)) != 1:
        return False
    identity_maps = tuple(tuple(range(m)) for m in sizes)
    return all(payoffs[s][i] == payoffs[action((p, identity_maps), s)][i]
               for p in permutations(range(len(sizes)))
               for s in payoffs for i in range(len(sizes)) if p[i] == i)


def relabel_game(payoffs, g):
    """Transport exact payoffs along a typed game bijection (including players)."""
    result = {}
    for s, row in payoffs.items():
        target = [None] * len(row)
        for i in range(len(row)):
            target[g[0][i]] = row[i]
        result[action(g, s)] = tuple(target)
    return result


def matchings(sizes):
    if len(set(sizes)) != 1:
        return ()
    m = sizes[0]
    return tuple((tuple(range(m)),) + fs for fs in product(tuple(permutations(range(m))), repeat=len(sizes)-1))


def matching_element(f, p):
    return p, tuple(tuple(f[p[i]][inverse(f[i])[a]] for a in range(len(f[i]))) for i in range(len(p)))


def strategy_trivial(group):
    return all(p[i] != i or f[i] == tuple(range(len(f[i]))) for p, f in group for i in range(len(p)))


def transitive(group, n):
    return all({g[0][i] for g in group} == set(range(n)) for i in range(n))


def subgroups(elements):
    """Enumerate all subgroups by adjoining each element and closing products."""
    index = {g: i for i, g in enumerate(elements)}
    table = [[index[multiply(g, h)] for h in elements] for g in elements]
    identity = next(i for i, g in enumerate(elements) if all(table[i][j] == j == table[j][i] for j in range(len(elements))))
    seen = {frozenset([identity])}
    todo = list(seen)
    while todo:
        h = todo.pop()
        for x in range(len(elements)):
            if x in h:
                continue
            k = set(h) | {x}
            while True:
                new = {table[a][b] for a in k for b in k} - k
                if not new:
                    break
                k.update(new)
            frozen = frozenset(k)
            if frozen not in seen:
                seen.add(frozen)
                todo.append(frozen)
    return tuple(tuple(elements[i] for i in sorted(h)) for h in sorted(seen, key=lambda h: (len(h), sorted(h))))


def partition(sizes, group, focal=False):
    """Equality constraints: automorphisms or focal-stabilizer invariance."""
    profiles = tuple(product(*(range(m) for m in sizes)))
    cells = tuple((s, i) for s in profiles for i in range(len(sizes)))
    ids = {c: k for k, c in enumerate(cells)}
    parent = list(range(len(cells)))
    def root(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for g in group:
        for s, i in cells:
            if not focal or g[0][i] == i:
                a, b = root(ids[s, i]), root(ids[action(g, s), i if focal else g[0][i]])
                parent[max(a,b)] = min(a,b)
    return tuple(root(i) for i in range(len(cells)))


def implies(p, q):
    """Every equality imposed by q follows from p."""
    return all(q[i] != q[j] or p[i] == p[j] for i in range(len(p)) for j in range(i))


def union_implies(ps, qs):
    # Assign a distinct integer to every p-block: exact witness if no q follows.
    return all(any(implies(p, q) for q in qs) for p in ps)


def satisfies(values, p):
    return all(p[i] != p[j] or values[i] == values[j] for i in range(len(p)) for j in range(i))


def audit(sizes):
    n = len(sizes)
    ambient = bijections(sizes)
    groups = subgroups(ambient)
    ms = matchings(sizes)
    sn = tuple(permutations(range(n)))
    trans = [g for g in groups if transitive(g, n) and strategy_trivial(g)]
    full = [g for g in trans if len({x[0] for x in g}) == len(sn)]
    mgroups = [tuple(matching_element(m,p) for p in sn) for m in ms]
    weak_m = [partition(sizes,g,True) for g in mgroups]
    weak_g = [partition(sizes,g,True) for g in full]
    std_g = [partition(sizes,g) for g in trans]
    std_m = [partition(sizes,tuple(matching_element(m,p) for p in {x[0] for x in g})) for m in ms for g in trans]
    full_g = [partition(sizes,g) for g in full]
    full_m = [partition(sizes,g) for g in mgroups]
    theorem423 = all(any(set(g) == {matching_element(m,p) for p in {x[0] for x in g}} for m in ms) == strategy_trivial(g) for g in groups if transitive(g,n))
    # Cor5.3: every standard-symmetry constraint implies equal utilities on
    # every tuple of at least one matching, directly checked as partitions.
    cells = [(s,i) for s in product(*(range(m) for m in sizes)) for i in range(n)]
    diag=[]
    for m in ms:
        rows = {tuple(f[a] for f in m) for a in range(sizes[0])}
        p=list(range(len(cells)))
        for s in rows:
            ids=[cells.index((s,i)) for i in range(n)]
            for k in ids: p[k]=ids[0]
        diag.append(tuple(p))
    result=dict(sizes=sizes,ambient=len(ambient),subgroups=len(groups),matchings=len(ms),strategy_trivial_transitive=len(trans),theorem423=theorem423,cor424_repaired=union_implies(weak_m,weak_g) and union_implies(weak_g,weak_m),cor51=union_implies(std_g,std_m) and union_implies(std_m,std_g),cor52=union_implies(full_g,full_m) and union_implies(full_m,full_g),cor53=union_implies(std_g,diag))
    if sizes == (2,2):
        count=0; failures=0
        for values in product(range(2),repeat=8):
            count+=1
            weak=any(satisfies(values,p) for p in weak_m)
            original=any(satisfies(values,partition(sizes,g)) and satisfies(values,partition(sizes,g,True)) for g in full)
            failures += weak != original
        result.update(binary_games=count,original424_failures=failures)
    return result


if __name__ == '__main__':
    results={'method':'All subgroups of full typed bijection group; equality partitions characterize all real payoff assignments exactly. Binary n=2,m=2 additionally exhaustive.', 'domains':[audit(s) for s in [(1,1),(2,2),(3,3),(1,1,1),(2,2,2),(1,2),(1,1,2)]], 'original_counterexample':{'sizes':[2,2], 'payoff_at_every_profile':[0,1]}, 'minimal_counterexample':{'sizes':[1,1], 'payoff_at_every_profile':[0,1]}, 'nonconstant_counterexample':{'sizes':[2,2,2], 'formula':'u_i(s)=10*i+s_i for zero-based i; disjoint player payoff ranges'}, 'failed_strengthening':{'name':'matching pennies', 'sizes':[2,2], 'formula':'u_0(s)=1 if s_0=s_1 else -1; u_1=-u_0', 'automorphism_order':4, 'transitive_strategy_trivial_subgroups':0}}
    Path(__file__).with_name('matching-results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
