# LEARNING ledger — Run 139

Run138 trained 22 2D/3D ReLU RNNs (all A/E/w) using ordinary six-token sequence-output MSE, 1200 Adam steps, matched float32/float64 initializations. Run139 reanalyzes existing checkpoints, without retraining or prospective test-set separation.

Eight eligible checkpoints (5 float32, 3 float64) all passed length-256 evaluation but fail strict 0.1 plus-only counting at exact finite horizons between 1,400,043 and 2,218,939,927,293,197. Three matched eligible pairs (seeds 80/95/206) show float64/float32 horizon ratios of 7.24e7–5.80e8. This is not evidence of unbounded learned algorithmicity.

The raw 22-checkpoint archive and original training source are preserved in the local reproducibility package; GitHub currently has the eight minimized trained witnesses. Next discriminating action: a prospectively frozen quantitative task-coupled diagnostic with hidden-gate and nonnormal transient adversaries.
