# NOESIS Kernel 001 — Run 318 frozen repair-transfer protocol

Frozen before any Run 318 training or endpoint evaluation. Parent: Run 317 exploratory single-seed repair.

## Question
Does the **unchanged** Run 317 two-parameter repair transfer to previously unseen gradient-trained width-three ReLU persistent-latch networks, yielding sound all-length algorithmicity rather than merely delaying failure?

## Cohort and training
Exactly 48 new seeds, integers 22700 through 22747 inclusive, disjoint from Run 315's 22600–22695. Copy Run 315's training configuration verbatim: float64 PyTorch, width 3, length-six token-supervised persistent latch, 160 random plus four fixed strings per seed, Adam lr 0.025, 80 epochs, snapshots at 0/20/80. No hyperparameter changes, reseeding, exclusion, or model selection. No laptop or paid resources.

## Three conditions
For every epoch-80 model, compare (A) original 28 binary64 parameters, (B) bias-only replacement p[27] = -1/100, (C) fixed repair p[0] = 11/10 and p[27] = -1/100. All other parameters unchanged. Use Fraction.from_float on original weights and exact rational replacements. Do not tune the two constants or select a different hidden coordinate.

## Primary success criterion (single scalar)
Count **S** = number of unseen networks where C passes the unchanged Run 317 all-length cone certificate, B has an independently verified incorrectness witness, and C has an independently checked exact proof. S >= 3 supports limited transfer of this *fixed* intervention; S < 3 fails the frozen criterion. Report all 48, including abstentions. Certificate incompleteness is not proof of incorrectness.

## Secondary controls
For every model and condition, enumerate binary words lengths 1..10 (or to earliest failure), recording exact first error and margins. If C fails, minimize a counterexample; if no counterexample <=10, mark bounded-only, not correct. Independent checker must not call discovery certificate. Report differences in train loss, exact witness counts, cone proof counts, and repair-induced regressions. Preserve all results.

## Strongest competitor
The Run 317 repair is seed-specific, not an invariant learned-memory mechanism. Replacing a single hard-coded coordinate on unseen networks can corrupt other trained representations or fail to repair the true memory-bearing coordinate.

## Cheapest falsification
Exact first-error witness on a new trained model for C. For a successful C, independently recheck all invariant inequalities with rational arithmetic.

## Publication / learning relevance / kill
No breakthrough claim without primary literature audit, spoof baselines, independent checker, new architectures/tasks, and a mechanism-derived prospective transition prediction. This run is learning-relevant only because it applies a frozen intervention to newly gradient-trained checkpoints. If S < 3, kill the fixed numerical repair rule; do not revise it on these outcomes. Keep exactly one active Kernel 001, with no more than two backups.

## Prior art
RNN verification / automata extraction are established (Weiss et al., 2018; Jacoby et al., 2020); this protocol does not assert novelty.

## Evidence preservation
Commit scripts, configs, 48 full trained checkpoint trajectories, raw and derived outcomes, minimized witnesses, independent verifier, tests, CI status, and separate THEORY/LEARNING ledgers to this isolated branch. Do not merge active experiments to main.
