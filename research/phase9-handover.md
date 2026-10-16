# Game Fairness Phase 9 handover

16 October 2026. Proved candidate applications; novelty and external mathematical
review unresolved. Baseline bcf8bfc. This handover covers canonical fairness
results only; agent feasibility remains a separate local proposal.

## Findings and proofs

- **P9-I1: minimal candidate identification.** For an unknown utility array in a
linear class W, exact symmetry membership under a fixed logged protocol g is
identified by Lu iff ker(L|W) is contained in ker(D_g|W). Thus the minimum
unrestricted linear measurement rank is rank(D_g|W), rather than dimW. On the
full class, omit one discrepancy coordinate per utility-entry permutation
cycle. Restricted physical observation menus and nonconvex classes have their
own explicitly stated conditions; a known table needs no identification trial.
- **P9-S1/S2: noise limits and bounds.** The restricted smallest singular value
alpha controls inversion and certification. With Euclidean error at most eta,
exact zero versus norm-at-least-epsilon (epsilon>0) is uniformly testable iff
alpha*epsilon>2eta. No promised gap means no uniform exact certification with
positive bounded noise. Bounded independent samples give an explicit confidence
bound, with the standard exponential-tilt proof included.
- **P9-S3/F1: decision consequences and limits.** Small calibrated table errors
bound each matched role's optimized opportunity gap; mismatched response laws
add a total-variation term. Transported equilibria satisfy 2epsilon incentive
bounds. Fixed-tolerance approximate maps need not form a group. Exact symmetry
membership and ordinal ties can change under arbitrarily small perturbations.
- **P9-M1/M2: minimum masks.** For binary five-opponent tables, exactly five
uniform triple-masking contexts recover all ordered entries. A self-contained
Walsh/unsigned-incidence proof and graph characterization replace Schur–Weyl
in this finite case: the unselected complementary-edge graph must be connected
odd unicyclic. All252 five-context designs and210 four-context designs were
checked over rational matrices independently of the graph criterion. The all-r
threshold retains its separate established representation dependencies.

Full proofs: [identification/stability](phase9-identification-and-stability.md),
[mask designs](phase9-mask-designs.md).
Source assessment: [literature and gaps](phase9-literature.md).
Review provenance: [actual internal reviews](../reviews/R-P9-REVIEW.md).

## Fairness interpretation retained

The observation results identify structure, not moral merit. Assignment value
bounds require one participant's global calibration, matched commitments and
a disclosed behavior model. Procedural relabeling consistency, equal outcomes,
coalition stability and individual role indifference remain distinct. Independent
utility offsets still underidentify cross-role comparisons. VNM's verified
third edition, Nash's bargaining input and Shapley's coalition input retain
their own domains; no first-edition access or external criticism was invented.

## Manuscript and next questions

The manuscript adds only the minimal/noisy bridge to its existing observable-
symmetry narrative. The five-mask proof, sampling and approximate-group details
remain in research. Its eleven-page PDF compiles without undefined references
or overfull boxes; all rendered pages were inspected. Native editor tools were
absent from the exposed inventory; the existing local build was used.

Highest-value next work: compare the minimal linear test criterion with
statistical symmetry-testing literature; analyze cost-constrained and noisy
context selection rather than nominal rank alone; extend the finite graph
proof only when a specific problem warrants it. For endogenous strategic
behavior, specify the response or equilibrium-selection model before claiming
a welfare bound. The elementary five-mask result needs prior-art assessment,
not a broader classification campaign.

## Companion and exploratory programme

Game Symmetry's Phase9 packet is e896a5cae79c5c63a81be16f1577bc365e67a5a6;
its exact hypotheses and binary-potential contribution are preserved there.
New primary Cheng–Liu preprint reading is version-qualified; final-source gaps
remain. No fairness proof here depends on promoting those candidates.

The local agent-games feasibility report, outside both repositories, recommends
conditional continuation without creating a Git or GitHub repository. Its
persistent-state and task-specific-observation models reuse canonical fairness
results; potential-game existence alone fails as a welfare guarantee. That
proposal does not acquire canonical ownership of the proofs here.

## Verification

45 exact Python tests pass (seven new checks); all 42 imported provenance
records verified. The manuscript build and diff checks pass. Root plus two
separate agents reviewed the principal claims, with shared-model limitations
explicit. No contact, submission, authorship change or ZIP modification.
