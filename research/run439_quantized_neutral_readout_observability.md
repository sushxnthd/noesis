# NOESIS R439 — Exact quantized-readout observability obstruction and frozen R418 precision audit

**Disposition:** new verified exact *classical* all-history quantized black-box nonidentifiability result; retrospective neural precision diagnostic; **no neural causal discovery, prospective replication, or publication-grade novelty**. R438 early Jacobian predictor remains retired. Only physically valid full-DFA-state-neutral 20-bit u/v words were used.

## Frozen design and theorem
Primary protocol SHA256: `6b5c332ca4b5c8c6fe5eea02efdf5bc9d71c5bbb74c55477989254ed2e5897cb`. All nine original R418 complete DFA states and 18/18 independently verified legal neutral words; no changes to R418/R438 weights, words, probes or gates.

For a *synthetic* auxiliary state, let U(x)=x/4, V(x)=x/4+1/2, x0=0, with physically reachable closure in [0,2/3]. Fix Q_delta(y)=delta floor(y/delta+1/2), delta=1/8. Two readouts G_±(x)=2±a x, with a=(3delta/4)(1−2^(−p)), p=4,8,12,20, yield **identical quantized logits and correct labels under every legal word history**, although the physically realizable next-word v-versus-u gap effects are ±a/2. A fixed-quantizer black-box estimator thus has minimax absolute error >=a/2 on the two-model class; the sharp **supremum** as p→infinity is 3delta/8=3/64 (not attained under the half-open rounding convention). Known white-box readout weights distinguish the models: this is **not** an identifiability limitation for the archived known R418 weights.

A measurement-only K-shift threshold sweep t_j=j delta/K identifies each arbitrary scalar output to a half-open interval of width delta/K; the contrast of two arbitrary outputs has width 2delta/K and minimax uncertainty delta/K. This changes the measurement apparatus, **not** the DFA path or neural hidden state. Classical quantization geometry, not new theory.

Exact Fraction primary: 4,599/4,599 histories (511 per each of nine states), 36,792/36,792 quantized readout checks, 18/18 complete-state returns. Independent integer recurrence 4,599/4,599; independent SymPy 485/485 shifted-interval tests and slope/effect suprema 3/32 and 3/64.

## Frozen retrospective actual-R418 numerical audit
All 108 R418 contexts tracked (both tasks, LSTM/GRU/MGU, four seeds). Original R438 physical u^16 versus u^k v u^(15−k), actual appended suffix1, two rival gap effects. Synthetic quantization of **archived float64** baseline-plus-effect pairs at 2^−20,2^−32,2^−44,2^−52, not exact-real neural certificates. At delta=2^−20 across all16 positions, Task A changed 141/1,152 pairs and Task B 582/2,304; a separately frozen heldout k0..11 diagnostic found Task A **9/864**, Task B **199/1,728**. At 2^−52 heldout changes were Task A129/864, Task B793/1,728. This quantifies a readout-effect floor, not a new predictor or causal-path result.

SHA-selected 12 cases spanning both tasks and all three architectures, k0,7,15, 120/160/220-digit pointwise mpmath: 108 comparisons, maximum discrepancy versus archived float64 1.59e−11. Independent PyTorch pointwise 36/36, max discrepancy 1.16e−11. Separately frozen 400/800-digit escalation at k0,7: 0/24 nonzero Task-A rival-position differences and 7/24 Task-B at both precisions. **Numerical zeros at 800 digits are not exact-real equality proofs**; no directed interval or IEEE execution theorem.

## Negative evidence, reproducibility and prior art
No non-ceiling cross-task predictive improvement, prospective neural training, DFA-path mediation or novel RNN theorem. Initial Task-B prefix DFA oracle erroneously counted a virtual leading 01, and an independent integer recurrence had a preflight factor error; both corrected before primary outcomes. High-precision import dependency and string-parsing errors, and the timed-out 400/800-digit escalation with deterministic checkpoint/resume, are all retained. No thresholds retuned.

Schuchman (1964), DOI 10.1109/TCOM.1964.1088973; Zhao et al. (2010), DOI 10.1137/070707877; Fan and Tarraf (2016), arXiv:1607.03193 establish substantial prior art for quantized observability. Distinct from R437 finite-data Lipschitz ambiguity, R436 off-support Jacobian, R431 hypothetical path mediation, and R435 known linear-head reconstruction.

**Full SHA256-manifested local archive** `NOESIS_R439_Reproducibility.zip`, SHA256 `0a24b5f01216def532e1a9770560055afe7d2470a5d0887fe519287ff521509a`, 69 payloads including immutable R438->R418 checkpoint chain, frozen protocols, all raw/negative/errors/independent source. Independent manifest verification 69/69 and clean replay of four deterministic outputs passed.

**Next:** retire fixed artificial quantizer as breakthrough candidate; investigate neural-specific finite-precision/exact-real readout-effect stability and seek a genuinely non-ceiling cross-task physical input observable, or freeze another distinct negative necessary-condition experiment. No user spend or laptop access.
