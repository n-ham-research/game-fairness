# Fairness preparation after the structural audit

Historical preparation note. The subsequent systematic work is indexed in
[fairness-programme-handover.md](fairness-programme-handover.md); its utility
normalizations, assignment propositions and annotated sources supersede this
note's suggestions as a description of completed research.

Exploratory notes, 16 October 2026. No new fairness theorem is promoted to the manuscript. The purpose is to specify independently meaningful decision questions before asking whether symmetry characterizes their answers. Calling an automorphism condition “fair” is a definition choice, not a discovery of an equivalence.

## Decision primitives to specify first

An individual must compare **assignment lotteries**, **feasible choices**, **information about opponents**, and **utilities under a stated normalization**. Record whether the individual knows opponents' identities, whether strategies have external meaning, whether opponent behavior can depend on the assignment, and whether the comparison permits a re-encoding of the individual's actions. A symmetry classification alone does not supply these primitives.

Possible operational questions, to formalize and test rather than assume equivalent:

- **Player-label indifference:** before assignment, would a decision maker pay a positive amount to exchange one position for another under a specified belief and decision rule? With risk and strategic uncertainty fixed, this concerns opportunity values; it need not compare whole payoff tables.
- **Ordered opponents:** repeat that exchange comparison while retaining individually identified opponents and their distinct feasible behavior/beliefs. Specify exactly which opponent is displaced by an exchange and which identities/information are held fixed. Do not silently replace this comparison by full permutation equivariance.
- **Unordered opponents:** use information that reveals opponent aggregate choices but not their identities; compare opportunities under that information partition. Structural opponent anonymity is a possible consequence to investigate under sufficiently rich tests, not the definition of indifference itself.
- **Strategy relabeling:** allow choice-preserving correspondences only when physical consequences/feasible decisions justify treating the labels as interchangeable. Require a coherent family if several roles are compared simultaneously. Independently selected pairwise bijections can fail to describe one common experiment.
- **Payoff comparisons:** fix the assignment law, action-profile law and solution/selection rule. Equality under one law, equality for all invariant laws, and equality under every law ask different questions.

## Concrete separations already available

1. Uniform-profile expected equality is too weak to characterize structural opportunity equivalence. On binary actions let `u_1(s)=2s_1+s_2` and `u_2(s)=3-2s_1-s_2`. Each has uniform expected payoff 3/2. There is no player-swapping exact automorphism: changing the focal player's own action changes player 1's utility by absolute amount 2 and player 2's by absolute amount 1, an invariant under local strategy bijections. Exact enumeration independently confirms the actual player image is intransitive. This is an illustrative separation, not a claimed new result.
2. Equal security values do not force structurally identical roles: a one-action player and a two-action player with constant zero payoffs have the same security value, yet no player-swapping typed bijection exists. This remains an example even though equal cardinality is automatically forced by structural symmetry.
3. Total symmetry need not give equal realized payoffs: own-action utilities `u_i(s)=s_i` are a standing example. Conversely identical utility functions depending asymmetrically on the first coordinate need not be symmetric.
4. Equality for every profile distribution is exactly pointwise payoff equality, by applying Dirac distributions and then linearity. That universal test is much stronger than structural role symmetry.
5. Expected numerical comparisons across players are not preserved by independent positive affine rescaling. An operational interpretation must justify common scales or replace numerical equality with a different comparison.

The next fairness investigation should choose one decision primitive and its admissible beliefs/tests, prove the basic consequences from those primitives, and only then compare with the now-audited symmetry hierarchy. Seek minimal counterexamples before trying to prove an equivalence.

## Coalition-value comparison

The inspected third-edition von Neumann–Morgenstern §28.2.2 condition is that v(S) depend only on |S| in their zero-sum characteristic-function framework. It is a structural assertion about coalition opportunities, not a declaration that a selected outcome gives each person the same utility. A general-sum extension must first choose a coalition solution/guarantee, what opponents may coordinate, whether transfers are allowed, and how utilities are aggregated or compared. Those choices need independent justification. One should not call an arbitrary constructed coalition value “their fairness notion” merely because it is invariant under permutations.

The first-edition comparison and full coalition-value construction remain source work. Plan's final published body is also still unavailable; conclusions about it cannot be inferred from the 2017 author draft.
