# Phase 10 — assignment timing and common commitments

18 October 2026. Nicholas Ham programme. Reconstructed from the pre-restart
assignment branch's theorem message; root supplied complete retained proof and
checks. This is a model-specific characterization using standard finite-choice
and polynomial arguments, not a universal definition of fairness.

## Independent model

A participant has one globally calibrated preference over a common finite
ordered physical consequence set. There are roles i, a common finite state
space T with announced role-independent law mu, and a common finite set A of
PHYSICAL commitments. Fixed bijections f_i:A->A_i specify how commitment a is
implemented in role i. They are announced constraints, not chosen after seeing
preferences to manufacture symmetry. Conditional consequence laws L_i,a(t)
include any fixed opponent-response policy and objective risk. The participant
does not observe t before acting. Opponents' actions need not be equilibrium
responses; a different response model requires recomputing these laws.

Role lottery lambda is announced. In the BLIND experiment a is committed
before the role is revealed, with f_i(a) implemented after assignment. In the
INFORMED experiment the participant learns i before choosing a. Write v_i(a)
for expected utility at fixed mu and common utility U, M_i=max_a v_i(a), and

    B(lambda)=max_a sum_i lambda_i v_i(a),
    I(lambda)=sum_i lambda_i M_i.

Randomization over commitments cannot improve these linear expected utilities.
One common affine change of U preserves the comparisons; separate role offsets
would change this specified assignment preference. No interpersonal calibration
or uniform uncertainty over roles is imposed.

## P10-A1: exact timing characterization at fixed preferences/beliefs

B(lambda) is constant over ALL role lotteries iff (i) M_i=M for all roles,
and (ii) there is a commitment maximizing every role simultaneously.

Proof: Dirac role lotteries imply (i). At any full-support lambda a maximizing
commitment must attain M in every role, since every term is <=M and their
positive weighted average equals M. This gives (ii). Conversely a common
maximizer attains M under every lambda, and no other commitment can exceed it.

More generally, for ANY fixed full-support lambda, I(lambda)=B(lambda) iff
there is a common maximizer, WITHOUT requiring the role maxima equal. Indeed
the gap for a commitment is sum_i lambda_i(M_i-v_i(a)); all terms are
nonnegative and equality forces each to vanish. Thus equality of opportunities
across roles and absence of value from learning one's role are distinct
requirements. P7-A1 concerns the former under choice AFTER assignment. The
older A2 comparison tested every fixed action, rather than optimizing blind
choice; neither was this conjunction characterization.

## P10-A2: universal blind indifference recovers ALIGNED consequence menus

Let consequences be z0<...<zL and X_i,a(t,l)=Pr(L_i,a(t)>=z_l). Suppose every
physical commitment a is uniquely optimal in AT LEAST ONE role for some
full-support mu and strictly increasing common U. This excludes behaviorally
unused commitments and duplicate laws within the witnessing role. Then the
following are equivalent:

1. B(lambda) is independent of lambda for every full-support mu and common
   strictly increasing U.
2. For each SAME commitment a, X_i,a=X_j,a for all roles i,j; equivalently,
   its state-conditioned consequence laws agree in the fixed physical encoding.

Proof: 2 implies identical expected commitment values, hence1. For necessity
fix a and a role where it is uniquely optimal at an interior preference/belief
point. Strictness persists on a nonempty open neighborhood in coordinates
(mu_1,...,mu_(|T|-1),d_1,...,d_L), d_l=U(z_l)-U(z_(l-1))>0. By A1 a common
maximizer exists at every point there. The witnessing role's unique maximizer
forces that common choice to be a; equal maxima imply v_i(a)=v_j(a) throughout
the neighborhood. The difference is a polynomial in these coordinates. It
therefore vanishes identically. Vary d and tend mu to each Dirac law to obtain
X_i,a=X_j,a entrywise. Repeat for every a. This uses the elementary identity
lemma in phase10-risk-opportunities.md, not convexification of rank-one tests.
If there is only one physical consequence, all laws are identical and the
conclusion is immediate, regardless of action labels.

P10-R2 only recovers menus up to action bijections under post-role choice.
A2 identifies the SAME independently fixed commitment across roles. It does
not infer simultaneous preservation of all other players' payoffs. That would
require shared full-game transports and all recipients, the stronger data
already distinguished by F1/A4.2. The theorem never defines fairness as a
symmetry condition.

## Counterexamples and failed stronger conjectures

Post-role indifference does not imply blind indifference. Two roles have rows
(1,0),(0,1) in role0 and the REVERSED rows in role1, on a common two-state
space with Pr(t0)=p. Every action is essential at some full-support prior.
Both optimized role values are max(p,1-p) for every prior. At equal role
probabilities the blind value is1/2, while the informed value is
1/2+|p-1/2|. The information premium vanishes at p=1/2 but is positive otherwise.
For a general common increasing utility on binary consequences multiply by
U(1)-U(0). This is a physical action-encoding/timing distinction, not an offset.
It can be embedded with two binary players having matching/mismatching
receipts; no untransported belief law is silently identified with the law
transported by an available typed automorphism.

Essentiality cannot be dropped in A2: give both roles a safe commitment paying1
surely, while the other commitment pays0 in role0 and -1 in role1. Blind
lottery indifference and zero role-information value hold for every prior and
common increasing utility, but the unused aligned rows differ. Equality at
one belief does not establish universal alignment, as the reversed-row example
at p=1/2 also shows. Role-value equality alone cannot detect commitment costs
unless those costs are included in the physical consequences.

## Prior, significance and checks

The no-information-premium criterion is a finite equality case of the usual
value-of-information inequality, not a new information theorem. The aligned
universal characterization is a technically distinct extension of the local
P7/P8 assignment model using the elementary polynomial lemma. Novelty remains
unresolved; no substantial original paper is claimed from this proof alone.
Kreps 1979 menu choice is relevant prior (actual source-access limits in the
risk note); Blackwell compares every decision problem, whereas this model
fixes physical consequences/commitments and varies specified preferences.

Five exact tests check A1 across exhaustive small payoff matrices and role
lotteries, the common-argmax information criterion, full-support reversal and
risk scaling, a stochastic-law aligned example and essentiality failure.
The tests corroborate finite identities; they do not prove the universal
polynomial theorem or originality. Fresh independent proof attack requested.
