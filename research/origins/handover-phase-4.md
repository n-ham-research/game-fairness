# Research Phase 4 handover — 16 October 2026

This pass treats Figure 4 and Example 5.13 as **prior Ham 2021 work**, independently
checks the Phase3 candidates, and extends the mechanism classification to three
strategies. Complete internal proofs/certificates are supplied; novelty and
external mathematical scrutiny remain separate. The manuscript is unchanged.

## 1. Binary theorem: adversarial verdict

[phase4-binary-verification.md](phase4-binary-verification.md) reconstructs the
kernel classification, complement/stabilizer actions, Coxeter adjustments,
three-player signed potential, four-player passive exception and larger-player
rigidity separately. No defect was found in P3-E1/E2/E3. The exact-potential
conclusion is not conditional on accepting an unexplained classification.

A new independent GF(2) solver checks every embedded full-image binary subgroup
for n=3,4,5,6: respectively 15,35,51,99. Formal square-cycle coefficient checks
cover every real payoff assignment invariant under each subgroup. Every family
passes potentialness; every n≥5 family forces some full matching. Eight n=4
families lacking that conclusion are own-action indifferent. These are subgroup
coverage counts, not numbers of nonisomorphic games. Unbounded n uses the
written proof, not finite extrapolation.

## 2. Novelty: precise comparison, not clearance

[phase4-novelty-comparison.md](phase4-novelty-comparison.md) separates established
ordinary/renaming potential results from the current strengthening. The actual
Hofbauer–Sorger2002 §4.2.2 construction is now inspected: equation(4.15), with
weights one, gives the ordinary binary potential before later coordination
assumptions. Cheng et al. and the inspected Cao–Yang2015 proof are compared at
their exact assumptions. The n=3 signed potential is a direct consequence of
Ham's published table; Figure 4 is not a new classification discovered here.

The broad full-typed-image theorem is a **potentially new strengthening**, not
certified novelty. Final Cao–Yang2018 and relevant newer potential proof bodies
remain comparison gaps. The table also includes modern typed-symmetry work,
common-label permutation-group work and the alternating/skew literature.
No unsuccessful search is treated as absence of prior results.

## 3. Nonsplit witness: analytic proof survives

All three agents checked the binary-payoff S1b proof analytically: simultaneous
zero profiles force a common strategy permutation; repeated-action profiles
force parity; two reflections are excluded; only parity-matched translations
remain. All transposition lifts have order 4. Thus the full group, standardness,
full player image, nonsplitting and absence of a full matching remain verified.
The original three-value alternative and pinned history are retained.

## 4. Three-player ternary boundary and classification

[phase4-ternary-boundary.md](phase4-ternary-boundary.md) proves:

- **P4-T1:** standard plus full player image forces a section for three players
  with three strategies each. Therefore S1b's four strategies are minimal
  **at three players**.
- **P4-T2:** in the non-full region the actual full automorphism group, after
  labels are normalized, is either the twisted S3 of order 6 or
  `L={(p;(f,f,f)): sign(p)=sign(f)}`, of order 18 and kernel C3.
- **P4-T3:** the same statements hold for cardinal/ordinal groups using their
  exact normalized representatives. No arbitrary-player ternary theorem is
  asserted.

The complete finite proof reduces standardness to a bare C3 and checks every
one of 648 odd lifts in the 1296-element ambient group. They generate19 distinct
groups. Explicit complement certificates settle splitting. Payoff-orbit closure
shows only three minimal generated groups can occur in a non-full game; an
additional algebraic argument classifies their possible full overgroups as
order 6 or18. This is a theorem about **all real payoff tables** on this fixed
domain, not a sample of games. Two independent implementations reconstruct the
utility-cell actions, one without importing any group/matching code.

A temporary inference that only the minimal order 6 groups could occur was
rejected: it confused generated subgroups with full overgroups. The orientation
game exposed the missing order 18 case, which is now proved and recorded. Another
false strengthening—requiring a section to contain a preselected standard
three-cycle—is explicitly excluded by the certificate.

## 5. Uniqueness, reductions and a new mechanism

[phase4-mechanisms.md](phase4-mechanisms.md) gives a separate algebraic
individual-game proof of the binary claim: every three-player binary full-image
non-full game is a specialization of 5.13 with beta!=gamma. The earlier complete
seven-family/cover verification of Figure 4 is retained as an audit of prior
work, including parameter coincidences, not rebranded as novelty.

