# NOESIS K001 Run304 — exact paired-checkpoint audit

## Frozen primary outcome
- Retrospective selection: all **18** epoch-80 cone-certified networks from Run303 (384 total trained).
- Exact binary64 rational audit: **18/18** epoch-20 checkpoints have an incorrect one-symbol prefix. All 18 epoch-80 checkpoints admit exact unrestricted-correctness cone certificates.
- Frozen success threshold >=12 paired transitions: **PASSED**.
- Independent second implementation: **18/18** paired endpoints verified; **72/72** invalid-premise mutations rejected locally.
- Early wrong words: 17 cases input 0; seed 22438 input 1.
- **Posthoc confounder control:** For **12/18** early checkpoints, changing only the scalar output bias could separate all latch-positive and latch-negative prefixes of lengths <=6. This does **not** prove all-length correctness after bias correction.

## THEORY ledger
The scalar-cone certificate is a sufficient all-length correctness proof for a restricted class of width-three ReLU RNNs, not a model-agnostic law. The exact all-length transition result does not establish that a new internal algorithm was learned rather than that a simple readout decision boundary was repaired. This caveat materially weakens the mechanism claim.

## LEARNING ledger
All 18 early/late pairs come from the same seeds of the Run300 gradient-training cohort, without post-training modification. Thus exact functional correctness changed from false at epoch20 to true at epoch80 for at least 18 trajectories. These were **selected conditional on late correctness**; they are not an unbiased estimate of acquisition frequency. 12/18 are finite-horizon bias-only rescue candidates, so the present evidence does not isolate representation learning.

## Provenance
Frozen before running Run304: FROZEN_PROTOCOL.md commit 9ac91d94643f3cbbc6dc46fcb37b368fb0a64f5f.
Source Run303 local checkpoint SHA256: early 0aa10a00406a6316d2808a7d1424022724c7ce75a5cbbdc741dd0ad44ef2f6a1; late 71f384d19e4e5ae95198b6bce2ec35f29f547b166ba293ffae60fe8a2d2d6f8d.
Local exact audit passed. Public workflow must independently regenerate Run300 checkpoints and upload all raw evidence. Public status remains **unverified** until Actions completes.
