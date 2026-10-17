# Phase 10 — unordered opponents, ambiguity and timing

18 October 2026 reconstruction of17 October exploration. Nicholas Ham programme.
Finite minimax and convex support methods are prior; no new general ambiguity
or normative fairness theorem is claimed.

## Independent comparison model

A participant learns its assigned role i, then chooses a private action lottery
sigma before seeing an opponent arrangement t in finite T. Arrangements are
partitioned into coarse classes o (e.g. opponents' action histograms), with
announced probabilities pi_o. The participant sees neither the class nor the
arrangement before acting. Conditional arrangement probabilities are UNKNOWN,
not automatically uniform. Receipts r_i(a,t) are on one participant's globally
calibrated scale. A physical role-specific opponent correspondence is supplied.

In the hidden-law model, an adversary can know sigma but not the realized own
action and chooses any conditional arrangement distribution separately in each
class. The robust value is

    S_i(pi)=max_sigma sum_o pi_o min_(t in o) sum_a sigma_a r_i(a,t).

In the action-reactive model it observes the realized action and may choose
t conditional on that action and class. Then

    R_i(pi)=max_a sum_o pi_o min_(t in o) r_i(a,t).

These are TWO explicitly stipulated worst-case response models, not a claim
that opponents in every game minimize the participant's utility. Rational
responses under other utilities may give different policy sets. Exogenous
private randomization and its secrecy are resources. An exchangeable Bayesian
law instead fixes UNIFORM conditionals in each class, a third model.

## P10-OA1: robust opportunity characterization

Define

    G_i={z: exists sigma in Delta(A_i),
              z_o<=sum_a sigma_a r_i(a,t) for every t in o},
    H_i=conv{(min_(t in o)r_i(a,t))_o:a in A_i}+R_-^O.

These closed convex downward sets have finite LP lifts. G_i is closed by
compactness of sigma and passage to a convergent subsequence; both are bounded
above coordinatewise. Their support functions at pi are S_i and R_i, and
H_i is contained in G_i. The inclusion follows from
min_t sum_a sigma_a r_i(a,t)>=sum_a sigma_a min_t r_i(a,t).

Therefore equality of optimized role values for ALL class laws pi is equivalent
to equality of the corresponding G_i, or of H_i, respectively. Proof: the
same downward-convex separation argument as P7-A1; any finite separating normal
must be nonnegative because the sets are downward, and it can be normalized
to a probability vector. Full-support tests suffice by continuity. This applies
a known method to a distinct response-information experiment, not a new
convex-analysis theorem or a new Reynolds-average observation result.

## P10-OA2: sharp hidden-randomization advantage and planwise equality

For n own actions and receipts in[0,1], put c=R_i(pi). Then

    0<=S_i(pi)-R_i(pi)<=(1-c)(1-1/n).

For any sigma choose an action a with mass p>=1/n. In each class the adversary
may minimize this action's receipt. Other receipts are <=1, giving an upper
bound p sum_o pi_o min_t r_i(a,t)+1-p<=pc+1-p<=1-(1-c)/n.
Maximize over sigma. Pure strategies give S>=R. The bound is attained by one
class with n arrangements and r(a,t)=c+(1-c)1[a!=t]: pure worst-case value c,
while the optimal hidden uniform lottery gives c+(1-c)(1-1/n). The adversary
chooses the most likely action as t, verifying optimality. Endpoints n=1,c=1
are included. General bounded scales are obtained by common affine rescaling.

For a SINGLE class, equality

    min_t sum_a sigma_a r(a,t)=sum_a sigma_a min_t r(a,t)

for EVERY sigma holds iff one arrangement minimizes ALL action rows. Sufficiency
is direct. Necessity follows by taking full-support sigma: a minimizing t
has a sum of nonnegative gaps equal to zero, so every gap vanishes. Apply
classwise. This common least-favorable-arrangement condition implies G=H and
all optimized values agree. It is NOT necessary for optimized equality: add
a safe constant1 action to the matrix [[1,0],[0,1]]. Both optima become1,
although no arrangement minimizes all rows and some mixed plans still differ.
All-plan and optimized opportunity criteria must stay distinct.

## P10-OA3: identical unordered records can reverse assignment preferences

Let T={01,10} be ONE unordered class. Role0's two-action receipt matrix is
[[1,0],[0,1]], while role1 pays1/4 surely. Under uniform exchangeable beliefs,
role0's optimized value is1/2. Even with unknown hidden conditional laws it
can hedge privately and guarantee1/2, so it is preferred to role1. Under
action-reactive responses role0 guarantees0 and role1 is strictly preferred.
Revealing the ordered arrangement before own choice would give role0 value1.
Thus coarse observation alone does not determine role preferences; response
timing, conditional beliefs and private randomization all matter.

A single finite-game embedding has focal roles0,1 and opponents2,3, all binary.
Set u0=1[a0=a2], u1=1/4, u2=u3=0. In role0's experiment fix a1=0; in role1's
fix a0=0. Restrict opponents2,3 to arrangements01/10. This is a stipulated
CORRELATED opponent policy family, not unrestricted independent mixed play.
Every permitted response is a weak best response for the indifferent opponents,
but no unique equilibrium selection predicts worst-case behavior. The embedding
contains degenerate roles; it is an explicit model witness, not a nondegenerate
symmetry theorem. A one-action role with receipts(0,1) versus constant1/4
already reverses preference when uniform hidden beliefs are replaced by worst
hidden beliefs, without an action-reaction issue.

## Prior, novelty and exact checks

P8-B1 already handled a FIXED response policy; P8-V1 distinguished security
from full opportunity envelopes. Here the response is optimized adversarially
under two information structures. [Epstein–Schneider, Recursive Multiple-Priors](https://people.bu.edu/lepstein/files-research/rectang50.pdf), September 2002 primary
working manuscript, section 3, is relevant established rectangularity/dynamic
consistency prior; the earlier branch read that section and the source was
reopened18 October. This note does not derive a new recursive-prior axiom or
claim the timing bound absent from matrix-game literature. OA1 is a standard
convex/minimax application; OA2 is an elementary sharp bound with unresolved
exact priority; OA3 is a calibrated foundational separation. The substantive
lesson is that 'unordered' is not a complete preference/information model.

Nine reconstructed exact tests check small rational matrix timing bounds,
sharpness over action counts, planwise versus optimized equality, preference
reversal, class timing, calibration and the explicit game embedding. A
specialized exact two-action breakpoint optimizer is used, not a floating LP.