A ternary common-interest game has payoff0 at repeated actions, +1 at even
permutations of 012, and -1 at odd permutations, for **every** player. Its full
Aut is exactly L of order 18. It is standard and full-image, splits, but admits
no full matching. The proof excludes all additional local strategy maps;
all 1296 ambient maps and all 36 matchings independently check it.

This game cannot reduce to non-full5.13 through any sequence of arbitrary
rectangular restrictions, full-payoff clone quotients and exact isomorphisms:
those operations preserve common interest, whereas beta!=gamma violates it.
It is clone-free, and every binary restriction loses the target region. Thus
minimal-reduction uniqueness fails for this specified, fairly permissive exact
system. It says nothing about operations altering utilities or deleting players.

By contrast, S1b **does** restrict on common actions {0,1} exactly to5.13 with
alpha=gamma=delta=0,beta=1. It is irreducible only under inherited-full-image
restrictions, not arbitrary restrictions admitting emergent automorphisms.
All216 binary rectangles were checked. The reduction notion materially changes
the answer; structural distinctness alone is not irreducibility.

The three witnesses have kernels1,C3,C2, with the last nonsplit. They therefore
have distinct projection-aware mechanisms. The raw orientation array is related
to established alternating/skew mathematics; its novelty is not claimed merely
because the explicit game was derived in this pass.

## 6. Utility invariance and one assignment model

[phase4-interchangeability.md](phase4-interchangeability.md) proves and attributes
the individual/coherent/matching implications under all three utility notions.
An additional direct finite-range consequence is useful: exact player
transitivity makes all three automorphism groups identical; cardinal player
transitivity makes cardinal and ordinal groups identical. Thus these exactly
standard witnesses are not artifacts of choosing exact utility preservation.

[phase4-assignment-model.md](phase4-assignment-model.md) fixes one risk-neutral
participant, monetary calibration, after-assignment actions, disclosed
assignment probabilities and transported opponent beliefs. Individual exact
realizability already gives equal conditional opportunity values; a section
adds no stronger one-shot indifference there. All-action/all-belief tests have
precise focal converses. Typed path independence of repeated exchanges is
exactly a section condition; utility-only history independence is weaker
because kernel discrepancies preserve payoffs. The review added the needed
reference normalization t0=id. No welfare cost of nonsplitting is assumed.

## 7. Sources, publication and next investigation

[phase4-source-requests.md](phase4-source-requests.md) lists the exact passages
needed from DM86, final Plan, final Cao–Yang and potential-game comparisons,
and first-edition VNM. Inaccessible URLs were not retried repeatedly. No
external messages or submissions were sent.

**Publication recommendation:** prioritize a possible PaperA on actual player
actions, lifting, binary rigidity and the ternary boundary/mechanisms, subject
to novelty comparison and human review. Corrections and prior Figure 4 belong
as attributed foundations, not the principal new contribution. PaperB is a
research programme on utility/assignment fairness; its current normalizations
and elementary transport comparisons do not yet establish sufficient new
content for a separate publication. Do not create either manuscript yet.

Next mathematical work should distinguish increasing strategies from increasing
players: analyze three-strategy games with four or more players, and ask which
new kernels/stabilizer actions survive payoff-orbit closure. Do not seek a
universal one-exception statement without specified reductions or a general
realization theorem. The two ternary mechanisms and the four-action nonsplit
mechanism already demonstrate richer behavior than binary5.13 alone.

## 8. Validation and provenance

74 tests currently pass; source-integrity checks preserve all 5 pinned artifacts
and the original 41-result registry (33 verified,7 corrected/clarified,1 original
ambiguity). Independent ternary verifiers also pass. General binary proofs and
finite ternary certificates are distinct evidence types. Final fresh-checkout
build/test and Git push results are recorded in chat.

A,B,C received the same repository/full conversation context with separate
initial assignments, then exchanged candidate constructions and proof checks.
They are same-family AI reviews, not blinded human or external peer review.
The actual corrections, derivations and review scope are recorded in
reviews/R-PH4-BINARY-A.md, R-P4-TERNARY-B.md and R-P4-MECHANISMS-C.md.
The original manuscript, archive, counterexamples and correction history remain
traceable; no copyrighted source PDF is tracked.
