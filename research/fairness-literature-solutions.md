# Fairness literature: solution rules, allocations and utility invariance

16 October 2026. **Annotated primary-source review and standard mathematical
comparisons; no novelty claim.** This note accompanies the utility and assignment
research. It does not identify a universally correct fairness criterion.
Version and access limitations are part of each annotation. Only short
paraphrases and formulas needed for comparison are retained; no third-party
PDF is tracked.

## 1. Nash (1950): symmetry of a bargaining solution

**Primary text inspected:** John F. Nash, Jr., *The Bargaining Problem*,
Econometrica 18(2),155–162, [journal scan](https://www.haverford.edu/sites/default/files/Nash1950.pdf),
DOI [10.2307/1907266](https://doi.org/10.2307/1907266). The web tool returned all
nine PDF pages, including its modern cover sheet.

**Annotation.** Pages156–157 formulate utility on probabilistic anticipations
and state positive-affine freedom and mixture linearity. Page158 normalizes
disagreement utility to zero, leaving independent positive scales. Feasible
utility pairs form a compact convex set containing zero, with possible strict
gains for both. Page159 imposes: rejection of a point strictly improvable for
both; contraction consistency when the larger problem's solution remains
available; and equal solution coordinates when the normalized feasible set
is invariant under coordinate exchange (assumptions 6–8). Nash derives the
unique maximizer of the product of utility gains. This is a requirement on
selected bargaining outcomes under specified assumptions, not an assertion
that every outcome of a symmetric strategic game is fair. The original
symmetry axiom concerns a problem that is itself invariant. It should not be
silently quoted as the globally quantified equivariance formula for arbitrary
pairs of relabeled problems.

**Research implication (our comparison).** Distinguish a rule's relabeling
consistency from its response to a symmetry of one fixed input; Section 8 below
makes the logical distinction precise. Independent affine changes also move
the disagreement point. Rescaling a player's utility without rescaling its
reference level is a different operation.

## 2. Kalai–Smorodinsky (1975): different principles, common representation care

**Primary text inspected:** Ehud Kalai and **Meir** Smorodinsky, *Other Solutions
to Nash's Bargaining Problem*, Econometrica 43(3),513–518,
[journal scan](https://www.haverford.edu/sites/default/files/KalaiSmorodinsky1975.pdf),
DOI [10.2307/1914280](https://doi.org/10.2307/1914280). The paper's author line,
not an inconsistent institutional metadata entry, establishes the second name.

**Annotation.** Pages513–514 use a disagreement point d and compact convex
feasible S, restricted to individually rational points and admitting strict
gains. Axioms1–3 require Pareto optimality, **global** coordinate-exchange
equivariance `f(Td,TS)=T f(d,S)`, and equivariance under separate positive-affine
utility changes. Page515 replaces Nash's contraction axiom with monotonicity:
holding player1's ideal maximum fixed, increasing player2's available Pareto
frontier must not lower player2's selected utility. Formally, with their
extended frontier functions g_S, equal b_1 and `g_S<=g_R` imply
`f_2(d,S)<=f_2(d,R)`. Page516's theorem selects the maximal feasible point on
the line from d to the ideal coordinatewise maximum b(S). Thus normalized
gains have equal ratios, rather than maximizing their product. The two
solutions share symmetry and affine invariance but differ in another axiom;
those shared requirements alone do not uniquely define fairness.

**Research implication (our comparison).** A normal-form model must specify
which feasible utility set and disagreement mechanism it induces before
importing either bargaining solution. Equal normalized gain ratios are not
unqualified interpersonal equality of utility levels.

## 3. Shapley (1953): equivariance and equal treatment in a TU value

**Primary content inspected:** Lloyd S. Shapley, *A Value for n-Person Games*,
originally in Kuhn–Tucker, *Contributions to the Theory of Games II*,307–317.
The inspected text is the identified original-paper reprint, Chapter2,
pp. 31–40, in Roth's1988 collection, via [publicly indexed reprint text](https://www.scribd.com/document/594980325/The-Shapley-Value).
It is not a newly inspected original 1953 printing. The [RAND P-295 record](https://www.rand.org/pubs/papers/P295.html)
is a separate 1952 precursor; its scan returned zero text through the web
reader, and an ordinary local download returned 403.

**Annotation.** Reprint pp. 31–33 explicitly assume cooperative characteristic
functions, transferable objective utility, and finite carriers. They define
`(p v)(p S)=v(S)`. Axiom 1 makes the value independent of player names; in
current notation `phi_{p(i)}(p v)=phi_i(v)`. The OCR omits its displayed formula,
but the surrounding definition, commentary and p. 34 application fix this
interpretation. The other original axioms are carrier efficiency and
additivity. The theorem on p. 35 gives the marginal-contribution formula.
Consequently, if exchanging i,j leaves v unchanged, their values are equal.
This concerns an allocation rule and the coalition data it receives, not equal
realized utilities at all strategic profiles. Independent playerwise affine
renormalizations of normal-form utilities need not preserve the TU coalition
sums or their interpretation; a transfer scale is additional modeling data.

**Research implication (our comparison).** The exact strategic automorphism
bridge to coalition values must be proved for the chosen coalition model.
Then an equivariant coalition value gives equal allocations to positions in
the resulting coalition game's symmetry orbits. These are two separate maps
and two separate invariance arguments.

## 4. Varian (1973 working paper; 1974 article): envy is within-person comparison

**Primary content inspected:** Hal R. Varian, *Equity, Envy, and Efficiency*,
MIT Economics Working Paper115, August1973. [MIT repository identity](https://dspace.mit.edu/entities/publication/36feeece-962b-4695-a49f-95be2a23ead6)
confirms the version; [indexed scan transcription](https://paperzz.com/doc/7025845/equity--envy--and-efficiency---dspace%40mit)
was read. The direct MIT PDF was not obtained. The later [JET9(1974),63–91
publisher record](https://www.sciencedirect.com/science/article/abs/pii/0022053174900751)
was inspected as metadata, not substituted for a full final/draft comparison.

**Annotation.** Working-paper pp. 1–2 motivate equal prior claims and define
an equitable allocation by `x_i >=_i x_j` for all i,j; fairness adds Pareto
efficiency. Page10 distinguishes strong and weak efficiency/fairness. The
relevant preference evaluates **both** bundles using person i's ordering;
it does not compare `u_i(x_i)` numerically with `u_j(x_j)`. Notes on p. 9
attribute equity to Foley 1967 and fairness to Schmeidler–Yaari. Foley's original
body was not retrieved here, so its precise original formulation remains a
source gap. The paper's framework makes physical bundles and their feasibility
essential. Equal agent names or transitive game automorphisms do not supply
that allocation structure or guarantee the no-envy inequalities.

**Research implication (our comparison).** In a normal-form game whose utility
depends on the whole outcome, exchanging bundles can change externalities.
The counterfactual being evaluated must specify all resulting consequences.
Changing only a player label is generally a different test.

## 5. Bogomolnaia–Moulin (2001): procedural equality and lottery comparisons

**Primary text inspected:** Anna Bogomolnaia and Hervé Moulin, *A New Solution
to the Random Assignment Problem*, JET100(2),295–328,
[full journal PDF](https://rohitvaish.in/data/Papers/%5BBogomolnaia%2CMoulin%5D%20A%20New%20Solution%20to%20the%20Random%20Assignment%20Problem.pdf),
DOI [10.1006/jeth.2000.2710](https://doi.org/10.1006/jeth.2000.2710).

**Annotation.** Section 4 uses n agents, n objects, strict rankings, no money,
and bistochastic random assignments. Pages301–302 define first-order
stochastic dominance by all cumulative probabilities along an agent's ranking;
it is equivalent to expected-utility comparison for every VNM utility compatible
with that ranking. Section 7's no-envy criterion compares each agent's own
lottery with each other's under that agent's dominance relation. Equal
treatment of equals means identical reported rankings receive identical
lotteries (p. 309). Random priority treats equals equally but can fail no envy;
probabilistic serial satisfies no envy. For n>=4, Theorem 2 rules out combining
ordinal efficiency, strategyproofness and equal treatment of equals on their
full ordinal domain. Thus a procedurally symmetric randomized rule can satisfy
one fairness requirement and fail another. These results concern lotteries
over objects, not lotteries over player identities without an outcome model.

**Research implication (our comparison).** Robustness over all utilities
consistent with an ordinal ranking is a dominance test, usually incomplete;
it is not one fixed participant's complete expected-utility order. Expected
fairness of lotteries also differs from fairness of each realized allocation.

## 6. Mechanisms: anonymity acts on agents; neutrality acts on outcomes

**Primary research text inspected in publisher-indexed preview:** Jonathan
Perry and Robert C. Powers, *Aggregation rules that satisfy anonymity and
neutrality*, Economics Letters100(1),108–110(2008),
[publisher](https://www.sciencedirect.com/science/article/abs/pii/S016517650700420X),
DOI [10.1016/j.econlet.2007.12.005](https://doi.org/10.1016/j.econlet.2007.12.005).
The introduction, model and results preview were readable; a later direct
open failed. This is not inspection of May's1952 original proof.

**Annotation.** Its binary aggregation model permits each vote in {-1,0,1}.
Anonymity removes voter-name dependence, hence `F(P_p r)=F(r)`; neutrality
exchanges alternatives, hence `F(-r)=-F(r)`. The paper characterizes and
counts rules satisfying these requirements without imposing responsiveness.
It illustrates that agent permutations and outcome permutations are separate
actions on a rule. The Harvard link to May's original redirected to an
unavailable archive; no original May proof reconstruction is claimed.

**Research implication (our comparison).** An allocation mechanism has a
player-indexed output, so agent anonymity is normally **equivariance** of
that output, not the scalar invariance formula above. If A is the object set,
object neutrality separately relabels A and the assigned objects. A fair-looking
property of the induced normal-form game does not automatically imply either
rule property across all possible reports.

## 7. Utility representation: what is supported and what remains to read

Nash 1950 pp. 156–157 supplies an inspected primary statement of expected-utility
mixture linearity and positive-affine representation freedom (already annotated
in Section 1). Herstein–Milnor, *An Axiomatic Approach to Measurable Utility*,
Econometrica21(1953),291–297, DOI [10.2307/1905540](https://doi.org/10.2307/1905540),
is an important mixture-space primary source. Its body was not obtained here;
no theorem from it is treated as independently inspected. The existing
von Neumann–Morgenstern source record concerns the inspected 1953 third edition,
not a verified 1944 first-edition comparison.

For this project's finite outcome sets the representation statements can be
proved directly, without pretending a historical theorem has been inspected.
For pure weak orders, equal ranking representations differ by a strictly
increasing map on the attained range. For preferences over **all** lotteries,
expected-utility representations of the same nonconstant preference differ
by a positive affine map. A proof uses a worst and a best outcome: every
intermediate outcome is indifferent to one uniquely weighted mixture of them.
These standard facts and their automorphism consequences are proved in
`utility-invariance.md`; independent product laws and unrestricted correlated
lotteries must not be silently identified.

## 8. General comparison lemma: equivariance versus a fixed input's symmetry

**Standard elementary group-action fact; not a novelty claim.** Let a group
G act on a problem space X and an outcome space Y. A single-valued rule
F:X->Y is equivariant if `F(g x)=g F(x)` for **every** g,x. It follows that
`g F(x)=F(x)` whenever `g x=x`. Thus a rule that respects relabelings sends
a fixed input into the fixed-point set of its stabilizer. For a correspondence,
equivariance guarantees an invariant **set** of recommendations; it need not
make each recommendation fixed. This distinction matters for equilibria.

The converse fails. Let C2 exchange x1,x2 and exchange y1,y2, with no fixed
points in either space. Every input stabilizer is trivial, so the fixed-input
condition constrains no rule. The constant rule F(x1)=F(x2)=y1 satisfies it
but is not equivariant. Hence a fixed-problem symmetry condition alone must
not be silently identified with global anonymity/equivariance.

A second standard comparison makes the representation issue concrete. With
preferences on a common bundle space, no envy is the family of inequalities
`u_i(x_i)>=u_i(x_j)`. Independent strictly increasing changes of the u_i
preserve all of them. For lotteries evaluated by expected utility, independent
positive-affine changes preserve the analogous expected no-envy inequalities.
The reason is that both sides of each inequality use the **same** person's
utility. In contrast, `u_i(x_i)=u_j(x_j)` can be destroyed by separate offsets.
This supplies a useful ordinal/cardinal distinction without requiring equal
physical shares or numerical interpersonal comparisons.

Neither condition asserts that an arbitrary selected outcome has equal
physical shares, equal realized utilities, or no envy. Those conclusions need
the specified action on outcomes, the rule's other axioms, and the relevant
preferences. This is the common mathematical pattern linking these sources
to the present research; it is not a universal fairness theorem.

## Access and historical cautions

- All cited dates/pages identify the version actually read. Nash and KS scans
  include modern archive cover sheets, so PDF-page numbers differ by one from
  printed article positions.
- The Shapley original content was read in an explicitly identified 1988 reprint;
  RAND's1952 precursor was not treated as an inspected 1953 original printing.
- Varian's1973 working paper was read as such. Its1974 final publication and
  Foley's1967 body remain distinct source tasks.
- Ordinary cache downloads of RAND/Nash/KS returned 403, MIT returned 429, and
  one older random-assignment teaching URL returned 404. Readable web text from
  the sources listed above, not those failed downloads, supports the annotations.
  No access-control workaround, login or external correspondence was used.
- Kohlberg 2021, blend-in fairness, and the detailed VNM §28 reconstruction are
  addressed in the coordinator's companion literature notes. They should be
  joined by explicit model maps, not by asserting that all authors use the
  same meaning of symmetry or fairness.
- No psychological or political motive is inferred for objections to calling
  symmetric games fair. Substantive objections include missing interpersonal
  scales, neglected allocation feasibility/externalities, unequal realized
  outcomes, and incompatibilities among independently attractive rule axioms.
