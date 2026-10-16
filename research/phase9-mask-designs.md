# Phase 9 — minimal masks and an elementary five-opponent proof

16 October 2026. Candidate applications; novelty unclaimed. P8-O4 retains
its original hypotheses: all reference profiles for each available uniform
subset context, common action alphabet, exact commitment expectations.
A context is a whole matrix, not one scalar, sample or bit.

## P9-M1: general bounds and a combinatorial interpretation

P8-O4 decomposes the common kernel into partition shapes with at most k
rows and first row shorter than r. Thus a surviving shape is a diagram fitting
inside a k by (r−1) rectangle. Such a diagram with m boxes exists iff
m≤k(r−1). This explains the threshold combinatorially, but is NOT an
independent elementary proof: Schur–Weyl decomposition and branching supply
the correspondence between diagrams and invisible tensors.

For a chosen collection of r-subsets, scalar matrix rank remains an exact
criterion. A single mask has rank q=k^{m−r} binomial(k+r−1,r), since it fixes
the outside word and only the histogram inside. Every mask rowspace contains
the fully symmetric space of dimension h=binomial(k+m−1,m). Therefore d
contexts have joint rank at most h+d(q−h). If q>h, full recovery requires
 d≥ceil((k^m−h)/(q−h)).
If q=h<k^m no number suffices. This is only a lower bound, not a claimed
optimal design theorem.

A sharper standard representation bound uses any tensor Specht constituent:
if it has dimension f_lambda and its S_r-fixed subspace dimension b_lambda,
then d contexts contribute at most d*b_lambda of its dimensions. Thus full
recovery requires d≥ceil(f_lambda/b_lambda) for every occurring constituent,
with b_lambda=0 forbidding recovery. Schur multiplicity cancels from this
bound. Both are rowspace dimension arguments, not new representation theory.

## P9-M2: exactly five triple contexts suffice and are necessary

Take m=5 opponents, binary action labels, and uniform triple masks. The
complete collection has ten contexts; the minimum is FIVE. One optimum is

  012, 013, 014, 023, 024.

Here indices are zero based. The following proof does not use Schur–Weyl
or branching, giving a separate elementary reconstruction for this case.

Identify a binary word with x in {−1,+1}^5. Its payoff table has the unique
Walsh expansion f(x)=sum_{A⊆{0,...,4}} c_A product_{i∈A}x_i. Permuting
coordinates permutes the coefficient subsets. Uniform triple masks preserve
subset size, so analyze coefficient degrees separately. Complementation of
subsets identifies degrees d and5−d equivariantly. Degrees0 and5 are
constant one-dimensional modules, never in a nonzero mask kernel.

Degree1 is a vector a_i. Vanishing of a triple average forces every outside
coordinate zero and sum of inside coordinates zero. For a family of triples,
the common invisible vectors are those supported in their intersection and
having total sum zero. Hence degree1 (and4) recovery holds iff that
intersection has size at most1.

Degree2 is the edge-coefficient space a_ij on K5, dimension10. Define
(Ca)_i=sum_{j≠i} a_ij. The unsigned vertex-edge incidence C has rank5:
a linear dependence of its rows gives v_i+v_j=0 for every edge, and a triangle
forces all v_i=0. Thus H=ker C has dimension5. The map C commutes with
all permutations and hence all masks. If degree1 is recovered and every
chosen mask kills a, then every mask kills Ca and consequently a lies in H.

For a triple B with complement {u,v}, an invariant vector in H has coefficients
A on B's internal edges, D on its edges to u, E on its edges to v, and F
on edge uv. The vertex constraints read
  2A+D+E=0, 3D+F=0, 3E+F=0.
They determine A,D,E from F; the invariant subspace has dimension1.
For any a∈H its averaged uv coefficient is STILL a_uv, since uv is fixed.
Therefore the triple mask kills a exactly when a_uv=0. Since each mask
has rank1 on the five-dimensional H, fewer than five cannot recover all
tables, regardless of the degree1 behavior. This proves the lower bound.

For the displayed five triples, their complementary observed edges are
34,24,23,14,13. A commonly invisible a∈H is zero on these edges, hence
supported on F={01,02,03,04,12}. Vertex constraints at3 and4 force a03=a04=0;
constraints at0,1,2 on the remaining triangle force all three edge coefficients
zero. The triple intersection is {0}, so degree1 is recovered too. Thus
degree2 is recovered; complementation handles3,4. This proves all32
coefficients are recovered, without relying on exhaustive rank evidence.

### All five-context designs: a graph characterization

For any collection of five DISTINCT triples let E be their complementary
edges and F the remaining five edges of K5. Full recovery holds iff the graph
F is connected and has a unique cycle of odd length.

Necessity: H-supported invisible vectors are the kernel of C restricted to
F. A square unsigned incidence matrix on five vertices/five edges is
invertible iff every connected component is odd unicyclic. To prove this,
a connected bipartite component has incidence rank v−1, while a connected
nonbipartite component has rank v, by the row-dependence equation above.
Full column independence plus full row rank therefore requires e=v in every
component and nonbipartiteness, exactly one odd cycle. On five vertices,
two disjoint odd unicyclic components are impossible. Hence F must be
connected odd unicyclic.

Sufficiency: such F has invertible incidence, killing the H obstruction.
The triple intersection equals the vertices isolated in E. At most one
vertex can be isolated in E: two would force F to contain all seven edges
incident to those two vertices, but F has only five. Thus degree1 is recovered.
The preceding intertwining argument then finishes recovery of degree2/3 and
all other degrees. This supplies an explicit optimal-design test for this
small setting, not a universal hypergraph criterion for arbitrary m,k,r.

## Scrutiny and novelty

P8-O4's representation proof was independently reconstructed by the Phase9
symmetry agent. The rectangle interpretation and Specht rank bound use the
same established ingredients. P9-M2's Walsh/incidence proof is a new internal
proof route for this finite design problem; originality has NOT been established.
Walsh/Fourier analysis on the Boolean cube and unsigned graph-incidence
ranks are standard mathematics. Equivalent designs may already be known
under symmetrizer ranks, invariant observations or graph-based experimental
design; no publication priority claim is made. It is not communication
complexity in bits, and exact measurements still require noise analysis.
