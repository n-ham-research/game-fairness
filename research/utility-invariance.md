# Utility invariance before assignment interpretations

Status: **foundational reconstruction and candidate corollaries**. The three
isomorphism notions and their equilibrium-preservation properties have prior
literature, including Ham's 2011 thesis. No novelty is asserted. The binary
potential consequences depend on the candidate Phase 3 theorem and require its
literature comparison. This file defines mathematical invariants, not fairness.

## U1. Preferences and typed transformations

Let Γ be a finite game with nonempty action sets and real payoff tables u_i.
Write A=product_i A_i. A typed bijection g=(p;(f_i)) consists of a player
permutation p and bijections f_i:A_i→A_{p(i)}. It acts by
(g s)_{p(i)}=f_i(s_i). Compose right to left; for ordinary coordinate
permutations (P_p s)_j=s_{p^{-1}(j)}. Let B be the full typed-bijection group.

Define three subfamilies of B:

- Exact: u_{p(i)}(g s)=u_i(s) for every i,s.
- Cardinal: u_{p(i)}(g s)=a_i u_i(s)+b_i for every i,s, for constants a_i>0,
  b_i which may depend on i and g, but not on the profile.
- Ordinal: u_i(s)≤u_i(t) iff u_{p(i)}(g s)≤u_{p(i)}(g t), for all i,s,t.

Ordinality concerns the complete pure-outcome preorder, including ties. It is
stronger than merely preserving unilateral best responses. Equivalently,
there is a strictly increasing bijection φ_i between the finite payoff ranges
with u_{p(i)}(g s)=φ_i(u_i(s)). Equal source utilities give equal target
utilities by applying the two inequalities; this makes φ_i well-defined.
Strict order and surjectivity follow from the equivalence and the profile
bijection. Conversely such a φ_i preserves precisely the preorder. One may
extend φ_i to a strictly increasing onto real function by linear interpolation
between successive points and positive-slope tails. The theorem does not
require the false claim that every increasing real function has a real inverse.

For von Neumann–Morgenstern preferences, cardinality means equality of the
preorders over **all lotteries on A** after transport, not equality of numerical
expectations. Positive affinity suffices by finite linearity. Necessity also
has an elementary proof. Pull back the target utility to a function v on A.
Choose profiles a,b minimizing and maximizing a nonconstant u. For each z,
its u-value equals the expected utility of the lottery giving b probability
λ=(u(z)−u(a))/(u(b)−u(a)) and a otherwise. Preserved indifference gives
v(z)=(1−λ)v(a)+λv(b), with positive slope by preserved strict endpoint order.
If u is constant, v must be constant and a positive affine relation still
exists. This proof permits correlated profile lotteries. Positive affinity
also preserves independent mixed-profile preferences; no assumption that
products of marginal laws form a convex set is made.

### Independent mixed profiles also suffice, with the full quantifiers

**Foundational proposition, previously asserted by Ham (2011), independently
reproved here.** Suppose two payoff tables u,v on the same finite profile set
have the same weak preference ordering over *all independent mixed profiles*,
using their expected utilities U,V. Then v=a u+b for constants a>0,b.
The affine sufficiency was already proved. Here is a necessity proof that does
not treat arbitrary mixtures of joint product laws as product laws.

If U is constant, pure profiles show u and v are constant and the claim is
immediate. Otherwise let D=product_i Delta(A_i), expressed using free marginal
probability coordinates in its affine hull. Both U and V are polynomials,
affine in each player's whole marginal block separately. D is connected and
compact, so U(D)=[m,M], with m<M. Equality of all weak orders makes
V=f(U) for a well-defined strictly increasing function f on [m,M].

Fix any t in (m,M). There are relative-interior profiles x,y with U(x)<t<U(y),
since interior marginal profiles approximate every boundary profile. For a
subset S of players let h_S(x,y) take marginal x_i on S and y_i otherwise.
The polynomial U(h_S(x,y))−t is not identically zero: on the diagonal x=y=z
it equals U(z)−t, a nonconstant polynomial. A nonzero real polynomial has a
zero set with empty interior. Consequently one may choose x,y in the
nonempty open region U(x)<t<U(y) such that **all** the finitely many hybrid
values avoid t. (Finite unions of such polynomial zero sets have empty
interior, for their product is again a nonzero polynomial.)

