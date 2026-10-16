# Run 192 — Finite observational equivalence, infinite unary divergence

Status: **post-hoc discovery, independent exact verification protocol frozen before exact checking**. The pair was selected after inspecting Run 191. No prospective predictive claim.

## One active kernel
1. **Question:** Can two checkpoints from the same gradient-training trajectory have identical complete prefix decisions on all binary strings through length 12, while having provably opposite eventual behavior on an infinite unary family?
2. **Primary literature frontier:** ICML 2025 streaming parity algorithm development; CAV 2021 RNN verification; Run 191 certified zero-tail failure. Finite-window indistinguishability is established background, not novelty.
3. **Exact scalar success:** finite disagreement count **0** over all 8190 nonempty binary prefixes of length <=12 (counted once per distinct prefix), AND exact interval proof of negative output for all 0^k at epoch 600 AND positive output for all k>=181 at epoch 300.
4. **Strongest competitor:** Numerical roundoff or merely aggregate-score equality, rather than exact prefixwise agreement.
5. **Cheapest falsification:** Find one differing prefix <=12 or one failed interval inclusion/sign inequality at epoch 600.
6. **Publishable threshold:** Independent checker, artifact hashes, cross-trajectory replication, priority audit, and unseen task/architecture prediction. This run alone does not reach it.
7. **Learning threshold:** Both networks must be actual saved checkpoints from one Adam trajectory, without hand-coded parity transitions; document loss and broader generalization. Repair of a unary failure does NOT imply all-length parity acquisition.
8. **Kill condition:** Any disagreement through 12 or failure of the epoch-600 all-k proof kills this particular pair as a witness; after 3 substantive failures reformulate.

**Inputs:** Run 191 frozen training artifact, seed 163 epochs 300 and 600. Parameter interpretation: exact rational values of stored binary64 floats; recurrence evaluated over exact reals using tanh. Prediction is logit >0 for odd parity and <0 for even parity.

**Verification:** (i) complete binary prefix tree depth 12 with outward-rounded intervals, (ii) direct interval prefixes plus forward-invariant fixed-point box for epoch 600, (iii) independently replay Run 191 epoch-300 two-cycle certificate. Preserve failed proof searches and exact scripts. Do not claim an algorithm-acquisition transition or novelty from this single pair.

**Backup kernels (inactive):** mod-3 cross-task certificate; causal intervention near a certified transition.
