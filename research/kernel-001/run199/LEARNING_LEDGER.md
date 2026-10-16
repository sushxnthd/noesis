# LEARNING — Run199
Four unseen training seeds (283,293,307,311), two checkpoints each (400/800), width-12 tanh RNN, float64 Adam, all 64 length-six modulo-three prefix tasks. Training accuracy 100% for all eight.
Length-15 numerical error counts at epochs 400 -> 800: 283: 17448 -> 16557; 293: 1573 -> 1702; 307: 2649 -> 660; 311: 4385 -> 3551.
Adaptive search outperformed all three fixed baselines in six of eight checkpoints. Seed283 failed to improve on strongest baseline at either checkpoint.
Prospective success is restricted to finite failure detection; no certified acquisition transition.
