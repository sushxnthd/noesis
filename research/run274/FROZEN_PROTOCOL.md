# NOESIS K001 Run274 — frozen retrospective exact audit
Frozen before full exact proof sweep on 2026-10-20. This is a retrospective re-analysis of previously trained Run273 checkpoints, NOT a newly prospective training experiment. No retuning of Run273 predictions.

1. Question: Do matched sampled-perfect gradient-trained networks separate into unrestrictedly correct baseline models and provably incorrect adverse-regularized models?
2. Primary frontier: Ryou et al. CAV 2021 (RNN polyhedral verification); Van Rossem and Saxe ICML 2025 (algorithm-development transitions). Existing verification and transitions constrain novelty.
3. Scalar exact success: >=12/18 matched epoch-500 sampled-perfect seed pairs have independently checked full-alphabet positive baseline induction AND all-future SET HOLD^n RESET adverse failure proof.
4. Competitor: engineered positive RESET gain is sufficient to force failure; this is not a spontaneous learning law.
5. Cheapest falsification: exact dyadic proof of all 36 stored checkpoints, with independent SymPy checker and corrupted-certificate controls.
6. Publishable threshold: prospective non-engineered training and cross-architecture/task transfer with incremental discrimination beyond finite accuracy.
7. Learning relevance: all eight recurrent/readout parameters were optimized by gradient descent; audit actual stored learned checkpoints.
8. Kill: <12 exact separated pairs, a soundness failure, or three consecutive nontransferable attempts.

Two inactive backups: parity task transfer; matched curriculum without adverse regularization.
The original Run273 prediction miss remains a negative result and is not rescored. No main-branch merge.
