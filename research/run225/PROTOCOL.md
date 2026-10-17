# NOESIS Kernel 001 / Run 225 — frozen robustness-gauge spoof

Question: Is absolute L-infinity parameter robustness intrinsic to the binary algorithm acquired by a gradient-trained RNN?

Cohort: Six epoch-200 and five epoch-100 all-length certified Run223 3D tanh checkpoints (seeds 1301,1319,1327,1409,1427,1451 at epoch 200; seeds 1319,1327,1409,1427,1451 at epoch 100). Source checkpoint SHA256: 4cc24de3636fa8aaf98bbd96470d8e9f3509b2c16b7fcce021cd6d681b542dd8.

Frozen construction: Append a fourth recurrent state initialized to zero, with all incoming recurrent weights and token biases zero and readout weight K=2^24. At baseline this coordinate is identically zero for all inputs, so binary outputs are unchanged at all lengths. Perturb only the new coordinate's token-0 bias by delta=2^-20; test word (0), target 0. Controls: delta=0 and K=0. Verify signs under exact-real tanh using two independent interval implementations (mpmath.iv and directed Decimal). Do not tune K/delta or choose a new witness after seeing results.

Exact success criterion: 11/11 baseline functions identical at all lengths by construction, and 11/11 wrong predictions after the one-parameter perturbation, independently interval verified. Competing explanation: robustness .03 remains valid for the original fixed 3D parameterization. Falsification: any strict interval sign test fails or checkers disagree. Publication: rigorous proof, independent trained-model replay, priority audit, explicit limitations. Learning relevance: >=4 previously trained all-length certified networks affected. Kill: if no verified spoof survives, retire this diagnostic attack.

THEORY: Investigate architecture dependence of parameter-space robustness, not all-length functional correctness. LEARNING: Evaluate existing trained checkpoint cohort, not prospective acquisition prediction. Kernel 001 stays the sole active kernel. Zero spend.
