# LEARNING ledger — Run 194
Four heldout independently initialized gradient-trained tanh RNNs, seeds 137,139,149,151, checkpoints 300 and 600.
Frozen prospective score success: 0/4. Beam depths: none,10,4,none. Matched random success /100: 8,92,65,0.
Seed 137 witness 100000000000001 has even parity: epoch 300 predicts negative (correct); epoch 600 positive (wrong), despite continued optimization and lower training loss. Thus the proposed drift beam misses a real trained-model correctness regression.
Seed 139 beam witness 1010101011: epoch 300 wrong, epoch 600 correct. Seed 149 witness 0010: epoch 300 wrong, epoch 600 correct.
These are finite-length changes only, not evidence for acquisition or loss at all lengths.
