# NOESIS R372 — Frozen full-cycle forecast FAILED; numerical instability replicated

**Date:** 2026-10-23
**Status:** one active kernel: gate-mediated DFA-state retention under neutral cycles.
**Decision:** primary prospective mechanism gate FAILED. No new theorem or publication-level causal law is claimed.

## Frozen prospective design
- 64 newly trained networks: 16 GRUs and 16 MGUs per task; count-ones mod3 and count-'01' mod3.
- GRU width 6, 273 parameters; MGU width 7, 248 parameters. Identical task/seed training strings, Adam schedule, first-perfect short-training checkpoint. Width and parameterization remain unmatched across architectures.
- 12 frozen neutral cycles per task, three DFA-state representatives, update-gate logit shifts 0,+2,+4 after cycle 32.
- A shared ridge affine full-cycle map was fitted using ONLY hidden states from cycles 32–48. Predicted n256/n512 outcomes before either was evaluated.
- Frozen protocol SHA256: `f00c4f2ab3432b0efc7df13959f1dc09e5e5695c2634a00ca191f9d5832e799b`.
- Frozen cycles SHA256: `4c1aa68603fe3c105d5dd4d16ae7dcdb5d8724297da56b5de727bf56eafcbbfb`.
- Frozen forecast SHA256: `9aac5a4da804150058d96922c529cdca461cb446019e5bc73a378c9bf925a437`.

## Prespecified primary outcome (after 120/160-digit arbitration)
- n32-eligible, n48-correct opportunities: GRU 596 (70 n256 failures), MGU 568 (76 failures).
- Affine forecast AUROC: GRU **0.797963**, MGU **0.858045**, pooled **0.831788**.
- Seed-cluster bootstrap 95% CIs: GRU [0.709,0.866]; MGU [0.795,0.906]; pooled [0.785,0.876].
- Primary criterion required AUROC >=0.80 in BOTH architectures, >=0.05 above strongest non-oracle comparator, >=20 delayed failures each, and <=64-cycle nominal horizon MAE each.
- **Primary FAIL:** GRU misses 0.80; do not round up or substitute pooled result. Full training-state coverage exploratory AUROC: GRU 0.637, MGU 0.616.

## Major numerical counterexample
A complete independent PyTorch–Numba audit across 2,304 model-cycle-variant cases found **107/6,912** discordant n256 prefix predictions and **133/6,912** discordant n512 predictions. Of the n256 discrepancies, 73 occurred on count-'01' mod3 under +2 gate shift. This effect appeared in BOTH GRU and MGU cohorts. Baseline count-'01' cases had zero n256 disagreements in either architecture.

A reproducible GRU witness (task count-'01' mod3, seed 41002, prefix `1`, neutral word `000110010001`, gate shift +2 after n32) gave three distinct n256 predictions for the SAME stored parameters and input: **Numba=2, PyTorch=1, mpmath at 70/120/160 digits=0** (true DFA class 0). Float64 hidden-state difference grew from **7.20e-15 at n48 to 0.675 at n256**, an observed amplification of **9.37e13** over 208 cycles. This is an observed implementation-sensitivity witness, not a certified Lyapunov exponent or universal theorem.

All 16 implementation-discordant cases that entered the primary delayed-failure population were independently arbitrated at 120 and 160 decimal digits, with 16/16 precision-converged. Six Numba labels changed. Some n512 cases still disagree at 70 versus 120 digits (tested 120 and 160 agree). Unchecked float64-concordant cases are not claimed high-precision certified.

## Scientific decision and novelty
Retire affine/DMD forecasting as the flagship causal mechanism. Retain it as a strong baseline. The next frozen test will examine precision-robust transition dynamics, with new seeds, a third gated architecture, a fixed 0/+1/+2/+3/+4 shift grid, matched training controls, and prospectively tested Jacobian-cocycle perturbation-growth predictions. The observed +2 instability window is exploratory, not yet a law.

Prior art includes Weiss et al. (2018) automata extraction; Dan et al. (2022) regular-language generalization; Buitrago & Gu (2025) state coverage; Vogt et al. (2024) Lyapunov RNN diagnostics; classical DMD; Metric Automata Theory (2025); Brandoit et al. (2026) finite-precision state tracking.

## Reproducibility
Complete frozen protocol, code, all 64 first-perfect checkpoints, 2,304 forecasts, raw Numba outcomes, full independent PyTorch sweep, 16 high-precision primary arbitrations, figures, negative results and SHA256 manifest are preserved in local archive `NOESIS_R372_Reproducibility.zip`, SHA256 `df96f75899f9a1c97cf05c2f66eee581d789a0e2a0cd8e38f5696d2ad919df6b`. This commit records the result and archive checksum, **not** an assertion that raw evidence was uploaded to GitHub.

**Smallest defensible claim:** bounded cross-architecture predictive association plus a concrete precision-sensitive recurrent trajectory; publication-level causal novelty unestablished.
