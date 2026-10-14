# Run 154 THEORY and LEARNING ledgers

THEORY: Frozen local ReLU Jacobians are only exact while activation masks stay unchanged. Seed 216 is an exact-confirmed false negative at length 33. In the width holdout, seed 225 is another false negative. For seeds 229 and 237, increment linearization predicts errors of 29.464 and 465.500, but the corresponding real 32-step errors are approximately 0.0000176 and 0.0000180. Their actual trajectories change activation mask on repetition two. Thus frozen-mask extrapolation is neither a certificate nor a reliable prospective predictor.

LEARNING: 8 new width-4 and 16 new width-5/6 gradient-trained ReLU checkpoints, all length-six ternary counting training. The first holdout achieved 7/8 observed beam-label agreement but failed its minimum-two-witness success gate. The width holdout achieved 13/16, below its frozen 14/16 criterion (TP5, FP2, FN1, TN8). Seven total witness sequences were independently verified by rational and 110-digit decimal arithmetic. Beam no-witness is not certified correctness.

Decision: kill frozen-mask extrapolation and reformulate Kernel 001 around all-alphabet reachable-region verification and task-coupled output simulation. No intervention yet. Existing exact-counting work: El-Naggar et al. (PMLR 217, 2023). No novelty claim.
