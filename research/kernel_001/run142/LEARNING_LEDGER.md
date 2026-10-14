# LEARNING — Run 142

Four ordinary gradient-trained 3-state ReLU RNN checkpoints from Run 138, selected retrospectively (seeds 202 and 206, float32/float64). All initializations fail the binary latent certificate. Three trained checkpoints pass: 202/f32, 206/f32, 206/f64. The 202/f64 coefficient A[2,2] differs from one. All three certified checkpoints have nonunit original output gain, so exact binary task outputs require one-point post-hoc readout calibration. All three retain nonzero neutral-token drift, with exact symbolic family failure counts in RESULTS.md.

This is a restricted observed training transition, not proof of spontaneous task-level exactness. Architecture bias, optimizer rounding and retrospective selection remain strong alternative explanations. Next discriminating step: prospective training on an unseen architecture and all-token invariant verification.
