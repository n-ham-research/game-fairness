# Assignment indifference with choice and hidden opponent identities

Status: **proved research candidates and explicit separations; novelty not
cleared**. Support functions, convex separation, stochastic dominance and
information averaging are established mathematics. This note applies them to
one specified assignment experiment; it does not declare a group property to
be fairness. Stable identifiers P7-A1–A6 are new research identifiers, separate
from transferred A1/A4. All finite sets below are nonempty.

## The experiment and what the participant can choose

A single participant may occupy a role i in a disclosed set I of positions
of a finite game. Opponent states are a fixed finite set T. For each role an
announced physical correspondence θ_i:T→A_{−i} specifies the opponents'
actions in that role. This correspondence is data, not assumed to be a game
automorphism. Where identities are moved, their actions and laws move through
θ_i. The participant knows the game, correspondences and a probability μ on T
before the role lottery. Nature selects i with announced probabilities λ;
the participant observes i and then chooses an available own action a∈A_i.
Opponents follow θ_i(t) with t drawn from μ, independently of that own choice.

Receipts r_i(a,t) are consequences on ONE money scale. The participant is
risk neutral in P7-A1–A5, with global utility W(i,a,t)=r_i(a,t). This is
cross-role calibration, not an interpersonal comparison of arbitrary player
representations. No hidden role offsets, action-reset costs or history rewards
are present. A common positive affine change of W represents the same
preference. Correlated opponent laws are permitted; restrictions on μ define
different information/behavior models. Own randomization does not improve
expected payoff because optimization is linear in the own mixed action.

The conditional optimal value is

    V_i(μ)=max_{a∈A_i} ∑_{t∈T} μ(t)r_i(a,t).

The ex ante value of λ is ∑λ_i V_i(μ), since the action is selected after
the role is observed. Indifference between ALL role-assignment lotteries at
this μ holds iff every V_i(μ) agrees: Dirac role assignments prove necessity.
Call the experiment robustly role-indifferent on a family Λ if this equality
holds for every μ∈Λ. This observable condition is defined before any group.
If a specific law or lottery alone is intended, retain that weaker quantifier.

## P7-A1: an exact characterization of optimized indifference

Let x_{ia}=(r_i(a,t))_{t∈T}, and form the closed convex downward set

    D_i=conv{x_{ia}:a∈A_i}+R_{≤0}^T.

Then robust role indifference for ALL laws μ∈Δ(T) is equivalent to
D_i=D_j for every pair of roles. The same conclusion holds if only full-support
laws are tested.

**Proof.** V_i is the support function of D_i on the probability simplex:
adding nonpositive coordinates cannot improve a nonnegative linear objective.
Equality of D_i therefore implies equality of every V_i. Conversely if
x∈D_i\D_j, closed-convex separation of the point x from D_j gives a nonzero
normal w with w·x>sup_{y∈D_j}w·y. Each coordinate of w must be nonnegative;
a negative coordinate would make that supremum infinite along a downward
ray. Normalize ∑w_t=1. Since x is a convex mixture of role-i rows minus a
nonnegative vector, w·x≤V_i(w), while the supremum is V_j(w). Hence the two
values differ, a contradiction. The sets are closed because a compact
polytope plus a closed polyhedral cone is closed (or use convergence of a
subsequence of the compact summands). Continuity extends equality from the
relative interior of the simplex to its boundary. ∎

Thus optimized tests identify an opportunity envelope, not every unused action.
This distinction is a consequence of post-assignment choice, not a failure of
calibration. The geometric theorem is a standard separation argument applied
here, not a claimed new convex-analysis result.

## P7-A2: when optimized tests recover the focal table

Suppose every row of each role is uniquely optimal for SOME full-support law.
This is decision-essentiality: no action is invisible to every strict
optimal-choice experiment. It excludes dominated actions and duplicate rows,
but does not require one action to be best under every belief.

