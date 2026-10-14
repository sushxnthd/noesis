# LEARNING — Run 160

Archived Adam-trained checkpoints (no retraining): seed222 width4 original train MSE 2.991490071416634e-15; seed239 width6 original train MSE 5.198301033232786e-17. Both trained on all 729 ternary length-six sequences with hidden-state neutral regularization.

Task-aware post-training sparse repair: seed222 5 scalar edits, max |delta| 1.192092895e-7; seed239 6 edits, max |delta| 3.876403833445767e-9. Exact-rational induction certifies every word after repair. Independent 110-digit Decimal interpreter checked all 3,280 words through length seven for each.

**Limit:** These are post-hoc repaired trained weights, not exact algorithms acquired by SGD. They are retrospectively selected ray-like networks. Further testing requires prospective, frozen eligibility rules and spoof-aware cross-architecture coverage.
