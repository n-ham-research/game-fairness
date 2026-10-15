# First investigation: inverse-permutation condition

Date: 16 October 2026. Provenance: established literature; Ham v5 Theorem 3.21, v1 Theorem 3.18; Vester (2012), Appendix B Theorem 32. Not a new theorem. Manuscript includes the established finite-game statement only. Extended formulations below are candidate expository improvements whose novelty has not been checked.

## Exact conventions and claim

Finite player set I={1,...,n}; n>=3. Common nonempty action set A. Let
P_pi(s)_j=s_{pi^{-1}(j)} and compose permutations right to left.

- Correct C: u_i(s)=u_pi(i)(P_pi s) for every i,s,pi.
- Inverse condition D: u_i(s)=u_pi(i)(P_pi^{-1} s) for every i,s,pi.
- E: u_i(s)=u_j(s) for every i,j,s.

Theorem: D iff C and E. With real payoffs and finite A this is Ham's exact equivalence. No finiteness of A is used. This document does not yet certify the typography/conventions of the original 1986 Definition 7: the formula is source-checked against Ham and Vester. An original-author scan is located but its body was not successfully downloaded. The discontinuous-equilibrium theorem consequences remain unverified.

## Extract of Ham v5 original proof

The original statement and proof, source label DMprop, are reproduced below under the author's request. The preceding Lemma 3.20 states: if D holds for pi and tau, then u_i=u_{(tau pi)(i)} composed with (pi tau)^{-1}.

```latex
Suppose Condition (i) holds, then for each $i \in N$ and $\pi \in S_N$,
$u_i = u_{\pi^{-1}(i)} \circ \pi^{-1}
= u_{\pi(i)} \circ \pi^{-1}$.
Conversely suppose Condition (ii) holds, and hence that $\Gamma$ is fully
symmetric. Let $i, j, k \in N$ be distinct. Since
$(ik) \circ (ijk) \circ (jk) = (ijk)$ and
$\bigl((jk) \circ (ijk) \circ (ik)\bigr)^{-1}
= (ik) \circ (ikj) \circ (jk) = e$,
it follows from Lemma 3.20 that $u_i = u_j$.
```

### Line-by-line check

1. Forward direction: C at pi^{-1} followed by E yields D; correct.
2. Reverse: D on transpositions equals C. Closure under composition plus generation by transpositions yields total symmetry; correct implicit use of Theorem 3.18.
3. Both permutation identities are correct under the declared composition convention. Reviewer A explicitly expanded them; the program checks permutation composition for supporting examples.
4. Apply Lemma 3.20 twice, first with alpha=(jk), beta=(ijk), then gamma=(ik). Player product is gamma beta alpha=(ijk); reversed profile product alpha beta gamma=e. The player image of i is j; hence u_i=u_j. The compressed iteration is valid, but should be expanded or replaced for clarity.
5. Distinct third k exists exactly because n>=3.

## Short proof

D agrees with C on every transposition; hence C holds on S_n. Compare D for pi and C for pi^{-1}. They give
u_pi(i)(P_pi^{-1}s)=u_pi^{-1}(i)(P_pi^{-1}s).
Since the profile map is onto, u_pi(i)=u_pi^{-1}(i). For a!=b take a third k and pi=(k a b). This gives u_a=u_b. Conversely C and E imply D immediately by applying C to pi^{-1}.

## Alternative derivation

After establishing C, use C with player pi(i) and profile P_pi^{-1}s to rewrite D as u_i(s)=u_pi²(i)(s). Squares of three-cycles move any chosen player to any other when n>=3. Thus E. This was also the counterexample reviewer's derivation; no claim that it is previously unpublished.

## Vester comparison

Inspected institutional report LSV-12-23: external cover December 2012; inner title page 27 August 2012; Appendix B printed pp.49–50, Definition 31, Theorem 32, Definition 33. Theorem 32 proves D implies E and notes the zero-sum consequence. Vester derives own-payoff invariance under exchanging a focal player's action with an opponent's, then full profile-permutation invariance for each payoff; D then equates players. Ham instead tracks opposite orders of composition. Both arguments establish the same common-payoff consequence. Ham states the full equivalence; D implies C by transpositions, and the converse from C+E completes the comparison. Vester's middle displayed equality in the three-player chain appears unnecessary for that chain, not an invalid inference. No requirement of finite A is used in these algebraic arguments.

Ham explicitly credits Vester with the first publicly released proof, while reporting his own earlier identification in 2011. The report's cover date does not establish its exact first online publication day.

## Boundary cases and counterexamples

- n=2: every pi is self-inverse, so D iff C; u_i(s)=s_i on {0,1}² disproves D=>E.
- n=3: u_i(s)=s_i is C but violates D for pi=(123), i=1, s=(1,0,0).
- Arbitrary finite n>=3: same three-cycle argument fixes all other players.
- Constant across profiles is false: u_i(s)=5+7*1{sum(s)>=2} on {0,1}³ has common payoff 5 at 000 and 12 at 110 and satisfies D.
- E alone is insufficient: u_i(s)=s_1 for every player fails C under swapping 1 and 2.
- Checking D only on a generating set of transpositions gives C, not D on all S_n. D is not itself the correct equivariance condition for a group action.
- Singleton A: C and E already coincide; no separation between two-player conditions is possible there.
- n=1: trivial equality; the theorem concerns n>=3, not an impossibility for n=1.
- Unequal A_i: bare coordinate swaps may be ill-typed. Fixed bijections b_i:A_i->A allow transport to A^n. Pairwise maps must satisfy coherence b_jk o b_ij=b_ik. Equal cardinality alone does not fix the maps.
- Right-action notation is valid if both indices and actions are changed consistently. Merely renaming pi to pi^{-1} throughout cannot repair a mismatched pair.

## Candidate abstract formulation (research only)

For any S_n-set X and common payoff codomain Y, functions u_i:X->Y satisfy the inverse-action condition iff correct equivariance and pointwise player equality, for finite n>=3. The same proof uses only action composition, invertibility and three-cycles. No topology, arithmetic or Cartesian-product structure is needed. Coherent strategy-coordinate changes are a special case. This is not claimed novel and is withheld from manuscript theorem statements pending literature comparison.

## Limits

Three recorded reviews and exact finite constraint partitions support the proof checks; agreement is not the basis of the theorem. The displayed proof is the evidence for generality. No author sign-off, external peer review, final Plan comparison or audit of the 1986 existence arguments has occurred.