Under this hypothesis P7-A1's indifference is equivalent to equality of the
sets of focal payoff rows, hence a bijection of own actions preserving all
state-contingent focal receipts. It still does not imply one simultaneous
automorphism of the full game.

**Proof.** A row uniquely best for a strictly positive normal is the unique
maximizer of that normal on D_i. The common downward set D_j has the same
unique maximizer; its maximum is attained at a generating role-j row. That
row must equal the original one. Do this for every row and reverse i,j.
Distinctness gives the required bijection. Conversely identical row sets
have identical support functions. ∎

The hypothesis is substantive and sometimes fails; the theorem must not be
advertised as recovery without it. Without it the two role menus
{(1,0),(0,1),(1/2,1/2)} and {(1,0),(0,1),(1/4,1/4)} have the same optimized
values under every law. Neither third row is dominated by a PURE action;
lottery/menu geometry, not just duplicate strategies, explains the failure.

A stronger group-theoretic converse fails even WITH decision-essentiality.
Take three binary players and r(0)=1,r(1)=0,r(2)=0, with

    u_i(s)=1[s_i=s_{r(i)}].

Each role has the same two-row focal coordination table after matching its
relevant opponent to one common position. Both actions are uniquely best for
suitable full-support product beliefs. Consequently the focal experiments
have identical opportunities and values. But the full actual player image
is trivial. Each focal payoff depends on exactly one other coordinate, so
an automorphism must satisfy p r(i)=r(p(i)). The directed successor graph
has distinct indegrees 2,1,0, forcing p=id. Local flips cannot change this
dependency argument. Hence even complete essential focal opportunity equality
does not recover simultaneous strategic interchangeability. A common map
must work for ALL payoff recipients to give a game automorphism.

## P7-A3: unordered observations project the opportunity sets

Let a finite group H act on T, with orbits O. Opponents' conditional law is
uniform within each orbit, but the law over orbits is arbitrary. This is a
specific hidden-identity experiment, not ex post indifference to arrangements.
Put

    (P_H x)_O=|O|^{-1}∑_{t∈O}x_t.

Robust optimized role indifference for all such exchangeable laws holds iff

    conv{P_H x_{ia}:a∈A_i}+R_{≤0}^{T/H}

is identical across roles. **Proof:** write every admissible law as an
arbitrary mixture of uniform orbit laws and apply P7-A1 in orbit space. ∎
Ordered tests imply these tests; the converse fails. With two binary opponent
positions take role0 rows d and −d, where d(00)=d(11)=0,d(01)=1,d(10)=−1;
take role1's two rows both zero. Every exchangeable law gives optimized value
zero in both roles, but the ordered law δ_01 gives role0 value1 and role1
value0. Concealing identities changes the evaluated opportunities rather
than making the original table anonymous.

## P7-A4: optimization separates IID from exchangeable testing

Let the two opponent actions be binary and use the same labels in each
experiment. Consider these role menus, with columns 00,01,10,11:

    role0: (2,0,0,0), (0,0,0,2), (0,0,0,0)
    role1: (2,0,0,0), (0,0,0,2), (0,1,1,0).

For every IID opponent law with probability p of action1 both optimal values
are 2 max{(1−p)^2,p^2}. Role1's additional value 2p(1−p) never exceeds that
maximum, since p(1−p)≤max{p²,(1−p)²}. However the exchangeable law giving
probability1/2 to each of01,10 yields values0 and1. Thus IID-optimal
indifference is strictly weaker than exchangeable-optimal indifference.

This can be embedded in ONE finite game: roles0,1 have three actions, players
2,3 have binary actions. Let u_0,u_1 be the displayed rows as functions of
their own action and (s_2,s_3), and put u_2=u_3=0. In each role experiment
fix the other candidate role's action at0. The IID comparison concerns only
the two active binary opponents, exactly as specified. No uniform full-game
strategy count or general transitivity is claimed for this example.

