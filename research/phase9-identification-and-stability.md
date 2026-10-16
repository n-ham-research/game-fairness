# Phase 9 — minimal symmetry tests and stable role comparisons

16 October 2026. Proved candidate applications of standard finite linear
algebra, inverse-problem stability and decision inequalities. Novelty is
unresolved. Exact utility scale and laboratory design are part of the model.
P8-I1 is the canonical shared-intervention model; no moral definition of
fairness is introduced here. Compose typed maps right to left.

## P9-I1: deciding a symmetry can need less than recovering the game

Write a finite game's entire numerical utility array as u in V=R^{I×S}.
A fixed physically calibrated typed map g permutes these entries: let R_g
be the orthogonal permutation representation, with R_g u=u equivalent to
u_{p(i)}(g s)=u_i(s) for every i,s. Set D_g=R_g−I. The discrepancy's sign or
index convention is immaterial to its zero set, but is fixed in an actual
measurement design. A candidate is a symmetry iff D_g u=0.

The unknown game lies in a specified class C. Observations are Lu with L
known and linear (rows may be conditional expectations; signed contrasts
can be constructed from several recorded means). **Exact symmetry status is
identifiable on C iff**

  L(C∩ker D_g) ∩ L(C\ker D_g) = empty.

Proof: equal data must never come from a symmetric and a nonsymmetric game;
otherwise any decision rule gives the same answer for two opposite truths.
If the two data sets are disjoint, membership defines a correct noiseless
rule. This is a general criterion, not necessarily computationally tractable.
If the payoff table is already completely known, direct evaluation of D_g u
settles the question; the observation problem concerns uncertainty about u.

If C=W is a linear subspace, the criterion is exactly

  ker(L|W) ⊆ ker(D_g|W).

Necessity: compare any w in ker L with the zero game, which is symmetric.
Sufficiency: equal data differ by such a w, so D_g u agrees. Equivalently
D_g|W factors as A L|W: define A(Lw)=D_g w on im(L|W), well-defined by
kernel containment, then extend linearly. Thus linear symmetry-status tests
on a subspace actually determine the full discrepancy, and at least
rank(D_g|W) independent real scalar measurements are required. With unrestricted
linear measurement choices this minimum is attained by measuring a basis
of the discrepancy. A physical restricted menu of stochastic contexts may
need more measurements, or may never suffice. Count rows separately from
whole masking contexts, each of which contains many rows.

For an affine class u0+W with at least one symmetric member, translate to that
member: the same kernel criterion applies. If it has no symmetric members,
status is always false and zero observations suffice. The linear criterion
must not be claimed for every nonconvex or finite class. On a finite class,
a generic positive-weight scalar mean can distinguish every listed table
(avoid finitely many hyperplanes); its precision and noise sensitivity may
be arbitrarily demanding. This is not a finite-bit communication bound.

For a finite family G of candidate protocols and a linear class W, complete
automorphism-membership data are identifiable iff

  ker(L|W) ⊆ W∩intersection_{g∈G} ker D_g.

The zero game proves necessity for all g; factorization proves sufficiency.
Thus the minimum unrestricted measurement rank is
 dim W−dim(W∩intersection_g ker D_g),
not necessarily dim W. If G is a group, the rightmost space is its fixed
utility subspace intersected with W. No assumption that W is G-invariant is
needed for this kernel statement.

### A concrete reduced design

On the full class V, R_g decomposes the utility-entry index set into c cycles.
D_g has image consisting of arrays whose sum on each such cycle is zero,
and rank dim V−c. Therefore observe the discrepancy at all but one entry
of each nontrivial cycle. The omitted entry is minus the sum of those seen.
This identifies the candidate with exactly rank D_g scalar discrepancy
observations, meeting the unrestricted lower bound. Each observation uses a
paired, logged original/transformed receipt comparison; one contrast need
not equal one raw trial. Discrepancies, rather than original tables, are
being measured. Uniform averaging over each entire cycle, by contrast,
erases ALL candidate discrepancies: its rowspace consists of fixed arrays.
An identity-hiding design may therefore destroy exactly the asymmetry we
want to test even though it reports meaningful payoff averages.

