# Exact source classification audit

16 October 2026. Internal audit of previously established Ham v5 examples, unnumbered claims and diagrams. These computations and mathematical explanations are evidence, not external peer review, historical-priority findings or author approval. Candidate corrections below are not claimed novel. The coordinating agent assigned this follow-up to reviewer A after R-MATCH-003-A. No other new review report was consulted. The existing experiments/matching_audit.py API was reused without edits for typed bijections, matchings, subgroup enumeration and equality partitions.

Convention: compose right to left; (P_pi s)_j=s_{pi^{-1}(j)}. An element (p,f) has component f_i from player i's strategies to player p(i)'s strategies; its profile action has t_{p(i)}=f_i(s_i). All original games here are binary, and a coordinate's first displayed strategy is encoded 0, second 1. Tables are read in displayed block order, then row order, then column order. This agrees with lexicographic profile order. Equal strategy labels never identify different player coordinates.

## Artifacts, extraction and exact scope

- experiments/classification_audit.py extracts actual payoff cells from immutable research/inventory.json, preserving integer values and symbolic parameter names. It reads the original source Hasse nodes/edges from pinned research/original-diagrams.json, extracted from the author-owned v5 source. It needs neither a temporary source directory nor network/cache access on a fresh clone.
- experiments/classification-results.json records every extracted table, exact automorphism elements for 5.13–5.16, player images/kernels, and every matching-lift subgroup. For each matching M it checks H_M={pi:M_pi is an exact automorphism}; standard symmetry is precisely transitivity of some H_M, full symmetry H_M=S_N.
- experiments/test_classification_audit.py supplies an independently expressed payoff-preservation predicate, checks it against every ambient bijection for the major examples, checks group closure and fixed source cells, checks generic classifications, parameter boundaries, and exhaustive diagram nodes/edges/generator constraints. Five tests pass with `python3 -m unittest discover -s experiments -p test_classification_audit.py`.

Every binary n-player ambient group consists of all n! 2^n typed bijections. Exact automorphism enumeration tests every element against all payoff cells, using equality only. Hence different symbolic names mean arbitrary pairwise distinct real parameters, not a numerical sample. Numerical ordering of symbols is never used to infer equilibria. Numeric-specialization equilibrium lists in the JSON apply only to the displayed block integer values; equality partitions alone do not exhaust preferences or weak orders.

Examples 4.4 and 5.5 introduce no new payoff table: 4.4 refers to 3.16 with changed coordinate labels; 5.5 lists the automorphism group of 4.1 (Matching Pennies). Examples 4.18 and 4.25 contain matchings, not utility tables. Their absence of payoff data is recorded, not filled with invented utilities. 4.3 contains two separate games, encoded 4.3a/b; 5.14 contains two, encoded 5.14a/b. All other requested source tables were extracted: 2.1, 3.10, 3.12, 3.14, 3.16, 4.1, 5.12–5.16.

## Exact classifications

Here 'generic' means distinct parameter names have distinct values. Numerical source examples have their actual values.

| Source | Aut order | Player image order | Player kernel order | Standard | Fully | n-transitive |
|---|---:|---:|---:|---|---|---|
| 2.1 | 6 | 6 | 1 | yes | yes | yes |
| 3.10 | 1 | 1 | 1 | no | no | no |
| 3.12 | 1 | 1 | 1 | no | no | no |
| 3.14 | 6 | 6 | 1 | yes | yes | yes |
| 3.16 / 4.4 | 3 | 3 | 1 | yes | no | no |
| 4.1 / 5.5 | 4 | 2 | 2 | no | no | yes |
| 4.3a / 4.3b | 1 | 1 | 1 | no | no | no |
| 5.12 | 2 | 2 | 1 | yes | yes | yes |
| 5.13 | 6 | 6 | 1 | yes | no | yes |
| 5.14a | 8 | 4 | 2 | no | no | no |
| 5.14b | 16 | 4 | 4 | no | no | no |
| 5.15 | 48 | 24 | 2 | no | no | yes |
| 5.16 | 12 | 12 | 1 | no | no | no |

