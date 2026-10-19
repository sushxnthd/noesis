# Run 280 — Frozen cross-task transfer result (negative)

Executed 2026-10-20 in a sandbox CPU, not on user's device. Protocol SHA commit: 00c7ac23c3eae4544de24cbacd6b02d4fe8fbbb8.

- 96 ordinary-BCE gradient-trained RESET/TOGGLE scalar ReLU RNNs; six parameters trained; epochs 0..160.
- 576 checkpoints, 556 with 100% sampled token accuracy.
- Exact rational witnesses within length 64: 8 sampled-perfect checkpoints are actually wrong (7 at epoch 0; 1 at epoch 20).
- Frozen two-coordinate repair with a_toggle=-2: **0/8 pass simultaneous 6D parameter-box certification** at radius 2^-12. Frozen primary criterion FAILED.
- Example seed 20419 epoch 0: wrong on 12 TOGGLE symbols despite sampled perfection.
- Witness candidates proposed using float64 but all eight reported witnesses confirmed with exact dyadic rational inference. No all-length correctness claim for the 548 witness-negative checkpoints.
- Critical boundary issue: with E=[0,b_toggle/8], O=[3*b_toggle/4,5*b_toggle/4], a_toggle=-2 gives T(E upper)=3*b_toggle/4 exactly; hence any positive independent perturbation of a_toggle or b_toggle breaks that particular fixed-region robust certificate. This does NOT prove perturbed networks wrong.
- The protocol's specific repair rule is falsified; a new protocol must be frozen before modifying it.

THEORY: fixed-boundary certificates cannot claim strict box robustness at zero-margin faces.
LEARNING: 8 actual gradient-trained, sampled-perfect parity models have exact failures on unseen words. No successful robust repair in the frozen rule.

Infrastructure: local first audit timed out; the optimized audit uses float64 only to propose witnesses, with exact rational verification of each positive witness. GitHub CI for full cohort is not yet verified. Do not merge.

Checkpoint JSON SHA256: 1ad489e05732886e1ba0a6f76866ce32a2c59b0213e85df2bfa317ca8c63ad64.
