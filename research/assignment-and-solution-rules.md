# Assignment preferences, procedures and solution-rule symmetry

16 October 2026. **Candidate framework and elementary propositions with complete
proofs; novelty not established.** This continues phase3-fairness.md after the
user's utility-invariance instructions. It does not define fairness to be a
game symmetry. The three kinds of questions below concern different objects:
conditional strategic structure, an assignment procedure, and selected outcomes.

## A1. The decision maker and the missing cross-role data

Let the role set be I. For role i let Omega_i be a finite set of consequences
including the complete profile and any relevant external outcome. A single
participant has expected-utility preferences over lotteries on the *disjoint
union* `Omega = union_i ({i} × Omega_i)`, represented by W(i,o). This is a
preference over assignments and consequences, not merely the separate
preferences of the existing players. One common positive affine change of W
preserves this entire preference. Separate positive affine changes on the
individual role fibers need not preserve cross-role preferences.

A disclosed decision procedure gives a conditional consequence law L_i in role
i. The conditional assignment value is `m_i=E_{L_i} W(i,o)`. If assignment
probabilities are lambda, the value is `sum_i lambda_i m_i`. Indifference
between every assignment lottery is equivalent to all m_i being equal: Dirac
assignments prove necessity and linearity proves sufficiency. It is weaker
than equality of entire conditional payoff menus or tables.

**A1 (underidentification proposition).** Within-role expected-utility
preferences alone cannot determine literal indifference between assignments.
Fix any finite role utilities u_i and conditional laws L_i. For every desired
vector c in R^I there are representations of exactly the same within-role
preferences with expected values c_i: choose any a_i>0 and put
`b_i=c_i-a_i E_{L_i}u_i`, `W(i,o)=a_i u_i(o)+b_i`.
Then `E W(i,o)=c_i`. These independent affine changes also leave the cardinal
and ordinal game automorphism groups unchanged, as proved in
utility-invariance.md. Thus neither of those groups, nor the individual role
preferences they preserve, can identify the missing assignment comparisons.
This constructs different global assignment preferences with the same
conditional data; it is not an assertion that one may independently rescale
an already fixed global W without changing it. ∎

Small example: each of two roles has one action and outcome. Constants (0,0)
and (0,1) describe identical within-role choice preferences, with transitive
cardinal/ordinal player groups, but one common participant is indifferent
between roles in the first assignment model and strictly prefers role1 in the
second. With two meaningful actions use `W(0,s)=s_0`, `W(1,s)=s_1+c`.
The same physical own action yields a c advantage in role1, while conditional
expected-utility preferences and cardinal interchangeability are unchanged.

Accordingly cardinal interchangeability can justify *equivalence of conditional
choice preferences*. Literal subjective assignment indifference additionally
requires cross-role utility calibration, consequences or explicit preferences.
Exact common-scale interchangeability is relevant after those data have been
specified. Equality of utilities belonging to different people is a further
interpersonal comparison, not supplied by an affine representation theorem.

## A2. Timing: chosen plans versus optimized opportunities

Assume for this paragraph that consequences are profiles, W(i,s)=u_i(s) on a
justified common participant scale, opponent laws are disclosed, and physical
own choices have specified identifications f_i:A→A_i. This identification is
part of the experiment; an automorphism does not force physical labels to be
interchangeable.

If an action a must be selected before assignment, its value is
`sum_i lambda_i V_i(f_i(a),mu^i)`. For *every fixed a* all assignment lotteries
are indifferent iff `V_i(f_i(a),mu^i)` is independent of i. If the experiment
permits actions after assignment, optimized value is instead
`sum_i lambda_i max_a V_i(a,mu^i)`, and indifference for all assignment lotteries
requires only equality of those maxima. The assertions follow from the same
Dirac-assignment argument as A1. They are distinct: the phase3-fairness.md
example with own payoff menus {1,0} and {1,-1} has identical maxima and
different conditional menus. Complete all-action/all-ordered-belief tests
recover pointwise focal preservation by F1; one optimized decision rule does
not. This separates necessity/sufficiency conditions rather than assuming
all “equivalent opportunities” have one meaning.

## A3. Uniform assignment is a procedural property

Let there be n participants and n roles, and choose a uniformly random
bijection alpha from participants to roles. A role-contingent procedure has
fixed role values m_i, identical for participants with the same utility over
role consequences. Each participant's role marginal is uniform, so each has
ex ante expectation `(sum_i m_i)/n`, regardless of structural symmetry of the
underlying game. This follows by counting `(n-1)!` assignments giving any
specified role to any specified participant. A common identical utility model
and role-contingent procedure are essential; heterogeneous participant
utilities or person-dependent behavior can invalidate the conclusion.

For role values (0,2), random assignment gives both participants expectation1,
although each strictly prefers the high role once roles are compared
conditionally. The underlying singleton game has no exact player swap.
An equal random prospect across people is different from indifference between
the roles themselves, from a fair realized allocation, or from structural
interchangeability. This is a mathematical distinction, not a verdict that
randomization is normatively sufficient for every fairness concern.

