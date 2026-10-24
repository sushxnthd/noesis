# NOESIS R388 — prospective neutral-word commutator prediction (2026-10-24)

**Frozen primary PASSED, with important limits. Not a novel theorem or publication-grade law.** One kernel, existing branch `research/kernel-001-causal-generalization`, draft PR #21. Do not merge.

For full-state-neutral 12-bit words u,v, the symbolic DFA has δ(q,uv)=δ(q,vu)=q, while learned continuous word maps need not commute. The prospective score was the complete hidden/cell-state commutator norm `||F_v(F_u(x))-F_u(F_v(x))||_2` at prefix end. Within each frozen trained model/prefix, compared `(uv)^n` versus `(vu)^n` and appended bit 1. Each u/v pair was matched on length, six ones, six transitions, first/last two bits, and **exact trigram histogram**, so uv and vu have identical 1/2/3-gram counts and symbolic full-state action.

**Protocol frozen before any fresh training:** `FROZEN_RUN388.json` SHA256 `17f18aeacabf4251ae06012b0dd07dbd161ec939205ff38e59efaf3abda75df2`; word design frozen separately SHA256 `b85aec9b18204d6f17665cd3df985a5df7713fcbf3b1e4d7fe9dfad5f2f1b99c`. Separate R387-checkpoint pilot used disjoint word pairs and seeds, never pooled with holdout. Pilot thresholds: LSTM q25=1.39943/q75=3.35450, GRU q25=.09729/q75=.40294.

**Fresh prospective panel:** 32 new LSTM/GRU models (8 per architecture per task), 160 matched Adam updates, identical 196 realized training strings per paired seed, 258/273 parameters; all short-perfect. Two new prefixes and three new word pairs per complete state, 864 paired cases, both orders through n512. Full training-state coverage in all seeds.

**Task-B frozen conjunctive primary (all gates passed):**
- n256 order-dependent suffix1 classifications: LSTM **3/288**, GRU **16/288**.
- Raw commutator AUROC: LSTM **1.000** (only 3 positives from 2 seeds), GRU **0.9653**, both ≥.80.
- Pilot-calibrated high versus low commutator: LSTM **3/6 vs 0/192**; GRU **16/88 vs 0/97**; pooled **19/94 vs 0/289**, risk difference **+20.21 pp** (required ≥15 pp).
- Eight shared-training-seed-block mean difference **+18.26 pp**, exact one-sided sign-flip **p=4/256=.015625** (required <.05); seed-bootstrap pooled risk-difference CI **[+7.32,+33.33] pp**.
- Architecture-normalized pooled commutator AUROC **.9635** versus negative initial-margin AUROC **.6358**; advantage **+.3277** (required ≥.10).

**Critical limitations / negative controls:** task A produced **0/288** order-dependent n256 classifications. **18/19** task-B n256 order differences were already visible at n1; n1 label-disagreement baseline AUROC was **.9965 LSTM / .9522 GRU**, nearly matching the commutator. Thus this does NOT establish a delayed error mechanism or superiority to the strongest early-label baseline. LSTM high-score stratum has only six cases. Four-gram and longer sequence statistics were not matched; architecture capacity differs slightly. Changing word order is causal, but the commutator-score association is predictive, not an isolated causal manipulation of score magnitude. No novelty claim.

**Independent verification:** batched independent NumPy vs Numba **24,192/24,192** sampled one-bit labels agree. Pure-Python checker independently confirmed all 864 full-DFA neutral actions, exact 1/2/3-gram matching, complete traces and exact sign-flip count. Outcome-selected *all 19* n256 positives plus 12 preselected controls were independently recomputed at 120/160 digits: **310/310** sampled classification groups converged and matched Numba, all **19/19** positives survived. Two posthoc selected architecture witnesses also agreed at 160/220 digits through n512. No full-panel high-precision census or formal interval invariant-set certificate.

**Complete 60-entry local SHA256-verified reproducibility archive**: `NOESIS_R388_Reproducibility.zip`, SHA256 `3acf88c06b0b35c698c9dbc34548f8a83a18838024ba8d549e7274c4ad7d799d`. Contains all frozen protocols, source, old pilot checkpoint inputs, 32 new model parameter arrays, 864 complete paired trajectories, 62 high-precision jobs, independent checkers, exact stats, figures, negative results, and logs. **Raw archive remains local; it has not been uploaded to GitHub.**

**Next decisive gate:** fresh third architecture (MGU) and new GRU/LSTM seeds; prespecified equal-n1-output cases with exact 4-gram-matched neutral-word orders, test truly delayed divergence against the near-perfect n1 class baseline, with independent high precision and validated interval witness. Complete primary-literature novelty audit before manuscript claims. Keep PR draft, do not merge.