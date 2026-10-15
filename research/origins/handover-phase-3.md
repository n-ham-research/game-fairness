# Research Phase 3 handover — 16 October 2026

This pass produces two substantive mathematical answers with complete internal
proofs and exact checks. They remain **candidate contributions**, since novelty
and external mathematical review are outstanding. The main six-page manuscript
and pinned source/counterexample records are preserved. No submission occurred.

## 1. Specification resolutions

[phase3-specifications.md](phase3-specifications.md) chooses the natural
set-bijection interpretation of Corollary 4.10, gives the intrinsic bitorsor
formulation, and explains precisely which choice transfers a group law. The
original ambiguity remains recorded, not silently certified. Definition 3.24
is given explicit moved-player pair quantifiers for pure and independent-mixed
preferences; exact, ordinal and expected-utility preservation are separated by
examples. Correlated-lottery affine representation is explicitly a different
variant. Geometry is made measurable with finite positive area; recommend
omitting its formal machinery from the eventual central paper.

## 2. Splitting: the universal converse is false

[Complete construction and proof](phase3-splitting-proof.md): three players,
four actions each, payoffs in {0,1}. Full Aut is the 12-element fiber product
`S3 ×_{C2} C4`, acting by a player permutation and a common translation of
Z/4 with matching parity. It projects onto S3 and contains the strategy-trivial
transitive bare C3. Every transposition lift has order 4; a section would require
an involution lift. Thus no section exists.

The full automorphism group is proved analytically and verified against every
one of82,944 typed maps. All8 subgroups were checked independently for a
complement. Three players and two payoff values are minimal in their stated
senses; four-action minimality is **not** established. A separately derived
four-player/six-action obstruction is retained in
[phase3-splitting-search.md](phase3-splitting-search.md).

Splitting and strategy-trivial splitting remain distinct. The latter is
exactly full matching symmetry (audited Ham 4.23/5.2); Ham 5.13 already separates
it from ordinary splitting. Factor-set and Coxeter-lift criteria are explicit.

## 3. Binary pure equilibria: affirmative, with stronger conclusions

[Complete theorem and proof](phase3-equilibria.md): every binary
n-transitively standard game has an exact potential, so has a pure Nash
equilibrium and finite strict improvement paths. More strongly, **for n≥3
standardness is unnecessary**: actual player image S_n already suffices.

For n≥5 such a game is fully symmetric up to exact relabeling. For n=4 it is
either fully symmetric up to relabeling or every player is indifferent to
all own-action deviations, so every profile is a Nash equilibrium. Standardness
excludes the latter obstruction when it is not fully symmetric. The n=3 signed
exception has potential alpha on homogeneous profiles and delta otherwise.
The proof classifies binary kernels and actual permutation actions and handles
Coxeter relations; it is not an inference from small-player experiments.

The exact finite check covers all full-image binary subgroups at n=2,3,4
(5,15,35 respectively) and every real payoff assignment obeying their utility
orbit equalities. Formal square-cycle identities verify potentialness.
Representation copies are not counted as distinct games. Matching pennies
shows why n=2 needs standardness; a directed three-cycle shows why transitive
standardness alone is insufficient. The fully symmetric special case is prior
literature and is not claimed new.

## 4. Fairness comparisons

[phase3-fairness.md](phase3-fairness.md) fixes participant utility, assignment
lottery, information, actions, beliefs and admissible transports first.
All-action/all-product-belief conditional tests recover focal pointwise
preservation; testing one transport for every participant recovers exact game
automorphisms. Coherent implementation of all player permutations adds a
section requirement, which the new counterexample shows can fail.

Explicit examples separate local focal opportunities from simultaneous role
transport, optimal values from payoff menus, equal averages from structure,
and hidden-identity aggregation from ex post opponent indifference. The
coalition-value bridge is attributed to von Neumann–Morgenstern's actual
set-transitivity argument and supplied with a zero-value/nontransitive example.
There is no canonical general-sum fairness extension or manufactured universal
fairness/symmetry equivalence.

## 5. Sources and novelty limits

[phase3-literature-and-sources.md](phase3-literature-and-sources.md) distinguishes
inspected Cheng/Ham/2017 Plan/VNM text from Cao–Yang abstract/preview and
unavailable final Plan/DM86 bodies. New bounded attempts included the actual
Harvard PDF via web and browser; no readable DM86 proof was obtained. The
requested Definition 7/Lemmas 6–7/Theorems 6/6* trace remains unverified. The Plan
final PDF retrieval failed; no final/draft body comparison is claimed.

Cao–Yang's renaming symmetry and exact-potential theorem is a priority source
for full-text comparison. Broad searches did not find another settlement of
Ham's exact questions, but they do not establish novelty.

## 6. Reviews, tests and provenance

[phase3-results.md](phase3-results.md) records every theorem's assumptions,
dependencies, finite scope and provenance. A,B,C were separate subagents with
full conversation context and repository access. Their initial assigned
investigations differed; subsequent proof exchange was explicitly shared and
not blinded. A derived the principal splitting witness; B independently found
a second obstruction; C derived the binary theorem. Significant proofs then
received checks by the other agents and coordinator. These are same-family
AI reviews, not three independent human verifications or external peer review.
Actual findings and computations are in reviews/R-P3-*.md and the review log.

The original audit denominator remains41:33 verified,7 corrected/clarified,
1 unresolved original wording. The two definition replacements are now
specified; original immutable texts remain intact. Current validation and
commit/push results are recorded in the final chat handover.

## 7. Publication direction and next investigation

[Preliminary outline](phase3-publication-outline.md): a coherent main paper
could connect individual player realizability, nonsplitting obstructions, and
binary rigidity/potentialness. Keep only the operational fairness comparison
needed to explain coherent exchange. The wider normative fairness programme
may deserve a separate paper after its primitives and literature are settled.

**Next recommendation:** seek adversarial human review and targeted full-text
literature comparison of these proofs before expanding the manuscript. Then
investigate the strategy-count boundary: can the nonsplit standard witness
use three actions, and which additional hypotheses force a section for
nonbinary games? Two actions are ruled out by the binary analysis (including
the exceptional n=4 exclusion under standardness); four actions suffice.
Develop one justified fairness assignment model in parallel. Keep the DM86
source trace open without delaying independent research or inferring a verdict.