The player images in every row marked standard or n-transitive are transitive. The last three examples 5.14a/b and 5.16 also have transitive images, so are only-transitive symmetric rather than asymmetric. 3.10/3.12/4.3 have intransitive images.

These computations confirm the major examples' intended generic classifications. They repair the incomplete inference in 5.13's original proof: failure of transposition lifts for ONE matching is insufficient by itself to rule out full symmetry under ANOTHER matching. Here all four binary three-player matchings are tested. Their H_M orders are 3,1,1,1; none is S_3. For 5.14a all eight H_M are trivial. For 5.14b all eight have order 2 and are intransitive. For 5.15 all eight have order 3 and are intransitive. For 5.16 eight of its 32 H_M have order 3 and the other 24 are trivial; all are intransitive. Thus no omitted matching can alter the generic verdicts.

5.16's full Aut group, not just its proposed generated subgroup, has order 12 and player kernel 1. Its image has order 12 on six players, transitive but proper in S_6. This independently verifies the stated split player-image example and its non-standardness for the actual numerical table.

## Parameter coincidences and corrected quantifiers

The claim following 5.12 that different parameter choices always have the same automorphism group is **false**. Generic 5.12 has Aut order 2; setting alpha=beta=gamma=delta yields a common constant payoff table and the full ambient group of order 8. Likewise 5.13 changes from order 6 to 48 when all parameters coincide; 5.14a/b and 5.15 become fully symmetric with ambient order 384. Strictly, Gamma(G) imposes a subgroup of automorphisms for every assignment, not a fixed entire automorphism group.

A precise replacement: let H=<G> act on payoff cells N x A by (i,s)->(g(i),g(s)). Give each H-orbit an independent real parameter. The entire automorphism group at an injective parameter assignment is the subgroup of ambient bijections preserving EACH H-orbit setwise. This can strictly contain H. An arbitrary assignment may merge those orbit colors, so can only enlarge that generic automorphism group. Even injective assignments do not by themselves justify equality Aut=H; that requires checking orbit preservation. This distinguishes the subgroup closure from its orbit closure.

All equality partitions of the four parameters were exhaustively checked for 5.12, 5.13 and 5.14b (15 patterns each); both patterns for 5.15. This is a complete automorphism analysis of their real parameter assignments because the exact automorphism equations depend only on equality. The initial reviewer pass checked eight-parameter5.14a only at generic and all-equal values. The coordinator follow-up below now exhausts all 4140 equality patterns with an independent constraint verifier.

For 5.13 the exact boundary is particularly simple: **fully symmetric iff beta=gamma**; it remains n-transitively standard symmetric for every assignment. If beta!=gamma its Aut order is 6 and it is non-fully symmetric, even when alpha or delta coincides with another parameter. If beta=gamma, Aut order is 12 except that all four equal gives 48. Thus merely 'at least two payoff parameters distinct' does not suffice for its advertised non-full classification. This equality characterization follows from exhaustive checking of all 15 equality partitions and is recorded case by case in the JSON.

For 5.15 alpha!=beta gives the advertised n-transitively non-standard class; alpha=beta gives a fully symmetric constant game. For 5.14b the full/n-transitive degeneracy occurs precisely when alpha=beta AND gamma=delta (including all equal). Other coincidences can enlarge Aut without making it n-transitive or standard; e.g. alpha=delta, beta=gamma, alpha!=beta gives Aut order 32 and player image order 8. The JSON preserves all cases. Pairwise distinct parameters are sufficient for both 5.14 tables' advertised classifications, and all-equal values refute any parameter-uniform assertion of non-standardness or only-transitivity.

The original payoff-vector exclusion arguments are valid only when the proposed excluded tuple truly does not occur. Distinct parameters ensure this for the given examples. Without parameter restrictions, absence cannot be assumed.

## Pure equilibria in 5.13

