# NOESIS Run 380 — frozen training-time forget-gate intervention (2026-10-23)

**Decision: FROZEN PRIMARY FAILED.** Do not promote this result to a new law.

Eight independently initialized training seeds (4 count-ones-mod3, 4 count-'01'-mod3), each with three seed-matched width-5, 258-parameter symbol-conditioned LSTMs: baseline, forget-gate persistence penalty 0.5*(f-.9)^2, and anti-persistence penalty 0.5*(f-.1)^2. Each arm used the same 196 length-eight strings, initialization, Adam .035 and 240 epochs. All 24 models achieved perfect short-training accuracy. Mean persistence-minus-anti-persistence CE difference 0.00144446; mean forget-gate activation difference 0.789387.

Frozen primary: positive identity-minus-transition interaction at n256, mean >=0.25, paired exact one-sided sign-flip p<0.05, CE/gate manipulation and high-precision agreement. Observed seed differences [0,1,0,0,2,1,0,1], mean +0.625, **p=0.0625**. Thus primary FAILED (do not round or retrofit). On first unseen transition words, anti-persistence retained the tested DFA class on 8/8 seeds versus persistence 3/8, a descriptive result only. Some failures occurred already by n32, so do not call all of these delayed forgetting.

**Precision:** 48 primary conditions evaluated independently at 120/160 decimal digits through n512 (96 reference runs, 240 condition-endpoint pairs), zero classification disagreements; independent NumPy/PyTorch float64 matched all primary labels. Eight independent Decimal160 checks matched. In the secondary sweep (216 conditions), four NumPy/PyTorch disagreements arose on task-B seed49000, second neutral word. Targeted 120/160/220-digit adjudication on three DFA representatives x n128/n256/n512 agreed on 9/9 high-precision labels, but NumPy float64 was wrong on 3/9 and PyTorch float64 on 5/9; two implementations can agree with each other and still both be wrong. Never use secondary float64 flips as truth.

**Limitations:** Training-time gate regularization changes the objective and all learned weights, not isolated gate causality. Task-B neutral words preserve the selected ending-1 DFA states, not all six states. This does not establish a novel theorem, general architecture effect, or publication-ready discovery. Prior art includes Weiss et al. 2018, Chen et al. 2018, Dan et al. 2022, Muskardin et al. 2024, Buitrago & Gu 2025, and Metric Automata Theory 2025.

**Frozen protocol SHA256:** `83aa17151afd90cc19bd0cbf83ccaaa24f97730f545360249d10fc91d862d802`.
**Complete local reproducibility archive:** `NOESIS_R380_Reproducibility.zip`, SHA256 `1c9ac9814de7689ea162907aef8e7932eada200998c93aa37abcbd224254cd72` (37 files including manifest; raw data and checkpoints are local, not uploaded to GitHub).

Run 381 was independently frozen **after** the Run380 exploratory observation and before training new seeds. It tests the anti-persistence retention hypothesis prospectively on 16 fresh seeds, 3 DFA representatives and unseen neutral words. It does not alter Run380's failed primary.

Single active kernel, existing branch `research/kernel-001-causal-generalization`, existing draft PR #21. No force-push or merge.
