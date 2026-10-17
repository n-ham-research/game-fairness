# Phase 10 — equal opportunity and the obstruction to global symmetry

Recovered and completed 18 October 2026 from the 17 October staged derivation.
Nicholas Ham programme; internal Codex work. These are graph-theoretic
applications answering foundational fairness questions, not new graph theory.

## P10-O1: complete opportunity equality with prescribed structural limitations

Let G be a connected simple d-regular graph, d>=1. Roles are its vertices,
actions are binary, and common monetary receipts are

    u_i(a)=(1/d) sum_(j adjacent i) 1[a_i=a_j].

In a choice-after-assignment experiment announce a separate opponent ordering
for each role, placing its d neighbors first. A common state t is the ordered
binary vector of all opponents under that correspondence. These physical
correspondences are data, not assumed game automorphisms. Every role then has
EXACTLY the same focal table r_i(b,t)=sum_(l<=d)1[b=t_l]/d. Consequently all
roles have identical opportunities for every common correlated opponent law
and every common increasing utility on monetary receipts. Both actions are
decision-essential: an independent full-support law putting probability3/4
on label b makes b uniquely optimal, with expected receipts3/4 versus1/4.
No passive role, duplicate action, directed influence or uncalibrated offset
is used.

Nevertheless the full exact typed game automorphism group is Aut(G) x C2,
where C2 simultaneously complements all actions. Thus its player image is
Aut(G), and player transitivity holds iff G is vertex-transitive.

Proof: the essential opponent arguments of u_i are precisely its neighbors;
bijective coordinate relabelings preserve essential dependence. Any player
permutation in a typed automorphism must therefore preserve graph adjacency.
Every graph automorphism itself preserves receipts. Remove this player map
from an arbitrary typed automorphism and write the remaining binary flips as
x_i -> epsilon_i x_i in spin coordinates. Since
u_i=1/2+(x_i/(2d))sum_(j adjacent i)x_j, uniqueness of Boolean multilinear
coefficients forces epsilon_i epsilon_j=1 on each edge. Connectivity makes
all signs equal. Both global signs work and commute with player permutations.
Every role attains the same finite range {0,1/d,...,1}; an increasing bijection
of this ordered range is the identity. Hence cardinal and ordinal typed
automorphisms also coincide with this exact group. This is not a general
permission to compare independent utility representations as welfare.

## P10-O2: a strong negative answer even for reciprocal interactions

Take the twelve-vertex Hamilton cycle 0--1--...--11--0 and chords
(0,7),(1,11),(2,10),(3,5),(4,9),(6,8). The exact adjacency backtracking search
checks edges AND nonedges and returns only the identity. This is a connected
cubic rigid graph. Its game has identical essential focal opportunities but
NO interchange of distinct players at exact, cardinal or ordinal level.
A short analytic rigidity certificate also avoids relying on exhaustion. Color
each vertex by its number of neighbor-neighbor edges, then repeatedly replace
its color by the lexicographic rank of (own color, sorted neighbor colors).
The initial colors are [1,1,0,1,1,1,1,1,1,0,0,1]. Four rounds give respectively
[3,2,1,2,2,3,3,3,2,1,0,2], [5,3,1,3,3,5,6,6,4,1,0,2],
[7,4,1,5,5,8,9,9,6,2,0,3], [8,4,1,5,6,9,11,10,7,2,0,3].
Every color is then distinct. Graph automorphisms preserve each refinement,
so every vertex is fixed. This uses standard color refinement only as a
finite proof certificate, not a symmetry-identification research extension.

Any nonidentity player permutation with any local flips has some monetary
receipt discrepancy at least1/3: all discrepancies are integer multiples of
1/3 and O1 excludes their all vanishing.

More broadly, the established connected cubic graph realization theorem,
combined with O1, realizes any finite abstract group as a player image despite
identical focal opportunities. This is a direct corollary of deep PRIOR,
not an assertion about a prescribed permutation action on fixed roles.
Within this class d=1 gives K2 and d=2 gives cycles, both transitive; d=3
already admits rigidity. No degree threshold for arbitrary games follows.