The claim that every parameter choice in 5.13 has a pure equilibrium is **verified by direct inequalities**, independently of the automorphism computation. At 000 and 111 each player gets alpha and obtains delta upon unilateral deviation, so both are equilibria iff alpha>=delta. At each of the other six profiles exactly one player changes payoff from delta to alpha by deviating, while the other two retain their own beta/gamma payoff. Hence each such profile is an equilibrium iff delta>=alpha. At least one of those inequalities holds; if alpha=delta all eight profiles are equilibria. No assumption on beta or gamma is needed.

This resolves the example-specific unnumbered assertion, not the stated broader open question about all n-transitively standard symmetric binary games. The generic numerical 3.16 table has no pure equilibrium, as the source notes; Matching Pennies has none. Symbolic equality representatives in the JSON are not a substitute for the inequality proof above.

## Euler diagram

The implication edges are mathematical, not empirical: fully symmetric implies standard symmetric and n-transitively symmetric by 5.1–5.2; standard symmetry gives a transitive automorphism subgroup; n-transitivity gives transitivity. Thus both imply symmetric. Full symmetry is a proper subclass of the intersection: generic 5.13 lies in standard AND n-transitive, outside fully. Other intended regions are witnessed exactly by 3.16 (standard outside n-transitive), 4.1/5.5 (n-transitive outside standard), 5.14a/b (symmetric outside both), 2.1 (fully), and 3.10 (outside symmetric). Therefore the source Euler inclusion/separation diagram is verified when player and strategy counts may vary as in the source's examples. It does not assert that every region is populated for each fixed n,m; for n=2 standard and fully coincide, for example.

## Two- and three-player binary Hasse diagrams

A precise finite interpretation makes both displayed graphs **verified**. A parameter family is the equality subspace imposed by a subgroup H of the binary game-bijection group; its coordinates are the H-orbits on N x A. Families are considered modulo a single player/strategy relabelling and permutation of independent parameter names. Order is reverse inclusion of represented concrete-game isomorphism classes: F<=F' when every game in F' is isomorphic to some specialization of F.

Method: enumerate ALL subgroups of the full ambient group (10 subgroups for n=2, 98 for n=3), retain those whose actual player action is transitive, form orbit equality partitions, and quotient these partitions under all ambient cell permutations. This produces exactly 4 and 7 families respectively. Every source node is one of these and each appears once. The source displayed generators give exactly their displayed table partitions; the three asserted pairwise unions defining three-player G32 were all checked as equality partitions. All displayed cover edges match the computed transitive reduction, with no missing or extra edge. Full class partitions, source-node correspondence and cover lists are in the JSON.

Why equality refinement proves the required quantified order: if after one relabelling all F-equalities follow from F'-equalities, every F' assignment specializes F. Conversely choose an F' assignment with distinct values on every block. If that game belongs up to some relabelling to F, the F-equalities must follow from the F' partition after that relabelling. Thus a generic distinct-block witness detects inclusion failure exactly, despite the original order allowing a relabelling that depends on the assignment. No finite sampling of real payoffs is used.

Completeness here is restricted to Gamma(G) families generated by player-transitive subgroups for fixed binary n=2 or 3. It does not classify all strategic/ordinal equivalence classes or verify the cited 144 count. Every symmetric concrete game belongs to at least one of these families (take H=Aut(game)), but a family includes specializations of several automorphism types and cannot be identified with a single type.

The statement that this relation is a partial order on unspecified parameterized presentations needs qualification: it is a **preorder on presentations**, since redundant generators and renamed parameters give distinct presentations with mutual inclusion. On mutual-inclusion equivalence classes it is a poset. For finite equality families the equivalence is exactly conjugacy of equality partitions: mutual inclusion forces equal block counts and then a refinement with equal block counts must be equality. This is the quotient implemented above. The source's admitted lack of a precise parameterized-isomorphism definition is therefore a real definitional gap, although its two finite graphs survive a natural precise repair.

The 'only parameterised n-transitively non-fully standard symmetric 3-player 2-strategy game' claim following 5.13 is verified **for generic Gamma(G) orbit-equality families modulo the equivalence just defined**: among the seven exhaustive family classes, exactly one generic class has these three properties, the 5.13 class. It is not literally one concrete game up to exact isomorphism: varying distinct real payoff values yields many nonisomorphic games. Nor does the entire family retain non-full classification at every specialization (beta=gamma is fully symmetric). Those quantifiers must be stated.

