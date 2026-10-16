# LEARNING ledger — NOESIS run 197

- Frozen task: count 1s modulo 3 at every prefix of all 64 binary strings of length 6.
- Width-12 tanh RNN, 3-logit head, Adam lr 0.02, 800 full-batch steps, float64. Seeds 241, 251, 257, 263; checkpoints 400 and 800. All eight checkpoints achieved 100% training-prefix accuracy.
- Held-out exhaustive length-10 accuracy varies from 878/1024 to 1024/1024. Random 128 length-64 words require every prefix correct; outcomes vary from 7/128 to 128/128.
- **Strongest deceptive checkpoint:** seed 257 epoch 800 passes all 1,024 length-10 inputs and all 128 frozen random length-64 inputs, yet has an independently verified error at length 15. The first incorrect input length is exactly 15. This is a direct demonstration of evaluation spoofing by a naturally trained network, not a constructed finite-state cap.
- Fixed suffix-box certificate abstained on all eight checkpoints, so its cross-task transfer is not established. This is a substantive negative result and counts toward the kernel's kill condition.
- There is no evidence here of a prospectively predicted acquisition transition. The frozen success criterion (>=1/8 all-length certified) failed.