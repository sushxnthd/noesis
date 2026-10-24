# NOESIS R401 — second prospective finite-horizon causal error-reachability test: negative primary

Date: 2026-10-24. Kernel: causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **FROZEN PRIMARY FAILED. R400+R401 finite-horizon error-reachability flagship retired.** No novel theorem or publication-grade law.

## Frozen before outcomes
Independent pilot design SHA256 `974c675b3b2976bcb3b82d3668c6eb9a5a459659b707e9ea540bd5819ce05193`; pilot protocol SHA256 `c4f683865d5758834db03aaa8a45c13c74be08fc2116802bc2274be2e9f1176d`. Pilot seeds 99400–99403, three architectures, two tasks, prefix lengths 6/10/14, word lengths 20/40/60, snapshots 20/40/60/80/100. Snapshot 40 passed the frozen **aggregate** pilot feasibility gate (task A 5/624 from one MGU seed; task B 9/365 across three architectures/two seeds), but the signal was fragile. All pilot outcomes and first code crash preserved.

Fresh design frozen before new training SHA256 `ede634c122dc08ffbb7de43fa5f09662031b64bab942aea52f8885d80cebe819`; confirmatory protocol SHA256 `5791e753b8289eec1c331635712cf233342e8c8cb43b0379a7bd624249af221a`. Verification cases frozen before HP/interval SHA256 `10f04d99b10e82b2526d3b59946205100d34a8c3cd23935e6cb6844ebef0189d`. No retuning.

## Fresh prospective holdout
48 **new** LSTM/GRU/MGU-style models (8 shared seeds 99420–99427 × 2 DFA tasks × 3 architectures), matched 196 length-8 training strings and 40 Adam updates; 20/48 short-perfect, all seeds ITT. Three novel prefix lengths per complete state, two fresh exact overlapping 1–5gram-matched neutral word pairs/state, 20/40/60-bit compositions. Same prefix and exact full symbolic DFA state in both arms; individual positions and 6grams not matched.

3,888 paired cases, 7,776 complete n0..512 trajectories, 3,989,088 suffix1 labels. Both arms correct at n0/n1/n2 for 2,021 eligible pairs. **Only 6** new n3..8 error pairs, all arm-discordant: LSTM A 0/423, LSTM B 0/242, GRU A 0/357, GRU B 2/334 (seeds 99424/99426), MGU A 3/285 (seed 99421), MGU B 1/380 (seed 99424). Required >=8 events, >=2 each task, >=2 architectures, >=3 seeds, >=80% arm discordance. All except >=8 passed: **conjunctive primary FAILED**.

Frozen n1/n2 margin-trend risk predictor AUROC .566501 vs strongest frozen baseline min signed n0..2 margin AUROC .737055; advantage −.170554, not +.05. Eight-seed 5,000-replicate bootstrap 95% interval [−.830871,+.116267] (4,865 valid). Predictor's frozen minimum 8 positives also unmet. No posthoc rescue.

## Independent audit
Pure-Python DFA and true overlapping 5gram: 1,134/1,134 final symbolic checks. Initial independent checker incorrectly counted leading 1 as a 01 event; seven false prefix failures, correction and original audit retained. Fused Numba n0..8 matches original for all 7,776 arm traces. Independent NumPy vs Numba on 12 preselected cases: 648 early/late comparisons, **five disagreements, all late n255/256/257/512**; no early disagreement. Do NOT infer exact-real long-horizon labels from float64.

All six positive pairs (both arms) agreed on full exact-zero finite n0..8 labels at 120/160/220-digit precision. Six hash-selected controls checked at 120 digits. Conditional mpmath.iv 100-digit directed intervals certified strict classes for both arms at all six first-error horizons (12/12); complete n0..8 classification only 6/12 positive arms due wrapping. Finite-string certificates only; no invariant-set/attractor theorem, no weight-perturbation robustness.

Complete **89-file** local SHA256-verified reproducibility archive, including ALL source, frozen protocols, raw full traces, checkpoints, negatives, precision disagreements and checkers: `/mnt/data/NOESIS_R401_Reproducibility.zip`, SHA256 `c9f6434d0a3d060d9f653348342e375285e9ff831d6307472a1eb0ebfdce9398`. Raw evidence is **not** uploaded to GitHub.

## Decision
R400 and R401 are two failed prospective finite-horizon error-reachability primaries. **Retire this flagship mechanism.** Next: separate-pilot **exact-real vs finite-precision shadowing under neutral-word transitions**. Freeze a quantitative Jacobian-growth/perturbation/readout-margin predictor and controls before new seeds, compare float32/64 to 120/160/220+ exact-real trajectories, test causal precision intervention, seed-cluster exact inference and independent interval checks. This is classical numerical-analysis territory; no novelty without sharp, cross-task/architecture, prospective validation and prior-art audit.

Repository constraints: only `research/kernel-001-causal-generalization` and authorized draft PR #22; do not create branches/PRs, merge or force-push.