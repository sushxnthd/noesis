# NOESIS Run 374 — prospective cocycle prediction fails precision-robust confirmation (2026-10-23)

**Kernel:** learned DFA-state retention under neutral cycles. **Decision: frozen conjunctive primary FAILED.** Do not promote the early-Jacobian-cocycle extrapolation to a precision-robust certificate or novel law.

## Frozen experiment
- Frozen protocol SHA256: `7e61090526736d1abaf0a5aceb2a5e7b1c968e12feea8ea8a1bff3b7507bc088`.
- Frozen 12 new neutral cycles SHA256: `86d82368cc1c58e24e60d7b39a432b7b6d9d010f601d3e81eed9ec0787d1aa15`.
- Sixteen independently trained first-perfect symbol-conditioned LSTMs, eight per task (count ones mod 3; count '01' mod 3), width 5, 258 parameters, Adam 0.035, 196 training strings/seed. All 16 attained perfect short training accuracy.
- Six unseen 12-bit neutral cycles/task; three DFA-distinguishable prefixes; forget-gate shifts 0,+2,+4 after n32. Total **864 model–cycle–shift–prefix conditions**.
- At n48 inject `1e-9` times the dominant right singular vector of the learned 16-cycle Jacobian cocycle (n48–64). Frozen score extrapolates the early finite-time growth to n256, with readout-margin normalization. This is a heuristic, not a nonlinear bound.
- Frozen primary required >=8 positive outcomes/task, AUROC >=0.80 and >=0.05 above margin-only in BOTH tasks, plus >=99.9% independent float64 agreement OR full high-precision adjudication.

## Findings
| Metric | Count ones mod 3 | Count '01' mod 3 |
|---|---:|---:|
| n256 Numba float64 intervention flips | **6/432** | **14/432** |
| Positive seeds | **1/8** | **5/8** |
| 16-cycle cocycle AUROC on float64 labels | 0.98865 | 0.93148 |
| Readout-margin AUROC | 0.48435 | 0.65243 |
| Local one-cycle Jacobian AUROC | 0.97105 | 0.60748 |

**Failure #1:** Task A has only six apparent positives, all from seed 44004; the frozen eight-positive gate failed.

**Failure #2:** Independent Numba/PyTorch float64 recurrences disagree on the n256 baseline/perturbed label pair in **34/864** conditions. The frozen reliability gate failed.

**Independent precision falsification:** Fifteen targeted cases were recomputed with an independent mpmath LSTM at 120 and 160 decimal digits, all agreeing at the tested checkpoints. **Seven of 15** complete label pairs differed from Numba float64; **eight** appeared to flip under Numba, but only **three** flipped at high precision. This is a targeted, nonrepresentative sample; **24/34** independent-float64 discordances remain without high-precision adjudication. Three illustrative cases were additionally verified at 220 digits.

**Adversarial witness:** Task count-ones mod 3, LSTM seed 44004, prefix `0`, neutral cycle `111010010010`, shift +4 after n32, n48 state intervention of `1e-9` along the frozen cocycle singular vector. At n256, Numba float64 labels are **[0,2]** (apparent flip), whereas 120/160/220-digit recurrence yields **[2,2]** (no flip). This directly falsifies the precision-robust interpretation of the apparent float64 intervention effect.

**Derivative implementation check:** Eight independent PyTorch-autograd vs Numba centered-difference cycle Jacobians; max absolute matrix-entry discrepancy 2.46e-8.

## Scientific interpretation
The nominal prospective AUROCs are conditional on numerically unstable float64-defined outcomes. They are NOT validated high-precision predictor results. The primary failed and no novel mechanism or theorem is established. A standard finite-time mean-value/Lipschitz readout-margin certificate was derived with explicit domain assumptions; it is classical and was NOT certified for these trained networks. Exact rational `F(x)=10^18 x^2` demonstrates that zero local derivative at x=0 does not protect a finite 1e-9 perturbation from a classification flip.

**Decision:** Retire early 16-cycle point-Jacobian extrapolation as a flagship precision-robust certificate. Next test should prospectively use verified nonlinear perturbation tubes or interval/affine arithmetic, with high-precision reference labels and held-out architecture replication. No Run350–362 single-coordinate claim revival; no universal +2 instability law.

## Reproducibility
The full local `NOESIS_R374_Reproducibility.zip` contains frozen protocols, source, 16 checkpoints, 864 raw conditions, independent PyTorch replay, autograd check, high-precision 120/160/220-digit records, exact-rational counterexample, statistical analysis, figures, negative results and SHA256 manifest. **This GitHub note does not imply that raw artifacts have been uploaded to GitHub.** See local `NOESIS_R374_Research_Note.md` for methods, limitations and literature priority audit.
