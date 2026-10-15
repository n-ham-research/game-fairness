# Coalition guarantees, equal treatment and reassignment histories

Status: **elementary comparisons and proved counterexamples**, not new claims
to cooperative-game theory. This extends the preserved VNM§28 comparison.
VNM edition actually inspected remains the1953third edition, not1944.

## A precise cooperative comparison

Use the existing F5 transferable zero-sum coalition convention: members of a
coalition may coordinate a JOINT mixed action; its complement coordinates
jointly and minimizes the coalition's summed receipts. Then finite minimax
gives a characteristic function v with

    v(N)=0, v(∅)=0, v(N\S)=−v(S).

Exact typed transports carry v covariantly. If the player image is
set-transitive, v(S) depends only on |S|, the VNM§28 fairness predicate.
This implication concerns cooperative guarantees, not a selected allocation
or a participant's subjective assignment preference. Separate player-affine
changes alter this transferable-payoff model; they are not mere units unless
one common scale and the transfer convention are retained.

Consider TWO later cooperative comparisons, clearly distinct from their
historical §28definition. The core is the set of efficient vectors x satisfying
x(S)≥v(S) for every coalition. The Shapley value is the usual uniformly
averaged marginal-contribution allocation. Its permutation covariance follows
by changing coalition labels in that formula; its efficiency is telescoping
along every ordering. These are established facts, not candidate discoveries.

**P7-C1.** For any coalition-size-dependent zero-sum characteristic function
with the complement identity above, its Shapley vector is zero. Its core is
nonempty iff v is identically zero; in that case the core is {0}.

**Proof.** Every player permutation preserves v. Covariance and efficiency
therefore force every Shapley coordinate equal with sum zero. If the core
contains x, it contains every permuted x, and by convexity their average zero.
The core inequalities at zero imply v(S)≤0 for every S. Apply this also to
the complement and use v(N\S)=−v(S); hence v(S)=0. Conversely for v=0,
zero is in the core, and singleton constraints x_i≥0 plus efficiency force
x=0. ∎

More generally a constant-sum TUgame has a core only if its v is additive:
coalition and complement inequalities combine to equalities x(S)=v(S).
P7-C1 is this standard obstruction specialized to the historically relevant
anonymous zero-sum data. It is not a claim that VNM proposed the core as their
§28fairness concept.

**Explicit strategic witness.** Three binary players receive zero on 000and111.
Otherwise the two majority players receive1each and the minority receives−2.
The game is zero sum and ordinary fully symmetric. For a singleton choosing
1with probability p, the opponent coalition's four pure joint actions give
expected payoffs −2p,1,1,−2(1−p). The singleton maximizes their minimum at
p=1/2, with value−1. Complementary two-player coalitions therefore have
value1, while v(N)=0. This is VNM-fair by coalition sizes, has Shapley
allocation(0,0,0), and has empty core: the three pair constraints sum to
2∑x_i≥3, incompatible with efficiency. Thus cooperative guarantee fairness,
equivariant equal treatment and coalition stability genuinely differ, even
for one tiny fully symmetric normal-form game. No priority claim for this
example or core observation is made.

## The common mathematical principle and its limits

If a data-reduction or allocation map F is equivariant, input stabilizers
also stabilize its output: g x=x implies g F(x)=F(gx)=F(x). This elementary
principle underlies exact transport of coalition values, symmetry constraints
on Nash's bargaining solution, and equal treatment by the Shapley rule.
It is covariance of a chosen map with a specified domain/action, not a common
universal fairness predicate. VNM's statement is instead about its reduced
coalition data. Aggregation can forget asymmetries; equivariance of a rule does
not ensure that its value lies in a core, is incentive compatible or supplies
cross-role subjective calibration. The explicit example separates these.
Primary texts and exact domains are compared in phase7-literature.md and the
preserved literature annotations.

## P7-C2: what coherence can and cannot add to this decision model

Consider a finite history of requested player permutations. Every implemented
lift is an exact automorphism; let g_h denote their product. Suppose two
histories have the same total player permutation p. For every original pure
profile s and focal i,

    u_{p(i)}(g_h s)=u_i(s)=u_{p(i)}(g_{h'}s).

Consequently any terminal expected-utility comparison depending only on that
final role and its transported base-game receipt is identical for both
histories, for every initial distribution and every increasing utility of that
receipt. No section is needed. The same is true for multiple dated receipts
if at each matched observation date the two histories have the same player
permutation, and preferences depend on those receipt vectors alone: each
receipt agrees pathwise. Different intermediate player positions, new choices,
external commitments and action meanings require their own specified model.

This follows directly by composing exact payoff identities and extends the
preserved A4.3 beyond one expectation. It rules out a payoff-only welfare
advantage of coherence in this model. Coherence is required for the stronger
operational demand that the final TYPED state itself depend only on the total
permutation. If a participant separately values reset effort, physical labels,
identity privacy or history, those are additional consequences. Recompute the
complete preference-preserving group of that enlarged experiment; the old
nonsplit group need not remain a symmetry. Such augmentation might make
coherence instrumentally useful but does not establish it from the original
game alone. No normative superiority of sections is asserted.

Review clarification: multistage comparisons transport the same reference
profile, or a coupled common reference process, at matched dates. Fresh
history-dependent choices require a separately specified behavioral model.
