# NOESIS R390 — Prospective finite-word quotient consistency (2026-10-24)

**Scientific decision: frozen conjunctive primary FAILED.** One-kernel continuation on `research/kernel-001-causal-generalization`; draft PR #21 must remain unmerged.

## Frozen experiment
- New 14-bit full-DFA-neutral words `u,v` matched exactly on symbol counts, transitions, first/last three bits, and 1–4-gram histograms; three unseen 10-bit prefixes per complete DFA state, including the previous-bit component on count-`01`.
- **Word design frozen** SHA256 `dff89bc2b843aa414245db32c07e56657a77294da2b9a3d60130caf2512a0960`. Archived R389 pilot: 324 cases, only two late-depth positives, both from one GRU seed. Pilot excluded from confirmation.
- **Confirmatory protocol frozen before fresh training** SHA256 `3510ef725ddda31a15dbbf33d9a0023cca4acf1bd3bb62e67489a59662cb5599`.
- 96 fresh seed-matched LSTM/GRU/MGU-style models, 196 identical realized eight-bit training strings per matched seed, 160 Adam updates, parameter budgets 258/273/248; 95/96 short-perfect, **all 96 retained**.
- For pairs of histories reaching the **same complete DFA state**, tested 31 common neutral-word compositions through depth four and the empty, 0, and 1 continuations. Define first finite distinguishing depth as the earliest composition length at which the two learned response signatures differ. Restrict primary population to pairs identical at depths zero and one.

## Outcomes
| Task | Architecture | Eligible | Newly distinguishing at depth 2–4 |
|---|---|---:|---:|
| Ones mod 3 | LSTM | 144 | 0 |
| Ones mod 3 | GRU | 144 | 4 |
| Ones mod 3 | MGU-style | 140 | 2 |
| Count-'01' mod 3 | LSTM | 754 | 1 |
| Count-'01' mod 3 | GRU | 780 | 6 |
| Count-'01' mod 3 | MGU-style | 802 | 24 |

Task B: **31/2,336 eligible** cases from six shared training seed IDs; 17/31 also had all tested depth-zero/one responses **oracle-correct**. Six task-A positives (GRU/MGU-style) were also initially oracle-correct. Cases within a seed are dependent; this is not a universal rate.

**Frozen predictor FAILED:** architecture-normalized pooled AUROC of the depth-one normalized continuous quotient defect = **0.973200**, versus raw centered-logit gap **0.962564** (advantage **+0.010636**, below prespecified **+0.08**). Seed-bootstrap 95% CI for advantage **[-0.01184, +0.02943]**; exact seed-block sign-test **p=0.1875**. Only one LSTM task-B positive, below minimum three. All four failing conjunctive gates remain failed; do not retune or reverse.

## Independent checks
- Independent pure-Python DFA and 1–4-gram checker: **281,232/281,232** state-equivalence comparisons; all 3,024 cases valid.
- Independent NumPy vs Numba: **38,874/38,874** individual classifications agree over 209 stratified/outcome-selected cases (all 31 tree nodes, both prefixes, all three suffixes).
- Independent 120/160-digit recurrence: **37/37** outcome-selected positive finite-word witnesses reproduced; all **49/49** positive/control cases label-converged. Three selected witnesses also matched at 220 digits.
- **Three conditional finite-depth directed-interval certificates**, one each in fresh LSTM seed 81100, GRU 81108, and MGU-style 81106 on task B, certify different winning labels after the same two-word composition from same-symbolic-state prefixes. Assumes `mpmath.iv` backend soundness. **Not an invariant-set or unbounded-horizon certificate.**
- Exploratory local Jacobian and DMD diagnostics were archived but cannot establish attraction.

## Interpretation and next gate
The bounded same-DFA-state quotient violations replicate across three architectures, but are largely rare and seed-concentrated; the stronger predictive mechanism failed. These are classical finite-word conformance counterexamples, **not** a novel automata law. Relevant prior art: Weiss et al. ICML 2018, Dan et al. ICML 2022, Merrill/Tsilivis 2022, Muškardin et al. IFM 2022, Buitrago/Gu ICML 2025, Metric Automata Theory NeurIPS 2025, Brandoit et al. arXiv:2609.32447 (2026). Additional audit remains.

**Next same-kernel experiment:** prospectively freeze a seed-matched *training-time quotient-consistency intervention* versus CE-only and equal-budget wrong-state/random-pair controls, test unseen prefixes and neutral compositions with intent-to-treat analysis and high-precision witnesses. R390 is the first failed primary in this mechanism; change after the second substantive failure.

Complete **51-entry SHA256-verified local reproducibility archive**, including all raw results/checkpoints/frozen protocols/source/independent checks/figures: `NOESIS_R390_Reproducibility.zip`, SHA256 `aa6883b039361e4ba15b2df3ae78c1b1c65d4a7d421d91fc38465ea6fd10de40`. **Raw evidence is not uploaded to GitHub. No new branch or PR, no merge, no force-push.**
