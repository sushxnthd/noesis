# NOESIS R402 — Numerical shadowing pilot; frozen feasibility gate failed

**Date:** 2026-10-24. **Status:** archived-model PILOT ONLY, not confirmatory. One kernel: causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. No fresh confirmatory models were trained.

## Pre-outcome freeze

Pilot protocol SHA256: `40e98916bded5437306de96ace628d9352d585be3f63cc587caf68b4fbb5510b`. Archived R401 checkpoints and word design are **pilot data only**; they are not independent R402 holdout results. Frozen 4 seed IDs (99420, 99421, 99424, 99426), LSTM/GRU/MGU-style, both DFA tasks, all complete symbolic states, length-10 unseen prefixes from the archived design, exact overlapping 1–5gram matched neutral alternatives of lengths 20/40/60, complete cycle n0..64 suffix-1 traces.

The intervention keeps exact serialized binary64 weights fixed and rounds recurrent hidden/cell states to binary32 after **every symbol**, while computing gates in binary64. This is isolated state rounding, **not** a genuine IEEE float32 implementation. Secondary control rounds weights and states, still with binary64 intermediates.

Frozen feasibility gate: >=5 classification divergences, both DFA tasks, >=2 architectures, >=3 seed IDs, and >=3 independent high-precision arbitrations. A failed gate prohibits a fresh confirmatory cohort.

## Pilot results

**648/648** planned trajectories evaluated. **9/648** state-rounding-versus-float64 class divergences by cycle 64; first divergences at cycles 6,8,9,10,12,16,18,34,35. **All 9** arose in **task B GRU**, on only seeds **99424 and 99426**. No task A, LSTM, or MGU divergence was detected in the frozen panel. The cross-task, architecture and seed feasibility gate **FAILED**. The weight-plus-state-rounded control also had nine divergent trajectories; this does not isolate weight quantization.

High-precision case selection was frozen after pilot, before HP evaluation: SHA256 `1aaa1e51038537d0285e4be89ea74b7581582cbeb3454237f12b38e4dfcebcf2`. The six earliest divergent cases plus six deterministic architecture/task controls all had identical labels at 120/160/220 decimal digits through their frozen case-specific horizons. Binary64 labels agreed with all 12 high-precision trajectories. The six state-rounded positive cases disagreed at their selected divergence. This is pointwise numerical arbitration, **not an interval proof**.

Independent symbolic checks: 54/54 neutral, 54/54 oracle, 135/135 exact overlapping 1–5gram checks. Original Numba versus new Numba baseline 133/133; independently implemented pure NumPy versus Numba **133/133 baseline and 133/133 rounded-state** labels. The directed `mpmath.iv` verification attempt timed out after 220 seconds without a certificate; the failed source and log are retained.

## Exploratory pilot-only predictor audit

Predefined six-cycle state-drift/readout-margin forecast AUROC **0.654147**; minimum early signed-margin baseline **0.848548**, raw d2 **0.764041**, n2 margin **0.670318**, short CE **0.406103**, word length **0.424883**. Only nine correlated positives in two seeds and one architecture/task; no statistical generalization or cross-validated superiority. The proposed forecast was worse than the strongest simple baseline.

A classical conservative one-symbol GRU Lipschitz bound is `L <= 1 + ||A_n||∞(1 + ||A_r||∞/4) + ||A_z||∞/2` for hidden states in [-1,1]. A baseline top-two readout gap exceeding `2||R||∞ L ||δh||∞` guarantees unchanged class for two exact states. It is not a new theorem, nor a validated long-horizon shadowing certificate.

## Decision and reproducibility

**First shadowing-mechanism feasibility attempt failed.** No confirmatory training, no retuning, no publication-grade discovery. Next run should use a separate pilot with prespecified rounding precision, word challenges and cross-task/architecture/seed incidence gate, and compare against simple margin and state-distance baselines. Do not infer exact-real truth from float64 alone.

Complete SHA256-verified 114-file local archive: `NOESIS_R402_Reproducibility.zip`, SHA256 `bbf39fedb0eb1bc77a82b7c2dc7f0f814c4df45cc11a0750beed741dabc22c0c`. It includes the frozen protocols, all R402 raw data/source/checkers/negative results, timed-out interval attempt and full archived R401 source/checkpoints. **Full raw data are not uploaded to GitHub.**

No new branch or PR, force-push or merge. Canonical branch `research/kernel-001-causal-generalization`, authorized draft PR #22.