For discrepancy-only designs M D_g u, the necessary and sufficient uniform
criterion is ker M∩D_g W={0}. Full column rank of M on all of V is unnecessary.
For a specified finite or bounded class use its attainable discrepancy set,
not an unjustified ambient-rank requirement.

## P9-S1: quantitative identification on the attainable space

Let Delta=D_g W, equipped with Euclidean norm, and let M be a known linear
observation map. The measured vector satisfies y=M d+e, d∈Delta, ||e||2≤eta.
For nonzero Delta define

  alpha=inf{||M d||2 : d∈Delta, ||d||2=1}.

By finite-dimensional compactness alpha>0 exactly when M is injective on
Delta. For Delta={0} every game in W is already symmetric; no recovery bound
is needed. With alpha>0,

  ||d||2 ≤ (||y||2+eta)/alpha.

A least-squares inverse on Delta gives an estimate d_hat with
||d_hat−d||2≤eta/alpha (project y orthogonally to M Delta first).
Also ||d||2≥max(0,||y||2−eta)/||M|Delta|| when the denominator is nonzero.
Two observationally feasible discrepancies differ by at most 2eta/alpha.
Proof: triangle inequalities and the defining minimum singular value; the
inverse norm is 1/alpha. These are standard inverse-problem bounds.

Noiseless injectivity does NOT guarantee uniform stability over a changing
design. For B_q=qI+(1−q)T on a nonzero antisymmetric direction,
alpha=|2q−1|. A discrepancy of norm one produces arbitrarily small observations
as q→1/2; at q=1/2 it is invisible. Bounded receipts restrict how large the
hidden error can be, not this failure of relative stability.

With eta>0 no test uniformly certifies exact zero versus every nonzero d in
an unrestricted nonzero linear Delta: arbitrarily small discrepancies have
overlapping error balls. For a separated alternative ||d||2≥epsilon with epsilon>0, a
uniform deterministic test exists iff alpha*epsilon>2eta. Proof: null
observations fill the radius-eta ball at zero; alternative observations are
the union of such balls centered at M d. The centers' minimum norm is
alpha*epsilon, attained. Their balls are disjoint exactly under the strict
inequality. Rejecting when ||y||2>eta then works. At equality the balls touch.
Without injectivity no such uniform test exists, even at eta=0.

## P9-S2: finite-sample certification under a bounded noise model

If an observation row is estimated by N independent draws of a RECEIPT
DIFFERENCE in [−B,B], with B>0, the standard bounded-difference exponential
bound gives

  Pr(|estimated mean−true mean|>t) ≤ 2 exp(−N t²/(2B²)).

For J≥1 rows and 0<delta<1, a union bound gives all coordinate errors at most
 t=B sqrt(2 log(2J/delta)/N)
with probability at least 1−delta. Independence BETWEEN different rows is
not needed, but independent bounded sampling WITHIN each row is. On that
event ||e||2≤sqrt(J)*t, so S1 applies with eta=sqrt(J)*t.
Payoff range and coupling must justify the difference bound; a difference
of receipts in [0,B] indeed lies in [−B,B]. These are repeated calibrated
measurements, not a model of arbitrary language-model behavior. Stronger
noise models or adaptive contexts require their own concentration argument.
This section uses the established Hoeffding inequality, not a new probability
result. A deterministic eta statement remains valid without sampling claims.

## P9-S3: approximate maps are generally not a group

Use the sup norm on utility entries. Define
 defect_u(g)=||R_g u−u||∞.
Permutation isometries give

  defect_u(gh)≤defect_u(g)+defect_u(h),
  defect_u(g^{-1})=defect_u(g).

The maps with defect≤epsilon contain identity and are inverse closed, but
need not be closed under composition. One player with three actions and
receipts (0,3/4,3/2) supplies a counterexample at epsilon=1: adjacent local
transpositions each have defect3/4, while their product has defect3/2.
The same example embeds in larger constant-opponent games. Approximate
symmetry gives no automatic exact automorphism or exact player transitivity.
A word of length L in epsilon-defect generators has defect at most L epsilon.

