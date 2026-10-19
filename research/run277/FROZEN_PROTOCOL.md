# NOESIS Kernel 001 — Run 277 (frozen before training)

Active kernel: full-alphabet algorithm acquisition, dual defect mechanism. No other active kernel.

1. **Precise question:** Under a shifted training length (12 rather than 20), does a frozen combined HOLD-escape/RESET-amplification mechanism discriminate prospective acquisition of unrestricted correctness from persistence of a finite heuristic in ordinary gradient-trained scalar symbol-gated ReLU RNNs?
2. **Primary frontier:** van Rossem & Saxe (ICML 2025), Jacoby et al. (ATVA 2020), Ryou et al. (CAV 2021). Infinite generalization and RNN inductive verification are known; no priority claim.
3. **Exact success scalar:** S = TP - 4 FP - 2 FN; PASS if S >= 5 AND (S > score of all-eligible-positive forecast) AND at least 5 verified acquisitions. All eligible models are scored, not only predicted positives. FP includes any positive lacking exact earlier failure and independently verified later all-length certificate. FN is any predicted negative with exact earlier failure and later certificate.
4. **Strongest competitor:** Predict all eligible uncertified sampled-perfect checkpoints acquire unrestricted correctness by the target snapshot; also report persistence and sampled accuracy baselines.
5. **Cheapest falsification:** Deterministic 256-seed CPU training with exact rational checking and independent SymPy verification; do not tune after outcomes.
6. **Publishable threshold:** Replicate in another task/architecture, survive adversarial spoof and independent verifier, demonstrate advantage beyond all-positive baseline and prior art.
7. **Learning relevance threshold:** >=5 independent natural wrong-to-exact-correct transitions without adverse regularization, with predictive improvement.
8. **Kill condition:** Three frozen failed cohorts OR one unsound positive certificate; if this run fails, count it and do not post-hoc tune.

**Frozen design:** seeds 19884..20139 (inclusive), disjoint from previous cohorts; 256 random length-12 ternary sequences plus 27 all-length-three words padded with HOLD per seed; scalar ReLU recurrent h'=relu(a_symbol*h+b_symbol), readout v*h+c, eight trainable parameters; float64 Adam lr=.03, BCE only, 125 epochs, no regularizer. Snapshots 0,10,20,30,40,50,60,75,85,100,125. For each seed choose first sampled-perfect but uncertified checkpoint among 30,40,50,75; targets 30->50,40->60,50->75,75->100.

**Frozen predictor:** predict acquisition if every failed sufficient-certificate obligation is in {hold_low, hold_high, reset_antitone}, AND the earlier checkpoint has a valid exact counterexample of form SET HOLD^n, RESET HOLD^n (0<=n<=500), or SET HOLD^n RESET via an exact rational growth proof (0<=n<=500). Otherwise predict negative. All negative eligible checkpoints also receive independent counterexample search and exact later certification. For all-eligible baseline predict positive for every eligible checkpoint, with the same witness requirement. The certificate failure alone is NOT treated as incorrectness.

**Arithmetic:** stored float64 values interpreted as exact dyadic rationals, exact-real recurrence, strict threshold v*h+c>0. Independent verifier required. Training accuracy is sampled, not exhaustive. Preserve abstentions and all failures.

**Ledgers:** THEORY records proof soundness, failure-family completeness limits and strongest spoof; LEARNING records actual trained checkpoints, outcomes and acquisition transitions. Keep no more than two inactive backups. Wildcard budget <=10% and strictly isolated.

**Repository provenance:** branch research/kernel-001-run277-dual-defect-heldout; this protocol must be committed before training. Keep any CI and connector failures.
