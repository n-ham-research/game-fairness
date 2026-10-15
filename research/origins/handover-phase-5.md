# Research Phase 5 handover

16 October2026. Nicholas Ham's symmetric-games programme. New mathematical
results remain candidate contributions: internally proved and adversarially
checked, with novelty provisional and human review outstanding. The original
LaTeX manuscript is unchanged.

## Main answer

**Ternary splitting survives through five players and fails at six.**
More generally, standard ternary games with full actual player image split
whenever3 does not divide the player count. A six-player binary common-interest
game has full exact group of order2160, player kernelC3, a player-transitive
strategy-trivial subgroup, and no projection section. Thus six is the sharp
minimum player count in the ternary setting. Exact/cardinal/ordinal versions
follow separately through canonical normalization; the witness itself is
unchanged by those normalizations.

The witness uses the known triple-cover representation3.S6. That group and
its nonsplitting are prior algebra, explicitly credited. The candidate game
application establishes full exact realizability and standardness, not merely
an abstract extension. No priority claim is made.

## The nine requested deliverables

1. **Final ternary audit:** [phase5-ternary-audit.md](phase5-ternary-audit.md).
   Independent completeness reconstruction reduces648 odd lifts to32local
   conjugacy classes and11generated-group classes. All19embedded groups and
   actual payoff closures agree with Phase4. Order6/18 are still exhaustive;
   cardinal/ordinal conventions are checked. A symbolic replacement for the
   finite eleven-class lemma is not claimed.
2. **Four-player ternary results:** [phase5-splitting.md](phase5-splitting.md)
   proves splitting under standardness/full image. It has a conceptual route
   through the general theorem, plus an independently reconstructed251case
   regular-cycle certificate. Full mechanism classification at this size is
   still open.
3. **General theorems:** local-sign kernel lemmas, the3∤n splitting theorem,
   and the necessary order3n!/commonC3/parity-twisted type of larger nonsplit
   obstructions. See the same proof and [result dependencies](phase5-results.md).
4. **Explicit games:** [six-player binary common-interest game](phase5-six-player-obstruction.md),
   with eighteen winning profiles; [opposite-face mechanisms](phase5-mechanisms.md),
   including a binary four-player ternary split/non-full group of order72 and
   a generalmstrategy realization. Full groups are proved, not assumed.
5. **Reductions:** [phase5-reductions.md](phase5-reductions.md) defines exact
   rectangles, inherited groups, full-vector clones, multiplicity-preserving
   quotients and fixed-action player deletion separately. A canonical clone
   quotient has a split exact sequence when multiplicities are retained.
   Common interest rules out reducing the six-player game to non-full5.13
   even with fixed-action player deletion; minimality at fixed player count
   allows emergent rectangular symmetries.
6. **Publication proofs:** [phase5-publication-proofs.md](phase5-publication-proofs.md)
   gives definitions and standalone binary/ternary/four-action statements and
   proofs; the linked general and six-player notes give the new lifting proofs.
   Essential finite lemmas specify input encodings, exhaustive domains and
   verification predicates. Python names are not substitutes for arguments.
7. **Novelty:** [phase5-novelty-comparison.md](phase5-novelty-comparison.md).
   Newly inspected full primary covering-group and Hadamard texts sharply
   delimit the contribution. Orbit closure, alternating arrays, triple covers
   and the known18point representation are prior. The game classification,
   minimal boundaries and exact reductions remain candidates. Existing final
   DM/Plan/Cao requests are retained, not repeatedly retried.
8. **Publication structure:** [phase5-publication-outline.md](phase5-publication-outline.md).
   Lead with actual actions, matching versus sections and the ternary player
   boundary. Separate prior work, refinements, candidate contributions and
   open questions. Keep binary potential/fairness projects separate.
9. **Strongest questions:** [open-questions.md](open-questions.md). Which
   parity-twisted cyclic three-extensions at larger3-divisible counts survive
   standardness and actual payoff closure? Is six's mechanism unique within a
   useful equivalence? What are all four-player ternary non-full groups?
   Can the residual finite lemma become conceptual, and can stronger reductions
   support a useful core theorem?

## Verification and provenance

The complete suite currently contains88passing tests. The audit checker
preserves all5pinned originals and the41formal-result counts33/7/1. The build
passes; no paper source is changed. A clean staged-tree checkout in /tmp/symmetric-games-phase5.QEb1UJ also
passed all88tests (9.72seconds), the audit check and a fresh six-page build. No source downloads, third-party PDFs or user zip
are tracked.

Three initially separate same-family agents contributed independent proofs
and implementations, then cross-reviewed each other's results. See
[review log](../reviews/review-log.md), [AI contribution record](ai-contributions.md),
and the three R-P5 reports. The six-player full-group claim is independently
checked three ways; the short analytic kernel proof reduces it to twelve
cases, with exhaustive46656pointwise maps as supplementary checks. A
perfect even-player preimage forbids any section, not merely strategy-trivial
ones. Shared model/context limitations remain explicit.

Nothing was submitted to a journal or arXiv. No human proof sign-off or
exhaustive novelty clearance is implied by this handover.
