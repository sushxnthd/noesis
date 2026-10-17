# NOESIS Run 213 frozen protocol

Frozen before training: 2026-10-17.
20 unseen seeds: 821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947.
Use Run 210 coupled-2D tanh RNN, Adam 0.03, 729 length-6 words, epochs 0,50,100,200.
Predict at epoch 100 using minimum negative final logit on words 1 0^k 1 for k=0..8. Compare against negative training loss and random length-64 prefix error count (128 words, PCG64 seed+310000).
Outcome at epoch 200: independent interval all-length certificate = POS; independently interval-certified incorrect word = NEG; otherwise unresolved. Do not label abstentions as failures.
Success requires AUROC improvement >=0.10 above strongest baseline, >=4 POS, >=4 NEG, <=4 unresolved. Failure kills this predictor; insufficient endpoint labels = inconclusive.
Primary alternative: predictor only measures finite accuracy. Probe is not an all-length certificate.
