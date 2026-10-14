# NOESIS Run 149 THEORY / LEARNING ledgers

## THEORY
An outward-rounded binary64 interval enclosure proves that a *modified* frozen four-state ReLU recurrence with neutral-only hidden coordinate 3 set to zero has maximum task error <= 0.007240039268581634 on every ternary word of length <=13, with binary32-stored weights interpreted as exact real parameters. This is a finite-horizon statement only. Independent rational arithmetic proves that the same intervention fails for trained seed 210 on word 02 with error -0.9999035132247276. Thus hidden-coordinate-index interventions are not model-agnostic.

Primary literature: El-Naggar et al. (2023) https://proceedings.mlr.press/v217/el-naggar23a.html ; https://arxiv.org/abs/2211.16429 ; thesis https://openaccess.city.ac.uk/id/eprint/33010/. Novelty unestablished.

## LEARNING
All checkpoints 210,214,215 were obtained by gradient descent before this run and were not retrained. Seed214 original maximum length-13 error 0.11199123726426041 (two failures); neutral-only coordinate3 clamp maximum <=0.007240039268581634 (zero failures). Clamp coordinate0 or1 worsens seed214; clamp coordinate2 unchanged. Seed210 original maximum error 0.00011241967176900403, but clamp3 fails at length2 and reaches 11.999373765633408 error at length13. Seed215 unchanged under clamp3. Therefore a mechanism-specific local rescue does not transfer to independent trained checkpoints. No unbounded task algorithm acquired.

## Eight-field active kernel
1. Question: Can an all-alphabet task-coupled inductive reachable-state diagnostic extracted from trained networks predict failure without fixed hidden-coordinate assumptions?
2. Frontier: ICGI 2023 single-cell counter indicator conditions; neural reachability verification; no novel law claimed.
3. Criterion: >=25% reduction in median absolute worst-case first-failure prediction error vs frozen training-loss baseline on >=8 prospective checkpoints and >=2 architectures.
4. Competitor: training loss or finite validation already predicts generalization.
5. Falsification: freeze diagnostic, enumerate unseen trained checkpoints and adversarial spoof controls.
6. Publishable threshold: independent exact checker, priority audit, prospective frozen evidence, >=2 architectures, bounded claim.
7. Learning relevance: incremental predictive or causal effect in gradient-trained networks.
8. Kill: three substantive tests without incremental predictive value or exact spoof defeating claimed sufficiency.

Fixed-index neutral clamping retired as a general intervention. No active backup kernels.
