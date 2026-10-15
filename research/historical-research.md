# Historical evidence — inspected 16 October 2026

## Verified records and qualified conclusions

| Date | Primary record | What it establishes | What it does not establish |
|---|---|---|---|
| 1944 | First edition bibliographic lead; not yet inspected | A source to compare with later edition | No verified first-edition text or wording in this project |
| 1953 (third edition; scanned printing lists 1955) | von Neumann–Morgenstern title/copyright pages; §28 printed pp.255–259 | Correct permutation formula, composition warning and coalition-size fairness definition | No audit of their entire theory or original 1944 text |
| 2011 on title page | [Ham honours thesis](https://arxiv.org/abs/1905.00636v1), §5.8 printed p.21, PDF p.23 | Explicit diagnosis, Definition 5.8.1, transposition proposition and separating three-player example | ArXiv posting occurred in 2019; title page alone is not a contemporary public timestamp |
| 4 May 2011 12:30:02 UTC | [Wikipedia diff 427397486](https://en.wikipedia.org/w/index.php?title=Symmetric_game&diff=427397486&oldid=406077743) | Anonymous edit changes RHS strategy indices to inverse indices; edit summary identifies a definition correction | Does not alone identify the anonymous editor as Nicholas Ham |
| 8 May 2011 05:48:50 UTC | [Wikipedia diff 428033030](https://en.wikipedia.org/w/index.php?title=Symmetric_game&diff=428033030&oldid=427397486) | User Antimatroid reverts the preceding edit, restoring non-inverse indices | Does not itself document the no-published-reference motivation reported retrospectively by Ham |
| August/December 2012 | Vester report LSV-12-23; inner title 27 August, report cover December | Appendix B Definition 31, Theorem 32, Definition 33; mathematical proof publicly available as a 2012 report | Exact first online release day and an exhaustive priority search remain unverified |
| 18 November 2013 | [Ham arXiv v1](https://arxiv.org/abs/1311.4766v1) submission history; PDF Theorem 3.18 | Public version contains the inverse-condition equivalence and proof | Does not turn the 2011 thesis into a 2011 public proof of common-payoff consequence |
| 13 March 2017 | Plan author PDF title page; §2 footnote 7 | Working-paper account credits Vester and Ham and cites the earlier warning | It is not the 2023 journal text |
| 5 May 2021 | [Ham arXiv v5](https://arxiv.org/abs/1311.4766v5) | Updated theorem numbering and historical account; acknowledgement reports Plan's correction to a proof | Reported correspondence and priority details are not independent contemporary records |
| January 2023 | [Plan journal metadata](https://doi.org/10.1016/j.jet.2022.105549) | Final title, journal, volume 207, article 105549 | Full article body/version comparison not yet inspected |

## Thesis verification

The thesis is publicly accessible, so no upload is presently needed. Its exact title is *Some Structure Properties of Finite Normal-Form Games*; the later survey bibliography uses a slightly different title. The arXiv first submission is 2 May 2019; the thesis title page says 2011, Bachelor of Science with Honours, University of Tasmania, supervised by Des FitzGerald. §5.8 identifies the player/profile mismatch and supplies a symmetric three-player game failing D. It does not state or prove the later D=>common-payoff theorem. The 2011 identification and the later proof should therefore be distinguished.

Proposition 5.8.2's intended result follows from transpositions generating S_n, but its printed converse explanation does not actually give that argument. The last paragraph worries that transpositions are not closed under composition; the correct equivariance condition nonetheless extends from generators by subgroup closure. This is a thesis exposition issue to record, not a reason to discount the explicit error diagnosis.

## Wikipedia inspection method

Fetched MediaWiki API revisions with IDs, parents, timestamps, users, summaries and full main-slot content, over 3–9 May 2011, then fetched parent 406077743 separately. Both revisions and parent are cached privately; hashes appear in references/checksums.sha256. The source register gives the exact retrieval query. The inverse-index change and subsequent revert were inspected in the actual revision content, not inferred from a later citation. No claim that May 8 adds a new published explanation is warranted by its content.

Suggested priority wording: Ham's 2011-dated honours thesis identifies the mismatch; Ham attributes the May 2011 correction to himself; the actual revision record confirms that correction's content and date. Vester's 2012 report supplies the earlier publicly available proof of the common-payoff consequence compared with Ham's 2013 arXiv proof. Avoid claiming exhaustive first discovery.

## von Neumann–Morgenstern primary-source findings

Internet Archive identifier `in.ernet.dli.2015.215284` has misleading metadata date 1944. The scanned title says 1953 and the copyright/printing page lists fifth printing (third edition), 1953, then sixth printing 1955. Treat it as a third-edition scan, not verified first-edition evidence.

Inspected page images: PDF pages 7–8 (title/printing), 280–283 (printed pp.256–259). OCR text also supplies printed p.255 and surrounding context. Chapter VI is the general theory of zero-sum n-person games.

- §28.1.2, equation (28:3), follows a careful argument moving both player choice and payoff indices. Footnote 4, p.256 continuing onto p.257, warns that the placement is needed for correct successive permutations and explains why the two-player case conceals the distinction. Exact short excerpt: **“This is the correct arrangement”**. Do not inflate this into an accusation about later authors' intentions or a proof that either author previously made the error.
- §28.1.3 defines an invariance group and relates it to coalition-value invariance. This permits intermediate groups, not merely full symmetry.
- §28.1.4 and §28.2.1 use set-transitivity (transitivity on subsets of each size) to obtain a characteristic function depending only on coalition cardinality. This is stronger than simple player transitivity at the group-action level.
- §28.2.2 calls the game fair when its characteristic function v(S) depends only on |S|. The definition belongs to their zero-sum characteristic-function framework and is not itself a selection of a Nash equilibrium, an allocation, or a profile-wise equal-payoff requirement. They explicitly warn that for n>=3 fairness/total symmetry need not give the same individual outcome under good play.
- For two players the same passage recovers zero value. The transfer of coalition-size fairness to arbitrary general-sum normal-form games requires specifying how coalition values are defined; it is not an immediate generalization by replacing the word fairness.

The full definition/construction of their characteristic function and solution theory has not been audited here. The inspected text establishes what §28 means by fairness, not a completed equivalence with any of our proposed structural definitions. The 1944 comparison remains pending.

## Remaining historical questions

1. Inspect the original 1944 edition rather than reusing the 1953 text with a 1944 citation.
2. Inspect Dasgupta–Maskin's Definition 7 and symmetric-existence proofs in the original scan; the hypothesis that the error leaves their conclusions intact is unverified.
3. Obtain Plan's final journal body and compare it with the dated draft.
4. If publication requires stronger attribution of the anonymous Wikipedia edit, request author confirmation/records; public revision identity alone is insufficient.
5. Inspect any correspondence only if provided and authorized; do not invent or publish private letters.
