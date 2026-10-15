# LEARNING — Run 184
Checkpoint: Run 181 original gradient-trained width 7, seed 409, epoch 200; train MSE 7.237924895283261e-6. Parameters unchanged. Protocol frozen at commit 8550d653d55909fb168249815996effa776182f2 before evaluating the ten cyclic rotations.
**Observed:** Seven rotations fail by 2048 repetitions (first failures 57..186); three are exactly certified correct for all repetitions. Independent 100-digit Decimal direct replay agrees with all ten clocks through 2048.
**Baseline:** Frozen Run 183 four-point linear forecast from repetitions 8,16,24,32 predicts failure for all ten; 3/10 false-failure predictions. Exact certificate fixes all three *in this selected checkpoint*. Retrospective within-checkpoint comparison, not prospective multi-model superiority.
**Consequence:** Passing an all-length periodic-word test does not transfer even to cyclic permutations with the same symbol multiset. Add phase-rotation adversaries to evaluation.
**Limits:** No new gradient training or training-transition prediction; all ten outcomes correlated within one model. Do not claim model-agnostic algorithmicity.
