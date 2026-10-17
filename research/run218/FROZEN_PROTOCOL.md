# Run 218 frozen protocol — function-only margin-ratio spoof

**Active Kernel 001.** Precise question: Does the finite-probe signed-margin ratio proposed in Run 217 remain intrinsic to the *classification function* under strictly sign-preserving readout transformations, when evaluated on the same gradient-trained checkpoints?

**Data frozen:** Run 217 `RUN217_DATA.json`, twelve epoch-100 gradient-trained 2D tanh RNNs, four later verified all-length acquisitions and eight persistent failures, nine fixed words totaling 54 prefixes. No label-based tuning, retraining, or changes to frozen words.

**Score:** `min_t y_t z_t / max_t |z_t|`, where `y_t` is the reset-parity target sign. Zero denominator => abstain (must report). Baseline expected AUROC 0.75.

**Spoof:** Append a strictly sign-preserving scalar readout activation `g_p(z)=sign(z)|z|^p`, with `p=2^(e/4)`, `e = SHA256("NOESIS-R218|trial={trial}|seed={seed}")[0] % 33 - 16`. Use 32 predetermined trials, independently chosen by model identifier, without labels. This preserves the binary classifier at **every input and prefix** for every `p>0`, while changing function-level confidence ratios. It is not a claim about unchanged real-valued logits.

**One scalar criterion:** range of transformed AUROCs across 32 trials >= 0.10, plus independently reproduced scores and exact sign-preservation theorem. Report all trials even if failure. If no variation, reject this spoof and do not search exponents post hoc.

**Strongest competing explanation:** ratio is predictive only under a fixed output calibration, not an intrinsic model-agnostic classifier property; arbitrary per-model warps are not encountered in a fixed architecture.

**Cheapest decisive falsification:** evaluate the 384 predetermined transformed scores on existing trained checkpoints; no new GPU or training. Independent implementation recomputes recurrent prefixes, labels, AUROCs, and SHA256 exponents.

**Publishable threshold:** this is only a negative evaluation-control result; publication requires prospective unseen-architecture acquisition prediction, independent certified outcomes, primary-literature novelty audit and stronger spoof controls.

**Learning relevance:** all score computations use actually gradient-trained neural checkpoints with previously certified acquisition/failure labels. No new learning-transition claim is made.

**Kill:** if the spoof fails, retire it. If repeated spoofs do not yield a positive acquisition predictor, reformulate Kernel 001 toward sign-only behavioral probes and certified transition localization. No claims of breakthrough from output warping.

**THEORY:** sign invariance of `g_p` is algebraic; margin ratio is not generally invariant.

**LEARNING:** retrospective 12-model discrimination may change without any learned decision behavior changing. Frozen held-out validation remains absent.

**Backups (inactive):** task-suffix distinguishability; proof-guided transition localization.