This is in contrast to UNOPTIMIZED all-action IID tests: polynomial coefficient
identification recovers orbit averages, so those tests have the same equality
power as exchangeable tests. See P7-O3 in phase7-independent-models.md.
The maximization changes the identification problem and invalidates that
linear conclusion. Ordered versus unordered information and before/after
assignment choice are separate dimensions.

## P7-A5: comparison with exact, cardinal and ordinal groups

A fixed exact transport preserving the focal payoff sends its rows and state
laws to identical rows and laws, so suffices for P7-A1. Exact player
transitivity with the corresponding physical transports gives this for every
role; no section is needed. These are sufficient conditions, not definitions.
P7-A2's graph game refutes the converse even when all actions are essential.
It also refutes recovering cardinal or ordinal transitivity: each coordinate's
essential dependence is preserved by any strictly increasing focal utility
map, so the same directed-graph obstruction applies to all three groups.

For an even more permissive optimal test, two three-action players can have
u_0(a)=1,0,0 and u_1(a)=1,0,−1, respectively, independent of opponents.
Both roles have optimal monetary consequence1 under every belief and EVERY
common increasing utility on {−1,0,1}. Nevertheless no ordinal automorphism
swaps roles: their utilities attain two and three levels. Thus allowing every
risk attitude does not restore a structural converse for optimized tests.

All exact common-scale indifference statements are invariant under ONE common
positive affine transformation, since V_i transforms by the same slope and
intercept. Independent role-affine transformations need not preserve them:
adding a constant to one role changes its value without changing its
within-role preferences. This is the preserved A1 underidentification, not
new permission to recode a fixed participant's global preferences.
Cardinal-normalized or rank-normalized receipts define DIFFERENT experiments
unless the participant's cross-role calibration justifies those choices.
They are valid algebraic representatives, not automatic welfare calibrations.

## P7-A6: risk-robust assignment indifference on common consequences

Now take a specified finite COMMON ordered monetary consequence set
z_0<⋯<z_L and a fixed opponent law μ. For each role/action form the tail
vector t_{ia}=(Pr[r_i(a,t)≥z_l])_{l=1}^L. Do not fix the participant's risk
attitude: require optimized role indifference for EVERY strictly increasing
expected-utility representation U on these consequences.

This holds iff the downward convex hulls of these tail vectors agree across
roles. Indeed write U(z)=U(z_0)+∑_{l=1}^L d_l 1[z≥z_l] with d_l>0.
Optimal expected utility is U(z_0)+max_a d·t_{ia}. Equality for all strictly
positive d extends by continuity to nonnegative d. The support-function proof
of P7-A1 applies. When L=0 every consequence is the same and the conclusion
is immediate. This is a finite first-order stochastic-dominance opportunity
criterion, not equality of ordinal game automorphism groups.

Risk-neutral indifference at one law need not satisfy it: a sure receipt1
and the equiprobable lottery on0and2 have equal means, but U(z)=z² separates
them. Conversely the best-receipt example in P7-A5 passes every increasing U
without even ordinal role interchangeability. A common consequence order is
extra cross-role data; role-specific ordinal preferences alone do not supply
it. No averaging of arbitrary rank numbers is proposed as welfare.

## What has been obtained

The independent decision model produces exact opportunity-set and tail-set
characterizations; natural information restrictions give strict separations;
and a decision-essentiality premise recovers focal tables but still not
simultaneous game symmetry. This is a limited positive result together with
decisive negative results. It does not assert one universal definition of
fairness. The companion information-design theorem identifies a different,
stronger commitment-test regime under which exact automorphisms CAN be
recovered despite some hidden identities, with a sharp alternating obstruction.

Full-support strengthening of A4: for 0<epsilon<1/2, the exchangeable law
(epsilon/2,(1-epsilon)/2,(1-epsilon)/2,epsilon/2) gives role values epsilon
and 1-epsilon. The separation does not depend on boundary beliefs.
