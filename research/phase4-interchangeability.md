# Individual, coherent and matching-based interchangeability

16 October 2026. Foundational reformulation of audited Ham results, with
candidate consequences labeled. No fairness interpretation or novelty claim
is built into the terminology. All sets are finite. Typed maps compose right
to left; `(P_p s)_j=s_{p^{-1}(j)}`.

For X in {exact,card,ord}, let A_X be its utility automorphism group and
q_X:A_X→S_n the actual player map. Define:

- I_X: q_X is onto (individual realizability of every player permutation).
- C_X: there is a homomorphism s:S_n→A_X with q_X s=id (coherent realization).
- M_X: there is such a section whose component on A_i is identity whenever
  its player permutation fixes i (matching-based realization).

Then M_X⇒C_X⇒I_X. These are immediate from the definitions. More contentfully,
M_X is exactly full symmetry after a matching in the exact game, or in the
cardinal min-max / ordinal rank representative. This follows from audited
Ham 4.23/5.2 and the actual subgroup normalization identities, not merely an
abstract isomorphism of groups. C_X implies X-standardness: lift an n-cycle
through the section. Its cyclic subgroup has order n and a regular player
action, so no nonidentity element fixes any player; it is strategy trivial.
This is the argument already present in Ham 5.6. Conversely standardness plus
I_X need not imply C_X: P3-S1b is a counterexample for all three X.

The implications are strict. Non-full Example 5.13 has C but not M. P3-S1b
has I plus standardness but not C. The ternary orientation example has C but
not M with a different, nontrivial player kernel C3; it is neither the
binary signed representation nor the nonsplit C2 extension. These distinctions
concern the specified projection and stabilizer actions. Calling them all
abstractly “symmetric” loses the data needed to distinguish them.

For any fixed game, group inclusions imply I_exact⇒I_card⇒I_ord and likewise
for C and M: the same typed maps/section continue to work in the larger group.
The utility-invariance.md examples `u_i=(i+1)k²` and `u=(k,k²,k)` show strictness
even for M across utility notions: their normalized common-payoff games admit
bare full matching actions, whereas the previous utility group's player image
is intransitive. These examples are representation comparisons, not welfare
claims.

## Transitive exact symmetry collapses all three groups

**Direct consequence of the finite range-signature lemma, novelty not claimed.**
If A_exact is player transitive, every player's sorted numerical utility range
is identical: an exact automorphism between two roles bijects all profiles
and preserves every payoff level. For any ordinal automorphism its increasing
bijection between those identical finite ranges must be the identity. Hence

`A_exact=A_card=A_ord`.

Thus every game in the user's original exactly standard/full-image/nonfull
region already has the same obstruction at all three utility levels. The
binary signed, ternary orientation and four-action nonsplit witnesses are
not artifacts of choosing exact instead of preference-preserving maps.
One should not repeatedly recount them as three independent counterexamples.

Similarly, cardinal player transitivity makes all sorted normalized ranges
identical. The range-signature criterion gives `A_card=A_ord`. Exact symmetry
can still differ because original utility units or offsets differ. These
statements require preservation of the complete pure-outcome preorder; they
need not hold for maps preserving only best responses.

For games standard only at the cardinal or ordinal level, P4-T1/T2 transfer
by their respective normalization: for three players and three strategies,
I_X plus X-standardness forces C_X, and a nonmatching full group has order
six or eighteen in the normalized labels. Four strategies are necessary for
a three-player counterexample to C_X under those hypotheses. This does not
prove a three-strategy theorem for arbitrary numbers of players.

## Why the hierarchy is not automatically a hierarchy of assignment welfare

The calibrated model in phase4-assignment-model.md proves I (indeed player
transitivity) sufficient for equal one-shot conditional opportunities under
transported behavior. A section adds no stronger equality there. If the
institution additionally requires typed path independence of successive
requests, C becomes necessary and sufficient. M additionally preserves
strategic encodings of fixed participants. These are distinct physical
requirements. Kernel discrepancies remain payoff-invisible in the base exact
game, so an economic or ethical cost cannot be inferred from them alone.
