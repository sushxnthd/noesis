# Run 275: Four naturally acquired unrestricted algorithms (provisional)
Frozen protocol commit: df0700e2dedcdc2a148c0babf3886fb81259be35, before training.
New cohort: 128 independent seeds (19500..19627), BCE-only Adam, scalar symbol-conditioned ReLU recurrent model, all eight parameters trainable, no adverse regularizer. Sampled length-20 accuracy is not exhaustive length-20 accuracy.
At epoch 200: 24/128 sampled-perfect and 24/128 certified. Earlier sampled-perfect uncertified snapshots appear in four trajectories and have exact wrong predictions, followed by all-length exact certificates in the same gradient trajectory:
- 19533: epoch 40 RESET HOLD^57 wrong (length 58), epoch 50 unrestricted correct.
- 19589: epoch 30 RESET HOLD^51 wrong (length 52), epoch 40 unrestricted correct.
- 19598: epoch 40 SET HOLD^76 wrong (length 77), epoch 50 unrestricted correct.
- 19615: epoch 75 RESET HOLD^34 wrong (length 35), epoch 100 unrestricted correct.
All four early failures are earliest in their indicated one-switch families, not globally shortest. Monotonic dynamics make all longer HOLD suffixes fail in those families. Exact binary64-to-rational semantics; independent SymPy verifier 4/4.
Primary exact success criterion met at epoch 100. **Important limitations:** This is one very simple task and one scalar gated architecture; no held-out predictive acquisition law, no independent retraining yet, and no field-level breakthrough. Frozen protocol requested epoch 500; extension remains pending after local runtime interruptions. Full 1280 phase-one snapshots and optimizer state are in the local evidence archive, not yet mirrored remotely. Public CI only verifies the four committed pairs unless the retraining job succeeds.
