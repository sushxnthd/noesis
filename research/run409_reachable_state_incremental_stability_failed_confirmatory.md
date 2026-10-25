# NOESIS R409 — reachable-state perturbation: frozen confirmatory primary FAILED

**2026-10-25.** One kernel: causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. This is the SECOND incremental-stability mechanism attempt after failed R408. The R409 pilot passed its frozen feasibility criteria, but the fresh holdout **FAILED its conjunctive primary**; the mechanism is retired as a proposed cross-task readout-retention explanation. No publication-grade discovery or general stability theorem.

## Frozen-before-outcome protocol and fresh models

Separate pilot design SHA256 `c12b232e14d272853fc7fab78a67bcdc9f655806d2e0e5a267a312afdea58c5a`; protocol `490bb5df98d71b7378303afb6f68f51727ddd851db7eaeab3b2c14d55f9c5e26`, both frozen before 36 fresh networks trained (LSTM/GRU/MGU-style, two tasks, six shared seeds 99780–99785, 85 Adam updates, 196 length-eight training strings). Pilot feasibility passed.

**Fresh confirmation** design SHA256 `9a037f451c5c7f7464115146625e7019465f3160a20fcfeabd5437ac6e100c67`; protocol `89d7b25df72b914523283a34332fa65d6716aacc01524d8a61944ed58b396529`, both frozen before training 48 NEW models with eight disjoint shared seeds 99800–99807. Fresh prefixes and 24-bit neutral words disjoint from pilot. All models intention-to-treat. Six architecture/task groups represented; all models >=95% short accuracy.

Two distinct length-14 prefixes reach the SAME complete symbolic DFA state from exact zero. Reset a trained network's full recurrent state after one prefix to the exact state reached by the other prefix, holding serialized weights, future 24-bit neutral word and suffix1 oracle fixed. Compare against a hash-frozen Rademacher off-manifold reset matched in initial infinity norm. Include local scaled secant and random-direction controls at eps=2^-8 and 2^-2, explicitly **not** claimed reachable. The neutral word pairs match overlapping 1..5-grams and four-bit boundaries. Primary estimand is mean `log10(gain_off(n1)/gain_reachable(n1))` with gains normalized by identical initial infinity norm.

## Frozen outcomes — CONFIRMATORY PRIMARY FAILED

| | Pilot task A | Pilot task B | Confirmation task A | Confirmation task B |
|---|---:|---:|---:|---:|
| Eligible contexts | 216 | 432 | 288 | 576 |
| n0-equal, new n1..64 class-divergence contexts | 19 | 63 | **11** | 89 |
| Event seed IDs | 6 | 6 | 6 | 8 |
| Event architectures | 3 | 3 | 3 | 3 |
| Seed-cluster mean log10 off/reachable n1 gain | +1.303766 | +0.749068 | +1.823123 | +0.674726 |
| Exact one-sided seed signflip p | .015625 | .015625 | .00390625 | .00390625 |

Confirmation required **>=12** task-A new class-divergence contexts. Observed **11**, so the frozen **conjunctive primary FAILED** despite passing all other gates (>=2 architectures and >=4 seeds per task, >=+.20 mean log10 gain, exact p<.01, all six architecture-task mean effects positive). No threshold retuning, no posthoc promotion of latent secondary.

**Crucial distinction:** Task A had ZERO genuinely reachable-state readout-divergence cases in both cohorts; all its qualifying events arose from the off-manifold arm. Task B had 28 pilot and 34 confirmatory genuinely reachable-state class divergences. Thus latent attenuation does not establish cross-task retention failure or an invariant neural automaton.

## Independent audits, raw recovery, mathematical boundary

Independent stdlib symbolic/NumPy checks verify all 648 pilot and 864 confirmation contexts, including complete DFA-state equality, exact neutrality, 1..5gram matches, oracle and infinity-norm matching. All 18 frozen outcome-selected cases (54 arm traces) agree through n0..2 across independent pure NumPy, original Numba, and 120/160/220-digit pointwise recurrences with exact serialized binary64 weights. Nine confirmatory selected cases also have independent Torch autograd Jacobian checks (max Torch/Numba n1 state difference 1.28e-14). **No directed interval proof; late n512 float64 not high-precision arbitrated.**

The confirmatory evaluator was interrupted. Original raw had 840 keys despite 864 saved context rows. A separate recovery script recomputed ONLY the missing 24 raw cases from seed99805, independently matching their existing row metrics; both original and recovered shards are preserved. Independent complete raw audit confirms 864 unique keys and **216** late contexts. The original analysis erroneously counted 210 late contexts; corrected count is 216*513*3=**332,424** long-horizon phase-arm classifications, with original erroneous output retained and frozen primary unchanged.

An exact-rational counterexample: `F(x,y)=(x/100,y)`, reachable displacement `(1,0)`, off-manifold norm-matched displacement `(0,1)` yields off/reachable gain ratio **100**, even for a one-state DFA with constant readout and zero retention errors. Hence a large attenuation ratio does not identify learned DFA memory. Classical affine fact, not novel.

## Reproducibility and next direction

Complete **63-entry** SHA256-verified local archive `/mnt/data/NOESIS_R409_Reproducibility.zip`, archive SHA256 `77d55769732e55a15f785d438b8aa348b3ca3fbfb59bb8aa81920a62a01dd7fe`. It includes 84 fresh network checkpoints, all raw/negative trajectories, frozen protocols, scripts, independent checks, error logs, recovery and immutable R408 dependency ZIP. **Raw/checkpoints are not on GitHub.**

**Decision:** R408+R409 two failed incremental-stability primaries => CHANGE mechanism. Next test should use a *randomized training-objective intervention*: explicit full-DFA-neutral invariance regularization versus compute/token/gradient-matched placebo, with a separately frozen pilot and fresh confirmatory models across both tasks/three architectures. This is not single-coordinate repair, edge-coverage ablation or gate-gradient masking. Freeze all methods and thresholds before new outcomes. No user spending, no user's laptop.

**Repository constraints:** only existing `research/kernel-001-causal-generalization` branch and existing OPEN/DRAFT PR #22; no new branches/PRs, force-push or merge.
