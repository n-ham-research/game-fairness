# Phase 8 — behavior, calibration and shared interventions

16 October 2026. Proved candidate comparisons; tools below are standard
support-function, game-equivariance and finite preference representation
arguments. No originality claim. Canonical continuation of P7-A1–A6 and
P7-C2, not a replacement for their assumptions.

## P8-B1: response policies preserve an opportunity theorem, with new rows

A participant knows the assigned role i before selecting a commitment c in
C_i. Nature's common scenario z in a finite set Z is drawn with announced
law mu. The participant does not observe z at commitment time. A disclosed
response policy Q_i(·|c,z) generates opponent behavior. Consequences and
one global utility W are fixed across roles. Put

  x_ic(z) = E[W(receipt)|i,c,z].

For finite C_i, optimized all-mu assignment indifference is equivalent to
conv{x_ic}+R_-^Z being the same for every role. For compact C_i and continuous
x_i, replace the finite row set by its compact image; the same criterion holds
and need not be polyhedral. Proof: compactness gives attained maxima, the
convex hull of a compact set in finite dimension is compact, and P7-A1's
support/separation proof applies verbatim. Own randomization over commitments
does not improve a linear expected utility objective. This is an application
of existing convex geometry, not a new strategic equilibrium theorem.

If opponents observe the realized pure action and respond to it, randomizing
before realization only convexifies the response-adjusted pure-action rows.
If they observe an announced mixed policy instead, the rows can change
nonlinearly. The original unadjusted game rows are then generally wrong.
Example: two scenario labels, own announced binary mixing probability p,
opponent action b in {0,1}, physical receipt b independent of own action.
A follower policy uses Pr(b=1|p,z=0)=p and
Pr(b=1|p,z=1)=1-p^2. Thus x(p)=(p,1-p^2). At mu=(1/2,1/2) the best
commitment p=1/2 gives 5/8; either pure commitment gives 1/2. An observer
reacting to the realized pure action instead gives convex mixtures of
(0,1),(1,0), value 1/2. The example is an explicit response policy, not a
claim that this policy is a rational best response. Its smooth curve also
has infinitely many exposed points for positive normals: maximize
w0 p+w1(1-p^2) at p=w0/(2w1) in (0,1).

Belief-dependent response or feasible policy correspondences Q(mu), C(mu)
need not produce one common opportunity set. Calling their value functions
support functions without checking this is incorrect.

## P8-B2: role-dependent beliefs identify a smaller class

Let the common test parameter be nu on Z, but the state law in role i is
mu_i=B_i nu, where B_i is a known column-stochastic matrix. Then

  V_i(nu)=max_a nu·(B_i^T x_ia).

The correct criterion is equality of the downward hulls of the transformed
rows B_i^T x_ia, not of the physical payoff rows. Proof is substitution and
P7-A1. If all B_i are the same invertible permutation, recovery reduces to
the old criterion; information-losing maps can conceal differences.
For one-action roles x0=(0,2), x1=(1,1) and both B_i mapping every nu to
(1/2,1/2), all role tests agree despite different physical rows. Conversely
identical physical rows need not give equal values with different role laws:
x0=x1=(0,1), B0 nu=delta0, B1 nu=delta1. Correlation among opponent positions
was already allowed by P7-A1's arbitrary common finite state law; it is not a
new extension. Correlation with a private recommendation observed before
choice changes the commitment set to contingent policies, or the timing.

## P8-B3: equilibrium is a correspondence, not an arbitrary fair selection

In simultaneous finite games all players choose strategically. For a fixed
game let E_N be its mixed Nash equilibrium set and E_C its correlated
recommendation-equilibrium set. Under any cardinal typed automorphism g,
pushforward takes each set bijectively to itself, by transporting best-response
or recommendation incentive inequalities. This is U5, a standard argument.
Exact automorphisms additionally permute physical payoff coordinates. An
exact-transitive game therefore has role-equal *sets* of attainable
coordinate equilibrium receipts. This does not make each selected
equilibrium role-indifferent.

