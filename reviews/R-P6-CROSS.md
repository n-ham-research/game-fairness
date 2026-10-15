# R-P6-CROSS: final migration and manuscript cross-review

16 October 2026. One delegated Codex instance, same model family/shared project
context. Root explicitly authorized read-only access to companion Game Symmetry
for this review. The reviewer wrote the initial fairness draft earlier in this
pass; review of that draft is consequently self-review, not an independent
reviewer or external peer review. No other-repository files were changed.

## Scope and conclusion

Read all active sections of the structural manuscript, especially
paper/sections/06-player-counts.tex, and research/phase6-sharp-audit.md.
Independently reconstructed the new multiplier closure and attempted to break
the kernel/cocycle reductions. No mathematical counterexample or defect found
in the stated player-count theorem. Approval is internal and conditional on
the imported classical multiplier theorem and stated finite lemmas; it does
not certify novelty or replace human scrutiny.

## The only-six-player extension

For n≥8, H=q^-1(A_n) is genuinely a central C3 extension because the residual
module action restricts trivially to A_n. Since A_n is perfect, its universal
central extension maps into H over A_n. The multiplier has order2; its image
in the C3 kernel is trivial by coprimality. The resulting image D maps
isomorphically onto A_n, and H=C3×D. Since D is perfect, H'=D; this is what
makes D characteristic in H and normal in G. Merely choosing an arbitrary
complement without this characteristic argument would be insufficient.

For any lift t of a player transposition, q(t²)=1, so t² lies in C3.
Conjugation by t fixes its own square (a group identity) and inverts every
kernel element (the residual action hypothesis). Thus t²=(t²)^-1 and t²=1.
This argument is valid without first assuming t has order2. Normality of D
then makes <D,t> an index3 complement of order2|A_n|, and the actual inclusion
in G supplies a represented section, not just an abstract group isomorphism.
The n5/n7 exclusions use the separate 3∤n argument; no exceptional A7
multiplier is inadvertently treated as order2.

Source check performed in this pass: opened the accepted author PDF of
Lassueur–Mazza dated18May2015 and read §3, printedp6, which states the multiplier
orders2 except A6/A7 with order6. This directly supports the imported n≥8
input; it is not a new proof of the classical theorem. Source:
https://eprints.lancs.ac.uk/id/eprint/82264/1/endoSchurAnSn_Revised.pdf
No historical-priority conclusion follows.

## Earlier reductions and actualness

- Permutation-invariant binary/ternary subspaces are exhausted by the
  transposition-difference argument: a nonconstant vector generates the
  entire sum-zero subspace; the quotient is one dimensional.
- In the large-sign case, coordinate characters of E2 are distinct/nontrivial
  for n≥3. Averaging uses a group of order prime to3, not all of B.
  N=0 therefore yields a cocycle that is killed by E2 averaging and normality.
- Payoff closure is essential when parity-constrained signs have additional
  invariant payoff symmetries. At profiles with zero, parity can be corrected
  invisibly at that coordinate. At all-nonzero profiles, the fixed-focal odd
  transposition equates the two product-sign payoff classes. This proves the
  additional independent signs are actual automorphisms.
- K=T2 averaging is valid on R/N because its central involution acts as minus
  identity. The Coxeter distant-commutator support bound needs n≥5; it is not
  used unqualified at n4. Standardness excludes the n4 order4 double-
  transposition lifts.
- For K=0 and 3∤n, the invariant direct complement lifts the quotient cocycle;
  the proof correctly does not claim the cocycle itself must be a coboundary.
- Ordinary-action N=T3 normalized involutions have no translation outside the
  two moved coordinates. Braid and distant defects therefore have support at
  most3 and4, respectively; a constant nonzero vector cannot have that support
  when n≥5. The sign-twisted residual extension is the remaining case.

The abstract subgroup D_n is a valid counterexample to deleting actualness:
for even n, an n-cycle is odd, so every lift has total sign1; its nth power
flips every coordinate, and its order is2n. A section would supply an element
of order n over that cycle, impossible. Bare A_n is transitive/strategy-trivial
for n≥4. Payoff closure explains why D_n cannot be a complete game group.

## Manuscript exposition and finite scope

The structural paper separates full player image, sections and matching-based
sections early, attributes Ham's binary Figure4, and states finite classification
rather than pretending the table is a symbolic proof. The six-player argument
properly uses the full pointwise kernel together with surjectivity to exclude
extra automorphisms. Its standard subgroup order60/local-C3 stabilizer argument
uses the coprime order10 stabilizer, and the perfect-group coset contradiction
is valid. This pass did not rerun the 32-class enumeration or independently
regenerate the finite perfectness certificate; their exact domains and
verification rules are stated, and separate reviewers/programs cover them.

## Fairness draft self-check

No universal fairness equivalence is claimed. U2 normalization and U3 finite-
range arguments handle constants and ties. A1 changes global preferences while
holding each conditional preference fixed, rather than independently rescaling
one already fixed global preference. A4.1 uses t0=id and a common monetary
calibration; its universal-belief converse is explicitly focal. The mixed-NE
example has indifference equations q=1/2, p=2/3, and its ordinal swap correctly
fails mixed preservation while preserving pure equilibria. Histogram factorization
and orbit averaging are distinct, with expected averaging requiring a cardinal
representation. Path independence observes typed actions, not just payoffs.
The initial five-page foundation draft is an appropriate migration deliverable;
new decision-theoretic characterization and external review remain outstanding.

## Validation already performed by this instance

Local fairness LaTeX build passed. Rendered and visually inspected all five
pages; bibliography sizing removed an orphan sixth page. Final log had no
undefined citations or overfull warnings. Eleven tests present at that moment
passed; root subsequently copied the four assignment-rule tests and owns final
clean-checkout validation. Passing tests are finite evidence, not proofs of
the universal statements or independent mathematical peer review.
