# Phase 4 targeted novelty comparison

16 October 2026. **No novelty certificate.** This compares hypotheses and
arguments actually inspected, and states remaining proof-body gaps. The
mathematical verification report is separate. Absence from search results
is not evidence of first discovery.

## Primary texts and exact differences

| Source/version actually read | Hypotheses and result | Relationship to current candidates |
|---|---|---|
| [Cheng–Reeves–Vorobeychik–Wellman, *Notes on Equilibria in Symmetric Games*](https://www.sci.brooklyn.cuny.edu/~parsons/events/gtdt/gtdt04/reeves.pdf), Definition 2/Theorem 1, printed second PDF page | Common-label ordinary fully symmetric binary game; a pure equilibrium exists. Proof uses adjacent population counts. | Established special case. Neither arbitrary typed full player image nor its extension/kernel classification is assumed or established there. |
| [Hofbauer–Sorger, *A Differential Game Approach to Evolutionary Equilibrium Selection*](https://homepage.univie.ac.at/josef.hofbauer/02igtr_sorger.pdf), IGTR4(2002),17–31, §4.2.2, printed p.27 | An A-player's payoff is a_k and a B-player's b_k, depending only on total A-count k. Equation(4.15) recursively constructs common potential levels c_k, with weights one. | Exact potential for ordinary fully symmetric binary games is established, not new. Coordination/supermodularity assumptions introduced **after** this construction concern selection and are not needed for the potential. |
| [Cao–Yang, *Symmetric Games and Symmetry Groups*, July29,2015 author draft](https://www.researchgate.net/publication/280600867_Symmetric_Games_and_Symmetry_Groups), Definitions4/6, Proposition 4 and proof | Name-irrelevant = full actual player image. Renaming = ordinary full symmetry after local labels. Proposition 4 applies only to renaming games and pulls back the Hofbauer–Sorger potential. Its negative broad-class example is two-player matching pennies. | The proof does not apply directly to nonmatching signed three-player or passive four-player cases. It does not supply the n≥5 rigidity step. This is a difference in inspected assumptions, not proof of novelty. |
| Same2015 draft, §6 Definition 8/Theorem 4 and AppendixJ | Common-label, multiplicity-based (weak) ordinal symmetry gives a binary ordinal potential. | Prior ordinal special cases must be credited. Its hypotheses are not stated as actual typed ordinal-player image S_n. Do not claim the basic ordinal-potential idea as new. |
| [Cao–Yang2018 final publisher preview](https://www.sciencedirect.com/science/article/abs/pii/S0165489618300490), MSS95,9–18; SSRN revised2018 record | Preview identifies binary ordinary/renaming exact potential and attributes it to Theorem 3. | Final body still not inspected. The2015 Proposition 4 must not be renamed final Theorem 3 without a full comparison. Whether the revised arguments imply more remains unresolved. |
| [Wang–Zhu2025, *On Symmetric Games With Respect to a Permutation Group*](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/cth2.70076), Definition 5/equation(5), theorem statements | Uses common action labels and bare coordinate/player permutation equivariance for a specified subgroup; derives discriminant equations. | This is the label-dependent action. It does not directly accommodate arbitrary per-player action bijections or establish their coherence. No binary full-typed-image potential theorem was found in the inspected statements. |
| [Wang–Li–Feng2024, *On potential equations of finite symmetric games*](https://onlinelibrary.wiley.com/doi/10.1002/asjc.3336), AJC26,2367–2376 | Publisher abstract identifies potential verification equations and weighted/skew variants. | Body not obtained; **novelty gap**, not an inspected exclusion. Its exact symmetry definitions and binary results must be compared. |
| [Tewolde et al., arXiv:2501.08905v2](https://arxiv.org/html/2501.08905v2), §§2,4–5 | Typed player/action symmetries, equivariant Nash transport, symmetric mixed equilibria, and complexity of respecting symmetries. | Directly relevant modern symmetry framework; no binary exact-potential assertion appears in inspected sections. Mixed symmetry-respecting equilibrium existence does not imply pure equilibrium or potentialness. Its introduction explicitly cites Ham 2021 on symmetry/fairness. |
| [Cheng–Liu2018, *From Boolean game to potential game*](https://www.sciencedirect.com/science/article/abs/pii/S0005109818303200), Automatica96,51–60 | Indexed publisher snippet explicitly covers ordinary, renaming and weighted symmetric Boolean games. | Full body unavailable in this pass. This is a priority additional comparison; a snippet cannot exclude stronger implications. |
| [Hao–Cheng, *On Skew-Symmetric Games*, arXiv:1712.02962v1](https://arxiv.org/html/1712.02962v1) | Defines signed permutation covariance and develops skew-symmetric game subspaces. | The ternary orientation payoff has a standard alternating-tensor character. Do not claim inventing alternating/skew payoff arrays. Its **full exact group**, matching obstruction and reduction behavior require their own comparison. |

The inspected Hofbauer–Sorger potential has increments
`c_{k+1}-c_k=a_{k+1}-b_k`. This is the same population-count construction
used in our full-matching cases. Therefore, at n≥5, the potentially substantive
new step is **full typed player image implies a full matching**, after which
potentialness is a direct use of established literature. For n=3 the signed
case is already Ham's Example 5.13 and Figure 4; its two-level potential follows
directly from the published payoff table. For n=4 the passive nonsplit case
has constant potential by own-action indifference. These components should be
credited and assessed separately, rather than presenting one undifferentiated
“new potential theorem”.

## Contribution-level assessment

| Candidate | Current classification | Reason / remaining work |
|---|---|---|
| Figure 4 seven binary family classes; Example 5.13's role | **Established in prior literature** | Ham 2021. Exhaustion and individual-game proof are verification/reformulation, not rediscovery. |
| Ordinary/renaming binary exact potential and pure equilibrium | **Established in prior literature** | Hofbauer–Sorger construction, Cheng et al., Cao–Yang. |
| Signed three-player potential from Example 5.13 | **Direct corollary of prior literature** | Check the published table: only homogeneous/minority deviations matter. |
| Broad n≥3 full-typed-player-image exact potential, with separated n≥5 rigidity/n=4 alternatives | **Potentially new strengthening** | Strictly broader than the inspected renaming theorem; full2018 and newer potential bodies still need comparison. No priority claim. |
| Explicit standard nonsplit four-action game, including binary-payoff realization | **Novelty unresolved** | Standard extension obstruction; actual full-group realization and small witness need targeted representation/game literature comparison. |
| Three-player ternary splitting and exact group 6/18 classification | **Novelty unresolved** | Complete finite-group certificate supplied here; no prior absence claim. |
| Ternary orientation mechanism and no reduction to5.13 under specified exact operations | **Novelty unresolved** | Alternating payoff construction is natural/related to prior skew literature; mechanism/reduction statement is the relevant candidate, not the raw sign array. |
| Utility normalizations, common-kernel and one-shot transport facts | **Direct corollary of prior literature / foundational reconstruction** | Prior utility representation/isomorphism results and finite ordered-range arguments. |
| Calibrated assignment model and typed-versus-utility history distinction | **Novelty unresolved** | Complete model/comparisons supplied; no standalone publication-level novelty established. |

## What this does and does not settle

The inspected Cao–Yang proof is literally a pullback from a full matching; our
nonmatching examples cannot satisfy that premise. An additional classification
or rigidity argument is required to extend it. This rules out *that direct
application*, not every possible consequence of all their results. Full-text
comparison of final versions is still necessary. Search terms covered typed
automorphisms, player exchange, binary/Boolean potential games, permutation
actions, renaming/name-irrelevant symmetry and skew symmetry; titles alone
were not treated as theorem comparisons.

No candidate receives “apparently new” solely because a search failed. The
recommended paper must describe its contribution conditionally until the
remaining comparison and human mathematical scrutiny are complete. The exact
missing texts/passages are collected in phase4-source-requests.md; no external
request was sent on the user's behalf.
