# NOESIS Runs 368–369: gate-controlled retention–transition trade-off

**Research date:** 2026-10-23  
**Status:** controlled within-checkpoint causal intervention and prospective new-cycle replication; not a publication-level novelty claim.

## Protocol

Run368 protocol SHA256: `08b49b4034e26ad03e5d1bc9d64cebdfede3ac1a8c6b0450cd835b78b001dad7`. Run369 protocol SHA256: `f861ba39cced062c22703a81e1bf503d4a5eccae1c3dd7695ce3a9eb288d9ab4`.

On fixed, previously trained CE-matched GRU checkpoints, branch identical hidden states at 32 complete neutral cycles. Only after that point, shift all update-gate logits +4/-4 or reset-gate logits +4/-4. Training data, hidden width, weights, optimizer trajectory, readout, short-training CE and initial n32 state are identical across variants. There are 40 confirmatory seed models per task, with predeclared eligibility (at least two of three correct prefixes at n32). Outcome is retention of previously correct labels at n256.

## Run368

| Task/cycle | Eligible seeds | Baseline | Update +4 | Reset +4 | Update +4 vs baseline (seed-bootstrap 95% CI) |
|---|---:|---:|---:|---:|---:|
| Ones mod3, 0 | 38 | 73.6% | 93.4% | 68.1% | +19.8 pp [+13.0,+26.6] |
| Ones mod3, 111 | 39 | 94.0% | 33.3% | 80.3% | -60.7 pp [-66.7,-53.0] |
| Count-01 mod3, 1 | 27 | 78.3% | 95.0% | 56.7% | +16.7 pp [+8.6,+24.6] |
| Count-01 mod3, 0 | 30 | 75.4% | 95.4% | 75.4% | +20.0 pp [+11.1,+29.2] |

Both predeclared primary identity-symbol comparisons passed. The neutral three-symbol cycle provided a decisive negative result: increasing gate persistence can severely harm state tracking when the *whole word* is neutral but its constituent symbol transitions are not.

## Run369: prospective new neutral-cycle prediction

After Run368, but **before opening Run369 outcomes**, we froze a prediction that update +4 would reduce retention by >=20 pp on both new nontrivial neutral words:

| New cycle | Eligible seeds | Baseline | Update +4 | Reset +4 | Difference (seed-bootstrap 95% CI) |
|---|---:|---:|---:|---:|---:|
| Ones mod3, 1110 | 39 | 100.0% | 31.5% | 86.5% | -68.5 pp [-71.2,-66.1] |
| Count-01 mod3, 010101 | 35 | 96.1% | 30.4% | 78.4% | -65.7 pp [-71.4,-59.2] |

Both prospective tests passed. These are new *conditions on existing trained cohorts*, not fresh independently trained model replications.

## Verification and numerical caveat

Run368: 160 independent PyTorch float64 replays, 0 n256 prediction discrepancies, 1 n512 discrepancy. Run369: exhaustive 480-case independent PyTorch primary crosscheck, **7 n256 disagreements**, all in the unmodified count-01 baseline, concentrated in 3 numerically sensitive models. Under PyTorch the eligible count-01 baseline retention is 99/102 instead of 98/102, while update +4 stays 31/102, leaving a -66.7 pp difference instead of -65.7 pp. An independent 70-digit witness verifies seed 36024 on the 111 cycle: all three baseline classes survive at n256, whereas update +4 collapses them to class 2.

The elementary 3-state toy transition B_z=zI+(1-z)P with P^3=I has nontrivial spectral squared modulus 1-3z(1-z). A word-level identity can therefore conceal nontrivial state-changing transitions. This is classical algebra, not a novel theorem, and it does not by itself explain the nonlinear GRU quantitatively.

## Smallest defensible claim

For these two formal-language tasks and fixed GRU checkpoints, an inference-time update-gate shift causally improves finite-horizon retention on identity-like neutral symbols but sharply degrades it on nontrivial neutral cycles, including two prospectively frozen new-cycle predictions. This does **not** establish that gating caused the original GRU–Elman architecture gap, prove all-length correctness, or establish publication novelty.

**Next gate:** a predictor computed from learned transition maps that forecasts benefit/harm before unseen cycle outcomes; compare against short CE, d32, readout margin, Jacobian and state coverage; validate on new independently trained cohorts and a third architecture; then intervene during training.

**Reproducibility:** full local archive `NOESIS_R368_R369_Causal_Cycle_Tradeoff.zip` (32 files, verified SHA256 manifest), including checkpoints, frozen protocols, raw results, independent checkers, high-precision witnesses, and vector figure. Archive has not yet been added to this repository.