Example: two players, actions A,B, unanimous AA pays (2,1), BB pays (1,2),
off-diagonal profiles pay (0,0). Swapping players and simultaneously swapping
A/B is an exact automorphism. AA and BB are strict Nash equilibria with
unequal receipts. Their equal mixture is a correlated equilibrium and has
expected receipts (3/2,3/2), whereas either pure equilibrium selection fails
role equality. Their mixed Nash equilibrium uses Pr(row A)=2/3,
Pr(column A)=1/3, with receipts (2/3,2/3). The automorphism fixes that mixed
profile. Equal mixing of AA and BB is generally NOT an independent mixed
strategy profile. This is why correlated recommendations and simultaneous
independent choices must be distinguished.

More generally average any equilibrium-selection law over a finite exact
automorphism group. The resulting law on Nash profiles is invariant and has
equal expected receipts when the player image is transitive. Its induced
law on action profiles is a correlated equilibrium: each Nash product law
is a CE, and CE inequalities are linear. This is ex ante random selection,
not selection of a single pure equilibrium. For cardinal groups, receipts
need normalization before numeric coordinate equality, which then describes
a chosen calibration rather than welfare on the original money scale.

## P8-I1: the missing information is shared intervention wiring

An independently specified laboratory controller exposes every actual pure
profile s (or all full-support laws whose expectations identify all profiles).
An assignment protocol p routes participants to recipient positions. Each
physical action controller has an unknown but fixed bijection
f_i:A_i→A_{p(i)}, calibrated once across all recipients and all trials.
Thus the actual joint intervention is g(s)_{p(i)}=f_i(s_i). These are
observed hardware/strategy labels, not inferred from equality of role values.
Each recipient's common-scale receipt is recorded in repeated trials.

For a fixed calibrated controller protocol g, absence of a receipt discrepancy
for every recipient and profile is equivalent to g being an exact game
automorphism. This is an identification statement, not a definition of
fairness: participants may prefer the same role opportunities even if the
multi-recipient receipt records reject the proposed routing. Full observation
of the JOINT distribution of receipts is unnecessary for deterministic
normal-form payoffs; recipient-wise conditional means under the SAME logged
intervention suffice. Separate experiments with unlinked controller choices
do not identify that shared wiring.

With known observation operators M_c on profile arrays, the records are
M_c d_i for d_i(s)=u_{p(i)}(g s)-u_i(s). Thus exact table recovery for
arbitrary arrays is equivalent to intersection_c ker M_c={0}. If the
intersection is nonzero, arbitrary multi-recipient game transport recovery
also fails uniformly: choose a nonzero invisible discrepancy d, two focal
players with identical singleton action sets, a nontrivial observed opponent
state space T, let u0=0,u1=d, and give other players zero payoffs. Swap the
two singleton players and fix opponents. Both discrepancies ±d are invisible
although the swap is not an automorphism. This construction permits unequal
action counts and assumes the common state channels act on T; it makes no
homogeneous strategy-count or minimality claim. Constant discrepancies are
visible because M_c 1=1 for every stochastic channel.

For a specified game and a finite candidate protocol set, a weaker exact
criterion suffices: no NONZERO attainable discrepancy tuple lies in the
product of channel kernels. Full rank is a uniform sufficient condition,
not necessary for every particular game. Observations can identify an entire
nontransitive group; player transitivity additionally asks whether the
identified protocols reach every role, and is never inferred from one
protocol alone. P7-A2 supplies a decision-essential focal equivalence example
with trivial player image when the shared wiring is not measured.

## P8-U1: what transformations preserve which tests?

