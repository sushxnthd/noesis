# Run 375 — Complete precision adjudication of Run 374 intervention labels

**Date:** 2026-10-23  
**Kernel:** DFA-state retention under neutral cycles  
**Decision:** Decisive falsification of float64-defined intervention flips as reliable mechanistic labels. No new causal law, theorem of novelty, or publication readiness claimed.

## Frozen selection and high-precision protocol

R374 had 864 LSTM condition rows, with 34 Numba–PyTorch n256 class-pair disagreements, 20 Numba apparent n256 state-perturbation flips, and 24 PyTorch apparent flips. Before new high-precision outcomes, R375 froze the **union** of all three sets, 39 distinct rows. This is a census of all float64 apparent positives/discordances, not a random sample of all 864. Frozen protocol SHA256: `24342228ee9fd61f1857cb459638fb35e20004e848deab4f7057508d614958e6`.

All 39 selected cases were independently evaluated with mpmath at 120 and 160 decimal digits; both baseline and perturbed n256 class labels agreed across precisions in 39/39. Seven deliberately selected cases were separately recomputed with an independent decimal.Decimal recurrence at 160 digits, with 7/7 matching mpmath160. Three R374 witnesses also matched at mpmath220. **Precision agreement is not a directed-rounding interval certificate.**

## Decisive results

| Outcome | Numba float64 | PyTorch float64 |
|---|---:|---:|
| Apparent flips (all R374 positives) | 20 | 24 |
| Still flips at 120/160 digits | 10 | 12 |
| Disappear at 120/160 digits | **10** | **12** |
| Newly detected high-precision flips within the 39 selected rows | 5 | 3 |
| Complete class-pair disagreements with high precision in selected rows | 20/39 | 25/39 |

By task: count-ones-mod3 had 6 Numba flips -> 3 retained and 7 PyTorch flips -> 3 retained; count-'01'-mod3 had 14 Numba flips -> 7 retained and 17 PyTorch flips -> 9 retained. The frozen threshold was at least 5/20 Numba flips disappearing; **10/20 disappeared**.

**Do not report the 15 high-precision flips in the selected set as the total over 864 rows:** 825 implementation-agreeing float64-negative rows remain unadjudicated. The selected cases share seeds and suffixes, so no independent-trial binomial inference is justified.

### Adversarial precision ladder (exploratory)

LSTM seed44004, case177, count-ones-mod3, neutral word `111010010010`, +4 forget shift, 1e-9 state perturbation at n48. Independent Decimal classification pairs at n256:
- 60 digits: [2,2]
- 80 digits: [0,2]
- 100 digits: [2,0]
- 110 digits: [0,2]
- 120 digits: [2,2]
- 160 digits: [2,2]

Independent mpmath 120/160/220 digits: [2,2]. Numba float64: [0,2]; PyTorch float64: [2,2]. Apparent agreement at low precision is not proof of convergence. No universal Lyapunov law is claimed.

## Limitations and next gate

R375 does **not** train new networks or certify all 864 outcomes. R374's original conjunctive primary remains failed. Retire float64 perturbation-flip labels as ground truth and do not revive R350–362 or the universal +2 window. Next: construct directed-rounding interval/affine-arithmetic enclosures for the nonlinear full-cycle map, preregister certificate coverage/false-certificate rates and held-out n256/n512 failure-horizon predictions, then test independently trained matched cohorts. Existing RNN verification/chaos literature limits novelty.

**Complete raw/source/checkpoints/protocol/independent-checker archive:** `NOESIS_R375_Reproducibility.zip` (preserved outside GitHub, SHA256 `a462db88e6b7d6a0611c1b11e56e53609bb0b94f7c9df5e12fff720a0e689d95`). Raw artifacts are not claimed to be uploaded to GitHub. The archive includes the 39-row adjudication and 7 independent Decimal checks, all original R374 files, analysis and figure. **Keep draft PR #21 open; do not merge.**