Finite candidate membership can be stable only with a separation margin.
If ||u_hat−u||∞≤rho then
 |defect_u(g)−defect_u_hat(g)|≤2rho.
For finite G, put gamma=min_{g∈G\Aut(u)} defect_u(g)>0 if nonautomorphisms
exist. If a lower bound on gamma is known and gamma>4rho, thresholding
estimated defects at gamma/2 recovers the exact membership list. Without
such a promised margin it is discontinuous: a two-action utility (0,t) has
a local-swap symmetry at t=0 and not at any t>0, however small t is. Ordinal
ranks likewise jump at ties; approximate cardinal data alone cannot certify
ordinal equality without a tie/separation model.

## P9-F1: what small discrepancies do imply for assignment

Retain the common physical calibration and disclosed transport from P7-A1.
Suppose corresponding focal rows differ by at most epsilon in every state.
For each matched source/target pair and every common correlated opponent
law their expected differences have
absolute value≤epsilon, and the optimized role values differ by at most
epsilon, since |max f−max h|≤max|f−h|. Thus every pair of role-assignment
lotteries differs in expected optimized utility by at most epsilon whenever
all role values lie in one interval of width epsilon. If merely each role
is within epsilon of one reference role, use width2epsilon instead. This
is a welfare statement about ONE specified participant's calibrated money
utility, not independent arbitrary affine representations across people.

For response-policy models P8-B1, this bound requires matched policies. If
the target/source transported conditional laws differ in total variation by
at most tau, and target receipts lie in one interval of width B, split the
expectation difference into a table error and a law error to get
 epsilon+B*tau.
With equal feasible commitment labels, taking maxima preserves this bound.
Small utility asymmetry alone cannot control unconstrained role-dependent
beliefs or response/selection changes. Example: identical row (0,1) and role
laws delta0 versus delta1 give a value gap1 with zero table discrepancy.

A useful strategic limit: an epsilon-defect exact-scale relabeling takes a
Nash equilibrium to a 2epsilon-Nash equilibrium (each unilateral incentive
compares two receipts, each transported with error≤epsilon). The same proof
works for correlated-equilibrium unconditional deviation inequalities. Under
this uniform pointwise error bound it also gives conditional 2epsilon
incentive errors for each positive-probability recommendation: condition first
and bound the two receipt errors by epsilon. If only an unconditional
measurement-error bound is available, rare recommendations instead require
their own normalization. Neither conclusion implies near efficiency or equal
realized outcomes.

## Foundations and manuscript decision

Rich shared interventions identify candidate structure; assignment tests
assess calibrated opportunities. S1 and F1 connect the two quantitatively,
without identifying structural/procedural/outcome fairness. Common affine
recoding scales epsilon,B,eta,gamma consistently. Independent role offsets
can alter assignment comparisons while preserving within-role preferences.
Risk-robust or ordinal conclusions require the common physical consequence
model or explicit preference tests, not approximate equality on a numeric
rank scale. Nash, VNM and Shapley comparisons retain their distinct domains.
Keep the manuscript focused: add I1/S1/F1's minimal and stable bridge, leave
sampling, approximate group counterexamples and mask-design exploration in
research unless they improve the main proof narrative.

### Independent derivation of the bounded-sample bound

For completeness, the concentration constant in S2 does not depend on an
uninspected source proof. If Z is in [−B,B], every exponential tilt of its
law still has support in that interval. Its variance is at most B²: for any
variable X in [a,b], E[(X−a)(b−X)]≥0 gives
Var X≤(E X−a)(b−E X)≤(b−a)²/4. For
psi(lambda)=log E exp(lambda(Z−E Z)), differentiation gives psi'' equal
to that tilted variance. Since psi(0)=psi'(0)=0, integration yields
psi(lambda)≤lambda² B²/2 for both signs of lambda. Independence and
exponential Markov then bound an N-sample mean tail by
exp(−N lambda t+N lambda² B²/2); optimize lambda=t/B² and apply both signs.
This proves S2 with its stated independence and boundedness assumptions.
It is the standard Hoeffding argument, not a new concentration inequality.
