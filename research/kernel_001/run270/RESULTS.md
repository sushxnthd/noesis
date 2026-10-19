# Run 270 — Exact trained-model all-alphabet certificates

Pre-run protocol commit: cf659899734511bbcfe0566b62ced167f668997b. Branch: research/kernel-001-run270-symbol-gated-certificate.

THEORY: An exact two-region simulation checker certifies 8/24 baseline and 9/24 intervention models at epoch 500. Independent Fraction interval-image implementation agrees on all 48 final checkpoints. Five corrupted controls and five within-family delayed-reset spoofs rejected. Exact-real mathematical semantics of stored binary64 weights only.

LEARNING: All 8 scalar parameters trained by Adam from seeded random initializations, 500 epochs, finite length-20 sequences. At epoch 0, 0/48 certified; by epoch 100, 8/24 control and 9/24 intervention certified. Only seed 19015 is discordant. Matched-pair improvement 1/24; exact two-sided McNemar p=1.0. No significant causal effect.

IMPORTANT NEGATIVE: Every sampled-perfect checkpoint was also certified and every uncertified checkpoint had imperfect sampled accuracy. This experiment does NOT show the diagnostic adds predictive value over sampled training accuracy on this cohort. Gating may favor the latch algorithm.

Adversarial family: a=(2,1,2^-K), b=(-1,2,-1), v=1,c=-1. Correct on every word through length K+2; fails at length K+3 on SET SET HOLD^K RESET. Exact independent checker rejects K=8,16,32,64,128. Exhaustive K=8 check found no error through length 10, five at length 11.

No model-agnostic acquisition law or field-level breakthrough is claimed. See generated checkpoints.json and certificates.json, training/checker sources and CI provenance.