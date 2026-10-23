# NOESIS Run 378 — Affine verification of learned LSTM neutral-cycle behavior

**Date:** 2026-10-23  
**Branch:** `research/kernel-001-causal-generalization`  
**Kernel:** causal transition dynamics of learned DFA-state retention under neutral cycles.  
**Decision:** **Frozen method-validation primary PASSED (4/4 paired n256 certificates; threshold >=2/4).** This is **not** a new theorem of algorithm acquisition or proof that gates explain the earlier GRU/Elman association.

## Frozen experiment

Protocol SHA256: `24784a81e595764471e24b90acf93075ad243f5729e1def05c9df179a8b28bd6`, saved before opening outcomes. Reused four preselected Run374 LSTM rows `[0,177,600,754]`, 160-decimal-digit arithmetic, exact serialized binary64 weights, exact-real decimal `10^-9` state perturbation at n48, and frozen checkpoints `48,64,96,128,192,256`. Primary success required >=2 of four *paired* baseline/perturbed readout-class certificates at n256 with zero disagreements against independent Decimal labels. No cohort or threshold changes.

## Result at identical 160-digit precision

| Cycle | R378 affine zonotope + QR | R376 natural interval | R377 recentered coordinate bounds |
|---:|---:|---:|---:|
| 48 | 4/4 | 4/4 | 1/4 |
| 64 | 4/4 | 4/4 | 0/4 |
| 96 | 4/4 | 2/4 | 0/4 |
| 128 | 4/4 | 0/4 | 0/4 |
| 192 | 4/4 | 0/4 | 0/4 |
| **256** | **4/4** | **0/4** | **0/4** |

At n256, the certified baseline/perturbed labels are:
- Count-ones-mod3 seed 44006, word `100011010101`, shift 0: **(0,0)**; correct DFA label 0.
- Count-ones-mod3 seed 44004, word `111010010010`, shift +4: **(2,2)**; correct DFA label 0. Both predictions are wrong despite certification.
- Count-`01`-mod3 seed 45005, word `101111001001`, shift +4: **(0,1)**; correct DFA label 0.
- Count-`01`-mod3 seed 45000, word `101000010111`, shift +4: **(1,2)**; correct DFA label 1.

The last two are **model-specific, long-horizon, within-checkpoint perturbation-induced class changes**. They do not identify the causal effect of training-time gate changes.

## Conditional enclosure method

For each LSTM bit step, propagate an affine zonotope `x_bar + A[-1,1]^m`. Apply the analytic interval Jacobian to the generators; add independent generators for rigorously bounded nonlinear Taylor remainders and point-rounding residuals. Use the global bounds `|sigmoid''|<=1/8` and `|tanh''|<=1`. At each complete neutral cycle, choose a basis `B` by numerical QR, then **independently compute an outward interval inverse** and upper bounds `s_j >= sum_k |(B^-1 A)_jk|`; replace the generators by `B diag(s)`. QR determines a basis, not the correctness of the enclosure. Strictly separated readout-score intervals yield class certificates.

This is established validated-numerics methodology, **not a new theorem**. The certificate is conditional on the `mpmath.iv` outward-rounding implementation (including interval matrix inversion) and has not been independently audited by a proof assistant.

## Independent controls

- Independent `decimal.Decimal` implementations at 160 and 220 digits agreed with all 48 certified endpoint labels at each precision: **96/96 comparisons, zero disagreements**.
- 12 independent PyTorch-autograd Jacobian/forward tests passed (maximum Jacobian difference `7.77e-16`).
- 1,000 randomized independent second-order remainder checks passed.
- 12 independent interval QR-inverse checks enclosed the identity.
- Independent DFA oracle confirmed the four suffixes preserve symbolic labels.
- An elementary **exact rational** finite-horizon spoof was checked on 774 cases: a 3-class contraction preserves labels through n256 and loses two at n257. Classical counterexample; no novelty claim.

## Limitations and next decisive science

Four **preselected, reused** LSTMs, not a prospective unseen training cohort. The intervention is a hidden-state perturbation at n48, not a training-time gate change. Only six fixed horizons are certified, not the first failure time or unbounded DFA equivalence. The verifier is expensive (~359–384 seconds per case). Priority precedents include Ryou et al. 2020, Jacoby/Barrett/Katz 2020, Ivanov et al. Verisig 2.0 2021, and Vogt/Zheng/Shlizerman 2024.

**Smallest claim:** A frozen four-case learned-LSTM benchmark achieves 4/4 paired n256 class certificates at 160 digits using direction-preserving affine enclosures, versus 0/4 for two previously frozen coordinatewise methods, with independent label agreement and two certified long-horizon state-perturbation flips.

**Next:** Freeze unseen seeds/neutral words and matched training-time gate interventions across architectures, then use this verifier as a measurement instrument. Do not promote the method into a general causal law until that prospective test succeeds.

**Raw evidence:** Complete frozen protocol, source, 4 per-case interval records, checkpoint/word inputs, independent Decimal160/220 records, PyTorch audit, 1,000 remainder tests, exact rational witnesses, figures and SHA256 manifest are preserved in the separate local `NOESIS_R378_Reproducibility.zip`. This commit does **not** claim the raw archive is uploaded to GitHub.