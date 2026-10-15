# Utility invariance and fairness: research handover

16 October 2026. This incorporates both additional user briefs into Research
Phase 3. The mathematical foundation precedes any normative terminology.
No fairness definition is manufactured to obtain a symmetry theorem. All new
claims remain in research notes; the manuscript is unchanged.

## Mathematical foundation

[utility-invariance.md](utility-invariance.md) proves the typed subgroup chain
`Aut_exact <= Aut_card <= Aut_ord`, with constants and ties handled explicitly.
Cardinal means positive-affine expected-utility equivalence; ordinal means the
complete preorder over pure outcomes. Strict player-transitivity separations
already occur with three binary-strategy players.

Two canonical representatives give actual subgroup identities:

- Cardinal automorphisms are exact automorphisms of the playerwise min-max
  normalized game, assigning zero to constant players.
- Ordinal automorphisms are exact automorphisms of the distinct-level rank game.

Range signatures give necessary and sufficient conditions for the groups to
coincide. Focal-fixed ordinal preservation is already exact, and all three
player projections have the same kernel. These are finite-game statements;
the numerical scales are not inferred to be interpersonally comparable.

The complete all-pairs ordering over independent mixed profiles is equivalent
to positive affinity. A full hybrid-marginal proof establishes necessity
without incorrectly convexifying joint product laws. This confirms the
finite-game cardinal identification in Definition 3.24 and independently
reproves the statement attributed to Ham's 2011 thesis, rather than claiming
the hierarchy as a new discovery.

**Important qualification:** ordinal transformations preserve pure best
responses and pure Nash equilibria. They may change mixed best responses and
mixed equilibria; a two-player rational counterexample is verified. Cardinal
maps preserve mixed Nash and correlated equilibria, with affine-transformed
payoff coordinates, not unqualified equality of numerical welfare.

## Consequences tied to the new binary theorem

For n≥3, full **cardinal** player image gives a positive weighted exact
potential and pure equilibrium/FIP. Full **ordinal** player image gives an
ordinal potential and pure equilibrium/FIP. At n=2 the corresponding standard
strategy-trivial hypothesis is sufficient. These follow by applying the
Phase3 exact theorem to the normalized/rank games. Explicit examples show why
cardinal does not imply an unweighted exact potential and ordinal does not
imply a weighted exact potential.

The principal nonsplitting game's common payoff alphabet {0,1} makes its exact,
cardinal and ordinal automorphism groups identical. Thus individual player
permutations can be realizable without coherent group implementation even
at either preference-equivalence level. Binary payoffs are not binary actions:
this witness has four strategies per player.

## Assignment, procedure and outcome are different objects

[assignment-and-solution-rules.md](assignment-and-solution-rules.md) models one
participant's preferences over the disjoint union of role consequences. It
proves an underidentification result: the same conditional role preferences
and cardinal symmetry can support **any** vector of conditional assignment
values through role offsets. A global assignment preference or common-scale
calibration is therefore indispensable for literal subjective indifference.
Independent affine re-representations preserve conditional data but need not
preserve the participant's already fixed cross-role preferences.

The notes give exact necessary/sufficient tests for fixed conditional laws,
chosen actions before assignment, and optimized choices after assignment.
Uniform random assignment can equalize identical participants' ex ante
prospects in an asymmetric game without making them indifferent between its
conditional roles. Ordered tests, histogram averages and ex post opponent
indifference remain distinct. Ordinal information alone supplies no numerical
orbit average.

Symmetry of a game is separated from equivariance of a solution rule. Finite
group averaging yields invariant outcome lotteries even when no invariant
pure outcome exists. An averaged lottery over pure equilibria is correlated,
and need not be a product mixed equilibrium. Complete proofs and exact
anti-coordination/offset examples prevent these distinctions from being
merely terminology.

## Annotated historical and current literature

Read [solution-rule literature](fairness-literature-solutions.md) and
[VNM/strategic-value literature](fairness-literature-vnm-strategic.md) together.
They annotate the actual definitions, domains, axioms, result identifiers,
versions and access limits for:

- Nash 1950 bargaining and positive-affine invariance;
- Shapley 1953 original content in an identified 1988 reprint;
- Kalai–Smorodinsky1975 bargaining;
- Varian 1973 working-paper equity/envy and efficiency;
- Bogomolnaia–Moulin2001 random assignment;
- agent anonymity versus outcome neutrality;
- utility representation and normal-form symmetry sources;
- Kohlberg–Neyman2021 *Cooperative strategic games*;
- Dimitrov–Sun 2025 *Blend-in fairness and equal split*.

The full VNM Section 28 was read in OCR and visually checked on printed
pp. 255–260 of the **third edition**. Its coalition value is the joint
coalition-versus-complement zero-sum value; set-transitivity makes it depend
only on coalition size. Their fairness is that size dependence, not a
normal-form equality-of-outcomes claim. They explicitly limit individual-fate
conclusions and discuss fixed-payment reduction. A two-player zero-sum
constant-offset example shows why that fairness is not invariant under
independent cardinal utility translations.

Nash's original fixed-problem symmetry axiom is distinguished from the
cross-problem equivariance explicitly used by Kalai–Smorodinsky. The modern
strategic-value and blend-in papers impose axioms on allocation rules with
specific domains; their shared vocabulary is not a proved equivalence with
normal-form anonymity or assignment indifference. Full modern
characterization proofs have not all received independent line-by-line
verification. This is an annotated research review, not exhaustive priority
clearance.

## First-edition search after the Library Genesis suggestion

A targeted search including Library Genesis and the 1944 title did not deliver
an inspectable edition body in the retrieved results. Two primary Archive
catalogue leads were checked directly through their public metadata:

- `theoryofgamesand030098mbp`: the metadata response contained no item record
  or file listing; the old indexed stream was unavailable through the web tool.
- [theoryofgameseco0000john](https://archive.org/details/theoryofgameseco0000john):
  catalogue date1944, but access-restricted, with the actual PDF and OCR marked
  private and no public download displayed. Metadata is not verified edition
  text. No access-controlled file was read.

The responses remain only in ignored `.local/references/` as
`*-metadata-phase3.json`. No Library Genesis body or1944 first-edition pages
were inspected. The previous scan's title/copyright pages identify1953 and a
1955 printing despite1944 catalogue metadata. Thus the eventual introduction
may cite the book's original publication year while precisely identifying the
edition actually supporting quotations and equations. A first-edition textual
comparison remains open; it is not silently inferred from later editions.

## Review, tests and next step

A derived the utility framework; B and C independently checked it, including
the hybrid necessity proof. The coordinator separately reconstructed that
argument and checked every main utility result. The assignment note received
A/B/C checks; B requested a useful clarification separating ordinal
factorization from expected-utility averaging, which was incorporated. The
literature agents record exactly which original bodies, reprints and previews
they read. These are same-family internal AI reviews, not human/external review.

Exact tests check normalized groups, strict separations, the mixed-equilibrium
failure, potential-strength obstructions, assignment offsets and randomized
selection. The original audit records and provenance remain intact. Final
clean-checkout validation and Git status are reported in chat.

Next: select one philosophically justified participant/assignment model and
specify its cross-role preference data, admissible physical transports, timing
and information. Use the proven invariant hierarchy to test that model.
Compare the possible new potential/lifting corollaries with full literature
and seek adversarial human review before deciding what belongs in a paper.
The historical connection is established with precise scope; a universal
claim that symmetry is sufficient or necessary for fairness is not established.
