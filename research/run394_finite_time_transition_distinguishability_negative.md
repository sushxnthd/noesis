# NOESIS R394 | Prospective DFA-conditioned finite-time transition distinguishability (negative primary)

**Date:** 2026-10-24. **Kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **Scope:** single existing branch `research/kernel-001-causal-generalization`, draft PR #21. Zero user spend, no user's laptop. No novel theorem or publication-readiness claim.

## Frozen provenance
- Symbolic 16-bit word/prefix design SHA256 `b538fab0c32a713ba3d6c0529251cfa4b31bda8eccb4267fe4566a145071374d`, frozen before pilot.
- Same-/different-complete-DFA-state control design SHA256 `a77911c5ef576c6e3ebcde17caae2cad03b06aeb0d2ba55b3e71e9263966f384`, frozen before pilot.
- Independent archived-R389 pilot, 540 new word-prefix cases, including a **failed/ill-conditioned cross-prefix readout-silent displacement-transfer idea**; raw negatives preserved.
- Confirmatory protocol SHA256 `556e0c0aa8ec92b7255fe1606a49bd1aeae0528c21fe2031f07d9dc7bc921848`, frozen **before 48 fresh networks were trained**. No holdout threshold changes.

## Experiment
48 new LSTM (width5/258 parameters), GRU (width6/273), MGU-style (width7/248) models, 8 shared seeds 95000..95007 across both count-ones-mod3 and count-'01'-mod3. Matched 196 length8 training strings and 160 Adam updates; **47/48 short-perfect**, all retained ITT. For each complete DFA state, compare two distinct same-state 10-bit prefixes with a different-residue, same-previous-bit, symbolically Hamming/ones-matched prefix. Apply the **same** 32-bit neutral word uv to all three learned recurrent states; u/v have matched 1..4-gram histograms and endpoints. Full 0..512 class traces for 1,728 cases (5,184 trajectories), with selected complete hidden/cell coordinates and margins.

Predefined selectivity `S1 = log10[(d_cross(1)/d_cross(0))/(d_same(1)/d_same(0))]` for complete recurrent-state Euclidean distances, numerical floor 1e-14. A positive score indicates more relative contraction of same-state histories than different-state controls under identical inputs, **not** uniform contraction.

| Task | Architecture | N | Median S1 | Fraction S1>=1 | n1 cross oracle accuracy |
|---|---|---:|---:|---:|---:|
| Ones mod3 | LSTM | 192 | 6.7021 | 100.00% | 100.00% |
| Ones mod3 | GRU | 192 | 6.9488 | 99.48% | 96.35% |
| Ones mod3 | MGU-style | 192 | 5.7062 | 98.44% | 96.88% |
| '01' mod3 | LSTM | 384 | 3.4292 | 73.70% | 76.30% |
| '01' mod3 | GRU | 384 | 4.7499 | 86.72% | 92.19% |
| '01' mod3 | MGU-style | 384 | 4.4614 | 89.06% | 89.58% |

Pooled eight-shared-seed mean S1 = **4.89277 log10**, exact one-sided signflip p = **0.00390625**, seed-bootstrap 95% CI **[4.4313,5.3673]**. All six task-architecture median/fraction/accuracy gates passed.

**FROZEN CONJUNCTIVE PRIMARY FAILED:** task-B LSTM seed **95007** had mean S1 = **-0.192**, violating the preregistered positive per-seed mean in every architecture/task stratum. That seed had 99.9362% short-training accuracy, but must remain ITT. No posthoc exclusion, gate adjustment, or success relabeling.

At n256 same-state class agreement on task B was LSTM 98.70%, GRU 96.35%, MGU 96.88%; cross-state oracle correctness 76.04%, 89.06%, 86.46%. Geometric separation **does not certify** readout correctness. Five LSTM task-B rows had late class flips and one differed between n256/n512; these late events lack high-precision arbitration.

## Independent checks
- Pure standard-library DFA checker: **117** neutral word pairs, **468** exact ngram checks, **351** complete-DFA-neutral checks; independently reproduced exact seed p.
- Independent pure NumPy vs Numba: **798/798** selected classifications and **532/532** complete-state distances agree across 19 disclosed sampled/outcome-selected cases.
- Exact serialized binary64 weights, independent mpmath **120/160/220-digit n1** distances: **14/14** selected cases converge and match float64 selectivity, including two negative seed95007 cases.
- Selected n8 labels: **4/4** cases converge at 120/160 digits; one additionally 220.
- **6/6** selected cross-state distinct-class finite-word witnesses conditionally certified with 100-digit `mpmath.iv` directed intervals. **Not** certificates of contraction ratios, n256, attracting invariant sets or unbounded time.
- A direct n256 high-precision attempt **timed out**, with no usable n256 HP result. Seven local Jacobian/cocycle/DMD exploratory calculations are not uniform contraction proofs.

## Smallest defensible claim and next science
This is **bounded prospective three-architecture/two-task replication of finite-time relative synchronization in many cases**, not a successful conjunctive primary, not a new general law, and not a causal isolation of abstract DFA state. Initial neural distances are not exactly matched, and state compression/automata extraction/contraction-separation are well established (Weiss et al. ICML 2018; Merrill & Tsilivis 2022; Dan et al. 2022; Buitrago & Gu ICML 2025; Metric Automata Theory NeurIPS 2025; Brandoit et al. arXiv:2609.32447).

Next: pilot **latent-distance-matched** same-/different-state counterfactuals and test a prospectively non-ceiling **causal effect on oracle errors**, beyond n0/n1 class/margin and local Jacobian baselines, on fresh architectures and unseen cycles. No novelty claim without prior-art audit and validated certificates.

**Full 69-entry local reproducibility archive:** `NOESIS_R394_Reproducibility.zip`, SHA256 `7b2f8cb3161f45f2a89422364343178417f720798717a2d60738d67ddee3b4ee`. Contains frozen protocols, complete raw/checkpoints/source, negative pilot, full traces, independent checkers, exact stats, figures and SHA256 manifest. **Raw archive not uploaded to GitHub.**
