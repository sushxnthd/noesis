# NOESIS Run 381 — prospective independent-seed replication (2026-10-23)

**Decision: FROZEN CONJUNCTIVE PRIMARY FAILED.** The pooled result does not rescue two failed gates. This is not a novel theorem or publication-ready causal law.

**Frozen protocol SHA256:** `76e3835ea916dd7cb383ebc0da1013dcd2e360c01093ff6db4b2b138dab737f8` (pre-training exact symbolic validation corrected invalid *secondary* word candidates before final freeze). Protocol committed earlier as `research/run381_frozen_training_gate_replication.md`.

**Training:** 16 new seeds (8 per DFA task), 3 seed-matched symbol-conditioned LSTMs per seed (48 models, width5, 258 parameters), identical initialization/training strings/Adam schedule. Arms no-penalty baseline, persistence pressure `0.5*(f-.9)^2`, anti-persistence pressure `0.5*(f-.1)^2`. Final epoch240 intent-to-treat; no replacements. Mean forget activation difference 0.785405; mean short CE anti-minus-persist -0.003698. 46/48 models perfect short training; minimum accuracy **0.985332**, below frozen .995 gate.

**Frozen primary n256:** 3 DFA representatives per task, new 12-bit neutral word, all 16 seeds. Mean anti-persistence minus persistence accuracy **+0.333333**, paired exact one-sided sign-flip **p=0.001953125**, descriptive stratified bootstrap 95% CI [+0.270833,+0.395833]. Task A (ones mod3) **+0.041667**, exact p=.5, **below frozen >.1 requirement**. Task B (count-'01' mod3) **+0.625**, exact p=.00390625, eight of eight seed-level differences positive. Thus **primary FAILED** on task-general transfer and minimum short-training accuracy despite a significant pooled contrast. Do not retrofit thresholds.

**Strong matched baseline, high precision:** task B anti-persistence **23/24** correct DFA representatives, no-penalty **21/24**, persistence **8/24**. The large anti-vs-persist contrast is principally **persistence-pressure harm** relative to ordinary training (baseline-minus-persist +0.541667, exploratory exact p=.0078125), NOT a proven anti-persistence improvement over baseline (anti-minus-baseline +0.083333, exploratory p=.25). Task A anti 24/24, persist 23/24. Task-B differences were already present at n32, so not all delayed forgetting.

**Precision and independent checks:** 96 primary conditions at mpmath120/160, 192 trajectories, 384 condition-endpoint comparisons, **zero 120/160 label disagreements**. Extra no-penalty baseline 64 high-precision trajectories, zero 120/160 label disagreements. Eight independent Decimal160 checks matched. Exact symbolic oracle verified 60 state-preserving representative/word/horizon cases; full symbolic training-state coverage 3/3 and 6/6 on every seed. Task B words preserve the selected ending-1 DFA representatives, not every six-state DFA state.

**Numerical adversarial witness:** task A seed50000, persistence pressure, prefix `0`, neutral word `010100100111`, n256: NumPy float64 class **0**, PyTorch float64 class **2**, mpmath120/160/220/300 and independent Decimal160 class **1** (readout margin ~4.791), symbolic class **0**. High-precision class changed from correct 0 at n32 to incorrect 1 at n64. No universal Lyapunov law is claimed.

**Mechanism decision:** Retire mean forget-gate occupancy as a universal retention predictor. Continue the *same single kernel* around state-conditioned learned full-cycle map basins and verified separation/contraction, with frozen unseen-cycle predictions and new architectures. The general contraction/separation concept is already in Brandoit et al. (2026, arXiv:2609.32447), Metric Automata Theory (2025), and other prior art. No paper-level novelty established.

**Complete local SHA256-verified reproducibility archive:** `NOESIS_R381_Reproducibility.zip`, SHA256 `829209b477d823dec13257b3ae15435c1c5dc425d2cc13e733d4afd16c6d52f7` (44 files including manifest). Contains frozen protocol, all checkpoints, source, raw data, high-precision checks, exact statistics, negative results, and figures. **Raw data remain local; do not claim GitHub upload.**

Only existing branch `research/kernel-001-causal-generalization` and draft PR #21. No force-push or merge.
