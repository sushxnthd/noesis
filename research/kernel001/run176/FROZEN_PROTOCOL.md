# NOESIS Run 176 — prospective 32-block mask-gate falsification (frozen 2026-10-15)

Kernel 001 only. No model weights are changed. This is a prospective evaluation on **new balanced words**, not new training seeds. Runs 174–175 are retrospective design evidence, not test evidence.

## Eight-field active-kernel contract
1. Question: Does verifying the first 32 repetitions of a neutral word remain sufficient to validate a fixed-activation affine clock prediction through 8,192 repetitions in archived gradient-trained ReLU counters?
2. Frontier: ReLU networks are piecewise affine; inductive verification of activation regions is established. NOESIS Run175 found 4 false clocks, all preceded by activation switches; a first-32 gate rejects three false-safe clocks retrospectively but missed a late-switch clock error. No novelty is claimed for affine algebra.
3. Exact run success criterion: At least 8 observed failures, at least 50% non-abstention coverage across 128 evaluations, and **zero** incorrect first-failure clocks (including false-safe cases) among accepted predictions. Count abstentions and per-width coverage; no threshold tuning after evaluation.
4. Strongest competing explanation: Local 32-block output error already predicts clocks; prefix mask stability does not imply long-horizon mask stability.
5. Cheapest falsification: Freeze all 128 first-32 gate decisions and affine predictions, then independently evaluate actual full ReLU recurrence through 8,192 cycles.
6. Publishable threshold: A surviving selective gate must also beat local error/MSE baselines prospectively, survive independent reimplementation and a late-switch adversary, and demonstrate relevance to new gradient-trained conditions. Passing this run alone is insufficient.
7. Learning relevance threshold: A diagnostic must predict unseen neutral-word failure in unchanged gradient-trained networks, not merely prove an abstract affine claim.
8. Kill: Any accepted incorrect clock falsifies the 32-block gate as a sufficient validity certificate. Retire/reformulate, preserving all failures.

## Frozen inputs / protocol
- Original archived Run174 checkpoints: widths 3,7; seeds 400..415 inclusive; no training. Checkpoint source: Run175 archive `run174/checkpoints`. Exact archived SHA256 manifest as in Run175 protocol: `39a01a0b051cadcb2c5114bbb65d04f35ce4c21bf5260cd79b438e78af9121a8`.
- Four deterministic SHA256-selected unseen neutral words: `1011001010`, `1011010100`, `001001010111`, `100101110100`. Selection: sort balanced binary strings of each length (10 or 12), excluding Run175 words, by SHA256 of `NOESIS-RUN176-V1:` concatenated with the string; take first two of each length.
- Start from six zero symbols (true count 6), then repeat each neutral word. After each full block, measure absolute output error from 6.
- Evaluation horizon 8192, failure if absolute error >0.1, strictly. float64 sequential recurrence in original Run175 order. No float32 equivalence is assumed.
- Affine predictor uses the first-block activation masks and computes the first threshold crossing through 8192.
- Gate abstains if ANY activation mask differs from the first block within blocks 2..32. Otherwise it accepts the affine prediction.
- Freeze 128 predictions and gate decisions as a file and SHA256 **before** evaluating the full network beyond block 32. Archive the SHA256 in a separate commit when possible.
- Report wrong accepted clocks, false-safe accepted clocks, coverage, per-width metrics, 32-cycle linear baseline and training MSE. No selection after seeing outcomes.
- All evidence must stay on `research/kernel-001-run176-mask-gate`, not main. No general certificate claim even if the gate passes.
