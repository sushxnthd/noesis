# LEARNING ledger — Run 343

Run342 trained 128 width-four ReLU RNNs on length-eight parity; at epoch 200, 88 were classified correct on all binary inputs through length 12. Run343 made **no changes** to weights or training. Frozen search of these 88 networks at lengths 13..16 tested 10,813,440 new model-word pairs. Seed 31089 failed at length 13; 87 had no observed failure through length 16.

The seed-31089 trained checkpoint is exactly correct on all 8190 words of lengths 1..12 and wrong on every `1 0^k`, k>=12, by an exact failure invariant. Thus the Run342 independent endpoint was a bounded-generalization proxy, not a ground-truth algorithm-acquisition label.

No claim that learning crossed an acquisition transition in Run343; this is an evaluation failure mode for an original gradient-trained model. No additional network training or user compute. All search outcomes and selected model weights are committed; the complete Run342 cohort remains in the prior archived provenance.

Failure counter: Run342 proof-deficit predictor independent transfer failed; Run343 supplies a decisive exact counterexample, not a second failed predictor.