Now move from x to y by replacing one entire player's marginal at a time.
The hybrid path starts below t, ends above t, and has no vertex at t, so one
step has endpoints strictly on opposite sides of t. On that segment only one
player's marginal varies: both U and V are affine. U is nonconstant there,
so V=f(U) forces f to be affine on an open interval containing t, with positive
slope. This works for every t in (m,M). A locally affine function on a
connected open interval is globally affine: its locally constant derivative
is constant. Thus f(t)=a t+b throughout (m,M), with a>0. Approach a minimizing
or maximizing pure profile by interior marginal profiles; continuity of U,V
extends the same identity to m and M. Evaluating at every pure profile gives
v=a u+b. ∎

The quantifiers are crucial: comparisons of **all pairs of whole independent
mixed profiles** suffice, but preserving only unilateral best responses or
only comparisons against one fixed opponent law does not. For a typed map,
apply the proposition to v(s)=u_{p(i)}(g s); expected v is exactly the target
expectation under transported marginal laws. Therefore the all-product-profile
and all-joint-lottery preference formulations give the same cardinal group in
finite games, despite their different lottery domains.

## U2. Groups, inclusions and canonical representations

**Foundational proposition.** These families are subgroups and
Aut_exact≤Aut_card≤Aut_ord. For g with player map p and h with player map r,
cardinal coefficients of h g are

a_i^{hg}=a_{p(i)}^h a_i^g,
b_i^{hg}=a_{p(i)}^h b_i^g+b_{p(i)}^h.

They have positive slopes; inverse coefficients are their reciprocal and
appropriately shifted intercept at the inverse player index. Identity has
slope 1 and intercept 0. For ordinal maps compose the finite-range order
bijections; invert them for inverse typed maps. Exact maps are the special
case of identity scalar transformations, and positive affine maps are strictly
increasing. This proves all claims, with no uniqueness of coefficients needed
for constant players. The same arguments give groupoids between games.
The inclusions need not be normal inclusions; no quotient chain is implied.

There are useful exact descriptions. Let m_i=min u_i, M_i=max u_i, and set

c_i(s)=(u_i(s)−m_i)/(M_i−m_i) if M_i>m_i, and c_i(s)=0 otherwise.

Let r_i(s) be the index of u_i(s) in the increasing list of its **distinct**
payoff levels, starting at zero. Tied profiles receive the same rank. Then,
as actual subgroups of the same typed group B,

Aut_card(Γ)=Aut_exact(c),    Aut_ord(Γ)=Aut_exact(r).               (U2)

**Proof.** A cardinal map transports minima and maxima by its same positive
affine relation, so the normalized values agree. Conversely equality of c
forces either two constant tables or two nonconstant tables. In the latter
case take a_i=(M_{p(i)}−m_{p(i)})/(M_i−m_i)>0 and
b_i=m_{p(i)}−a_i m_i. Constants allow any positive slope with a matching
intercept. Equality of ranks is equivalent to equality of all pure-order
comparisons because an order isomorphism takes the kth distinct level to the
kth distinct level. The converse follows as well. ∎

Thus the cardinal group is unchanged by independent positive affine
re-representations of the players, and the ordinal group is unchanged by
independent increasing re-representations. Exact groups need not be unchanged.
These normalizations choose formal representatives of preference structures;
they do not justify interpersonal welfare comparisons.

If every player has at most two utility levels, cardinal and ordinal groups
coincide: an increasing bijection between two levels is affine; constants
map only to constants. If all players' payoff ranges are the *same* two-element
set, exact, cardinal and ordinal groups coincide. In particular the binary-
**payoff** four-action nonsplitting witness P3-S1b in
[phase3-splitting-proof.md](phase3-splitting-proof.md) has all three groups
identical. Its individual-realizability/coherent-implementation obstruction
therefore survives both preference-based notions.

### Range signatures characterize the subgroup gaps

Write L_i for the increasing list of distinct numerical utility levels, and
C_i for the same list min-max normalized (a constant list becomes (0)).
For any *ordinal* automorphism g with player map p,

g is exact iff L_i=L_{p(i)} for every i;
g is cardinal iff C_i=C_{p(i)} for every i.

Indeed the order bijection must send each kth source level to the kth target
level. Numerical equality of the lists makes this map the identity; equality
of normalized lists makes it positive affine. Both converse implications are
immediate. Thus inside Aut_ord the two smaller groups are inverse images of
the stabilizers of these player-level signatures under its actual player
projection. This supplies precise equality conditions: exact and cardinal
groups coincide if all players in each cardinal player orbit share L_i;
cardinal and ordinal groups coincide if all players in each ordinal player
orbit share C_i. These conditions are also necessary. The signatures are
representation data, not interpersonal welfare units.

## U3. A focal-fixed invariance lemma

