# NOESIS Run 199

Prospective diagnostic-transfer test. Holdout seeds 283, 293, 307, 311. Epochs 400 and 800. Task: prefix count modulo three, width-12 tanh RNN, training length 6, Adam learning rate 0.02.

Query budget: 455 distinct length-15 words per checkpoint for each method. Compare task-margin-guided adaptive search against uniform, Hamming-stratified and Hamming-weight 7-10 random baselines.

Primary scalar: median over 8 checkpoints of (1+adaptive_errors)/(1+max(comparator_errors)) >= 1.5.

The method is a finite adversarial tester, never an all-length certificate. The search code and this protocol must be committed before holdout training. Third failure following Runs 197/198 requires kernel reformulation.
