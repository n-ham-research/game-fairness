# Internal reviewer C: mechanisms and ternary boundary

This reviewer received the Phase 4 request and existing Phase 3 mathematical
notes, then wrote `research/phase4-mechanisms.md`. This is a same-family AI
review, not an external peer review. The reviewer independently derived the
three-player binary classification from invariant flip kernels and focal
stabilizer actions, before consulting the binary agent's new code.

The S1b analytic proof was checked line by line: diagonal recognition, parity
rule, exclusion of the two reflections, exact fibre-product group and order-four
transposition lifts all hold. The restriction to common actions {0,1} was
noticed algebraically and checked against the pinned extracted Example 5.13
payoff table. All 216 binary rectangular restrictions were independently
classified; these distinguish inherited symmetry from emergent symmetry.

The reviewer found the common-interest ternary orientation witness with full
group of order 18, wrote its analytic exact-group proof, and checked all 1296
typed maps, 36 matchings and 27 binary rectangular restrictions. This exposed
an initially overstrong inference in reviewer B's emerging classification:
only testing <r,g> for one odd g does not justify saying the three exceptional
order-six groups are the only possible actual groups. Their joint overgroup
of order 18 is another possibility. Reviewer B acknowledged and repaired it.
The final deduction is that every odd element belongs to one of these three
twisted groups, forcing every even element into their parity fibre product;
the actual group then has order six or eighteen. Its projection splits in
either case.

For an independent implementation of B's finite exhaustion,
`experiments/phase4_ternary_independent.py` represents each typed map as a
permutation of the 81 utility cells, multiplies those permutations directly,
and constructs utility-cell orbit partitions by union-find. It does not import
B's script or its group/orbit/matching functions. It enumerates all 648 odd
lifts and independently obtains 19 groups, with order histogram
6:4,18:3,24:6,54:3,162:1,648:2. It constructs each possible matching from two
explicit local label permutations and tests all six transported player maps.
Exactly three groups have orbit closures without a full matching, all the
stated common-transposition twisted S_3 actions. The script completed with all
assertions passing. Shared primitive ambient-bijection enumeration is retained
and disclosed. The orientation witness has a separate analytic proof.

Fresh checking of the binary proof's sensitive four-player step confirmed:
normalizing the opponent transposition lift to flip focal i and applying its
central commutator with a disjoint lift forces the other fixed opponent's bit
to be unflipped. The normalized generators' product has no focal flip, so its
cube in <z> is identity. The opponent matching plus repeated binary opponent
bits supplies an odd lift fixing those bits and flipping the focal bit. This
proves own-action indifference in the exceptional case. The A_n utility-cell
orbit comparison for n>=4 and the signed complement classification also check.

The common-interest invariant obstruction applies only to exact restrictions,
full-payoff factor quotients and isomorphisms. The report explicitly leaves
more permissive reductions involving utility changes or player deletion open.
No novelty or external human approval is asserted.

## Targeted assignment-model review

The final `research/phase4-assignment-model.md` was independently checked.
With the reference transport explicitly fixed as t_0=id, A4.1 follows directly
from focal exact payoff preservation, A4.2 follows from Dirac opponent laws,
and A4.3 follows from equality of the observed typed transformations. The
one-shot result requires no compatibility between independently selected
role transports. The distinction between typed path dependence and utility
path independence is correct: two exact automorphisms with the same player
map deliver the same transported focal utility at each final position, even
when their strategy transformations differ by a kernel element.

One specification omission was reported to the coordinator: A4.2, stated for
arbitrary fixed transports, requires t_0=id (or an equivalent untransported
reference definition). Otherwise equal role values compare to u_0(t_0 s),
rather than u_0(s). This is repaired by fixing the reference identity in the
primitives. The common-money calibration and restrictions on cardinal/ordinal
inference are appropriately explicit. This is a check of the chosen model's
mathematics, not a claim that its transported beliefs or money calibration
are obligatory fairness assumptions.

## Interchangeability hierarchy and finite-range collapse

The final `research/phase4-interchangeability.md` was checked independently.
A section lifts an n-cycle to a cyclic subgroup with regular player action,
so it indeed implies strategy-trivial transitivity. Matching sections are
exactly normalized full matching actions by the audited matching theorem.
The strict utility-level witnesses fail even individual full-image symmetry
at the weaker level while having matching symmetry at the stronger one,
so they establish strictness of all three parallel implication chains.

The additional finite-range collapse lemmas are valid. Exact player
transitivity makes every finite numerical utility range the same ordered set;
an increasing bijection of this set is identity, hence every ordinal map is
exact. Cardinal player transitivity instead makes min-max-normalized finite
ranges identical; preserving rank then preserves each normalized numerical
level, giving a positive affine map on the original ranges. Constant utility
ranges cause no exception. Thus exact transitivity collapses all three groups,
and cardinal transitivity collapses cardinal and ordinal groups. These
arguments concern full pure-outcome preferences, as the note states, not just
best responses. No correction was needed.
