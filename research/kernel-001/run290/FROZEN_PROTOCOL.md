# K001 Run290 frozen before outcomes

Question: Can gauge-fixed invariant distance at epoch 20 predict independently established all-length correctness at epoch 80 for new gradient-trained width-two ReLU parity networks?

Primary metric: ROC-AUC(gauge-fixed LP score) minus ROC-AUC(negative BCE) on exactly certified vs exact-counterexample-resolved endpoints. Pass if difference >= 0.10, with at least 25 certified and 50 witnessed incorrect. Abstentions excluded and counted.

Fixed seeds 21184..21439 (256); same training as Run288 (160 random length-six sequences plus 4 fixed, neutral Gaussian 0.5 initialization, Adam 0.025, 120 epochs, float64). Score fixed from Run289: d_i=1/max_x|b[x,i]|, negative Run288 relaxed LP slack, delta 0.05. Score before outcome evaluation; persist score hash. Exact verifier and rational witness finder from Run286; do not treat missing certificates as incorrect.

Competitor: predictor only predicts its own verifier, not correctness. Falsification: low AUC gain or insufficient resolved cases. Publishable only with independent exact checking, positive gauge invariance, reproducible public training, and prior-art audit. Learning threshold: at least two witnessed incorrect sampled-perfect checkpoints becoming certified during training. Kill or reformulate on failure, or after three substantive failed refinements. THEORY: normalization fixes positive diagonal ReLU rescalings only. LEARNING: heldout correctness outcome unknown at freezing. Two backups: quotient-state simulation, architecture transfer. No other active kernel.
