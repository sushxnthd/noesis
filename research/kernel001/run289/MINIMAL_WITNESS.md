# Run289 minimal trained-model witness
Checkpoint: Run288 seed 21105, epoch 20, trained with ordinary BCE/Adam.
Original LP score: -1.9660673414343597.
Exactly function-preserving positive diagonal gauge G=diag(8,1/8) gives score -15.728538731474877.
Absolute score shift: 13.762471390040517.
Epoch80 certificate endpoint: noncertified/UNKNOWN, unchanged by gauge.
Exact rational identities: A'=GAG^-1, b'=Gb, v'=vG^-1, c'=c; ReLU(Gz)=G ReLU(z). Thus every finite-word logit is unchanged under exact-real arithmetic.
Independent exact checker tests every trained seed and four gauges. The witness is a *diagnostic spoof*, not a claim that this neural model computes an incorrect function.
The posthoc bias-column normalization returns canonical score -1.0 in both representations.
