# Run 209 frozen protocol

New seeds: 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739.

Task: resettable parity. Train scalar gated tanh RNN with deterministic Adam, learning rate 0.03, 800 epochs on all ternary words of length six.

Primary score: at least three independently verified incorrect epoch-800 checkpoints, and at least 80% of those checkpoints have a globally shortest counterexample of form 1 0^k 1. An inconclusive checkpoint is not counted as correct. First errors must be independently interval-verified. Frozen before training.

Alternative: the family was peculiar to previous seeds. Falsification: a shortest counterexample outside the family. Learning threshold: real gradient-trained models. Kill the family hypothesis if the score is below 0.8 with at least three incorrect checkpoints.
