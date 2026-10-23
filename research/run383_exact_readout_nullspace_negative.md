# Run 383 — Exact readout-nullspace perturbations and nonlinear basin-screening negative

Date: 2026-10-24. Single NOESIS kernel: causal DFA-state retention under neutral cycles. **Frozen primary FAILED.** This is the second consecutive failed prospective readout-silent basin/observability mechanism test (R382–R383); do not tune epsilon or reverse hypotheses on the confirmatory holdout.

## Preregistration and new training
- Separate 8-network pilot, epsilon grid 0.25/0.50/0.75, frozen fallback 0.50. Pilot protocol SHA256 `18c0502e307bb1bf0426c0a29837ffda3f9de4b4300280a00b804aff78f7a283`.
- Confirmatory protocol frozen **before training**: SHA256 `caad52ed0b412c4aac2430842f3b4a69b7ab83bac6c88205f68532263c2d0cea`.
- 32 genuinely new models: 8 per architecture (LSTM width5/258 params; GRU width6/273 params) per task (count ones mod3, count '01' mod3). All 32 short-perfect at 160 Adam updates. Training schedule matched, but realized training strings differ across architecture cohorts.
- 3 state representatives × 2 new full-DFA-neutral 12-symbol cycles × 32 networks = 192 model-cycle cases; 960 complete n32–512 trajectories.
- Exact rational nullspace from serialized IEEE binary64 readout W. Independent Fraction checker proves **768/768** selected Wδ=0 equations; norm 0.50 up to 1.11e-16. At n32 perturb h only, preserve LSTM c.
- Candidate screening uses nonlinear n33–48 full-cycle map and doubled-amplitude boundary probes, selecting high-risk/low-risk/random n48-safe null directions before any n256/n512 outcome. Frozen selection SHA256 `de1b0c7b46e4dbd34cb7952458b0cc2e374450d74e6c1d7d327257ad5bf108fc`. High-precision sample SHA256 `c06fa6857a271621c09f886515f75d2158cdfc0e9088f04154f45aa78b2fd972`.

## Frozen primary
Task-B n256 high-risk minus low-risk oracle error required >=10pp, one-sided exact 16-seed sign-flip p<.05, nonnegative effect in each architecture, and high-risk minus random-safe >=5pp. **Observed all contrasts 0pp, exact p=1.0, seed-bootstrap 95% CI [0,0]; FAILED.**

At n256 baseline/high/low/random correct:
- LSTM count ones: 48/48 each; LSTM count '01': 46/48 each.
- GRU count ones: 48/48 each; GRU count '01': 44/48 each.
- Rowspace secondary: 48/48,45/48,48/48,44/48 respectively.

All 960 trajectories retained the same predicted class at n48/n256/n512; six baseline task-B cases were already incorrect by n48. This is a finite-panel result, not a universal invariance theorem.

## Precision and mechanism checks
- Independently recomputed PyTorch vs Numba float64: **2,880/2,880** endpoint labels agree (n48/n256/n512). PyTorch float32 also agrees on these labels; trajectory identity is not claimed.
- 24 preselected conditions at 120/160 decimal digits agree at n256; four also agree at n512. Two post-hoc task-B examples at 160/220/300 digits show exact readout-silent perturbations with transient n33 logit changes (~0.006735 LSTM, ~0.091815 GRU) shrinking to ~7.40e-38 and ~3.06e-21 at n48. These are numerical witnesses, not formal interval certificates.
- Exploratory full-cycle Jacobian at n48 has spectral radius <1 in **192/192** cases; operator 2-norm <1 in **188/192**; full-cycle fixed-point residual <1e-10 in **190/192**. Two GRU task-B exceptions are not near fixed points; pointwise Jacobians are not uniform contraction certificates. Early-trajectory DMD and n32 state separation were retained as controls.

## Decision
Retire local readout-nullspace direction ranking after R382–R383 failures. Reformulate the same kernel around **DFA-state-conditioned basin capture / quotient consistency**: same-symbolic-state prefix representatives, matched hidden-state transplants, prospective neutral-cycle basin destination predictions, independent high precision and validated invariant-neighborhood checks. Do not claim a new law, architecture-level causality, or publication readiness.

**Raw data location:** complete 51-file SHA256-verified local archive `NOESIS_R383_Reproducibility.zip`, SHA256 `ec49eab0685c47c2130063f33a992856f04837cbef277c33533a48ad69d29c27`. Raw checkpoint and trajectory data are **not** uploaded to GitHub in this commit.

**Prior-art scope:** Weiss et al. ICML 2018 automata extraction and Vogt et al. 2024 Lyapunov RNN analysis verified; the broader requested primary audit remains incomplete.
