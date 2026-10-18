# NOESIS Kernel 001 — Run 236 — FROZEN before holdout training

Status: prospective paired intervention. Pilot is explicitly exploratory and excluded from all confirmatory counts. Branch: `research/kernel-001-run236-saturation-intervention`.

## Mandatory kernel contract
1. **Question.** Does encouraging hidden-state saturation during gradient training increase the incidence of exact all-length algorithm acquisition, rather than only finite-horizon fit, in independently seeded hardtanh recurrent networks?
2. **Primary-literature frontier.** Formal-language generalization, finite-state neural representations and exact RNN reachability are known; saturation regularization may improve finite-state formation. No novelty claim without a fresh priority audit.
3. **Scalar/exact success.** On the 24 unseen 3D paired seeds, at least four net additional all-length certificates with lambda=0.1 relative to lambda=0, and a one-sided exact discordant-pair sign test p<0.05. All certificates independently replayed, zero accepted corrupted controls. Training accuracy mean loss under intervention <0.01 absolute. Report all cases including abstentions.
4. **Competing explanation.** The regularizer merely makes finite-graph certificate discovery easier, while baseline abstentions might also compute correctly at all lengths; no learning change can be inferred without baseline incorrectness witnesses.
5. **Cheapest decisive falsification.** Frozen paired seeds and exact rational reachable-state checker. Fewer than four net certificates or non-significant paired test falsifies the predeclared positive prediction. Any checker disagreement or accepted corrupted control invalidates proof claims.
6. **Publishable threshold.** Independently confirmed baseline-wrong to intervention-all-length-correct paired rescues, mechanism-specific replication across dimensions/task, robust prior-art separation, and public reproduction; no standalone breakthrough from certificate-rate shifts.
7. **Learning relevance.** Actual gradient-trained networks, matched initial parameters per pair, all-length correctness proofs and strict wrong-sign witnesses. Distinguish correctness from certifiability.
8. **Kill condition.** After three substantive failed strengthening attempts, kill/reformulate the intervention claim; do not quietly change criteria.

## Prospective design (immutable)
- Task: ternary reset latch, 0=hold, 1=set, 2=reset; target evaluated at every prefix. Full 729 length-six strings, prefix-wise binary cross-entropy.
- Models: fully coupled hardtanh RNN with symbol-specific matrices/biases, linear readout; 3D primary, 4D secondary. Initial hidden 3D=(0.5,-0.5,0.25), 4D=(0.5,-0.5,0.25,0.125).
- Training: PyTorch float64 CPU deterministic, single thread, Adam lr=0.03, 200 updates, identical initialization within paired arms. Paired lambda=0 and lambda=0.1 applied to 1-mean(abs(hidden)) over all time steps and samples.
- Primary holdout seeds: 3401..3424 (24 pairs, 3D). Secondary unseen architecture seeds: 3501..3512 (12 pairs, 4D). No tuning or exclusions.
- Save exact float64 parameters at epochs 0, 50, 100, 200; independently classify epoch 0 and 200 for all pairs; intermediate epoch classifications as resources allow. Interpret binary64 parameters as exact dyadic rationals.
- Reachability BFS: exact hardtanh clipped affine recurrence, target state and hidden state, strict logit sign; cap 2500 states and depth 15, then ABSTAIN, never classify as negative. Independent integer-dyadic implementation must agree on all CERTIFIED/INCORRECT labels.
- Report: exact certified, incorrect, abstain counts per arm and dimension; paired transitions, baseline-wrong->intervention-certified rescues, finite training accuracy, saturation statistic, graph sizes, negative controls, exact one-sided discordant-pair p-value.
- Negative controls: flip readout sign on first four intervention-certified 3D networks (or all if <4); must be rejected by both checkers. Preserve raw checkpoint JSON, independent checkers, protocols, logs, code, seeds, and negative results.
- Mechanism prediction: lambda=0.1 increases saturation and finite reachable graph closure; it need not improve true correctness. The latter requires explicit paired wrong-to-correct evidence.
- Pilot seeds 3201..3206 and lambda sweep 0,.003,.02,.1 are retrospective exploratory, excluded from primary statistics. Pilot found 0/6 baseline certificates vs 5/6 lambda=0.1, motivating frozen test; no inference from pilot.
- No GPU, user laptop, or paid compute. Do not merge active branch. Open draft PR; CI must reproduce deterministic results where practical.
