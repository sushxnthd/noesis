# NOESIS Run301 — retrospective exact endpoint-selection attack

This audit uses **384 previously gradient-trained persistent-latch networks**, with **17 all-word certified correct, 175 exactly witnessed incorrect, 192 unresolved**. All unresolved networks have perfect sampled endpoint accuracy.

**Disclosure:** The completions were inspected before the protocol was committed. They are *hypothetical*, not newly verified neural correctness outcomes.

Exact local computation from the Run300 archived scores:
| Evaluation | Pos | Neg | Gauge AUC | Epoch20 -BCE AUC |
|---|---:|---:|---:|---:|
| Resolved only | 17 | 175 | 0.337647 | 0.923361 |
| Resolved sampled-perfect only | 17 | 18 | 0.527778 | 0.650327 |
| G: top40 unresolved by gauge hypothetically correct | 57 | 327 | **0.712860** | 0.562208 |
| L: top40 unresolved by -BCE hypothetically correct | 57 | 327 | 0.343473 | **0.947261 |

Both hypothetical completions preserve all 192 established labels and have identical total positive prevalence. The full-cohort score ranking is therefore **not identified** by currently established endpoints. This does **not** show the true unknown labels reverse the ranking, and does not validate either predictor.

Source local Run300 compact input SHA256: `c3de313180d1cc706dd85aba972975528b5b08161861988d20aea3dbf371ec2b`. Local independent rational rank-sum checker agreed on eight AUC values; four local unit tests passed. GitHub Actions re-runs the analysis on the separately reproduced Run300 public artifact, which may differ in low-order floating point bits. Its outcomes must be reported separately.

## Next action
Resolve a preselected sampled-perfect subset independently of the predictor and verify the resulting endpoints exactly before any prospective superiority claim.
