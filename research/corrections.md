# Correction ledger — second mathematical audit

16 October 2026. These are **corrections to, or clarified formulations of, Ham v5**, not claims of newly discovered theorems. The original statements remain unchanged in the inventory pinned by `original-record.json`. Source truth, validity of a proof, and status of the corrected result are separate fields in `audit.json`. The main manuscript has not been expanded.

## C4.24 — repaired anonymity characterization

**Original defect.** “Subgroup of Gamma” explicitly means subgroup of `Aut(Gamma)`. In the printed clause (ii), full player image and strategy triviality already characterize full symmetry up to relabeling (Corollary 5.2); the stabilizer-payoff condition is automatic. They do not characterize weak anonymity. Two players with one strategy each and payoffs `(0,1)` satisfy (i) and (iii) and refute (ii). The original binary-action counterexample remains valid as well.

**Corrected theorem.** Let `N={1,...,n}`, `n>=1`, and let every `A_i` be finite and nonempty. Write `B(Gamma)` for the full group of typed game bijections, independently of utilities, and `q` for its player projection. The following are equivalent:

1. Gamma is exactly isomorphic to a game with a common action set which is weakly anonymous: for each focal player i, all coordinate permutations fixing i preserve that player's payoff.
2. There is a strategy-trivial subgroup `G <= B(Gamma)` with `q(G)=S_N` such that `u_i(g s)=u_i(s)` for every player i and every `g in G_i`.
3. There is a matching M such that `u_i(M_pi s)=u_i(s)` for every i, every permutation pi fixing i, and every profile s.
4. There is a matching M with the same invariance only for opponent transpositions `(j k)` with i,j,k distinct.

No equal-cardinality premise need be added: each clause implies it. If cardinalities differ, all clauses are false. For n=1 or n=2 the opponent-transposition list is empty; for n=2 the theorem reduces to equality of strategy cardinalities. Finite real utilities are the original scope; the proof only uses equality of payoff values and bijections and therefore does not need finiteness of the action sets when the required matching/bijections exist. No stronger regularity or automorphism hypothesis is imposed.

Here a matching is a subset M of the profile product whose coordinate projections `p_i:M->A_i` are bijective. Set `c_ij=p_j p_i^{-1}` and `(M_pi s)_{pi(i)}=c_{i,pi(i)}(s_i)`. Then `c_jk c_ij=c_ik`, `c_ii=id`, and `M_tau M_pi=M_{tau pi}`. These are typed identities; strategy labels may overlap without identifying the player objects.

**Proof.** For (2)->(3), strategy triviality and transitivity imply Theorem 4.23's matching construction (proved independently below), giving `G=M_{S_N}`. Its stabilizer at i consists precisely of lifts of permutations fixing i, so the stated invariances coincide. For (3)->(2), take `G=M_{S_N}`. The displayed composition identity makes this a subgroup; its player projection is the identity on `S_N`; and any lift fixing i has component `c_ii=id`, so it is strategy trivial.

For (3)->(1), fix r, use the common label set `B=A_r`, and let `b_i=c_ir:A_i->B`. Relabel strategies by the exact game isomorphism F with identity player map and component b_i, transporting utilities by `v_i(t)=u_i(F^{-1}t)`. The identity `b_{pi(i)} c_{i,pi(i)}=b_i` gives `F M_pi F^{-1}=P_pi`. Therefore the focal invariances in (3) become weak anonymity of v.

Conversely let F be any exact isomorphism to a weakly anonymous common-action game, allowing player permutation sigma and strategy components `b_i:A_i->B`. Pull back the common-label diagonal:

`M={s: b_i(s_i)=b_j(s_j) for every i,j}`.

Every coordinate projection is bijective and `c_ij=b_j^{-1}b_i`. Direct component calculation gives `F M_pi F^{-1}=P_{sigma pi sigma^{-1}}`. If pi fixes i, its conjugate fixes sigma(i); weak anonymity and exact payoff preservation imply `u_i(M_pi s)=u_i(s)`. This proves (1)->(3). Finally opponent transpositions generate each point stabilizer; payoff-preserving profile bijections for a fixed focal utility are closed under composition and inversion, proving (3)<->(4). This is a complete proof, independent of the printed Corollary 4.24.

**Weakness/sharpness.** The direct matching/transposition clause removes an unnecessary existential group from the statement. Merely changing full player image to transitivity in clause (2) is false: on three binary-action players take the strategy-trivial cyclic rotation group (trivial player stabilizers), and `u_1(s)=s_2`. Stabilizer invariance is vacuous, but weak anonymity cannot be obtained by coordinate relabeling: exactly one of player 1's two opponents can affect its utility, a distinction preserved under such relabeling. Arbitrary unrelated pairwise strategy bijections also do not replace a matching; their coherence is necessary.

**Independent reviews and finite challenge.** `reviews/R-MATCH-003-A.md`, `R-MATCH-003-B.md`, and `R-FOUND-003-C.md` independently reconstruct the repair; shared model limitations are recorded. The complete equality-partition/subgroup checks in `experiments/matching-results.json` cover every real payoff assignment on seven explicitly specified finite domains. They corroborate, rather than replace, the general proof.

