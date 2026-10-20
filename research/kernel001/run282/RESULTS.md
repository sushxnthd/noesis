# Run 282 — Heldout neutral initialization and exact neural acquisition

Protocol was committed before training; results generated on sandbox CPU using torch 2.10.0+cpu. Frozen scalar threshold >=5/96 witnessed incorrect-at-initialization -> exact-certified-at-epoch160 neutral models: **25/96**, passed. Exact independently checked. Biased control: 96/96 certified at epoch40. 192 networks trained, 1152 checkpoint snapshots. Full raw local dataset SHA256: `c3cd466ff381c96c39f552df58b4185819535dca6fdd9ecd9415fffe340fc861`.

**Stronger five late transitions (post-hoc discovery, not prospective timing prediction):**

| Neutral seed | Sampled-perfect but wrong epoch | Later certified epoch | First incorrect TOGGLE^n |
| --- | ---: | ---: | ---: |
| 20575 | 20 | 40 | 14 |
| 20531 | 40 | 80 | 17 |
| 20547 | 40 | 80 | 9 |
| 20561 | 80 | 120 | 36 |
| 20567 | 120 | 160 | 244 |

Exact rational recurrence independently confirms the first failure in each pure-TOGGLE family and proves every later length of the same parity fails. Later checkpoints satisfy the two-state all-length simulation. All six weights updated by Adam, ordinary BCE, no intervention, no adverse regularizer, no task-biased initialization in the neutral arm.

**Reproducibility:** Full 192-model training and independent verification are encoded in train.py/verify.py. Workflow uploads all checkpoints and optimizer state. Local clean exact checks passed. Public workflow result must be checked separately; do not claim green CI until confirmed.

**Claim boundary:** Architecture-specific exact algorithm acquisition, not a model-agnostic law or general predictor. Five transitions found retrospectively. Retain failures, all checkpoint outcomes, and CI failures.
