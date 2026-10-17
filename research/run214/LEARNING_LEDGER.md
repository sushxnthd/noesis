# LEARNING ledger — Run 214

Thirty-two genuinely gradient-trained 2D tanh RNNs, Adam 0.03 on all 729 length-six reset-parity words with prefix BCE; epoch-100 probes predict epoch-200 behavior. 30/32 fit the finite training distribution perfectly at epoch 200, but eight have verified counterexamples and 21 have all-length proofs; three unresolved.

FROZEN NEGATIVE: Retention AUROC .892857; equal-step generic-final .922619, generic-prefix .952381, training-loss .910714, heldout-error .866071. Retention improvement over best -0.059524, failing required +0.10. This overturns the narrow predictive superiority hypothesis from Run 213; no causal mechanism is inferred.

EXPLORATORY CHECK: Restricting to perfect finite-training endpoints still leaves generic prefix ahead (.952381 vs retention .904762). Small negative count and architecture/task restriction prevent universal conclusions.

DECISION: Retire retention-margin superiority, retain structured retention probes for adversarial evaluation. One active next kernel: test whether generic low-margin diagnostics predict verified algorithm acquisition across an unseen architecture, against training loss and strong random testing. Kill after three substantive failed improvements; no predictor tuning on Run 214 data.