## M4.23 — coherent matching reconstruction and downstream results

For `G <= B(Gamma)` player transitive and strategy trivial, choose a group element taking i to j and define `c_ij` as its i-component. If g,h have the same target at i, `h^{-1}g` fixes i, hence its i-component is identity, so their components agree. Composition gives `c_jk c_ij=c_ik`. Fix r and set `M={(c_ri(a))_i:a in A_r}`. Every projection is bijective; its induced maps are exactly c_ij; hence `G=M_{q(G)}`. Conversely a lift through any matching has identity strategy component at every fixed player. This proves the original Theorem 4.23 under its stated assumptions.

If transitivity is removed, the precise replacement in the finite scope is strategy triviality **and equal cardinality of all strategy sets**. Each player orbit has coherent maps as above. Pick a common reference set B, an orbit representative r_O and a bijection `d_O:B->A_{r_O}`; then `b -> (c_{r_O,i} d_O(b))_i` gives a global matching. Unequal sizes obstruct any global matching, even for the trivial group. This scoped strengthening is kept in the notes; novelty has not been investigated.

Corollaries **5.1 and 5.2 survive**. Their subgroup ambient group genuinely is Aut(Gamma): exact conjugation through a matching changes transitive/full matching-lift automorphism subgroups into label-preserving transitive/full symmetry groups. The reverse conjugation preserves strategy triviality because a fixed-player component conjugates an identity to an identity. Neither proof needs Corollary 4.24. For **5.3**, choose M and a transitive lift subgroup from 5.1. Every s in M is fixed by every lift. Choosing a lift taking i to j yields `u_i(s)=u_j(s)`. Arbitrary transitive automorphisms without strategy triviality do not suffice (matching pennies).

## C2.2 — product distributions, exact boundary

For any finite nonempty player set N (including one player) and finite nonempty A_i, define

`f((x_i)_i)(s)=product_i x_i(s_i)`.

Then f is well-defined and injective. It is surjective **if and only if at most one A_i has more than one element**.

**Proof.** Products are nonnegative and summing over all coordinates gives `sum_s product_i x_i(s_i)=product_i sum_{a_i}x_i(a_i)=1`. The i-marginal of f(x) is x_i, proving injectivity without any division. If all but at most one coordinate are fixed, a joint distribution is determined by the sole variable marginal (or is the unique point mass if none varies), so it is product. Otherwise choose two players with distinct pairs of actions. Fix every other coordinate, and assign probability 1/2 to the profiles choosing the first pair together and the second pair together. The two varying marginals each have weights `(1/2,1/2)`; their product gives weight 1/4 to each crossed profile, whereas the joint assigns zero there. Thus it is not product.

The original statement omitted the nondegeneracy condition. Its non-surjectivity proof also selects a second action in every strategy set and divides by unguaranteed positive probabilities; neither step is justified on the stated domain. The source's injectivity elimination is separate and does not use those divisions.

No downstream formal result uses strict non-surjectivity. The mixed-profile notation and payoff expectation results require only well-definedness and injectivity; subsequent minimax proofs are directly checked on the product domains. Dependency flags distinguish these components.

## C5.11 — zero-sum fairness with strategy bijections

**Corrected proof of the unchanged finite-game statement.** Let a finite two-player zero-sum game have an exact automorphism g swapping the players, with arbitrary strategy components `a:A_1->A_2` and `b:A_2->A_1`. Push a mixed pair `(x,y)` forward to `(b_*y,a_*x)`. This is a bijection of the two independent mixed strategy spaces, interchanging their roles, and payoff preservation extends to expectations by finite summation:

`U_1(x,y)=U_2(b_*y,a_*x)`.

Consequently the players' lower security values coincide:

`max_x min_y U_1(x,y) = max_x min_y U_2(b_*y,a_*x)
 = max_{z in Delta(A_2)} min_{w in Delta(A_1)} U_2(w,z)`.

Both sides are genuine mixed-strategy maximin quantities. Finite two-player zero-sum minimax identifies the lower and upper values, and zero-sumness makes the players' values opposite. Equal and opposite values must both be zero. Thus the game is fair in the zero-value sense. The source proof incorrectly assumes the bare player swap is an automorphism and uses pure extrema. No such restriction is needed in this replacement.

## C2.4, C3.6 and C3.25 — valid statements, faulty proof lines