## P10-O3: coherence cannot be recovered from identity-forgetting depth alone

The rooted nonbacktracking universal cover of every cubic graph vertex is the
same rooted cubic tree. Every finite-depth anonymous UNFOLDED interaction view
therefore agrees across the rigid graph's roles. This forgets whether two
walks meet the SAME actual opponent, so it cannot recover cycle closure.
Actual induced graph balls differ already at radius1 in this witness (some
neighbor sets contain an edge and others do not). No claim about indistinguish-
ability under all local experiments, persistent identities, actual graph balls
or simultaneous recipient records is made. P8's shared controller wiring is
a different resource. The missing compatibility is a property of jointly
identified interactions, not something supplied by equal separate role values.

## P10-O4: cycle parity gives a constructive local-to-global obstruction

Give each undirected edge a bit b_ij and use receipts

    u_i(a)=(1/d) sum_(j adjacent i) 1[a_i XOR a_j=b_ij].

Each focal table is again the common coordination table after complementing
that focal role's opponent j by b_ij. Essential calibrated opportunities still
agree. These independent incident recodings may fail to fit a common controller.

A proposed player permutation p lifts to a typed game automorphism iff it is
a graph automorphism preserving the F2 sum of b on EVERY cycle. Indeed the
spin-coefficient argument gives the exact required equations

    b_(p(i),p(j)) XOR b_ij = e_i XOR e_j.

Summing around a cycle proves necessity. Conversely choose e_root=0 and
propagate e along a spanning tree using these equations. Each nontree edge
is then verified by its fundamental cycle's zero discrepancy parity. This
constructs a lift in O(|V|+|E|) bit operations AFTER p is supplied. There are
exactly two lifts, related by global complement. Graph automorphism enumeration
is not claimed polynomial. The player image is the stabilizer of the signing
class in F2^E modulo the cut space. No splitting theorem is asserted.

For K4 with only b_01=1, the odd triangles are012 and013. Any liftable
permutation preserves their common edge{0,1}. Conversely every permutation
preserving that edge preserves the signing. The player image is S2 x S2,
with two orbits, despite vertex transitivity of the underlying unsigned graph
and identical essential local opportunities. Exhaustive24*16 typed-map tests
agree with the independent spanning-tree lift solver.

## Literature, originality and verification

Graphical games are established; the earlier branch inspected Kearns–Littman–
Singh's UAI2001 primary author PDF, sections1/3. The precise tools here are
standard graph automorphisms, universal covers and SIGNED-GRAPH SWITCHING.
[Zaslavsky, Six Signed Petersen Graphs](https://arxiv.org/pdf/1303.3347), section 8.1,
already develops switching automorphisms. The source currently served has a
November 27, 2024 internal date despite its 2013 arXiv identifier; do not silently
call that body the original2013 version. The branch also inspected Zaslavsky 1982
Proposition 3.2 for cycle-sign characterization. These are close mathematical
PRIOR, not merely adjacent vocabulary.

[Krebs–Verbitsky](https://arxiv.org/pdf/1407.3175), section 2.1, supplies standard
universal-cover comparisons. The cubic realization input uses the corrected
construction in [Simplicial surfaces with given automorphism group](https://link.springer.com/article/10.1007/s10801-025-01424-4), section 3/Theorem 3.5;
that primary article identifies an oversight in an older Frucht construction.
The general existence corollary does not rely on adopting that old formula.
These primary bodies were reopened on18 October; exact finite witness/group
claims here are separately proved and tested. No third-party PDF is tracked.

Six reconstructed exact tests check rigidity, all 2^11 focal states, essentiality,
small complete typed groups, unfolded views versus actual balls, and signedK4.
Earlier temporary tests passed but were lost on restart; these are new retained
checks. The negative conclusion strengthens P7's directed witness substantially
in model scope. O4 supplies a concrete algebraic obstruction, but is a direct
application of known switching theory, not a novel general fairness invariant.
