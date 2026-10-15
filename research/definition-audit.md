# Definition and example audit — all 33 numbered items

Original statements remain pinned in original-record.json. Status here concerns a mathematical definition or an explicitly scoped example, not endorsement of its philosophical fairness interpretation. The 41 formal results have separate counts in theorem-audit.md.

| Item | Status | Mathematical check / required clarification |
|---|---|---|
| Example 2.1 | Verified | All source payoff cells extracted; full automorphism order 6, matching-lift full symmetry; displayed lookup checked. |
| Definition 3.7 | Verified | Exact equivariance typed by player index and left profile action; subgroup proof audited. |
| Definition 3.9 | Verified | Focal payoff invariance under actual point stabilizer; common-label requirement explicit. |
| Example 3.10 | Verified | All focal-stabilizer permutations checked on every extracted cell; no nonidentity exact automorphism. |
| Definition 3.11 | Verified | Separate each-player profile invariance from player-permuting equivariance; well-defined on common labels. |
| Example 3.12 | Verified | Each payoff constant on Hamming-weight profile orbits; extracted numeric table checked. |
| Definition 3.13 | Verified | Universal focal/target payoff condition; equivalent to total symmetry plus identical functions as audited 3.19. |
| Example 3.14 | Verified | Common payoff depends only on number of second actions; full anonymity and exact automorphisms checked. |
| Definition 3.15 | Verified | Transitivity is a property of the specified payoff-preserving player action, not abstract group type. |
| Example 3.16 | Verified | Extracted numeric table has cyclic image of order 3; some matching lifts transitive, none full. |
| Definition 3.17 | Verified | Full specified permutation-equivariance; requires common labels. |
| Definition 3.22 | Verified | Finite two-player zero-sum value exists by minimax; zero-value definition is mathematically well-formed. |
| Definition 3.24 | Resolved replacement | Phase 3 supplies explicit moved-player pure-profile and independent-mixed-profile pair quantifiers, subgroup proofs, implications and separating examples. Original unspecified intent is not retrospectively certified; see phase3-specifications.md S2 and utility-invariance.md U1 for the complete independent-mixed/affine identification. |
| Example 4.1 | Verified | Matching pennies: identity-only bare player symmetry, full typed Aut order 4 with transitive image and no transitive strategy-trivial subgroup; mixed zero value. |
| Definition 4.2 | Verified | All player/strategy source and target maps typed; bijection condition does not impose utilities. |
| Example 4.3 | Verified | Both full payoff tables extracted; the displayed swap/strategy-flip isomorphism checked on all 4 profiles. |
| Example 4.4 | Verified | Displayed composite and inverse checked by component multiplication and on all profiles; relation to3.16 is a strategy relabeling. |
| Definition 4.8 | Verified | Exact utility preservation has correctly typed target index; closure/inversion audited. |
| Definition 4.13 | Verified | Each fixed-player strategy component must be identity; this is stronger than trivial global player kernel. |
| Definition 4.17 | Verified | Coordinate projections of a matching are bijections; equal cardinality follows, including singleton/one-player boundary. |
| Example 4.18 | Verified | Two printed tuples use each of the two actions exactly once in every coordinate; matching maps and diagram agree. |
| Example 4.25 | Verified | The two binary and six ternary listed matchings are exactly all normalized reference-player bijection tuples. |
| Definition 5.4 | Verified | Use actual Aut player image for transitivity/full image; do not replace by abstract isomorphism type. |
| Example 5.5 | Verified | Listed matching-pennies generator produces all 4 exact automorphisms; subgroup/matching checks verify nonstandardness. |
| Definition 5.7 | Verified | Partition of a specified planar shape is data; measurable finite area is an additional requirement for later area comparisons. |
| Definition 5.8 | Verified after correction | Make allowed isometry group and permutation of whole partition pieces explicit; color names need not be pointwise preserved. See ordinal-and-domain-audit.md. |
| Definition 5.9 | Resolved replacement | Phase 3 fixes measurable pieces, finite positive Lebesgue area and whole-piece isometries; transitivity proof and n=1 boundary are explicit. Recommend omitting formal geometry from the central paper; see phase3-specifications.md S3. |
| Definition 5.10 | Verified | Specified actual color action defines transitive/full image; source implication to nontrivial group additionally requires n>=2. |
| Example 5.12 | Verified after correction | General symmetric2x2 family is correct; remove false assertion that every real parameter assignment retains the same full automorphism group. |
| Example 5.13 | Verified after correction | Full exact finite classification: standard and n-transitive always; nonfull iff beta!=gamma. Original one-matching exclusion proof replaced by all matching checks. Pure NE proof covers every real assignment. |
| Example 5.14 | Verified after correction | Both extracted tables have claimed classes for pairwise distinct parameters; special coincidences can enlarge symmetry. Do not state nonstandard/only-transitive uniformly in parameters. |
| Example 5.15 | Verified after correction | Claimed class holds for alpha!=beta; all equal gives a constant fully symmetric game. |
| Example 5.16 | Verified | All 46080 ambient typed bijections checked against64 profiles; exact Aut/image orders 12, kernel1, no transitive matching-lift subgroup. |

## Evidence

Exact source tables, all automorphisms and all matching lifts: [classification-audit.md](classification-audit.md), experiments/classification-results.json. Matching definitions and counts: reviews/R-MATCH-003-A.md, R-MATCH-003-B.md. Typed foundations: reviews/R-FOUND-003-C.md. Displayed isomorphism/composite checks and boundary counterexamples: experiments/test_second_audit.py. Shape and ordinal-domain qualifications: [ordinal-and-domain-audit.md](ordinal-and-domain-audit.md).

Unnumbered definitions of mixed laws, security values, player kernels and parameterized families are treated in corrections.md, action-and-torsor-audit.md and classification-audit.md. A complete philosophical justification of fairness terminology, geometric illustration audit, and original-source history remain separate work; they are not certified by checking the game tables.
