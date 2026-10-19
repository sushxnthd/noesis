# LEARNING ledger — Run269
Seed 18605, epoch 600, hidden size 3: independently initialized ReLU RNN, trained using Adam for 600 updates on sampled length-20 latch sequences. Recorded training accuracy 1.0 is sampled, not exhaustive.

Frozen long-HOLD and terminal-switch tests found no errors. Exact exhaustive all-symbol enumeration found three errors at length 14. This corrects the previous interpretation of finite-perfect training: sampled success is not universal correctness even inside the training-length window.

No retraining occurred, so this does not establish a training transition. No unrestricted algorithm certificate was obtained.
