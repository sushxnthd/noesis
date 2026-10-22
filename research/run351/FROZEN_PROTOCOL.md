# NOESIS Run 351 — prospectively fixed coordinate-18 transfer falsification

Frozen before any Run351 intervention evaluation. Source cohort: original Run348 gradient-trained width-three ReLU prefix-parity trajectories (training seeds 32000–32191), generated before this experiment. **Holdout subset is seeds 32000 through 32063 inclusive**, which excludes Run350 seed 32135. No Run351 intervention outcomes have been inspected when this protocol is committed. These are previously trained, not newly trained networks; this is a prospective *intervention-analysis* protocol, not prospective training.

## Mechanistic hypothesis
Run350's causal repair was unique to input-zero bias parameter index 18. Test whether the same specific coordinate is a transferable lever for finite-range generalization in other gradient-trained networks, instead of a seed-specific accidental coordinate.

## Frozen selection and intervention
For each of 64 seeds, select the earliest epoch t in [0,199] whose recorded training accuracy is exactly 1.0. If none exists, retain seed as ineligible with reason, do not substitute another epoch. Use original checkpoint p_t and p_(t+1) (28 double-precision parameters: 18 transition weights, 6 transition biases, 3 output weights, 1 output bias). For each coordinate j in [0,23], replace only p_t[j] with p_(t+1)[j]; retain all other parameters including original readout. Also evaluate baseline p_t and full p_(t+1). Never tune parameter choices or seeds against results.

## Frozen test family and labels
Reuse the *unchanged* Run350 words_gen generator: all binary strings length 1–10 plus four structured zero-run families, restricted to length <=23; exactly 2644 unique words sorted (length, lexicographic). Label is XOR parity of all input bits. The original output head predicts odd iff logit > 0; a zero logit is incorrect (strict margin).

## Scalar primary success
For each eligible seed, define G_j = number of correctly classified words for single-coordinate intervention j minus baseline count. Count a seed as a **coordinate-18 unique-transfer success** iff G_18 >= 27 words (at least ~1% of 2644), G_18 > G_j for every j != 18, and an independent exact-rational evaluator verifies the 2644-word count for that seed's baseline and coordinate-18 intervention. Primary scalar N = number of qualifying seeds among the 64 fixed seeds. Success iff N >= 3. Any ties fail uniqueness. Missing/unreadable checkpoints count as infrastructure failure, not a success.

## Secondary and safeguards
Report all 64 seeds, first training-perfect epochs, baseline/full-step and all 24 single-coordinate counts, ties, largest gains, regressions on the exhaustive length<=8 subset, and comparisons with other coordinates. Independent checker must use exact binary64 rational parameters and separate evaluation implementation on all *claimed successful* cases. For no-success outcomes, independently exact-check the best apparent candidate and at least one coordinate-18 regression, where available. For any apparent perfect finite-family repair, seek a longer adversarial counterexample before discussing algorithm acquisition. Do not claim unrestricted correctness from finite scores.

## Competing explanation and falsification
Strongest alternative: Run350's coordinate 18 was a geometry-specific, retrospectively selected repair. N<3 falsifies the pre-registered cross-seed success claim; N=0 especially argues against transfer, but does not prove no coordinate-18 intervention can help elsewhere.

## Thresholds and kill
Publishable only after an independent exact checker, causal comparisons, stronger spoof checks, a primary-literature priority audit, and a mechanism-derived unseen prediction. Learning relevance is original gradient-trained checkpoints, with actual next-step gradient-update coordinates. This is the second independent test of coordinate-specific transfer after Run350; if it fails, demote/kill the specific-coordinate hypothesis rather than stretching it. The broader Kernel 001-S remains active only if a representation-robust diagnostic is formulated with a falsifiable independent correctness endpoint. No claims of a general algorithmic law.

## Infrastructure
Use isolated branch research/kernel-001-run351-bias18-transfer, persist code, protocol, hashes, all outcomes, checker, tests, CI state, and THEORY/LEARNING ledgers; draft PR, no main writes. Zero paid compute or user laptop.