**Finite-range observation.** If g∈Aut_ord fixes player i, then
u_i(g s)=u_i(s) exactly for every profile s. Its finite-range order bijection
φ_i is now an increasing permutation of one finite linearly ordered set; it
fixes every level. Cardinal and exact maps are special cases. Consequently
all three player projections have the same actual kernel:

ker(q|Aut_exact)=ker(q|Aut_card)=ker(q|Aut_ord).

More generally every player stabilizer preserves that focal player's utility
exactly, even when it only preserves other players' preferences. Thus for
specified admissible transformations fixing a focal player, the exact,
cardinal and ordinal opponent-invariance conditions coincide in finite games.
This does not say those stabilizer *groups* are equal, since their behavior
on other players may differ. The lemma also applies to an individual typed
bijection fixing i which preserves only i's complete pure-outcome preorder.

Ham's strategy-triviality/matching definitions concern only the typed actions,
so they can be imposed unchanged on each of the three groups. Cardinal and
ordinal standard/full symmetry can equivalently be checked as exact symmetry
of c and r, respectively. The original exact numerical notions remain their
stronger common-scale versions; no retroactive redefinition is made.

## U4. Strictness on player positions

The implications for player transitivity are strict, even with three players
and binary actions. Write k=s_0+s_1+s_2.

1. Let u_i=(i+1)k². Every bare player permutation is cardinal (scale
   (p(i)+1)/(i+1)), so its cardinal player image is S_3. The three exact
   payoff ranges {0,i+1,4(i+1),9(i+1)} are distinct, so exact automorphisms
   cannot move players. Exact transitivity fails.
2. Let u_0=u_2=k and u_1=k². All players rank profiles by k, so the ordinal
   player image is S_3. The range {0,1,4,9} is not a positive affine image
   of {0,1,2,3}: ordered endpoint/intermediate spacings disagree. Thus no
   cardinal map moves player 1 to another player. Cardinal transitivity
   fails; the cardinal player image is precisely the order-two group
   interchanging players 0 and 2.

Strategy relabelings cannot evade these range obstructions because every
profile bijection is onto. These are structural equivalence examples; they
supply no interpersonal assignment-utility comparisons.

## U5. What is preserved

Cardinal maps biject mixed best-response correspondences and mixed Nash
profiles: their marginal pushforwards give
U_{p(i)}(g x)=a_i U_i(x)+b_i, and unilateral deviations are bijected by f_i.
The positive coefficient preserves every best-response comparison. Exact maps
have a_i=1,b_i=0. Cardinal maps also transport correlated equilibria, since
each focal incentive inequality is multiplied by a_i>0. Equilibrium payoff
vectors are permuted **and transformed by the relevant positive affine maps**,
not generally kept numerically equal.

Ordinal maps always preserve pure best responses against pure opponent
profiles, pure-strategy dominance comparisons against pure opponent profiles,
and pure Nash equilibria: these use only the corresponding pointwise order
comparisons. They do **not** generally preserve best responses against mixed
opponents, mixed dominance, or mixed Nash profiles. Thus the user's statement
that ordinal maps need not preserve “Nash equilibria” needs the qualification
**mixed**; pure equilibria are preserved.

Here is an ordinal automorphism that fails to preserve a mixed equilibrium.
For two binary players let the row and column payoff matrices be

u_0 = [[0,3],[2,1]],   u_1 = [[0,4],[9,1]].

The bare player swap is ordinal because u_1(swap s)=u_0(s)² and the reverse
relation is the increasing square root on these nonnegative finite levels.
It is not cardinal. With p the probability of row action 0 and q that of
column action 0, row indifference requires q=1/2 and column indifference
requires p=2/3. Hence (p,q)=(2/3,1/2) is a mixed equilibrium; its image
(1/2,2/3) is not. The two pure equilibria (0,1),(1,0) are exchanged correctly.
There is no contradiction between pure preservation and changed lotteries.

Preservation of equilibrium sets is much weaker than cardinal equivalence:
changing dominated payoffs can leave the same equilibrium set while changing
pure-outcome comparisons. No converse characterization is claimed.

## U6. Binary consequences of the new exact theorem

**Candidate corollary U6-C.** In a binary game with n≥3, full player image of
Aut_card implies a positive weighted exact potential, hence pure equilibrium
and the finite improvement property (FIP). For n=2 the corresponding cardinal
standardness hypothesis suffices; at n=1 every game has its own exact
potential.

**Proof.** U2 makes c an exact-full-image binary game. Apply candidate theorem
P3-E2 of [phase3-equilibria.md](phase3-equilibria.md) to obtain an exact
potential Φ for c. For nonconstant player i let w_i=M_i−m_i; for a constant
player put w_i=1. For each unilateral deviation,