1. Common-scale exact mean equality under all interventions survives one
common positive affine recoding. Independent role-affine recodings can
break it (role offsets); arbitrary common increasing recodings can break
mean equality (sure1 versus equiprobable0/2).
2. For a fixed protocol and focal recipient, preservation of all comparisons
between ALL profile lotteries is equivalent to
u_{p(i)}(g s)=a_i u_i(s)+b_i with a_i>0. Preservation of all pure-profile
comparisons is equivalent to the analogous strictly increasing finite-range
recoding. These are within-recipient preference observations; independent
positive-affine, respectively increasing, recodings preserve these tests.
They identify cardinal, respectively ordinal automorphisms when the same
calibrated controller protocol is used for all recipients. Proof: finite
expected-utility uniqueness and finite weak-order representation (U1).
These are richer behavioral observations than equality of optimized role
values. They do not supply the participant's cross-role calibration.
3. Nonconstant minmax-normalized utility tables are invariant under independent
positive-affine recodings; normalized ordinal ranks are invariant under
independent increasing recodings. Comparing their mean receipts is therefore
representation-independent in its stated algebraic class. It is a DIFFERENT
experiment from comparing original money. Constant roles require the fixed
zero convention; ordinal ranks are not generally expected-utility cardinal
representatives. Normalization BEFORE an observation channel matters.
4. For two lotteries on one common finite ordered physical consequence set,
equality of expected utility for EVERY strictly increasing utility holds iff
the consequence distributions agree. Threshold increments prove necessity;
sufficiency is immediate. This test is invariant under any common increasing
relabeling of consequences. Equality of pure consequence ranks is a distinct,
weaker question; equal means for one rank coding is not robust indifference.

For channels with trivial common kernel, commitment observations of normalized
cardinal tables detect cardinal automorphisms exactly; rank tables detect
ordinal automorphisms exactly. Subtract target minus source normalized array
and apply I1. No assertion is made that masking commutes with a nonlinear
normalization: in general it does not. Hidden consequence-law tests instead
apply the observation channels to EACH threshold indicator before using U1(4).

## P8-C1: exactly when label coherence is observable

Let H→P be the available exact implementation group with player kernel K.
Specify extra observations q on a physical state space X on which H acts,
including visible recipient role labels. Let
N={h: q(hx)=q(x) for every x}. Assume N is normal in H and N≤K. This is
not automatic for an arbitrary coarse observation; it holds when the
observations define an H-invariant equivalence relation: H preserves the
partition into q-fibers, and N is the induced action's kernel. Histories are
compared universally over the same reference x, not fresh endogenous play.

An implementation r:P→H, with r(1)=1 and projection r(p)=p, has observable
path independence iff r(p)r(q)r(pq)^{-1} lies in N for every p,q. Therefore
SOME observably path-independent implementation exists iff

  1→K/N→H/N→P→1

splits. Proof: compose r with H→H/N; the condition is exactly the
homomorphism equation. Conversely lift the finitely many values of a quotient
section arbitrarily, fixing identity. This is the standard quotient-extension
criterion applied to an explicitly specified observer, not a welfare claim.
If every kernel element is invisible, N=K and the quotient always splits;
if labels separate all implementations, N={1} and an actual section is
necessary. Payoff-only observations of an exact game make K invisible,
recovering P7-C2. If all roles are constant-payoff, all pure numerical
receipts are invisible even under many nonkernel maps, hence role labels
must be included to enforce N≤K.

Example H=C4→C2 with kernel {0,2}, X=C4 translated by H. Observe role x mod2:
N=K and quotient coherence exists. Observe the full physical label x:
N=0 and no coherence exists, since every odd lift has order4. Add switching
or label costs only if these form independently specified actual consequences;
the theorem identifies distinguishability, not a utility advantage from it.

## P8-V1: coalition-size opportunity envelopes before security reduction

For a coalition S in a zero-sum normal-form game, it may coordinate a joint
action a_S before an exogenous complement profile t. Form the vector of TOTAL
coalition receipts x_{S,a}(t)=sum_{i in S}u_i(a_S,t). A physical identification
of complement states across candidate coalitions is additional data and must
be disclosed; their action counts need not coincide. Apply P7-A1 to these
menus: all-belief coalition opportunity equality iff downward hulls agree.
This is a direct normal-form counterpart to a coalition comparison; it does
not attribute a new definition to VNM. If the correspondence is a bijection
of complement pure profiles, the zero-sum security value equals
max_{x in conv rows} min_t x(t), by finite minimax. Equal opportunity envelopes
therefore imply equal security values. The converse fails: matrices with
rows (0,0),(1,-1) versus the sole row (0,0) both have security0, but at belief
delta0 their optimized receipts are1 and0. These two strategic matrices
compare coalition experiments, not a claimed single homogeneous-role game.
Group relabelings transitive on coalitions of each size suffice to identify
such menus with transported states. Player transitivity alone is not
set transitivity. Coalition stability (core) remains a separate question.