- **2.4:** the correct equality is `max_x min_y U_1 = -min_y max_x U_2` and `min_y max_x U_1 = -max_x min_y U_2`, with each variable retaining its own player's domain. Source proof (ii) reverses the optimization-variable order. With `U_1=[[0,1],[2,3]]`, true upper value for player 1 is 2, while the printed `min_row max_col` equals 1. The statement remains true by negation and exchanging min/max.
- **3.6:** regard opponents' profiles as functions on `N\{i}`. For `T_pi^i`, set `(T_pi^i x)_j=x_{pi^{-1}(j)}` for `j!=pi(i)`. Its inverse has `(T_{pi^{-1}}^{pi(i)}y)_k=y_{pi(k)}`, `k!=i`. These formulas prove correct domains, inversion and `T_tau^{pi(i)} T_pi^i=T_{tau pi}^i`. They replace the malformed tuple indices in the printed surjectivity calculation; the groupoid statement is valid with player-typed objects.
- **3.25:** the source first says `u_i=u_i composed pi`, which is not implied by symmetry. The correct premise is `u_i=u_pi(i) composed P_pi`. It extends to independent mixed strategies and gives equality of lower and upper security values along every player orbit by separate bijective changes of focal and opponent variables. Transitivity equates all players' values. Zero-sumness is unnecessary. The own-action game `u_i(s)=s_i` refutes the erroneous same-i identity for a player-moving permutation while satisfying the theorem's symmetry premise.

## C4.19 — inferred groupoid objects must be explicit

Use objects `(i,A_i)` and arrows `(i,j,c_ij)`, not just an untagged set of functions. Then `c_jk c_ij=c_ik`, `c_ii=id`, `c_ij^{-1}=c_ji` prove a groupoid. If A_1=A_2 is a four-element set and `c_12` is a four-cycle p, the literal untagged set `{id,p,p^{-1}}` is not closed under ordinary composition (p² is missing). The source permits inferred groupoid objects, so its intended indexed reading is valid; the ambiguity needs clarification rather than an assertion that the typed construction is false. Downstream matching-lift results have direct typed proofs and survive.

## C4.10 — hom-sets are not naturally groups

Original `Iso(X,Y) congruent Iso(Y,Z)` does not specify a structure on these hom-sets. The unambiguous replacement is a **bijection of sets**, not a natural group isomorphism. Choose `a:X->Y`, `b:Y->Z`; then `h -> b h a^{-1}` is a bijection from Iso(X,Y) to Iso(Y,Z), inverse `k -> b^{-1} k a`. Each nonempty hom-set is a bitorsor under automorphism groups. A group operation can be transported after a choice of base arrow, but is not part of the original data. The original is classified Unresolved as written, with this safe correction fully proved; no downstream proof requires treating a hom-set as a group.

## CU2-M — order-preserving maps

Strictly increasing functions R->R form a composition monoid, not a subgroup of all bijections: `exp` is increasing but not onto. The strictly increasing **bijections** form a group: identity and composition are increasing bijections, and their inverses are increasing because if y<z and inverse(y)>=inverse(z), applying the increasing map is a contradiction. Positive affine maps `x->a x+b`, a>0, form a subgroup, with inverse `(x-b)/a`. The source's “positive linear” terminology should be replaced by “positive affine” when an additive constant is permitted.

No exact-isomorphism or matching proof depends on the false assertion. Preference-based generalizations require only order-isomorphisms of the finite realized payoff sets; these can be extended to increasing bijections of R by positive-slope piecewise-linear interpolation and linear tails. This finite repair does not justify arbitrary infinite-domain preference claims.

## C4.24-A / C4.24-FA — explicit anonymity analogues

The original prose after4.24 says “similarly for anonymous and fully anonymous games” without stating the quantifiers. The following explicit formulations remove that ambiguity; they are corrections/clarifications of the intended classification, not new fairness definitions.

**Anonymity up to exact isomorphism** is equivalent to the existence of a matching M with `u_i(M_pi s)=u_i(s)` for every i,pi,s. Equivalently there is a full-player-image strategy-trivial subgroup of the **full typed bijection group** under which each fixed utility function is invariant under every element, not only focal stabilizers.

**Full anonymity up to exact isomorphism** is equivalent to identical player payoff functions E together with that matching-anonymity condition. It is also equivalent to E together with full symmetry up to exact isomorphism (Corollary 5.2).

**Proof.** For any isomorphism F with player map sigma and strategy components b_i to a common action set, pull back the diagonal matching, giving `F M_pi F^{-1}=P_{sigma pi sigma^{-1}}` and `u_i=v_{sigma(i)} composed F`. Conjugation carries all S_N onto S_N, so invariance of each v_i under all pure permutations is exactly invariance of each u_i under all matching lifts. The matching/full-image strategy-trivial subgroup equivalence is Theorem 4.23 and the matching homomorphism. Identity permutation in full anonymity gives E; under E the remaining cross-player invariances reduce to anonymity. Exact isomorphisms preserve and reflect E because all utility components are transported through the same surjective profile bijection, even when players are permuted. Finally under E the matching invariance equations are exactly the automorphism equations for M_SN, yielding Corollary 5.2. This proves both directions of every stated equivalence.

For singleton strategy sets anonymity holds regardless of the players' distinct constants, while full anonymity holds precisely when those constants coincide. Unequal cardinalities make the common-label/matching/full-image conditions false; no extra equal-cardinality assumption is needed. The full typed group must not be replaced by Aut in the anonymity formulation. These statements and boundaries were separately checked by A, B and C in a final targeted follow-up; the coordinator retained these explicit proofs rather than relying on agreement.
