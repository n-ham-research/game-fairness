# Fairness research notebook

All proposals here are research material. A new name does not make a known equivalence novel.

## Distinct mathematical objects

1. **Label-preserving player symmetry:** H={pi:u_i(s)=u_pi(i)(P_pi s)}. Transitivity is Ham Definition 3.15 and the inspected Plan draft's weak symmetry.
2. **Player transitivity allowing strategy relabeling:** q(Aut(G)) acts transitively on players. This is already Ham Definition 5.4, with attribution there to Stein. It is weaker than requiring a transitive strategy-trivial subgroup.
3. **Opponent anonymity:** for each i, u_i invariant under the full point stabilizer (S_n)_i. With label-preserving transitivity it yields total symmetry (Ham Theorem 3.18); do not market this as a new fairness theorem.
4. **Equal realized payoffs:** u_i(s)=u_j(s). This is distinct from all the above; own-action payoffs provide a counterexample.
5. **Equal security values:** maximin/minimax notions in Ham Definition 3.24; verify independent vs coalition opponent randomization and utility normalization first.

## Ordered and unordered opponents

Specify whose identity/order is retained and which strategy correspondences are admissible. A candidate operational test is to compare the full focal payoff table under allowed position assignments, with fixed strategy identifications; requiring a single coherent family of correspondences is stronger than separately chosen pairwise comparisons. This is not yet a formal fairness definition. Opponent-anonymity itself is well defined, but adding it to transitivity must use the same coordinate convention.

## Expected utilities: the distribution is part of the claim

- Equality for all distributions is equivalent to pointwise equality: take Dirac measures; converse by linearity. No symmetry assumption needed.
- Equality under one uniform profile distribution is only one scalar equality per player; it cannot recover payoff-table structure. Find minimal counterexamples with exact integers.
- A common independent mixed strategy gives a distribution invariant under all coordinate permutations, but role comparisons also require the game's payoff equivariance.
- For an H-invariant correlated distribution, correct H-equivariance suggests equal expectations along player orbits by a change of variables. This elementary candidate observation needs literature/provenance comparison before any claim of novelty.
- A group-average distribution may enforce ex ante equality without each realization giving equality. This is not a claim that a group-average of mixed Nash profiles remains Nash: mixtures need not preserve product independence or Nash best-response conditions.
- Symmetric Nash equilibria and all Nash equilibria are different quantifiers. A symmetric game may have asymmetric equilibria/payoffs.
- Correlated equilibrium sets are convex, making symmetrization structurally different from averaging Nash profiles. Prove incentive preservation before using it.

## Utility comparability

Exact automorphisms preserve numerical utilities; ordinal/cardinal variants may allow transformations. Equal numbers across players are not invariant under independent positive affine utility rescaling. State normalization and interpersonal comparability assumptions before interpreting equality normatively.

## Historical work

The full third-edition scan has now been inspected. §28.2.2 defines fairness as v(S) depending only on |S| in its zero-sum characteristic-function framework. §28.1.4 uses set-transitivity to derive that condition; simple player transitivity is a different group condition. Do not identify this fairness automatically with general normal-form automorphism transitivity or expected-payoff equality. First-edition comparison and the underlying coalition-value construction still need audit.
