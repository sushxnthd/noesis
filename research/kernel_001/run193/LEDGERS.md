# NOESIS Kernel 001 — Run 193

## THEORY ledger
**Established (post-hoc):** For the unchanged Adam-trained seed-163 width-8 tanh RNN, epochs 300 and 600 have identical classification signs on every nonempty binary word of length <=16 (131070 words). The first disagreement is length 17, where exactly 2 of 131072 words disagree. All 262142 words through length 17 were evaluated with outward-rounded interval arithmetic using exact binary64 checkpoint parameters. Two witness logits were independently checked by directed 80-digit Decimal intervals.

**Important limitation:** This is exact finite minimization, not an all-length algorithm certificate, model-agnostic law, or prospective predictor. Run 192 independently established unary infinite divergence for this same checkpoint pair. The current two witnesses are both repaired by epoch 600.

## LEARNING ledger
Training checkpoint pair: seed 163, epochs 300 and 600, width-8 tanh RNN, Adam on length-six parity; same original weights as Runs 191–192. Training loss decreased 0.050327 to 0.045215 while all classifications through length 16 remained identical. At length 17, epoch 600 fixes exactly two final-token errors and changes no other classifications. These two sequences had correct earlier prefixes at both checkpoints. Broader length-128 random generalization worsened in Run 192; local repair does not imply algorithm acquisition.

The first separating length was screened in float64 before exact checking. This is not a prospective discovery. A random uniform length-17 test hits a changed classification with probability 2/131072; independent draws need 196327 samples for 95% chance of at least one hit.

## Wildcard anomaly probe (post-hoc)
Both separating words contain a run of at least nine zeros. Only 1280 of 131072 length-17 words have such a run, a 102.4-fold smaller search space. This motif was identified *after* inspecting witnesses and has no validated predictive value.

## Failed hypotheses and provenance
No claimed all-length parity acquisition. The proposed use of finite-horizon classification agreement as a retention diagnostic is falsified by Runs 192–193. GitHub draft-PR creation returned a safety-check block twice; do not claim a PR exists. Remote research-specific CI state is pending independent confirmation. Preserve any future failures.

## Primary-literature boundary
Van Rossem and Saxe, ICML 2025, 'Algorithm Development in Neural Networks: Insights from the Streaming Parity Task' already studies gradient-trained RNN parity acquisition and representational mergers. This one-trajectory counterexample is not claimed novel.
