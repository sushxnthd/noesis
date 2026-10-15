# Run 184 — cyclic phase transfer

Frozen protocol commit: 8550d653d55909fb168249815996effa776182f2.

One unchanged gradient-trained checkpoint (width 7, seed 409, epoch 200). Prefix 000000, then cyclic rotations of balanced word 1110001001.

Exact-rational all-length proof of first failure clocks for shifts 0..9:

`[null, 186, 87, 57, 87, 186, null, 186, null, 148]`.

Rotations 0, 6, and 8 are correct at all block boundaries for every repetition; seven other rotations fail finitely, although all have identical symbol counts and length. All ten share a verified one-active-neuron invariant region with strictly positive activation margins. Independent 100-digit direct replay through 2048 repetitions agrees.

The existing 32-cycle linear drift baseline predicts failure for all ten, including the three exact all-length passes. This is an in-sample, one-checkpoint diagnostic comparison, not a validated improvement in learned algorithmicity prediction.

Exact proof source and full artifacts retained in Run 184 local reproducibility package pending repository upload.
