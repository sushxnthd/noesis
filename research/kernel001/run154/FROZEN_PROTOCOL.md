# Run 154 frozen protocol

New seeds: 216 through 223. Four-state ReLU, 1200 Adam steps, 729 length-six ternary training words, neutral regularization 0.1.

Before long-horizon evaluation, compute task-preserving cycle linearization score from all six-token states: 32 neutral steps and 16 repetitions of 01, with each cycle's activation mask frozen at the prefix. Threshold score > 0.1 predicts an adversarial beam failure by depth 128. Beam parameters remain those of Run 153. Independently verify each found witness using rational arithmetic. Do not tune parameters after results. Exploratory archive 208–215 had 8/8 agreement, not a holdout.

Success: at least 7/8 observed agreements, at least two exact-confirmed witnesses, no more than one false negative. Beam no-witness is not proof of correctness. Kill or reformulate on failure. The diagnostic is not an inductive certificate.

THEORY: Local linearization is exact only within a fixed ReLU activation region. LEARNING: New gradient-trained checkpoints must be evaluated unchanged.
