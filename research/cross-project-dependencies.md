# Cross-project mathematical dependencies

The projects share the convention (P_p s)_j=s_{p^{-1}(j)} and compose right to
left. Each manuscript defines its own needed objects. The source baseline is
[game-symmetry at 976e227](https://github.com/n-ham-research/game-symmetry/tree/976e22798b8d679ec91339695a049f88d8ffbee5), formerly symmetric-games.

| Foundation or result | Canonical maintenance | Companion dependency |
|---|---|---|
| Typed bijections, matching theorem, original41-result audit | game-symmetry | game-fairness cites baseline corrections/definitions; imported support snapshots are frozen. |
| Exact/cardinal/ordinal groups, U1–U5, normalized representatives | game-fairness | game-symmetry cites transferred utility-invariance.md at baseline, retaining frozen historical copy. |
| Assignment A1/A4, calibrated role models, opponent ordering | game-fairness | Structural paper uses only the distinction between individual and coherent lifts, not subjective fairness conclusions. |
| Binary potential and rigidity; ternary splitting; six-player group | game-symmetry | Fairness cites exact source commit/identifier when using these candidate results; imported small game helper is frozen. |
| Full historical record and fairness sources | game-fairness | Symmetry keeps a short source-qualified account and historical evidence snapshots. |

Imported snapshots are not independently maintained theories. A suspected
error creates a dependency notice in research/companion-notices.md stating
source commit, result ID, evidence and affected conclusions. Agents must not
edit the companion repository without explicit user authorization. This
migration task expressly authorizes both repositories; subsequent independent
sessions do not inherit that blanket scope. No cross-session message is sent
without user authorization.

No shared code package is introduced. When a common definition changes,
record a notice and recheck the companion-dependent proofs before updating
its pinned version. Neither unpublished manuscript is represented as externally
reviewed literature. The2011 thesis/2021paper remain independently cited prior
sources, not interchangeable with candidate research.

The first independently runnable fairness snapshot is commit
[a5e7f06](https://github.com/n-ham-research/game-fairness/tree/a5e7f06).
Utility/assignment dependencies may cite this snapshot rather than relying on
a mutable companion branch. The underlying transfer source remains976e227.