## A4. Symmetry of the game versus equivariance of the rule

A solution/selection rule R maps games to outcomes, sets of outcomes, or
probability laws. Equivariance requires `R(g Gamma)=g R(Gamma)` with the
appropriate pushforward action. For g in Aut(Gamma), this implies
`R(Gamma)=g R(Gamma)`. Thus input symmetry constrains outputs **only together
with a rule property**. A rule can break symmetry deliberately; structural
symmetry alone does not establish equal realized outcomes or a fair rule.
The exact scope of Nash's fixed-problem bargaining axiom and stronger
cross-problem equivariance is distinguished in the literature notes.

For a fixed finite game and a finite group G of exact automorphisms, let mu
be a G-invariant law on pure profiles. Then players in one player orbit have
equal expected numerical utilities. If g sends i to j,
`E_mu u_j = E_mu[u_j(g s)] = E_mu u_i` by invariance and exact preservation.
Under cardinal automorphisms this statement holds for canonical normalized
utilities; original numerical expectations may have different offsets/scales.
Under ordinal automorphisms no general claim about original expected utility
follows. A common rank score is useful for representing pure order structure,
not a justification for its expected value as welfare.

## A5. Randomized equivariant selection and its limitations

**A5 (finite group averaging).** Let a finite group G act on a finite outcome
set X and let C be a nonempty invariant subset. For x in C, put
`mu=(1/|G|)sum_{g in G}delta_{g x}`. Its support lies in C and it is invariant:
left multiplication by any h permutes the summation indices. Thus an invariant
lottery exists even if no deterministic invariant outcome does. A deterministic
invariant choice exists iff C contains a point fixed by every element of G.
This is immediate in both directions from the definition of a fixed point. ∎

More generally, on a domain of inputs closed under a finite group, any lottery
rule R can be made equivariant by
`bar R(Gamma)=(1/|G|)sum_g (g^{-1})_# R(g Gamma)`.
For h substitute t=gh; then `(g^{-1})_#=h_#(t^{-1})_#`, yielding
`bar R(h Gamma)=h_# bar R(Gamma)`. This proves equivariance, not efficiency,
individual rationality, incentive compatibility or any other fairness axiom.
Those must be checked separately. Averaging preserves linear constraints and
support in equivariant feasible correspondences, not arbitrary nonconvex
solution properties.

For exact or cardinal game automorphisms the mixed-Nash correspondence is
equivariant; for ordinal automorphisms the pure-Nash correspondence is
equivariant but the mixed one need not be (utility-invariance.md). If pure
Nash equilibria exist, apply A5 to their finite invariant set. The resulting
lottery is supported on equilibria. As a joint distribution it is a correlated
equilibrium of the original numerical game: every recommendation in each
pure equilibrium already satisfies all unilateral obedience inequalities;
weighted summation preserves them. It need not be a product distribution or
a mixed-strategy Nash equilibrium.

Example: the exact symmetric two-player anti-coordination game pays each
player1 for unequal binary actions and 0 otherwise. Its pure equilibria are01
and 10; the player swap exchanges them, so no deterministic pure equilibrium
is invariant. Their equal mixture is invariant and correlated, with expected
payoffs(1,1). Its independent marginals are both uniform, whose product gives
expected payoffs(1/2,1/2) and is a different distribution. Even in a game where
that independent product is also a Nash equilibrium, equality of the two
procedures cannot be assumed. An invariant solution **set** is different from
an invariant selected pure point.

## A6. Ordered and unordered information

Use F3 in phase3-fairness.md: ex post indifference between opponent arrangements
is a utility factorization through action histograms; an unordered information
partition plus a conditional belief merely replaces payoffs by orbit averages.
Information does not itself establish indifference to every hidden arrangement.
The factorization/tie statements apply to within-role ordinal preferences as
well. Conditional averaging requires a selected cardinal expected-utility
representation; ordinal data alone does not define those averages. For the
participant, the representation used must also be consistent with their actual
global assignment preferences W.
Changing admissible transports is a second dimension independent of exact,
cardinal or ordinal invariants. No one total hierarchy is asserted across
experiments with different consequences, information or timing.

## A7. Substantive objections and research direction

Valid objections to “symmetry implies fairness” include: different intended
welfare criteria; absent interpersonal or cross-role calibration; asymmetric
information/endowments outside the game; non-equivariant selection; unequal
realized outcomes; and an assignment procedure that differs from the modeled
one. These are identifiable missing premises, not evidence about a critic's
motives. Historical solution axioms establish that symmetry is relevant to
many formal fairness models; they do not prove that one criterion is sufficient
or necessary for every defensible conception of fairness.

The next decision-theoretic task is to justify a participant's global assignment
preferences and admissible physical strategy correspondences independently,
then test which invariants characterize that model. The algebraic normalization
and obstruction results make this a precise research programme without
presupposing its normative answer.
