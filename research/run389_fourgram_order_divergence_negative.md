# NOESIS R389: Four-gram-matched neutral-map order divergence (24 October 2026)

**Scientific decision: FROZEN CONJUNCTIVE PRIMARY FAILED.** This is a substantive, prospective, fresh-seed experiment on the ONE existing causal DFA-state-retention kernel. Do not infer a novel general law, publication readiness, or certified n256 invariant basins.

## Frozen design and execution
- Frozen exact four-gram-matched neutral-word design SHA256 `cd689625d3517a80154b9c31f120b1fa5858d8d4862b48e2409e9979a21da336`.
- Frozen pretraining protocol SHA256 `1c2f62df2833ac548cd27967b9213db5e5e2b96485fdcef7310e52fe8817e6e0`.
- Frozen features **before n>=2 outcomes** SHA256 `2670e60ec6901bbf124c112c1e4959bbbce9bcabc85a8025afc41b2bd988877f`.
- Separate pilot: old R388 checkpoints and disjoint 4-gram-matched words; zero n1-equal/n256-different cases among 384 task-B pilot pairs. Pilot never pooled with holdout.
- Trained 96 NEW networks, 16 shared seeds per architecture/task, LSTM width5/258 parameters, GRU width6/273, explicitly implemented MGU-*style* single-gate width7/248. Identical 196 realized length8 training strings and 160 Adam updates per shared seed. 95/96 short-perfect; all retained intent-to-treat.
- 2,592 paired word-order cases (5,184 trajectories) through n512; each u,v 12 bits, exactly six ones, six transitions, same first/last three bits, identical 4-gram histogram; uv/vu have identical 1–4 gram histograms and preserve the complete symbolic DFA state. Pure-Python checker 2,592/2,592 passed.

## Primary results (conditional on EQUAL n1 suffix-1 classes)
| Task | LSTM | GRU | MGU-style |
|---|---:|---:|---:|
| count-ones mod3 | 0/288 | 0/288 | 2/287 |
| count-'01' mod3 | 3/513 | 0/572 | 7/561 |

Task-B pooled 10/1,646 = 0.608%, four shared training-seed blocks; descriptive 16-seed-block bootstrap 95% CI [0.117%,1.313%]. All first new order disagreements arose by n2 or n3, not at n256. The projected local Jacobian/cocycle forcing predictor AUROC was LSTM **0.668**, MGU-style **0.992**, GRU undefined (zero positives); raw commutator AUROC LSTM **0.951**, MGU-style **0.843**. Thus the proposed architecture-independent projected predictor FAILED its frozen >=0.80 LSTM gate and control superiority. Pilot-q75 versus q25 projected-score exact 16-shared-seed one-sided signflip p=**0.5** for LSTM+GRU. MGU pilot quartiles were not available, an explicitly recorded protocol weakness; do not invent them after holdout.

## Independent numerical evidence
- NumPy versus Numba float64: **82,917/82,944** sampled classifications agreed, 27 discordances concentrated in four model-prefix-word cases. Late discordances beyond n256 were not fully arbitrated.
- **All 12** n1-equal/n256-different cases (3 LSTM task B, 7 MGU-style task B, 2 MGU-style task A) retained their n256 labels at **120 and 160 decimal digits**. Four unique implementation-discordant cases were additionally arbitrated at **120/160/220 digits** through n256. Among 10 float64-discordant sampled classifications through n256, high precision sided with Numba 7 times, NumPy 2 times, and neither once.
- Two outcome-selected LSTM/MGU-style n512 witnesses converged at 160/220 digits.
- Conditional `mpmath.iv` directed interval certificates at **n2** established different classes for one LSTM (2 vs 1) and one MGU-style (0 vs 2) witness, conditional on the interval backend soundness. Naive n256 interval propagation failed with wrapping/overflow; **no n256 interval certificate or invariant-set theorem**.

## Interpretation and next direction
The observed n1-equal order divergence prospectively appears in two independently trained architectures and, for MGU-style, both tasks, under exact 4-gram matching; all such divergences begin by n2/n3. This is a bounded empirical phenomenon, not a long-latency algorithm-acquisition law. Retire raw commutator magnitude/cocycle projection as the flagship predictor of late retention; remain within the same kernel and prospectively study minimal distinguishing word horizons and neural transition-semigroup quotient identities, with independent interval-verified finite-horizon counterexamples and stronger long-horizon certificates.

Primary prior art includes Weiss et al. 2018, Dan et al. 2022, Muškardin et al. 2024, Buitrago & Gu 2025, Brandoit et al. arXiv:2609.32447, Oliva & Lago-Fernández 2021 and classical transition monoids. No novelty claim without further audit.

## Reproducibility
**Complete local 97-file archive:** `NOESIS_R389_Reproducibility.zip`, SHA256 `136b84a4b733067003927cb3b865c6b03f8f471c053ffe2dcf779c8cf8a00d48`. Includes frozen protocols, 96 serialized checkpoints, complete 2,592-case raw trajectories, pilot, independent recurrence/checker, selected 120/160/220-digit arbitration, two n2 interval certificates, exact seed-block statistics, figures, source, negative results and manifest. **Raw evidence is NOT uploaded to GitHub.** Only this scientific summary is committed on the existing branch; existing draft PR #21 remains unmerged.