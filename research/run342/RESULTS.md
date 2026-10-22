# NOESIS Run 342 — frozen independent-endpoint falsification
Protocol publicly frozen in commit d6ed8e1a362d3eabb7c6c8b98c359eb1131dde34 before new training. Original protocol is in FROZEN_PROTOCOL.md. No post-endpoint score changes.

## LEARNING
128 new width-four gradient-trained ReLU RNNs, seeds 31000..31127, 201 checkpoints each. Independent heldout endpoint: every binary word of lengths 1..12 (8190 per model) classified correctly at epoch 200. 88 positive, 40 negative, 0 ambiguous. Independent NumPy and PyTorch classification agree 128/128. At epoch 30, proof-deficit AUROC 0.6747159090909091, training BCE AUROC 0.7934659090909091. Paired delta -0.11875; frozen +0.05 success criterion FAILED. Descriptive paired stratified bootstrap 95% interval [-0.2306818181818182,-0.009375000000000022] (10000 replicates, seed 342, not preregistered).

92/128 checkpoints are training-perfect; four nevertheless fail on unseen length 9..12. Exact rational and independent SymPy verification of the four failures:
- seed 31012: 01100000101 (length 11), expected 0, exact logit +0.45583477623399058...
- seed 31033: 100000000000 (length 12), expected 1, exact logit -4.79779085208677477...
- seed 31034: 010100000 (length 9), expected 0, exact logit +11.47613978051664187...
- seed 31103: 000000001 (length 9), expected 1, exact logit -67.84361459074414310...
All 40 shortest failures checked by exact dyadic-rational arithmetic. Seven local regression tests passed. Training used CPU torch 2.10.0+cpu, Python 3.13.5.

## THEORY
No unrestricted certificate or model-agnostic law is claimed. This is a prospectively frozen falsification of transfer from predicting a certificate to predicting independent bounded generalization on an unseen architecture. Bounded correctness is not unrestricted correctness. Previous Run341's strong positive AUROC does not transfer in this experiment. The score is representation-dependent; loss is a stronger baseline for this endpoint.

## Kernel decision
Retain 001-S with one failed independent-endpoint transfer. Reconsider the diagnostic mechanism; do not tune on this heldout cohort. Next decisive test must be on new frozen conditions or exact proofs, not post-hoc rescue.

## Provenance
Local full evidence archive contains training and endpoint scripts, all 25,728 original epoch rows (128 x 201), exact failures, independent checker, outcomes, tests, hashes and ledgers. GitHub complete raw-cohort mirroring is pending; do not claim public CI reproduced these numbers until it does.