# NOESIS K001 — Run 321: frozen delayed-memory census

Frozen before reading Run 321 outcomes. Base: Run 320 branch. Source cohort: immutable Run 315 `checkpoints315.json` and `results315.json` (96 original gradient-trained trajectories, epochs 0/20/80). Do not retrain, relabel or tune to endpoints.

## Single active kernel
1. **Question.** Can exact task-opposed trajectory collisions at previously untested lengths expose finite-range learned heuristics among Run 315's 49 unresolved epoch-80 checkpoints?
2. **Frontier.** Classical automata distinguishability and RNN verification/extraction (Weiss et al. 2018; Jacoby et al. 2020) already establish the obstruction; the learning contribution, if any, is an exact audit of real gradient-trained trajectories. Run 316 supplied one delayed collision at length 11.
3. **One exact success criterion.** At least ONE formerly unresolved epoch-80 checkpoint has `h(0^n)=h(1 0^(n-1))` for some integer `11 <= n <= 64`, using exact binary64 rational arithmetic, with independent checker confirmation.
4. **Strongest alternative.** The restricted two-word family is unrepresentative; failure to find a collision is not a correctness certificate. A discovered collision may be an expected ReLU reset, not a novel acquisition law.
5. **Cheapest falsification.** Scan these two words for n=1..64 for all 96 epoch-80 models and epoch-20 controls; stop at first exact collision per model, preserve all outcomes.
6. **Publishable threshold.** Replication on an independent held-out training cohort, predictive acquisition timing beyond loss, architecture/task transfer, priority audit, and independent proof checker.
7. **Learning relevance threshold.** At least one previously unresolved *original gradient-trained epoch-80 checkpoint* gets an exact wrong-representation witness at n>=11. A reparameterization or post-hoc readout edit does not count.
8. **Kill condition.** If zero new late unresolved obstructions appear, reject this narrow probe as a useful endpoint resolver; after three failed strengthening attempts reformulate active kernel.

## Exact method
Parse every parameter with `Fraction.from_float(float(v))` as in Run 320. Initialize `h_0=(0,0,0)`. Recurrence `h'=ReLU(A_x h+b_x)`. For n=1..64 compare hidden states for `0^n` and `1 0^(n-1)`. These words have the same length and opposite persistent-latch labels. Equality is a proof that **no deterministic final-state readout** can classify both, including nonlinear/length-aware readouts. Record first collision, full rational states, and hash of inputs. Independently recompute any positives with a separately written exact implementation. No approximate tolerance. Report original endpoint labels separately; do not conflate certificate failure with algorithm failure.

## Interpretation
THEORY: Exact opposite-label collision obstructs every deterministic final-state readout. Absence of a collision on this path implies nothing beyond the tested family/horizon.
LEARNING: Compare epoch 20 vs 80 on the same trained seeds, but do not claim prospective prediction or natural acquisition from a retrospective census.

## Provenance
Run 320 fixed-cone canonicalizer rejected all four previously certified positives, so do not use it as a general diagnostic. Preserve failures. No GPU or personal spend. Branch `research/kernel-001-run321-delayed-memory-census`; PR draft if permissions allow.