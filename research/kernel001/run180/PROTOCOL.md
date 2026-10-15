# NOESIS Kernel 001 — Run 180 frozen hard-cohort test

Status: prospective candidate-selection protocol. Only one active kernel.

1. **Question:** On unseen balanced compositions of previously gradient-trained counting RNNs, can an execution-semantics-aware activation-region verifier provide predictive information that the 32-cycle linear-error baseline misses?
2. **Frontier:** Recurrent neural counting limitations (Weiss et al., ACL 2018; El-Naggar et al., 2023); interval/abstract-interpretation verification and piecewise-affine ReLU dynamics are established. No novelty is presumed.
3. **Scalar criterion:** On a deterministic hard cohort selected *without* full-model evaluation beyond 32 cycles, require at least 8 errors by the 32-cycle linear baseline and at least 10 percentage points higher correct classification by the proposed verifier, with no false certificates. A smaller improvement is a negative result.
4. **Strongest competitor:** Linear extrapolation from cycles 1 and 32, plus an unverified fixed-mask affine extrapolation.
5. **Cheapest falsification:** Exhaustively enumerate balanced words of lengths 2,4,6,8,10; compute only the first 32 cycles and frozen predictors; evaluate at most 128 deterministically selected model-word pairs to horizon 8192; independently replay disagreements.
6. **Publishable threshold:** A genuinely novel, priority-audited mechanism plus prospectively frozen baseline-beating predictions on new gradient-trained checkpoints and independent architecture/task transfer.
7. **Learning relevance:** All checkpoints must be verified unchanged artifacts from actual gradient training; report unique checkpoints and both widths, not merely pairs.
8. **Kill:** If the cohort contains no genuine baseline-disagreement failures, or if verifier adds no predictive value in three substantive tests, kill this line as an algorithm-acquisition predictor. Preserve bounded verification as a tool.

**Selection freeze:** Rank candidates by a deterministic score based only on cycles 1–32 and/or analytic affine-map data. No full neural rollout beyond cycle 32 before recording selection and prediction SHA256. At most 128 cases. Freeze selection and predictions on this research branch before evaluating true outcomes. All failures, abstentions, and numerical-semantic limitations remain visible. Exact-real certificates and binary64 numerical replay are distinct claims.

**Do not promote retrospective exploratory results as prospective evidence.**
