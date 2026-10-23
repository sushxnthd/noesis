# NOESIS Run 380 — matched training-time gate control (2026-10-24)

**Scientific status: both frozen mechanistic gates FAILED. No new algorithm-acquisition theorem or architecture-level causal law.** Complete source/checkpoints/raw data are preserved in the separately SHA256-verified local archive `NOESIS_R380_Reproducibility.zip`; do not claim that raw evidence is uploaded to GitHub.

## Pre-frozen primary experiment
- 16 seed-matched training datasets (8 count-ones-mod3, 8 count-'01'-mod3), 32 fixed-epoch LSTMs; same width 5, 258 parameters, per-seed strings, raw initialization, Adam LR 0.035, 240 updates. All 32 achieved perfect short-training accuracy; maximum paired short CE difference 0.000356465.
- Training-time forget-gate logit temperature τ=0.5 vs τ=1, four state representatives and two neutral-cycle families per task; all seeds retained, no first-perfect conditioning.
- At n256, identity/transition accuracy: ones τ1 31/32,32/32 and τ.5 31/32,32/32; substring-'01' τ1 24/32,31/32 and τ.5 25/32,32/32.
- **Frozen interaction D=0**, versus required D≤−0.20; independent exact seed-block sign-flip **p=163/256=0.63671875**, versus required p<0.05. Seed-bootstrap 95% CI [−0.078125,0.09375]. **FAILED.**
- **Full precision census:** 256/256 n256 conditions converged at 120 and 160 decimal digits; 0 disagreements against independent NumPy/PyTorch float64 (1,280 classifications across five horizons). Eight stratified conditions also agreed at 220 digits. Convergence is not formal interval certification.

## Matched-initial-function negative control
The naïve temperature arms share raw parameters but not the initial effective function. For forget affine parameters φ=τθ, the representable LSTM function is unchanged. Under Adam without clipping or weight decay, the effective forget-parameter update at temperature τ is equivalent to temperature 1 with forget-specific learning rate τη and epsilon ε/τ, all other optimizer groups unchanged. This is a classical algebraic reparameterization identity, **not novel**.

A second frozen control trained two additional arms on all 16 seeds: τ=.5 with forget parameters doubled initially, versus τ=1 with forget-specific Adam LR=.0175 and ε=2e-8. **Effective parameter, CE, and accuracy differences were exactly zero at every logged 20-epoch checkpoint through epoch 240** on both tasks. Thus temperature is not an independently identified gate-dynamics intervention under matched initial functions.

Against the original τ=1 control, gate-specific Adam LR half produced **4/128** n256 class differences in **4/16** seeds, against the frozen secondary requirement ≥8/128 and ≥4/16. **Secondary FAILED.** All 128 treated n256 conditions converged at 120/160 digits, with zero independent float64 disagreements. Across both cohorts, 384/384 unique n256 conditions were precision-convergent. Baseline accuracy 118/128; treated 119/128; seed-bootstrap CI for the difference [−0.015625,0.03125].

Four 120/160/220-digit n256 witnesses: ones seed48003 prefix `1` identity `0`: class1→2 (harm); substring-'01' seed49001 prefix `010` identity `0`: 2→1 (repair); seed49004 same prefix: 2→1 (repair); seed49007 prefix `011` identity `1`: 2→0 (wrong→wrong). The three repair/harm cases were checked at **every cycle 32–512** with 120/160-digit agreement: baseline seed49001 first failed at cycle43 and seed49004 at cycle228, while the gate-LR-half models stayed correct throughout; for ones seed48003 the reverse occurred from cycle32. **These are post-hoc selected model-specific causal witnesses, not population estimates.**

## Decision
Runs 379 and 380 constitute two substantive failed attempts since the R378 verification success. **Retire uniform forget-gate shifts and temperature magnitude as flagship mechanistic explanations.** Preserve the single kernel, but next prospectively distinguish hidden-state information loss under the learned full-cycle map from readout-boundary drift using held-out cycles, broader DFA-state representatives, and independently matched readout-vs-recurrence interventions. Existing state-coverage, automata-extraction, finite-precision, and Lyapunov literature remains a serious novelty barrier.

Main frozen protocol SHA256: `5a19005920c86880807dd73e0b101203d7ed148ab9d897cb465487ced890df2f`. The local archive contains all frozen addenda, source, 64 trained model checkpoints, raw trajectories, full high-precision censuses, independent checkers, exact statistics, negative findings, and vector figures. **Keep PR #21 draft. Do not merge.**
