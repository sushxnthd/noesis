# LEARNING ledger — Kernel 001
**Exploratory:** 8 CPU float64 seeds, exhaustive 64 binary length-six words with supervised state at each prefix, 350 Adam steps (lr .05). All trained token biases to within 4e-9 of +/-1; all cap gradients exactly zero and cap stayed 12. MSE <=1.32e-17. All words of lengths <=12 within 0.5 state error, first threshold crossing at 13.

**Frozen holdout:** Prediction SHA256 38b3f1dd56b18c800561f8a554612cc2243b7f2f237919c4331df5dbf692f5fe, frozen before seeds 8..11 and exact caps 9,10. 4/4 seed predictions passed; caps first fail at lengths 10 and 11. This is an *in-family* holdout.

**Task-relevant adversarial zero-test:** The explicit 25-token word '+'^13 '-'^12 gives a false zero-test for all 12 trained networks using the 0.5 output threshold. This witness was chosen *after* exploratory analysis, not prospectively frozen. Its global minimality is proved only for exact +/-1 token biases, not approximate learned biases.

**LIMITATIONS:** Architecture already contains saturation; no positive learned unbounded algorithm. Trained weights are approximate, not exact; classification threshold is 0.5 absolute state error. Training illustrates that finite supervision cannot identify a dormant cap.

**NEXT:** Evaluate task-relevant unbounded simulation obligations, not hidden norm alone (useless unbounded auxiliary states can spoof that).

**Run 145 — ordinary-gradient checkpoint:** Archived float32 seed 205 trained on length-six ternary reflected counting (MSE 2.9067269480265168e-8). Both active coordinates are coupled, no output calibration or parameter edits. Despite rho(raw A)<1, repeated increments first exceed 0.1 exact-real output error at n=141 (0.09953518 at n=140, 0.10074808 at n=141). Independent checker and CI passed. Exploratory mixed-word Pareto search timed out at depth 80; no global mixed-word shortest claim. No positive algorithm-acquisition certificate or unseen-family prediction.
