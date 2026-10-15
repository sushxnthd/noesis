# NOESIS Kernel 001 — Run 165 frozen protocol (before new-family evaluation)

## Question
Can a task-coupled, frozen-activation affine-cycle extrapolator detect repeated increment/decrement cancellation failure in unchanged gradient-trained ReLU counters, better than local one-cycle error?

## Data and holdout
Two archived 14-model cohorts from Run 161/163, unchanged parameters. Seeds 224, 226..238. These checkpoints have previously been assessed for neutral suffixes, **not** for this cancellation-cycle family; do not claim an unseen-model holdout. SHA256 of each checkpoint will be included in outcomes.

## Task, execution, and label
Starting at zero, feed six token-0 increments. Apply (0,1) cycles (token 0 increments, token 1 decrements). Correct count is 6 after each complete cycle. Float64 NumPy execution. Label positive if any complete cycle among 1..1024 has |w^T h - 6| > 0.1. Evaluate both cohorts independently. No model fitting.

## Frozen primary diagnostic
Compute h0 after six increments, hmid after one 0, hpost after subsequent 1. Freeze the two observed ReLU masks (pre-activation positive coordinates). Derive the *affine two-step map* F(h)=M h+b using these masks; no observed future cycle states are used. For k in {1,2,4,8,16,32,64,128,256,512,1024}, calculate F^k(h0) via binary exponentiation of the augmented affine matrix (dimension width+1), then score max_k log(1+|w^T F^k(h0)-6|). This is a local linearization extrapolation, not a certified reachable-set bound. If any computation overflows, record infinity (highest risk). Preserve mask violations observed later.

## Baselines and threshold
Baselines: abs initial readout error, abs one-cycle readout error, train MSE. Report tie-aware ROC AUC for each cohort, all 28 raw records, confusion at frozen score cutoff log(1.1). Primary SUCCESS iff AUC >=0.80 in BOTH cohorts AND improvement >=0.05 over one-cycle-error AUC in BOTH cohorts. Otherwise FALSIFIED for this setting. If no positive/negative in a cohort, criterion fails as unevaluable. No post-hoc threshold tuning.

## Strongest competing explanation
The score may simply magnify pre-existing readout error or train MSE, and fixed masks may break, yielding false alarms. Compare baselines and mask switches.

## Cheapest falsification
Run 28 archived models, 1024 two-token cycles each, and an independent direct-cycle implementation. No training or paid compute.

## Publishable threshold
Not met by AUC alone: requires independent training cohorts, unseen architecture/task, independent checker, a mathematically sound sufficient condition or carefully scoped predictive result, and primary-priority audit.

## Learning relevance
Every scored system must be an unchanged gradient-trained checkpoint. A successful score must predict unseen-family failures in BOTH cohorts, not only a hand-designed spoof.

## Kill condition
Primary criterion fails; after three substantive attempts without a diagnostic advance, reformulate active kernel rather than continue metric search.

## THEORY ledger
Affine frozen-mask composition is exact only while masks remain fixed. No all-length certificate claimed.

## LEARNING ledger
One new task-family evaluation on existing gradient-trained checkpoints; label frozen before inspecting cancellation outcomes.

## Primary literature frontier
El-Naggar et al., PMLR 217 (2023), https://proceedings.mlr.press/v217/el-naggar23a.html — exact single-cell ReLU counter conditions and empirical nonacquisition.
El-Naggar et al., EACL SRW (2023), https://aclanthology.org/2023.eacl-srw.15/ — linear counter indicator conditions.
Korda (2021), https://arxiv.org/abs/2102.02273 — stability/verification of neural-controlled systems, complexity caveats.
