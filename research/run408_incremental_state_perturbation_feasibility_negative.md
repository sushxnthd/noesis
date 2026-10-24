# NOESIS R408 — prospective neural-state incremental-stability pilot: frozen primary failed

Date: 2026-10-25. Kernel: causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. This is the FIRST failed incremental-stability mechanism pilot, not a general theorem or publication-grade result.

## Prospective freezes and new data

Symbolic design frozen BEFORE fresh training SHA256 `4bf6427732ba637d3c27087528f767e0f635a29024d0fa71ac4a09feaaf6e49c`; protocol frozen BEFORE fresh training SHA256 `49c7fe4a69b157a6d88f9b8838776941132628659d12ce99895b6d5a5ac06cf9`. Trained 24 fresh LSTM/GRU/MGU-style models across BOTH DFA tasks and four disjoint shared seeds 99760–99763, 70 Adam updates, 196 length-8 strings; 22/24 short-perfect, all 24 >=95% short accuracy, all ITT. New unseen 20-bit full-state-neutral word pairs match exact overlapping 1..5-gram counts and four-bit boundaries; all complete states, 10/14-bit prefixes. The causal comparison uses the exact SAME word, weights, oracle and prefix, changing only a frozen signed full recurrent-state perturbation after the prefix (epsilon 2^-12, 2^-5, 2^-1; 2 directions x 2 signs). Such perturbations may be off-manifold.

Evaluated 10,368 perturbation/control pairs through n64, preserving 1,347,840 paired classifications. An independently preselected 864 pairs were also evaluated through n512 (886,464 classifications including repeated early phases). Complete raw trajectories, negative cases, fresh checkpoints and all sources are archived.

## Frozen conjunctive feasibility result — FAILED

Task A: 78 n0-class-equal first n1..64 classification-divergence cases / 3,456 eligible pairs, all three architectures and four seeds. But n1 amplification gain >=1.25 in only **157/3456=4.5428%**, below frozen **10%** minimum. Task B: 394 n0-equal class divergences / 6,912 eligible pairs, n1 amplification **706/6912=10.2141%**, all three architectures/four seeds. All other frozen gates passed. Because task A fails, the conjunctive PRIMARY FAILS. No threshold retuning, no confirmatory cohort, and no secondary predictor promotion.

## Independent checks and mathematical limits

Independent stdlib DFA/Counter checks: 90 exact 1..5-gram, 18 boundary, 72 neutral/oracle checks passed. All 10,368 rows independently reconciled to 9,792 initial raw + 576 recovered raw cases, zero duplicates, all 9,896 negative cases preserved, 864/864 late-to-early phase checks passed. Frozen-after-outcome HP selection SHA256 `8e5ecb6fe70ed75bb0723d6c82f41829e418cbe2d3ee9edb3f51abf571fc8321`; 12 selected positive/negative cases agree NumPy/Numba and 120/160/220-digit pointwise through n2, maximum HP-vs-Numba selected margin difference 8.74e-14. These are NOT directed interval certificates. Independent Torch autograd at 24 separately selected points gives median local directional-derivative relative error 0.000848, max 0.01764; not a uniform bound.

Classical global infinity-Lipschitz bounds for GRU/MGU/LSTM gate maps were independently derived and checked against all 10,368 n1 gains, zero violations. However word-level log10 bounds ranged 27.67..131.19, with median **35.24 decimal orders** of slack. Thus the valid algebraic bounds are quantitatively useless for learned contraction certification; parameter constants were computed in float64 without directed rounding. No exact-real late-horizon theorem, path-only mediation identification, general stability law or novelty claim.

Evaluator interruption and recovery are preserved: first 9,792 raw pairs persisted; complete 10,368 rows persisted on resume; last 576 raw pairs recovered from frozen checkpoints/design and independently reconciled. Container git transport failed DNS resolution; the GitHub connector is used only to append this scientific note to the SAME branch. No new branch/PR/merge/force-push.

## Reproducibility and next science

Complete **38-entry SHA256-verified local archive**: `/mnt/data/NOESIS_R408_Reproducibility.zip`, SHA256 `dcc59821e7644b4f95d7f679c1c910642ba3b697addc965f3af65b15c22bcd5d`. Archive includes all R408 source, frozen protocols, raw shards, checkpoints, negative results, HP, Jacobian and global-bound checks, logs, recovery, and immutable R407 source dependency. Raw NOT uploaded to GitHub.

R409 should be a SECOND, disjoint, prospectively frozen incremental-stability test. Improve identifiable finite-horizon attenuation versus readout divergence with genuine-prefix-state difference controls, compare n0/n1/n2 margins, short CE, d32 and lexical/length baselines, require BOTH tasks, >=2 architectures and >=3 seeds, exact seed-cluster tests, HP arbitration. If second frozen primary fails, change mechanism. No user spending or user laptop.
