# NOESIS Run262 — pre-witness prediction freeze

This file records the prospective diagnostic output **before** running the independent long-hold witness evaluation.

- Training: 16 independently initialized 2D float64 ReLU RNNs, seeds 18201–18216, epoch 600.
- Checkpoint SHA256: 9ebc60ed3a02712be9379805c806d7c8c01d7559b8e94c1015b278f1923d0d6a
- Predictions JSON SHA256: c145475fc0ca4dc2aea42cedab416fb6e330460ec0cbb3ae5873b42b6583963a
- Exact independent SymPy checker: 15 sound certificates passed, 1 abstention; 3 corrupted certificate variants rejected.
- Finite-perfect (training accuracy 1.0): seeds 18203, 18205, 18207, 18211, 18212, 18214.
- Predicted eventual pure-hold failures among finite-perfect: **18205, 18207, 18212, 18214** (4/6).
- Other predicted eventual pure-hold failure: 18206 (train accuracy <1).
- All other seeds: NO FAILURE CLAIM; not a correctness certificate.

These are theorem-backed predictions: a strict positive wrong-attractor logit, exact forward-invariant polygon or box, and exact Schur stability imply eventual failure in ideal-real recurrent execution. The hold-failure lengths have **not** been consulted when freezing this manifest.

Training optimization deviation: the initially frozen seed-by-seed CPU loop exceeded the runtime limit. It was replaced with seed-separable batched tensor operations using identical seed-specific data, initialization, loss and Adam updates. First ten epoch600 training accuracies matched the interrupted serial run exactly. Both failed serial executions are retained as infrastructure provenance. No seeds or diagnostic thresholds changed.

Next: independently exact-replay hold inputs, find first failing lengths and check the >20 training horizon criterion.