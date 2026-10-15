# Fairness literature: VNM, strategic values, and blend-in fairness

16 October 2026. **Primary-source reconstruction and comparisons; no novelty
claim.** This supplements the broader literature review. It distinguishes
properties of games, cooperative characteristic functions, and allocation
rules. No third-party PDF is tracked or redistributed.

## Sources and inspection scope

- **VNM53:** John von Neumann and Oskar Morgenstern, *Theory of Games and
  Economic Behavior*, third edition, Princeton University Press, 1953. The
  inspected scan's printing page also lists sixth printing, 1955. [Library
  scan](https://archive.org/details/in.ernet.dli.2015.215284). Read the whole
  Section 28, printed pp. 255–260, in OCR and visually inspected its six scanned
  pages (one-based PDF pp. 279–284). Also read the defining coalition construction
  in §25.1, printed pp. 238–240, and the fixed-payment discussion §27.1,
  pp. 245–247, in OCR. This is **not a newly inspected 1944 first edition**.
  Archive metadata's 1944 date cannot change the scanned edition.
- **KN21:** Elon Kohlberg and Abraham Neyman, “Cooperative strategic games,”
  *Theoretical Economics* **16** (2021), 825–851,
  [published PDF](https://onlinelibrary.wiley.com/doi/pdf/10.3982/TE3648),
  [published HTML](https://onlinelibrary.wiley.com/doi/full/10.3982/TE3648).
  Read the published bodies of §§1–4, especially §3, pp. 832–834, and Theorem 1,
  p. 834; checked the proof conclusion §7.4, pp. 847–848. This is not the 2017
  working paper or 2019 expanded draft. Publisher PDF text was readable via
  web extraction; screenshot retrieval failed, so no visual-PDF check claimed.
- **DS25:** Dinko Dimitrov and Ching-jen Sun, “Blend-in fairness and equal
  split,” *International Journal of Game Theory* **54**, article 27 (2025),
  version of record 26 June 2025,
  [published article](https://link.springer.com/article/10.1007/s00182-025-00949-z),
  [published PDF](https://link.springer.com/content/pdf/10.1007/s00182-025-00949-z.pdf).
  Read §§2–4, article pp. 3–7, including the exact cooperation-equivalence
  quantifiers and both main theorem statements. The full HTML/PDF extraction
  was readable; PDF screenshot retrieval failed. The appendix characterization
  proof has not received a line-by-line independent verification here.

## VNM Section 28 reconstructed

### Objects and action, §§28.1.1–28.1.3, pp. 255–257

The setting is the zero-sum n-person theory developed in the surrounding
chapter. Players select pure strategies in normalized form; coalition members
may coordinate all their actions. For coalition S, §25.1 defines v(S) as the
value of the two-person zero-sum game between S and its complement. Each side
may randomize jointly within its own coalition; this is not the restriction
to independent individual mixed strategies. The coalition payoff is the sum
of its members' numerical payoffs.

Section 28 first defines permutations, their multiplication and induced
relabeling of both strategic choice variables and payoff recipients. The
book's right-action notation composes P before Q in the product PQ. To avoid
mixing conventions, the following reconstruction uses this project's left
action `(P_p s)_j=s_{p^{-1}(j)}` throughout.

Relabeling a game Γ by p gives a game Γ^p whose characteristic function obeys

`v_{Γ^p}(pS)=v_Γ(S)`.

This is equation (28:4). It follows because the same physical coalition has
merely received new names. Their invariance group consists of permutations
leaving the numerical normalized game unchanged. In the project's convention
its preservation identity is

`u_{p(i)}(P_p s)=u_i(s)`.

Consequently every invariant permutation satisfies `v(pS)=v(S)`, and v is
constant on the invariance group's actual coalition orbits, equations
(28:6)–(28:7). This is a statement about relabeling positions and recipients,
not the false same-direction convention identified in the Ham audit.

### The sufficient group property, §28.1.4–§28.2.1, pp. 257–258

The operative hypothesis (28:8) is **set-transitivity**: every pair S,T of
coalitions with equal cardinality lies in one group orbit. It is not merely
transitivity on individual players. Combining it with (28:7) yields

`v(S)=v_|S|`.

Full S_n suffices. Their p. 258 footnote also recognizes A_n as a proper
sufficient subgroup for n≥3. An elementary verification is to take a
permutation mapping S to T and, if it is odd, change its parity by a
transposition within T or its complement; at least one has two elements.
Thus full player-permutation image is a sufficient condition, not their
weakest stated one. Historical assertions in that footnote about then-open
group classifications are not being reported as current results.

They retain the characteristic-function restrictions in size coordinates:

`v_0=0`, `v_{n-p}=-v_p`,

`v_{p+q}>=v_p+v_q` whenever `p+q<=n`.

On p. 259 they use complementation to express the last inequality as
`v_p+v_q+v_r<=0` when `p+q+r=n`. By symmetry of the three indices and the
trivial p=0 case, it suffices to impose the original inequality for
`1<=p<=q` and `p+2q<=n`, equation (28:12). This reconstructs the calculation,
not only the section heading.

### Their definition and limitation, §28.2.2, p. 259

They **define** a game to be fair when its characteristic function is
coalition-size dependent. For n=2, complementation gives
`v({1})=-v({2})`; equal-size equality therefore means the zero-sum value is
zero. Their n-person definition extends that two-person criterion.

They explicitly caution that neither this fairness nor total symmetry
ensures equal individual fates in a particular play for n≥3. The definition
is neither equality of expected utilities under a selected normal-form
strategy law nor a claim of equal realized allocations. No Nash-equilibrium
selection rule or ex ante assignment model is specified in Section 28.

### Fixed payments and reduced form, §28.2.3, pp. 259–260

The preceding §27.1 permits fixed player payments a_i with `sum_i a_i=0`,
which change the characteristic function by

`v'(S)=v(S)+sum_{i in S}a_i`.

Such payments do not alter strategic choices. Section 28.2.3 observes that
a reduced three-person characteristic function is fair, whereas for n≥4
fixed payments need not remove the remaining asymmetries. This is a statement
within their characteristic-function reduction, not a theorem that every
three-player normal-form game becomes exactly automorphism-transitive after
adding constants.

## KN21 annotation (published version)

The domain is finite strategic games with transferable numerical utility.
Section 3, pp. 832–834, calls i,j interchangeable when `A_i=A_j`, `g_i=g_j`
pointwise, and swapping their strategy coordinates preserves the **entire**
payoff vector. Its symmetry axiom requires equal allocated values for this
pair. This is stronger than an ordinary exact swapping automorphism.

Coalition threat power is
`δ(S)=max_x min_y E[sum_{i∈S}g_i−sum_{i∉S}g_i]`,
with joint coalition laws. Theorem 1, p. 834, characterizes a unique allocation
rule by efficiency, balanced threats, symmetry, additivity under independent
game superposition, and null player. Individual rationality follows. Its
formula is `γ_i=(1/n)sum_{k=1}^n δ_{i,k}`, where `δ_{i,k}` averages δ over
k-player coalitions containing i. This evaluates cooperative allocations and
threats; it does not characterize Nash-equilibrium payoffs. The literal
symmetry premise includes identical utility functions, unlike the project's
ordinary interchangeability premise. Hence it cannot simply be substituted
for cardinal-automorphism transitivity or assignment indifference.

## DS25 annotation (version of record)

The domain is TU characteristic functions on fixed N. In §3, article p. 6,
superadditive v,w are cooperation equivalent for i if some permutation σ fixes
i and `v(S)=w(σS)` for every S intersecting `N\{i}`. Thus only ∅ and `{i}`
are excluded; focal singleton worth may differ. Blend-in fairness requires
`f_i(v)=f_i(w)` for these pairs.

Section 4, pp. 6–7, proves independence from allocation-rule anonymity:
Shapley satisfies anonymity but fails blend-in; allocating v(N) entirely to
a fixed named player satisfies blend-in but fails anonymity. This concerns
rules across games, not automorphism groups of one game.

Theorem 1, p. 7, characterizes `f_i(v)=v(N)/n` by additivity, symmetric
efficiency, weak null player, and blend-in fairness. Weak null player applies
when v(N)=0; symmetric efficiency demands equal division when all players are
symmetric. Theorem 2 gives the corresponding characterization on cohesive
games. Blend-in retains its superadditive-pair scope. These explicit domain
restrictions prevent transferring the theorem directly to arbitrary
noncooperative normal-form games or cardinal utility representations.

## Comparisons derived for this project

**Established elementary comparison; novelty not claimed.** The VNM coalition
fairness predicate is not invariant under independent positive affine
translations of utility, even within zero-sum games. Consider two players with
singleton action sets and utilities `(0,0)`. Their characteristic function is
zero and is fair. Change utilities to `(1,-1)`. There are no changed choices
or preferences, but singleton coalition values become 1 and -1, so the game
is not VNM-fair. The actual cardinal automorphism group is player transitive
in both representations: constants can be matched using affine intercepts.
Thus VNM-fairness cannot be identified with cardinal player interchangeability.
This is consistent with their treatment of fixed payments as economically
meaningful differences in positions; it is not a contradiction in their theory.

**Established elementary distinction.** KN21's pairwise premise implies the
ordinary bare-transposition exact automorphism condition: the swapped payoff
vector stays unchanged, and the two focal utility functions are identical.
The converse fails. In the common-label game `u_i(s)=s_i`, exchanging player
positions and their actions is an exact automorphism, but `u_i` and `u_j`
are different functions of a fixed ordered profile. Thus KN21's explicitly
chosen symmetry axiom is narrower in premise; it is an axiom on an allocation
rule, not a classification of all exact game automorphisms.

For DS25 the closest structural analogy is a **focal** comparison after
opponent renaming, but the data are coalitional worths and the axiom deliberately
ignores the focal singleton. Our F1 utility tests preserve all focal pure
outcomes. An equivalence between them would require a proved bridge, not
shared vocabulary. Neither DS25 anonymity nor KN21 symmetry is the same
object as weak anonymity of a normal-form payoff table.

## Consequences for the research programme

The historical connection is explicit and mathematical. Its scope is also
explicit: VNM uses a predicate on cooperative guarantees, KN21 axiomatizes a
cooperative allocation from strategic games with transfers, and DS25
axiomatizes equal division using across-game local comparisons. These support
investigating relationships without supplying a universal verdict that
symmetry is sufficient or necessary for fairness.

A useful next comparison would hold a common transfer scale fixed, derive a
coalition or allocation object from a normal-form game, and prove its
covariance under a specified exact action. Cardinal utility rescaling changes
that transfer model and must be handled separately. The independently
specified assignment experiment remains a fourth object, requiring its own
preferences, information and admissible transport primitives.

## Reproducibility and access record

VNM's ignored cache is `.local/references/vnm-full.pdf`, SHA256
`949e1b1d3ef123e8f77ba6dabfc1e1f18a93b38bffeaa81532e2675a4e30d3b0`;
OCR `.local/references/vnm-full.txt`, SHA256
`40300618d4e8f42c040ee1b34feaf065aeed1bfd2bbb591e7ab3259253713f64`.
The PDF skill was used read-only; rendered pages remained under `/tmp`.

Primary web bodies were inspected on 16 October 2026. Direct shell download
of KN21's journal URL returned HTTP403; its publisher HTML and `/doi/pdf/`
body were nevertheless readable through web extraction. The initially tried
`/doi/epdf/` and journal-host URLs failed. DS25's publisher HTML and PDF bodies
were readable through web extraction; a university-mirror shell download
failed TLS. Screenshot attempts for these two web PDFs returned cache misses.
No authentication, access-control bypass, external message, or submission
was used. First-edition VNM text and a full independent verification of both
modern characterization proofs remain outside the inspected scope.
