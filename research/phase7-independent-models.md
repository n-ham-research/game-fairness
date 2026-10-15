# Phase 7: independent information experiments and exact recovery

Research candidates, 16 October 2026. Author: Nicholas Ham. Developed in the
Phase 7 independent fairness agent pass. These are elementary information-
identification theorems, with novelty unclaimed; no claim that information loss
itself makes a game fair. They extend F1–F3 rather than repeat their conclusion.

## 1. A fixed participant experiment

One participant has a calibrated von Neumann–Morgenstern utility over the
consequences of every role assignment. It need not equal the other people's
utilities: in the game comparison below this identification is an additional
explicit hypothesis. The role, physical action correspondences and full table
are disclosed before assignment. The participant chooses an action after
learning the role; the following tests compare every available action, not
only the optimized value. All comparisons use one common cardinal scale.
These values can be elicited by offering a commitment contract for each
corresponding action (a singleton menu), together with a calibrated monetary
side payment. Indifference between two such contracts tests equality of their
expected utilities. The requirement is therefore indifference under every
specified action restriction; it is stronger than indifference when the
participant can freely optimize. We do not infer it from optimized indifference.
Opponent behavior is exogenous and independent of that action. Common opponent
action labels form a finite set A of size k. There are m≥2 opponents.

A designated pair {r,s} of opponent positions has hidden identities: conditional
on an ordered reference profile t, the participant assigns equal probabilities
to t and the profile τ_rs t obtained by exchanging those two positions. Other
positions remain distinguished. The experiment can be repeated with different
pairs. Thus no single experiment need disclose every identity. Equal expected
utility in these comparisons is behaviorally defined independently of any
automorphism group.

For two conditional consequence tables f,h:A^m→R, define their discrepancy
d=f−h. The pair-hidden tests are

    E_rs(d)(t) = (d(t)+d(τ_rs t))/2 = 0, for every t.

The same tests result if the hidden pair chooses IID actions with a common
arbitrary law q, the distinguished opponents have arbitrary independent laws,
and all these laws are varied. Indeed Dirac laws fix distinguished positions.
The expectation on the pair is the quadratic polynomial Σ_ab d(a,b)q_a q_b.
Its coefficients recover d(a,a) and d(a,b)+d(b,a). Vanishing on the probability
simplex implies vanishing as a homogeneous polynomial (scale positive vectors
and then use polynomial identity). Conversely those coefficients plainly
suffice. Full-support laws alone give the same conclusion by continuity.

## 2. Sharp recovery theorem for several masking experiments

**P7-O1 (pair-mask identification).** Let E be any nonempty collection of
unordered opponent pairs, interpreted as edges of a graph on the m positions.
Write its connected-component sizes as r_1,…,r_l, including isolated vertices.
The tables invisible to every pair-hidden experiment are exactly the tables
alternating in the coordinates of each component. Their vector-space dimension
is

    product_j binomial(k,r_j),

where binomial(k,r)=0 for r>k. Consequently all ordered table entries are
identified exactly when some connected component has more than k vertices.

Proof. Passing the test on an edge is d(τt)=−d(t). Edge transpositions generate
the full permutation group of their connected component: along a path one can
express the transposition of its endpoints by a word in its edge transpositions.
Each such word has odd length, because its sign is −1. More generally the sign
of every word equals the parity of its number of transpositions. Hence the
edge identities imply d(πt)=sgn(π)d(t) for every permutation within a component;
there is no dependence on a chosen word. The converse follows immediately.
If a component has repeated action labels, a transposition fixes t and forces
d(t)=−d(t), so its value is zero. Otherwise choose an unordered r_j-element
subset of A in that component. One coefficient specifies the values of all its
orderings by their permutation signs. Choices across components are independent,
giving precisely the displayed dimension and a basis obtained by their products.
If every r_j≤k at least one basis coefficient exists; if some r_j>k none does. ∎

**Corollary P7-O2 (optimal number of masking contexts).** If m>k, k pair-hidden
contexts suffice to identify the entire table: choose the k edges of a path on
k+1 positions, with every remaining position distinguished. Fewer than k contexts
never suffice uniformly over payoff tables. If m≤k, even all pair contexts fail.

Proof. A connected component with k+1 vertices requires at least k edges.
Conversely the path has the required component. The final assertion follows
from P7-O1. ∎

For example, with binary actions and three opponents, hiding positions {1,2}
in one experiment and {2,3} in another suffices, even though each experiment
leaves a different pair unresolved. With two binary opponents, the alternating
matrix [[0,1],[-1,0]] remains invisible. With three ternary opponents, the
orientation tensor (+1 for even orderings of 0,1,2, −1 for odd, zero otherwise)
remains invisible even when every pair is tested. These are sharp thresholds,
not probabilistic approximations. Cardinal calibration is essential for the
averaging formula.

## 3. Exact utility automorphisms emerge under sufficient information

Fix a disclosed typed bijection g=(p;(f_j)) of a finite n-player game, with
m=n−1 opponents and k common physical labels after transport. For each focal
participant i and action a define

    d_i,a(t)=u_{p(i)}(g(a,t))−u_i(a,t).

Assume the participant's cross-role utility really is the corresponding u_i
on one calibrated scale, and the g correspondence is physically admissible.
Apply the preceding pair-hidden tests to these conditional consequence tables.
If the masking graph has a component larger than k, passing every focal,
every-action test is equivalent to g being an exact game automorphism.
Necessity is exact payoff preservation; sufficiency is P7-O1 for every i,a.
No symmetry condition was used in specifying the information experiment.

