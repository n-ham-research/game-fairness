# Phase 3: assignment experiments and structural symmetry

16 October 2026. **Candidate framework and elementary comparison results; no
novelty claim and no normative equivalence asserted.** These experiments begin
with choices and information, not with a definition declaring symmetry fair.
They are exploratory research notes, not manuscript additions. Finite nonempty
action sets, common numerical utility scale, and right-to-left composition are
assumed. A participant evaluates the payoff of the position assigned to them;
this identification of personal utility with the role's u_i is an explicit
modeling assumption. Heterogeneous participants require separate utility data.

## F1. Assignment and ordered behavioral tests

Assignment chooses a role i according to a disclosed probability vector lambda.
Before assignment the participant knows feasible actions, role payoff tables,
and the specified opponent behavior. They may condition their own action on
the role. For a role i, chosen action a, and independently behaving ordered
opponents with laws mu_j, define

`V_i(a,mu)=sum_{t in A_{-i}} u_i(a,t) product_{j!=i} mu_j(t_j)`.

A proposed comparison of role i with role p(i) must specify a typed bijection
g=(p;(f_j)) of the *whole experiment*: it transports the chosen action and
every opponent law. Whether opponents retain their personal identities or
move with their positions determines which g is physically admissible. This
choice is not made by the algebra. The participant pays nothing to exchange
the two specified conditional experiments exactly when their values agree.
Equality of these conditional values makes every assignment lottery between
the two experiments equally valuable, by linearity in lambda.

**Candidate comparison lemma F1.** For fixed g and i the following are equivalent:

1. Every chosen action and every product law of ordered opponents give equal
   values in the two transported experiments.
2. `u_{p(i)}(g s)=u_i(s)` for every pure profile s.

Proof: apply (1) to Dirac opponent laws and the focal action s_i to get (2).
Conversely sum (2) against the finite product law. The same equivalence holds
if all opponent laws are required to have full support: approximate each Dirac
law by `(1-epsilon) Dirac+epsilon uniform` and use continuity of the finite
sum. Thus correlated beliefs are unnecessary for this characterization. ∎

If the same g passes these tests for **every** possible participant i, it is
an exact game automorphism. Consequently a group of admissible transports
passes every test for every participant iff it is a subgroup of Aut(Gamma).
Its transitivity guarantees robust assignment comparisons between all roles;
its image S_n guarantees individual realizability of every assignment
permutation. This derives a structural comparison from a rich operational
test, not a blanket assertion that fairness means automorphism transitivity.

Coherent implementation is an additional experimental requirement: a selected
transport for each assignment permutation must respect successive exchanges.
This asks for a section of the **specified** player projection. The Phase 3
three-player counterexample distinguishes universal individual realizability
from coherent implementation. Strategy-trivial implementation is stronger:
exchanges fixing a participant must not recode their actions. By audited Ham
4.23/5.2 this is equivalent to a full matching lift. These are three distinct
operational requirements, not interchangeable names for label indifference.

## F2. Limits of individual opportunity and optimal-value comparisons

Testing each participant separately may permit incompatible identifications.
For binary actions and successor map r(0)=1,r(1)=0,r(2)=0, set

`u_i(s)=2s_i+s_{r(i)}`.

Each role gives the same focal opportunity table: own action has coefficient
2, one opponent has coefficient1, and the other has coefficient0. Bijections
of opponents can therefore make every pair of focal experiments agree for
all actions and ordered beliefs. Yet the full game's actual player image is
trivial. To prove this, own-action differences force every component action
map to preserve 0 and1 (a flip reverses the nonzero own difference). The
remaining payoff identity requires `p r(i)=r(p(i))`. The directed successor
graph has respective indegrees2,1,0, so all three vertices must be fixed.
Thus separate focal opportunity equivalence does not imply transitivity of
exact game automorphisms. It does not supply one transport that works for all
participants simultaneously. This example is not minimality-certified.

Even equality of optimized values under every belief is weaker. Take two
binary roles with `u_0(s)=1-s_0` and `u_1(s)=1-2s_1`. Every opponent belief
gives optimal utility1 in either role, and both upper/lower security values
are1. No exact role-swapping automorphism exists: the attainable focal payoff
sets are {0,1} and {-1,1}. The dominated options differ even though the
best attainable values agree. The opportunity menus and their optimal values
are different objects; a theory should say which it cares about.

## F3. Ordered versus unordered opponents

Suppose opponents use common action labels. Let h(t) record their action
histogram. An ex post preference that depends only on the focal action a and
h(t), with no residual dependence on identities, is precisely a factorization
`u_i(a,t)=w_i(a,h(t))`. Its equivalence to focal invariance under every
opponent permutation follows because two finite tuples have the same
histogram iff one permutes to the other. This is the audited weak-anonymity
condition. The substantive premise is *ex post indifference* to arrangements.

