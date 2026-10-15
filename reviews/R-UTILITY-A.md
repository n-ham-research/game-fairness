# R-UTILITY-A: utility-invariance reconstruction

Role: agent assigned utility-level exact/cardinal/ordinal groups after the
user's two additional utility/fairness attachments. Read both attachments in
full. Independently derived definitions, closure proofs, normalizations,
strictness examples and equilibrium distinctions before reading other agents'
new utility reviews. Parent supplied the anticipated normalization route and
requested the connection to the already reviewed binary theorem.

## Mathematical findings and actual computation

`research/utility-invariance.md` proves group inclusions and exact canonical
group realizations via per-player min-max and distinct-level rank normalization,
including constants. It proves range-signature equality criteria, common player
kernels and exact focal utility invariance for every ordinal focal stabilizer.
It derives weighted/ordinal potential, FIP and pure-equilibrium corollaries of
P3-E2, and gives face-identity counterexamples to stronger potential conclusions.
The positive affine/all-lottery characterization is explicitly distinguished
from pure ordering and from numerical equality across people.

Three-player binary strict player-transitivity examples were constructed
analytically. A two-player ordinal swap was constructed with rational mixed
Nash equilibrium (2/3,1/2) whose swapped image is not an equilibrium, while
both pure equilibria are correctly exchanged. This corrects the user's broad
claim about ordinal Nash nonpreservation: only mixed preservation fails in
general, while pure best responses and pure equilibria are always preserved.

Ran `python3 -m unittest discover -s experiments -p test_utility_invariance.py`:
three tests passed. Tests use direct pure-order and affine checks independently
of the normalizers, rational expected utilities, complete ambient typed-map
enumeration for the named finite examples, and exact face differences. They
verify common kernels, stabilizer exactness and source range-signature criteria
on those examples. No finite examples establish the general theorems; proofs do.

## Source comparison actually done

Opened and inspected Ham's author-hosted 25-page 2011 thesis via web PDF text.
Read Definitions4.2.3–4.2.4 and Propositions4.3.1–4.3.6, with exact primary
URL and printed/PDF pages recorded in the note. Thus the three isomorphism
classes, groupoids and pure/mixed equilibrium distinctions are explicitly
credited prior Ham work, not presented as discoveries. The thesis attributes
proofs4.3.4–4.3.5 to Noah Stein. Hammond's author-hosted utility chapter and
Tewolde–Conitzer arXiv2111.00076 were opened as source leads; no uninspected
full theorem was relied upon. Broader novelty comparison remains incomplete.

## Repair of independent-profile necessity

After drafting the basic framework, derived a proof that agreement of complete
weak preferences over all independent mixed profiles already implies a single
positive affine pure-table relationship. It uses generic hybrid marginal
profiles to cross any interior utility level along a one-player segment, making
the utility transform locally affine and therefore globally affine. This avoids
mixing arbitrary product joint laws. Parent independently derived the same
route and checked it by message. C independently checked the hybrid-polynomial
argument, constants, relative-interior coordinates, connected image and endpoint
extension. The complete proof is under U1; its conclusion was already asserted
in Ham2011 and is labeled a foundational reconstruction, not a novelty claim.

## Reviews and limits

B independently checked the initial full U1–U6 note and approved normalization,
range criteria, common kernels, mixed-NE witness and both potential corollaries.
C independently checked all those results and then the hybrid necessity proof.
B was also asked to check the latter. These are internal same-family AI reviews,
not external review or author sign-off. Fairness interpretations are explicitly
not inferred from the algebra. The binary corollaries remain candidate
extensions until their dependencies and exact literature comparisons are ready.

B subsequently independently approved the complete hybrid necessity proof by
message, explicitly checking singleton blocks via relative coordinates, the
finite product of nonzero hybrid polynomials, and endpoint limits through
full-support laws. No correction was requested.

## Independent review of assignment-and-solution-rules.md

Read the coordinator's complete assignment note after deriving the utility
framework. A1's arbitrary conditional-value construction correctly varies
global assignment preferences while keeping conditional role orders fixed;
it does not rescale an already fixed global preference. A2's before/after
assignment criteria follow from Dirac assignments with the stated timing.
A3's uniform random bijection equalizes ex ante prospects only under its
explicit common utility and role-contingent procedure assumptions. A4's
invariant-law numerical conclusion requires exact utility; normalized-cardinal
and ordinal qualifications are correct. A5's averaging formula is equivariant
by t=gh, and averaging pure equilibria yields a correlated equilibrium via
linear obedience inequalities; product independence is correctly not inferred.
Its deterministic fixed-point criterion concerns the stated fixed invariant
set, not an unproved global selector existence theorem. A6's distinction
between ordinal ex post ties and cardinal averaging is sound. No mathematical
changes requested; normative justification remains deliberately open.