For all equal k-action games with n≥k+2, this gives a characterization using
only k masking contexts per focal participant. It is not a characterization
of optimized role indifference, interpersonal equality, or arbitrary hidden-
identity experiments. Focal tests for just one participant still do not imply
simultaneous preservation of the other players' utility tables.

The cutoff is sharp even for simultaneous game tests. Let m=n−1≤k, choose m
labels, and let Alt(t) be +1/−1 on their even/odd orderings and zero otherwise.
Index players 0,…,m and list opponents in their original index order. Set

    u_i(s)=(-1)^i Alt(s_-i).

For any player permutation p,

    u_{p(i)}(P_p s)=sgn(p)u_i(s).

To check the sign, the permutation between the two ordered deleted-index lists
has sign sgn(p)(−1)^{i+p(i)}; multiply by the focal factors. Thus a bare odd
player permutation is not an exact automorphism, but its discrepancy is −2u_i,
which is alternating in every opponent pair. Every pair-hidden test passes
for every participant and every own action. These examples use three utility
values. They are elementary alternating arrays; no novelty is claimed for
that construction or its signed covariance.

## 4. IID and exchangeability have the same linear identifying power

**P7-O3.** For fixed m,k, a table d has zero expectation under every IID law
q^⊗m if and only if its average on every opponent-action histogram is zero.
Equivalently it has zero expectation under every exchangeable law.

Proof. Expand the homogeneous degree-m polynomial

    Σ_t d(t) product_j q_{t_j}
      = Σ_histogram h [Σ_{t:hist(t)=h}d(t)] product_a q_a^{h_a}.

Vanishing on the simplex implies vanishing on the positive orthant by
homogeneity, hence all coefficients vanish. Conversely zero coefficients give
zero expectation. Exchangeable laws are convex combinations of laws uniform
on single histogram orbits, giving the last equivalence. ∎

This is equality of unoptimized expected action values for *every* IID law,
not one chosen IID law. It does not assert that the sets of IID and
exchangeable laws coincide. Optimization before comparison is nonlinear and
can separate their identifying power; see the separate Phase 7 opportunity-
menu investigation. The kernel dimension here is k^m−binomial(m+k−1,k−1),
whereas a connected masking graph leaves only binomial(k,m) dimensions.

## 5. A representation-independent ordinal variant

The following is a distinct decision model, not the assertion that ordinal
utilities can be averaged. Let all assignments yield physical consequences
in one finite, commonly ranked set C={c_1<…<c_R}. The participant's risk attitude
is unspecified. Require assignment indifference robustly for every VNM utility
φ strictly increasing on C. This condition is invariant under representing the
same consequence ordering differently, and requires a common cross-role
ordering rather than independent within-role ordinal data.

**P7-O4 (robust ordinal pair-mask recovery).** Two pair-hidden consequence
lotteries are robustly indifferent if and only if they have identical
probability distributions on C. For a pair mask this is equality of the
unordered multisets {f(t),f(τt)} and {h(t),h(τt)}. Under a collection of pair
masks whose graph has a component larger than k, robust equality for all t
is equivalent to pointwise equality f=h. This information threshold remains
sharp: the alternating examples of Section 3 pass even these robust tests
when m≤k.

Proof. For lotteries X,Y let z_r=Pr(X=c_r)−Pr(Y=c_r), so Σ_r z_r=0.
Writing each increasing φ as a constant plus positive successive increments,
Eφ(X)−Eφ(Y) is a linear combination of the upper-tail sums Σ_{r≥j}z_r,
with arbitrary positive coefficients. If it vanishes for all such choices,
every tail sum is zero, hence every z_r=0. Conversely equal distributions
plainly suffice. Equal two-point uniform distributions are exactly equal
multisets. Robust equality includes the particular increasing encoding
φ(c_r)=r. Apply P7-O1 to the two resulting numerical tables to get equality
of those encodings, and hence f=h. Finally a swap changes Alt to −Alt, so
{Alt(t),Alt(τt)}={−Alt(t),−Alt(τt)} for every pair; zeros cause no exception. ∎

The finite tail-sum fact is standard lottery theory (compare the existing
primary-source annotation of Bogomolnaia–Moulin 2001, §§4 and 7, in
fairness-literature-solutions.md); our direct proof asserts no new utility
representation theorem.

This robust criterion can be incomplete for comparisons other than equality;
no unique participant's risk preferences are inferred. It concerns one common
physical consequence ranking. It does not characterize the game's ordinal
automorphism group, whose increasing recodings may be different for each
recipient. Nor does it identify equal ordinal rankings across roles with
equal welfare for distinct people. Its main benefit is a precise operational
separation between known cardinal utility, robustness to risk attitudes over
common ordered consequences, and independent role-specific representations.

## 6. Representation limits and next questions

If common utility is replaced by αu+β with α>0, all equality tests and the
identification conclusions survive. Independent affine recalibrations by role
need not preserve assignment equality. Pure ordinal information alone cannot
justify the expected averages: independent increasing transformations can
change whether a pair-hidden expectation vanishes. For example averages of
(0,2) and (1,1) coincide, but squaring the nonnegative consequences separates
the averages. Equal averages therefore should not be named ordinal fairness.

The results concern recovery of the utility data from specific information
experiments. They do not imply participants gain from observing identities,
do not determine the morally appropriate information policy, and do not
establish equality of optimized role opportunities. A next useful question is
which masking designs recover only strategically relevant differences after
dominated actions and calibrated action menus are taken into account.

Computational check: experiments/phase7_independent_information.py and its
tests compute rational ranks of the actual observation matrices, independently
of the dimension formula, and check the simultaneous signed-game obstruction.
