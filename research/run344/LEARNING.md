# LEARNING ledger — Run 344

The original gradient-trained seed 31089 was evaluated without altering its recurrent parameters.

Epoch 140: 8190 of 8190 words through length 12 are correct. Training BCE is 0.01630776129933451. A rational affine readout separates the five selected long words.

Epoch 141: 8190 of 8190 words through length 12 remain correct. Training BCE falls to 0.01622239818863201. Exact hidden-state geometry makes the same five long words incompatible with any affine readout.

Epoch 200: an affine readout succeeds through length 14, but no affine readout can succeed through length 15.

The experiment is retrospective, not a prospective prediction. The observed optimizer step changes long-horizon representational separability while leaving bounded correctness unchanged. This is not proof of a universal law.
