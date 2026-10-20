# NOESIS Run300 — prospectively frozen negative diagnostic transfer (2026-10-20)

New gradient-trained width-three ReLU recurrent persistent-latch cohort: 384 seeds (22200–22583). Epoch-20 early-score SHA256 `aad9098f97fbffba02c54cd468477b90b229c95da4ef93771ee52cc7cce3bb40` was committed **before** endpoint training/evaluation. Training followed Run297's architecture, data generation, initialization, and Adam parameters.

## Frozen outcome (PASSED falsification criterion)

| Outcome | Value |
| --- | ---: |
| Exact all-word certified correct | **17** |
| Independently exact witnessed wrong | **175** |
| Unresolved | 192 |
| Sampled-perfect epoch80 | 227 |
| Sampled-perfect yet exact wrong | 18 |
| ROC-AUC gauge LP (resolved only) | **0.3376470588** |
| ROC-AUC epoch20 negative BCE (resolved only) | **0.9233613445** |
| Frozen Delta = AUC(loss) - AUC(gauge) | **+0.5857142857** |
| 95% stratified bootstrap (2,000 draws, seed300) | **[0.46285, 0.69413]** |
| Frozen threshold | >=0.20 and >=4 positives, >=50 negatives |
| Frozen criterion | **PASSED** |

All 17 positive certificates were verified using an independent rational-arithmetic premise checker; all 175 incorrectness witnesses independently checked using exact rational recurrence. No unresolved network is classified as wrong. The outcome pertains to the exact-real recurrence with float64 stored weights interpreted as dyadic rationals.

**Smallest supported claim:** The previously frozen gauge-normalized box-LP predictor fails to transfer usefully from parity to the persistent-latch task. In this new same-architecture, cross-task cohort, epoch20 training loss substantially outpredicts it for exact unrestricted correctness *among the 192 resolved endpoints*. This is a diagnostic falsification, not a general acquisition law. The scalar-cone certificate is sufficient, not necessary, so verification selection bias remains a serious limitation.

## THEORY ledger
The earlier gauge score cannot be promoted to a model-agnostic algorithmicity measure. Its ranking is worse than chance on this selected task, while early loss is much better. Prior Run292–296 representation spoofs remain additional disqualifications. A task-observable, reachable-state diagnostic would need new independent prediction evidence and spoof resistance. Existing invariant-inference RNN literature is prior art.

## LEARNING ledger
All 384 networks were newly gradient-trained (no post-training parameter edits). Exactly 17 were proven correct on *every finite word* by the Run299 cone proof; 175 were proven incorrect by exact counterexamples, including 18 networks with perfect sampled accuracy. No acquisition transition during training was established; no causal intervention. Architecture family unchanged; task differs from parity.

## Provenance / limits
Frozen protocol commit `414d6b1ec9eb441839a3ed4935739a801e65523a`; frozen early commitment `13eca5ddd2b6951c2890b1ceeb3f6b9718460f25`. Early checkpoint SHA256 `0aa10a00406a6316d2808a7d1424022724c7ce75a5cbbdc741dd0ad44ef2f6a1`; late checkpoint SHA256 `71f384d19e4e5ae95198b6bce2ec35f29f547b166ba293ffae60fe8a2d2d6f8d`. Complete local source/results/checkpoints in the separate research archive. Public CI is required to reproduce full cohort before claiming public replication. The branch remains unmerged.
