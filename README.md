# Game Fairness

Research by **Nicholas Ham** on utility invariance, player assignment, opponent
ordering and fairness in finite games. This is a substantial independent
programme, complementary to [Game Symmetry](https://github.com/n-ham-research/game-symmetry).

The foundations were transferred from the former symmetric-games repository
at commit976e227. See [transfer manifest](provenance/transfer-manifest.json),
[original handovers](research/origins), and [cross-project dependencies](research/cross-project-dependencies.md).
Original result identifiers and qualifications are retained. Canonical
maintenance of the transferred utility and fairness research is here.

The working paper, *Utility Invariance, Player Symmetry and Fairness in Finite
Games*, is a research draft with model-specific characterization theorems. Fairness characterizations require
independent decision procedures; structural symmetry alone does not imply
subjective assignment indifference or equal realized outcomes. No novel
universal fairness theorem or publication readiness is asserted.

## Build and verify

Python3.10+ standard library; pdfLaTeX, BibTeX and latexmk (TeX Live).

```sh
./scripts/build.sh
python3 -m unittest discover -s experiments
python3 scripts/verify_transfer.py
```

See research/roadmap.md and research/theorem-ledger.md. The manuscript is
paper/main.tex; local output is paper/build/main.pdf. Neither this manuscript
nor the companion has been submitted. No third-party PDFs are tracked.

Phase 8: [focused research report](research/phase8-report.md),
[observation theorems](research/phase8-observation-operators.md), and
[behavior and identification](research/phase8-behavior-and-identification.md).
