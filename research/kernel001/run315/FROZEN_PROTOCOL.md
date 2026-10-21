# NOESIS Run315 frozen protocol
Date: 2026-10-21. This file is to be committed before endpoint evaluation.

Active kernel: test whether early recurrent memory retention predicts later unrestricted correctness on unseen trained models.

Question: Among fresh 96 seed-disjoint 3-dimensional ReLU recurrent latch networks, does an epoch-20 retention score beat epoch-20 negative BCE for predicting epoch-80 exact-certified correctness versus exact-witnessed incorrectness?

Primary scalar: AUROC(retention) minus AUROC(-BCE). Success requires delta >= 0.05, >=3 exact positive certificates and >=20 exact negative witnesses. Otherwise fail or insufficient evidence; do not tune.

Generator: seeds 22600 through 22695, per-seed 160 random binary words length six plus four 2-bit prefixes padded to six, persistent-OR labels at each position, float64, Adam lr 0.025, initialization N(0,0.5^2) using seed+51000, 80 updates, snapshots epoch20 and epoch80.

Predictor: let d_n = w20 dot (h20(1 followed by n-1 zeros) minus h20(n zeros)), for n in {1,8,16,32,64}. Score is min over n=8,16,32,64 of d_n/(1+abs(d_1)). Higher predicts correct. If nonfinite use -1e300. Freeze all scores and hash before endpoint adjudication.

Endpoint: exact rational inductive cone proof for positive; exact rational replay of bounded breadth-first witness (length <=12) for negative. Unresolved excluded, never treated as negative. Independent checker mandatory. Report selection bias. Finite-memory spoof control mandatory.

Frontier: Weiss et al. ICML 2018 (RNN automata extraction), Jacoby et al. ATVA 2020 (RNN verification). Finite retention is not a certificate. Competitor: loss predicts better; delayed forgetting spoofs finite retention. Falsification: fresh seeded training and exact endpoint verification. Publishable only with independent replication, unseen architecture/task and spoof resistance. Learning relevance: unmodified gradient-trained checkpoints. Kill this predictor if delta fails or counts insufficient. THEORY and LEARNING ledgers required.