# NOESIS Run 215 — Temporal acquisition audit (2026-10-17)

Frozen Run214 cohort, 32 fully coupled 2D tanh RNNs; checkpoints at epochs 100 and 200. No retraining, no seed selection. Original checkpoint SHA256: `1833b17c2c31ce9da4c78885a4996069a8111df7f3cb80d3fe1110b75f5e3b59`.

## THEORY ledger
All-length correctness at epoch100: 14 independently verified positives (6 two-state invariants, 8 five-cell invariants); 15 independently verified incorrect finite words (both mpmath.iv and directed Decimal); 3 unresolved. At epoch200: 21 correct, 8 incorrect, 3 unresolved (inherited Run214 dual verification). All guarantees use exact-real semantics of stored binary64 parameters. Abstention is not a negative label. Numerical search candidates are not proofs until interval-checked.

## LEARNING ledger
Four *verified incorrect -> all-length correct* transitions between epochs 100 and 200: seeds **1019, 1063, 1087, 1171**. Eight persistently incorrect: 1009, 1013, 1049, 1061, 1069, 1093, 1123, 1151. Fourteen already all-length correct at epoch100. Six transition pairs contain an unresolved endpoint.

On the 4-transition versus 8-persistent-failure subset, epoch100 AUROC: generic prefix minimum margin **0.7500**, generic final margin 0.6875, task retention 0.4375, negative training loss 0.59375, training accuracy 0.59375, negative finite-heldout errors 0.5625. The frozen >=4 transitions and >=0.75 AUROC criterion is met **at the boundary**. Exact one-sided permutation p = **53/495 = 0.10707**. This is weak evidence; do not claim statistical significance.

## Decision
Run214's 0.9524 AUROC was mostly endpoint classification, not direct acquisition-transition evaluation. Run215 identifies four actual gradient-trained transitions and an exploratory temporal discrimination signal, but not prospective unseen-architecture prediction or a causal law. The same reused cohort and very small transition sample prohibit breakthrough claims.

## Reproduction / provenance
`epoch100_labels.json` contains 32 dual-verified outcomes and strict negative witnesses. `evaluate.py` reuses `research/run214/RUN214_CHECKPOINTS.json` and `RUN214_VERIFIED_LABELS.json`. Original dual checkers and five-cell candidate generator are in `research/run214`. Full Run215 candidate boxes, both checker outputs, exact scripts, and logs were also packaged locally. No failed hypothesis was deleted.