## Actual action versus abstract group type

The prose assertion that Aut(Gamma)/Gamma_N being abstractly isomorphic to SOME transitive subgroup of S_N characterizes symmetry is **false**. Let n=4, all A_i singleton, and the sole profile have payoff vector (0,0,1,1). The exact automorphisms may permute equal-payoff players, so their actual player image is <(12),(34)> = S_2 x S_2, intransitive with two orbits. The player kernel is trivial. Abstractly this group is V_4, which also admits the transitive degree-four representation {e,(12)(34),(13)(24),(14)(23)}. An abstract isomorphism does not preserve the specific action. Correct symmetry criterion: the actual image rho(Aut(Gamma)) must be transitive on its given N. An action-preserving isomorphism would also suffice.

The adjacent assertion with quotient abstractly isomorphic to S_N DOES imply the actual image is S_N in finite degree n: 4.12 identifies it with a subgroup of S_N, and equal order n! forces equality. The flaw does not apply to that stronger criterion.

Related structural cautions remain those in R-MATCH-003-A: nonempty cross-game isomorphism hom-sets are bitorsors, not groups under internal composition; a matching groupoid needs player-indexed objects/arrows when strategy labels coincide. The usual product-action convention for the full equal-cardinality bijection group is S_m wr S_n = S_m^n semidirect S_n; the source's S_N wr S_M order needs an explicit alternative convention or correction. None of these presentation issues changes the exact finite classifications above.

## Limits and dependencies

All equality-only finite results here are exhaustive over their stated ambient groups or equality partitions, not general theorems inferred from samples. The source generator and diagram interpretation have been made explicit; no external historical assertions or source code provenance are validated. The coordinator follow-up below closes the eight-parameter coincidence coverage; broad equilibrium conjectures remain outside this report. The scripts use exact integers/symbol names, no floating-point tolerance.

Logical dependencies: typed bijection group and exact automorphism composition (4.7/4.9); player-image kernel theorem (4.11/4.12); matching homomorphism and characterization (4.20/4.23, 5.1/5.2) justify matching-lift classification; fixed matching profiles (4.22,5.3) justify the source equal-payoff necessary condition. The incorrect original 4.24 is not used. Original inventory statements and shared audit tables were not edited.

## Coordinator follow-up: all 4140 eight-parameter patterns

The second pass additionally enumerated every equality partition of the eight
real parameter names in 5.14a. Restricted-growth strings enumerate each partition
exactly once; distinct blocks may be assigned arbitrary distinct real values
without changing any exact automorphism equation. Tracked reproduction:
`python3 experiments/parameter_audit.py`; complete results:
`experiments/parameter-results.json`. `--verify` independently compiles every
ambient bijection's payoff equations to equalities on the 8 parameter names
and checks every case, including all matching-lift classifications. This
provides a second formulation of the entire finite check, not real-value sampling.

Among4140 equality patterns,4099 have Aut/image orders 8/4;11 have16/4;24
have16/8;2 have32/8;1 has64/8;2 have48/24;and 1 has384/24. The all-equal
pattern is the only standard or fully symmetric case. Two nonconstant
patterns become n-transitively non-standard: gamma=rho distinct from the
other six equal parameters; or delta=omega distinct from the other six
equal parameters. Thus even “only-transitive” needs parameter restrictions.
All other patterns remain only-transitive non-standard. This is a complete
fixed-family classification, not a theorem about arbitrary parameterized games.

The printed generators for5.13, both 5.14 tables,5.15 and 5.16 were also
transcribed with explicit local strategy flips and checked on the source payoff
tables. Their generated orders are6,8,16,48,12 respectively, and in each
generic/numerical case the generated group equals the independently enumerated
full Aut. These checks are recorded separately as source_generator_checks in
classification-results.json and tested in the regression suite.