Merely hiding opponent identities does not imply that premise. If conditional
on a histogram the participant regards every arrangement as equiprobable,
the relevant payoff is the average

`bar u_i(a,h)=sum_{t:h(t)=h}u_i(a,t)/#{t:h(t)=h}`.

Every game has such an averaged table; information loss does not prove that
the original table is anonymous. More generally equality of values under all
exchangeable laws is exactly equality of these orbit averages: laws uniform
on one histogram orbit prove necessity, and decomposition into such laws
proves sufficiency. This loses all zero-average within-orbit components.

For three binary players, `u_i(s)=s_i+s_{i+1}-s_{i+2}` (cyclic indices) gives
`bar u_i(a,h)=a` for every i and h. Under identical independent opponent laws
the same cancellation occurs. Ordered profiles distinguish the two opponents:
for fixed own action0, arrangements(1,0) and(0,1) give1 and−1. Thus aggregate
assignment tests can agree while focal opponent anonymity fails. It is
inappropriate to infer structural anonymity from either IID testing or
uniform averaging over hidden identities.

## F4. Expected equality and transport of the selection rule

A single specified law is still weaker. The earlier two-role example
`u_0=2s_0+s_1`, `u_1=3-2s_0-s_1` has uniform expected payoff3/2 for each role,
but no swapping automorphism: own-action absolute differences are2 and1.
Conversely a fully symmetric game `u_i(s)=s_i` gives unequal expectations
under a procedure fixing one player's action0 and another's action1. Structural
symmetry implies expected equality only when the law/decision procedure is
transported appropriately (in particular an invariant law works). Proof is
the same finite change of summation indices as F1. Equilibrium selection may
also break symmetry; existence of a symmetric mixed equilibrium does not
force every equilibrium or realization to give equal payoffs.

Positive affine rescalings for individual players preserve expected-utility
preferences but can destroy numerical comparisons across roles. A common
interpersonal scale, common participant, or justified normalization is needed
for such numerical assignment tests. Ordinal and independent-mixed variants
are specified separately in phase3-specifications.md; they are not silently
identified with exact utility preservation.

## F5. Coalition values: a limited bridge to von Neumann–Morgenstern

The previously inspected third-edition §28.2.2 defines coalition-size fairness
using the zero-sum characteristic function. No first-edition text has been
newly inspected here. To make the present bridge precise, define in a finite
zero-sum game

`v(S)=max_{alpha in Delta(A_S)} min_{beta in Delta(A_{N\S})}
 E_{alpha x beta}[sum_{i in S}u_i]`,

with v(empty)=v(N)=0. Each coalition may coordinate its own joint strategy;
the two coalitions randomize independently. Finite minimax gives a value.
This convention and transferable sum scale are explicit; independent
individual randomization would be a different coalition model.

**Elementary bridge F5 (von Neumann–Morgenstern, extended to typed transports; novelty not claimed).** If g is
an exact automorphism with player permutation p, then `v(pS)=v(S)`.
Proof: g bijects both coalitions' joint action sets, preserves the sum of
members' utilities, and pushes each joint law to its target simplex. Change
variables in both optimizations. Consequently full player image S_n implies
that v depends only on |S|. The weaker sufficient condition is set-transitivity of the actual player image
(transitivity on subsets of every fixed size). This is explicitly recognized
in §28.1.4, equation (28:8), and §28.2.1, equations (28:9)–(28:10);
§28.1.3, equations (28:4) and (28:7), supplies the transport/orbit argument.
Mere transitivity only gives equality on actual
coalition orbits, not a proof of equality for all equal sizes. ∎

The converse fails even for equal binary action sets: use
`u_0=s_0-s_1`, `u_1=s_1-s_0`, `u_2=0`. Every coalition value is0. Its coalition
sum is either identically0 or one of the two displayed differences; the
coalition can guarantee0 by choosing its relevant action1, and the opposing
coalition can cap it at0 by doing the same. Nevertheless player2's utility
is constant while the other two are nonconstant, so no exact transitive
player action exists. Equality of cooperative guarantees discards strategic
data. This is a direct example, not a claim that the original authors asserted
the converse. Full strategic symmetry and cooperative fairness also do not
assert equal realized individual outcomes.

For general-sum games the same scalar construction requires a normative
choice of aggregation, transferability, and adversarial outsiders. A set of
coalition payoff vectors, bargaining rule, or another guarantee is a different
object. No canonical general-sum extension of their fairness concept has been
established in this pass.

## Assessment

The comparisons are nontrivial and useful as a separation of experimental
requirements: selected-law equality, aggregate-information equality, robust
focal opportunity equality, simultaneous exact transport, and coherent
implementation. They do **not** form one total hierarchy: changed information,
admissible transports, or utility scales change the tests. The next useful
fairness work should justify one assignment experiment philosophically and
compare its observable tests, rather than naming every algebraic property
“fairness”. All speculative interpretation remains outside the manuscript.
