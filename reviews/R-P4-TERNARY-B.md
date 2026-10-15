# Internal reviewer B: ternary boundary and S1b proof

This agent received the Phase 4 task, repository instructions, and Phase 3
splitting notes, with responsibility for the three-strategy boundary. It used
the shared exact typed-bijection primitives for its primary implementation;
this is not independent of every existing computational primitive. Its finite
group exhaustion and payoff-orbit closure code are new. All agents are from the
same model family and this is not external peer review.

The agent enumerated the 648 odd-player elements of the ambient three-player
ternary group and the nineteen groups generated with a fixed bare three-cycle.
All nineteen have a projection complement. Four do not have a complement
containing that specified bare three-cycle, so the stronger fixed-cycle claim
was discarded. These are exact exhaustive statements, not samples of payoff
tables.

The first closure calculation found three exceptional order-six groups. An
informal message briefly suggested that any larger actual group would force
full symmetry. Reviewer C's common-interest orientation witness exposed that
this inference did not follow from the minimal generated-group calculation:
two exceptional sections generate another nonfull group of order eighteen.
The final proof retains this group. Multiplication by one fixed odd element
forces the actual group into the parity fibre product; its kernel is a subgroup
of diagonal A3, giving the corrected exhaustive alternatives of order six or
eighteen. The written theorem and certificate contain the corrected argument.

Reviewer C independently recomputed the closure classification with a different
cell-permutation and union-find implementation, sharing only the enumeration
of ambient bijections. That review confirms the nineteen-group histogram,
three exceptional minimal groups, and final deduction. Root coordinated an
additional cross-check. The primary three tests regenerate the committed JSON
certificate and pass.

The complete P3-S1b proof was separately reread. Its simultaneous-zero diagonal,
two-equal-profile parity constraint, exclusion of reflections, and order-four
odd lifts are valid. The detailed checks appear in the last section of
`research/phase4-ternary-boundary.md`. The new splitting boundary establishes
four-strategy minimality for three players only; it makes no all-player-count
minimality claim. No manuscript, frozen original source, or audit-registry
status was edited by this agent.

The calibrated assignment model in `research/phase4-assignment-model.md` was
also reviewed. A4.1 follows directly from transported focal payoff equality;
A4.2's converse correctly requires all actions and Dirac opponent laws, and
its all-recipient strengthening is needed to identify an exact automorphism.
A4.3 distinguishes typed path independence from payoff path independence:
the latter cannot detect an exact kernel discrepancy. Observing the player
map as well as coordinate encodings avoids singleton-domain faithfulness
ambiguities. A4.4 properly separates canonical preference representatives
from the participant's already calibrated cross-role money utilities. No
mathematical defect was found under its stated one-participant/transported-law
primitives. This is a model-specific result, not a universal fairness axiom.

P4-T3 transfers the ternary results to cardinal/ordinal groups through the
already proved equality with exact groups of canonical normalized games.
P3-S1b is itself unchanged by those normalizations, establishing the same
three-player four-strategy minimality at all three preference levels.
