# One calibrated assignment model: coherence is not needed for one-shot indifference

16 October 2026. **Candidate comparison results; novelty unresolved.** This is
one fixed model, not a catalogue of fairness definitions. It uses the audited
typed action convention `(P_p s)_j=s_{p^{-1}(j)}`, right-to-left composition.

## Primitives and information

The game has finite players I, finite action sets A_i, and specified monetary
receipts r_i(s). A single participant is risk neutral over money, with one
calibration U(0)=0,U(1)=1; set u_i(s)=r_i(s). This fixes comparisons across role
positions without comparing different people's arbitrary utility scales.
It is an explicitly restricted model, not an interpretation forced on every
normal-form game. For a risk-averse participant replace all receipts by their
one common VNM function, and recompute the symmetry group of those utilities.

Before assignment the participant knows the entire game, a reference role 0,
a reference product law mu of the other players' actions, a disclosed typed
transport t_i from role 0 to each role i, and assignment probabilities lambda.
The reference transport is fixed to t_0=id.
The action is chosen **after** learning the role. Other players' behavior in
role-i experiment is the transported reference product law; it does not depend
on the participant's hidden personal identity. Own action a in A_0 corresponds
to (t_i)_0(a). Strategy labels may be recoded precisely through the disclosed
physical correspondence; no extra recoding is assumed admissible.

The participant's conditional value for that plan is

`V_i(a)=E[u_i(t_i(a,s_{-0}))]`.

The optimized conditional value is `M_i=max_a V_i(a)`. The ex ante value is
`sum_i lambda_i M_i`. Indifference to every assignment lottery is exactly
`M_i=M_j` for all i,j, by comparing Dirac assignments. A particular lambda
specifies one prospect, not a comparison between every conditional role.

## A4.1. Individual realizability suffices

Assume each t_i is an exact game automorphism taking 0 to i. Then
`u_i(t_i s)=u_0(s)` for every profile s. Summation gives `V_i(a)=V_0(a)`
for every a, hence all M_i equal. This works for every reference product law
and every assignment lottery. No equation between t_i and t_j is required.
Transitivity of the exact automorphism group is enough; full player image,
a section onto S_n, and a matching-based section are all stronger than this
one-shot argument needs. ∎

The full-player-image nonsplit game P3-S1b is a nonvacuous example: use any
chosen lift for each needed role exchange. It gives exactly the same
conditional action values even though no multiplicative selection of lifts
exists. Thus in this model coherent interchangeability does **not** imply a
stronger one-shot assignment-indifference conclusion than individual exact
realizability. This is a separation of algebraic and decision requirements,
not a claim that coherence is never operationally important.

## A4.2. Exact necessity under a specified richer test

For fixed typed t_i, equality of V_i(a) across roles for **every** own a and
**every** reference product law is equivalent to
`u_i(t_i s)=u_0(s)` for every pure s. Dirac laws prove necessity, finite
linearity proves sufficiency. This is focal payoff transport. To characterize
exact game automorphisms one must require the same t_i to pass the analogous
test for **every focal participant**, moving all payoff recipients. Testing
only one participant cannot infer the other players' payoff preservation.
This is the operational F1 distinction, now in a fully calibrated model. ∎

Optimized equality alone does not provide this converse: menus {1,0} and
{1,-1} have equal optimal value for every opponent belief but unequal action
values. A common participant scale, all-action tests, and simultaneous focal
requirements are substantive premises; they must not be hidden inside the
phrase “equivalent opportunities”.

## A4.3. Repeated exchanges and the observable obstruction

Now suppose the institution assigns a lift t_p for each requested permutation
p, with t_e=1, and implements successive exchanges by composition. This is a
specified dynamic extension of the model. Path independence of the **typed
strategy transformation**, for all initial pure strategies and all composed
requests, is equivalent to

`t_p t_q=t_{pq}` for every p,q.

Sufficiency is composition. Necessity follows by comparing the two histories
(q then p) and (pq); the experiment observes the player map and each strategy
coordinate as well as payoff. Thus path-independent implementation of every
player permutation is exactly a section of the actual projection. If a
request fixing a participant must also leave their strategy encoding intact,
require strategy-triviality, equivalently an audited full matching action.

However, a kernel discrepancy need not be observable **in payoff**. If two
histories have the same total player permutation, their implementations differ
by an exact player-kernel element. Each history is an exact automorphism, so
both transport every original focal payoff to the same numerical value at the
same final player position. All distributions therefore have equal expected
payoffs after the corresponding histories. Path independence of utility
alone does not imply path independence of typed actions.

In P3-S1b a repeated transposition implements common translation 2 on Z/4:
player positions return, actions need not. That translation is an exact
kernel automorphism, so there is no utility difference in the base game.
Action-reset costs, commitments or external meanings could make it costly,
but then they must be included as additional consequences and may destroy
the original automorphisms. The section obstruction cannot be advertised as
a demonstrated welfare disadvantage without such further data.

## A4.4. Cardinal and ordinal representations

The common money scale is essential. Positive-affine maps across different
roles preserve conditional preference orders but may shift role values; they
do not establish the numerical equality used in A4.1. If one deliberately
calibrates assignment utility by the canonical min-max game, the same theorem
applies there, but that calibration is an extra preference assumption. Rank
scores supply still less justification for expected welfare. The offset
underidentification theorem in assignment-and-solution-rules.md proves that
within-role preferences cannot determine this calibration.

The algebraic individual/coherent/matching hierarchy can be imposed on exact,
cardinal or ordinal groups, with the same typed definitions. Canonical
normalizations transfer each preference-group question to an exact game;
they do not transfer a participant's already specified cross-role money
preferences. This model therefore provides exact sufficient conditions,
precise limited converses, and counterexamples to coherence or cardinality
being necessary/sufficient for every possible notion of assignment fairness.
