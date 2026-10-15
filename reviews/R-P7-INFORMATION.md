# Phase 7 independent information proof and assignment attack

16 October 2026. Internal AI review, not external mathematical peer review or
author sign-off. The reviewer first read the user brief and repository's
existing model/information notes, then developed P7-O1–O4 independently of the
root's opportunity-hull derivation. After sending the initial theorem and
counterexamples, the reviewer received and examined P7-A1–A6. Same-model agent
independence is limited; novelty is not cleared by this review.

## Independent initial work

The supplied brief emphasized distinguishing ordered and hidden opponent
positions without declaring fairness to be group transitivity. This led to
pair-masked experiments and the following results, in
research/phase7-independent-models.md:

- The common nullspace of pair-mask observations consists of tensors
  alternating within connected masking components, of dimension
  product_j binomial(k,r_j).
- Exact recovery requires and suffices that some component has more than k
  positions. Thus precisely k mask contexts can suffice when there are more
  than k opponents; fewer cannot suffice for arbitrary tables.
- Applying all-action/all-recipient tests gives an exact automorphism
  characterization under the specified common utility calibration. Alternating
  boundary games supply sharp simultaneous counterexamples below the cutoff.
- Unoptimized IID testing and exchangeable testing identify the same orbit
  averages. Robustness to every increasing VNM utility on one commonly ordered
  physical consequence space instead identifies outcome distributions.

Six exact tests in test_phase7_independent_information.py passed. Actual
observation matrices are reduced over rational arithmetic rather than counting
ranks using the claimed formula. They check overlapping masks recovering binary
three-opponent tables, the ternary cutoff, disconnected components, nonzero
invisible orientation tensors, full-game odd-permutation failures and robust
ordinal multisets. The manuscript must preserve the distinction between
all-action commitment tests and unrestricted optimized assignment choices.

## Adversarial review of root P7-A1–A6

**Verdict:** mathematical arguments pass this targeted internal review. The
claims are appropriately narrower than characterizing strategic symmetry.

### Downward hulls, separation and full support

The compact-plus-negative-orthant set is closed, despite being unbounded.
If separation of x from D_j had a negative normal coordinate, the supremum
over a corresponding downward ray would be infinite, contradicting strict
separation. The normal is therefore nonnegative and nonzero and can be
normalized to an opponent law. Its support value is attained at a listed row.
This proves necessity without assuming every row is exposed or efficient.
Equality under strictly positive laws extends to boundary laws by continuity;
no unjustified extrapolation from an IID curve is involved. The normalization
also handles a singleton state space.

### Decision-essential recovery

Strict positivity is sufficient to prohibit a downward displacement from
sharing the maximum. A uniquely optimal row is consequently the unique
maximizer on the entire downward hull, not merely on the original finite menu.
A common hull forces an identical generating row in the other role. Duplicate
rows cannot satisfy unique action optimality, so the induced bijection is
valid. The hypothesis is genuine; a row can be nondominated by each pure row
yet be unexposed because of mixed-row dominance or a flat convex face. The
provided three-row example correctly illustrates this distinction.

### The directed coordination game

Essential dependence on opponent coordinates is invariant under local action
bijections and strictly increasing utility recodings. Thus any of the three
automorphism notions must preserve the successor graph. Indegrees 2,1,0
force the player map to be the identity. Independent exhaustive enumeration
of all 48 typed maps found exactly two automorphisms: the identity and the
simultaneous flip of all binary actions, both fixing every player. Since all
utilities attain exactly {0,1}, ordinal and cardinal preservation coincide
with exact preservation here, giving the same result independently of the
dependency argument. Both focal actions are uniquely optimal for open sets
of full-support product beliefs, so failure is not explained by unused actions.

This is a simultaneous-versus-focal separation. The physical correspondences
between separate focal experiments are permitted to depend on the tested
participant. One must not silently claim a common simultaneous correspondence.

### Optimization changes IID identification

For p∈[0,1], p(1−p)≤max(p²,(1−p)²), so the extra middle-histogram row never
improves the IID optimum. The exchangeable counterexample is valid. It can
also use full support: μ=(1/8,3/8,3/8,1/8) gives respective optimal values
1/4 and 3/4, verified independently with Fraction arithmetic. Thus the
separation does not depend on singular opponent laws. The linear IID
polynomial argument in P7-O3 cannot be applied after a maximum over rows.

One editorial correction communicated to root: the linear IID equivalence
reference in P7-A4 should be P7-O3, not P7-O1.

### Risk-robust tail hulls

Every strictly increasing utility on the finite common consequence set is
represented uniquely by a base level and positive threshold increments.
Expected utility is the corresponding positive linear functional of tail
probabilities. Equality on the positive cone extends to its boundary, and the
same downward-hull separation proves necessity and sufficiency. This is a
standard finite stochastic-dominance/support-function argument, not an ordinal
game-automorphism theorem. L=0 is correctly handled separately. The sure1
versus fair0/2 example is separated by the strictly increasing encoding
U(0)=0,U(1)=1,U(2)=4. Allowing all risk attitudes still cannot reveal unused
worse actions when both roles offer the same best sure consequence.

## Limits to retain in publication

The model requires one participant's global cross-role utility calibration,
exogenous opponent behavior and post-role action choice. Role-specific affine
or ordinal freedom does not supply that calibration. Essential focal menus
still do not imply a simultaneous transport. The ordinal-robust formulation
requires a common physical consequence ordering. All-action pair-mask recovery
is a stronger commitment-test experiment, not ordinary optimized indifference.
No welfare benefit from coherent group sections has been demonstrated by
these results. No historical source version has been newly inspected in this
review, and none of the argument checks settles originality.

## Final manuscript check

The reviewer read sections 10–12 and the abstract after integration. Statements
faithfully preserve the model qualifications. Requested explicit whole-history
exact-lift/same-total-player-permutation hypothesis in section 12; incorporated.
C1/C2 separate read-only proof review passed, with the fixed reference-process
qualification incorporated. No further mathematical defects identified.
