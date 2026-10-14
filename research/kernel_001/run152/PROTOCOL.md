# NOESIS Run 152 — one active Kernel 001
Date: 2026-10-14. Retrospective cross-seed extension of Run 150/151. This is NOT a prospectively frozen new experiment.

1. **Precise question:** Across all eight paired gradient-trained four-state ReLU RNN seeds (208–215), does hidden-state neutral regularization improve or worsen the globally shortest ternary counting failure horizon relative to baseline and output-only control?
2. **Primary-literature frontier:** El-Naggar et al., *On the Ability of Recurrent Neural Networks to Count* (ICGI 2023); formal neural counting and reachability already exist. No new general law claimed.
3. **Exact criterion:** Report every checkpoint's first error > 0.1 on any ternary word through depth 14; right-censor failures beyond 14. This threshold is inherited from Run 151.
4. **Strongest competing explanation:** Regularization improves a subset of neutral-token trajectories while breaking mixed-token compositions; architecture/seed effects dominate.
5. **Cheapest falsification:** Exhaustively evaluate all 3^n ternary words n<=14 for 24 archived checkpoints; certify no earlier failure using roundoff envelopes and exact-rational failure witnesses.
6. **Publishable threshold:** Prospective replication across new tasks/architectures with a task-coupled inductive certificate, independent formal checker, strong spoof controls, and primary-literature priority audit.
7. **Learning-system relevance:** All checkpoints are unchanged, ordinary gradient-trained models from the paired Run 150 protocol; no synthetic automata substituted.
8. **Kill condition:** If no prospective predictive value or architecture transfer emerges after three substantive attempts, kill this diagnostic/intervention path; do not elevate finite accuracy to an unbounded certificate.

**Evaluation:** Task symbols 0:+1, 1:-1 with reflection at 0, 2:neutral. Training length 6. Run 150 cohort: 8 seeds x (baseline, hidden-state consistency, output-only consistency), 1200 Adam steps at lr=0.025, identical initialization per seed. Complete alphabet, all words through length 14. Decimal stored float32 weights interpreted as exact-real parameters. All failures are for absolute error > 0.1.

**Provenance:** First explored depth 12, then extended to depth 14 after observing outcomes. Both must be disclosed. Longdouble alternate traversal verified all 24 depth-14 maxima; exact Fraction arithmetic verified each reported first-failure witness. Longdouble is numeric independent corroboration, not a formal independent all-word proof. Standard IEEE-754 error-envelope assumptions are explicit in executable code.

**Backup kernels (inactive):** (1) all-alphabet inductive simulation; (2) prospective cross-architecture training transition prediction. Exactly one active kernel.