u_i(s'_i,s_-i)−u_i(s)=w_i[Φ(s'_i,s_-i)−Φ(s)].

In the constant case exactness of c forces both sides zero. Thus Φ is a
positive weighted exact potential under the displayed convention. Every
strict improvement strictly increases Φ, so a finite game has no infinite
strict-improvement path. A maximizer is a pure equilibrium. For n=2 a
strategy-trivial cardinal transitive subgroup becomes the same exact subgroup
of c, so P3-E1 applies. ∎

**Candidate corollary U6-O.** Replace cardinal by ordinal in these hypotheses.
Then Γ has an ordinal potential and FIP, hence a pure equilibrium.

**Proof.** Apply U2 and P3-E2 to the rank game r. Its exact potential Φ has
ΔΦ=Δr_i for every unilateral deviation. Since ranks preserve strict order
and ties, sign(ΔΦ)=sign(Δu_i). This is an ordinal potential in the sense of
matching signs (including zeros), and proves FIP and equilibrium existence.
The n=2 standardness argument is the same. ∎

The potential strengths are sharp for these deductions. Example U4.1 has
weighted potential k² but no exact potential: on a two-player face with the
third player fixed at 0, the two players' mixed second utility differences
are 2 and 4. An exact potential would have to give both the same mixed
second difference. Example U4.2 has ordinal potential k, but no positive
weighted exact potential: the corresponding two differences are 0 and 2,
which cannot be equal after division by any positive player weights. These
face identities follow by computing the potential change round the square in
the two possible orders, so the impossibility proofs require no numerical
search. Cardinal full-image therefore does not generally imply *exact*
potential, and ordinal full-image does not generally imply *weighted exact*
potential.

Neither corollary asserts mixed-equilibrium invariance for ordinal changes.
The existence result uses only the pure improvement graph. Full-image alone
at n=2 is insufficient even under exact utilities (matching pennies). Nor
can “binary strategies” be dropped: fully symmetric rock-paper-scissors has
no pure equilibrium. Transitivity alone is insufficient: the binary odd-cycle
anti-coordination example in phase3-equilibria.md is already exact standard
and has no pure equilibrium.

For n≥5, P3-E2 additionally makes c (respectively r) fully symmetric up to
local strategy labels. For n≥4 the same follows under the corresponding
standardness hypothesis by P3-E3. These are preference-level statements
about the normalized games, not numerical welfare equalities in Γ.

## Prior work actually inspected and remaining source comparison

Ham, [*Some Structure Properties of Finite Normal-Form Games*, 2011 thesis](https://n-ham.com/pdfs/Some_Structure_Properties_of_Finite_Normal-Form_Games.pdf),
printed pp. 10–13 (PDF pp. 12–15), Definitions 4.2.3–4.2.4 and Propositions
4.3.1–4.3.6, already treats ordinal/cardinal isomorphisms, groupoids,
monotone/affine characterizations and pure/mixed equilibrium preservation.
The retrieved author PDF text was inspected directly. It defines cardinality
using independent-mixed-profile comparisons and credits proofs 4.3.4–4.3.5
to Noah Stein. The necessity argument above independently reconstructs the affine result
without identifying its product-lottery domain with all profile lotteries;
the two preference-preservation conditions are proved equivalent here.

The author-hosted [Hammond chapter *Games with Cardinal Utility*](https://web.stanford.edu/~hammond/utilInv.pdf)
and [Tewolde–Conitzer, *Game Transformations That Preserve Nash Equilibria or
Best-Response Sets*, arXiv:2111.00076](https://arxiv.org/abs/2111.00076) were
located and opened; only the latter abstract's stated transformation problem
and the former's cardinal-utility framing were used as source leads. No
uninspected theorem is invoked in these proofs. Ordinary finite utility
representation facts are not claimed as discoveries; the possible new content
is their rigorously proved connection to the Phase 3 exact binary theorem,
subject to full literature comparison.

`experiments/utility_invariance.py` implements rational min-max/rank
normalization, independent direct group tests, both strictness examples, the
rational mixed-equilibrium counterexample and face witnesses.
`test_utility_invariance.py` passed three tests. Finite checks corroborate the
specified examples and normalization identities on them; the general results
are established by the proofs above.

A further inspected comparison is Cao–Yang's 2015 author draft, §6,
Definition 8 and Theorem 4: binary games satisfying its common-label
(weak) ordinal symmetry conditions are ordinal potential games. Its
multiplicity-based hypotheses are not simply the full actual ordinal-player
image used in U6-O. That prior theorem must be compared, together with the
final version, before any novelty claim for our corollary.
