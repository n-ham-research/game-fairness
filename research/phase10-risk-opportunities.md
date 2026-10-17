# Phase 10 — universal common-risk indifference: characterization and limit

18 October 2026 recovery of17 October work. Nicholas Ham programme. Root proposed
the polynomial lemma and lottery application; the earlier assignment branch
independently reached that idea and supplied the explicit counterexample.
Fresh reviewers reconstructed the claims. Novelty remains provisional.

## Independent model

A participant observes role i, chooses an action from A_i, and then faces an
unobserved state t in a common finite set T with role-independent prior mu.
Fixed physical consequence lotteries L_i,a(t) have outcomes z0<...<zL on ONE
common scale. Fixed opponent responses can be included in these laws; no
unspecified endogenous response is inferred. A common strictly increasing VNM
utility U applies across roles and states. Write d_l=U(z_l)-U(z_(l-1))>0,
X_i,a(t,l)=Pr(L_i,a(t)>=z_l). Apart from the common baseline U(z0), the optimized
conditional role value is

    V_i(mu,d)=max_a sum_(t,l) mu_t d_l X_i,a(t,l).

Equality across roles for every full-support mu and positive d is universal
COMMON-RISK assignment indifference under post-role choice. It is defined
before referring to symmetry. Objective lotteries and their probabilities are
physical data. Independent role-affine recodings are not harmless changes of
this participant's already specified cross-role preferences.

## P10-R1: finite polynomial envelope lemma

For finite polynomial families f_a,g_b on a nonempty open Euclidean domain O,
suppose max_a f_a=max_b g_b everywhere in O. If f_a is strictly best among its
family at some interior point, it equals some g_b as a polynomial. Therefore
if every member in each family wins strictly somewhere, the polynomial SETS
agree. Action labels/multiplicities are not identified by values.

Proof: strictness persists on a nonempty open neighborhood W. At every x in W,
some g_b(x)=f_a(x). Hence product_b(f_a-g_b) vanishes on W. A polynomial zero
on an open set is identically zero (induct on dimension using the univariate
root bound). The real polynomial ring has no zero divisors, so a factor is
identically zero. Reverse families. A singleton family needs no competitors;
duplicate polynomials cannot each win strictly. This is an elementary use of
standard polynomial identity facts, not a new algebraic theorem.

## P10-R2: risk-essential opportunities are identified

Assume every action in every role is uniquely optimal for SOME full-support
mu and strictly increasing common U. Then universal common-risk indifference
holds iff the full state-conditioned consequence-law MENUS agree across roles,
up to an action bijection.

Proof: eliminate the last prior coordinate, making the interior simplex times
positive d an open parameter domain. Action values are polynomials. Apply R1;
polynomial equality means sum_(t,l)mu_t d_l(X_i,a-X_j,b)(t,l)=0. Vary positive d,
then approach each Dirac mu, obtaining equality of every tail entry and thus
every consequence probability. Essentiality excludes duplicate law matrices,
so equal sets give a bijection. The converse is immediate. If there is only
one consequence all laws coincide; values do not recover duplicate labels.

This extends P7-A2's deterministic fixed-risk essential-row test to physical
lotteries and essentiality across risk attitudes. It does NOT treat rank-one
positive mu*d as every positive state-consequence matrix. For tails
(9/10,1/10) and (3/5,2/5) on {0,1,2}, risk-neutral means tie but each wins for
some positive increments d, so the new essentiality need not hold at the
risk-neutral utility. The equality concerns focal menus, not a simultaneous
player map: the graph investigation still blocks that inference even for
identical deterministic menus with all actions essential.

## P10-R3: all common risk attitudes can miss a genuine opportunity

Without essentiality, universal mu/U tests can be strictly weaker than tests
with state-dependent increasing preferences. Let T have two states and outcomes
be {0,1,2}. Set X=(3/4,1/4;3/4,1/4). Role0 offers four tail matrices
X+(1/20)h_j, with row-major directions

    h1=(-1,5/2,0,-1), h2=(-1,0,5/2,-1),
    h3=(1,0,0,-4),   h4=(-4,0,0,1).

Role1 offers those four and X. All matrices are valid tail laws. Adding X
changes no optimized common-risk value for ANY prior. To prove it, write a
positive rank-one weight as w=(x,y,z,t) with xt=yz. If x>=4t, h3.w>=0; if
t>=4x, h4.w>=0. Otherwise x/t lies in(1/4,4), so
x+t<=(5/2)sqrt(xt)<=(5/2)max(y,z), giving h1.w>=0 or h2.w>=0.
Continuity covers boundary priors. Thus an original action always matches or
beats X under a common utility/prior test.

But w=(1,1/10,1/10,1) has h1.w=h2.w=-7/4 and h3.w=h4.w=-3.
It strictly exposes X over all four old actions. This is a legitimate DIFFERENT
preference model: at prior(1/2,1/2), use state-dependent positive utility
increments (2,1/5) and (1/5,2). The utility is still common across roles but
now includes state as a consequence attribute. This is extra preference data,
not an equivalent recoding of a common state-independent U. Positive w also
separates X from the old downward convex hull in joint tail space.

The four original actions are each common-risk essential (rational witnesses
in code); X is not. Thus there is no contradiction to R2. Quantifying over
'all preferences' is mathematically empty until the allowed state dependence,
consequence space and calibration are specified. The counterexample refutes
a real attempted stronger conjecture, rather than another symmetry definition.

## Belief restrictions and prior work

R1 also works for polynomially parameterized opponent laws. Independently
varying each named opponent's mixed action identifies ordered consequence-law
arrays, by multilinearity/Dirac limits. Requiring all opponents to use the SAME
IID mix identifies only coefficients indexed by action histograms, hence uniform
histogram averages. Under essentiality in the restricted parameter domain,
optimized equality identifies these action polynomials, not information beyond
them. This is a standard polynomial consequence, not a return to mask design.

P7-A1/A2/A6 are prior local convex-opportunity results and are not rediscovered
here. R1 is elementary; R2 is a technically distinct finite extension; R3 is a
scoped checked separation with unresolved priority. Kreps 1979's menu-choice
representation is relevant established decision theory. The primary Stanford
[author page](https://www.gsb.stanford.edu/faculty-research/publications/representation-theorem-preference-flexibility)
abstract was inspected before restart; its full proof was NOT reconstructed,
and reopening failed on18 October. No claim of absence from that literature.
Blackwell compares all decision problems, whereas these tests fix consequence
menus and restrict preference variation. No Blackwell novelty claim is made.
Four retained exact tests cover lottery validity, the analytic rank-one
certificate on rational probes, essential witnesses and the joint separator.
