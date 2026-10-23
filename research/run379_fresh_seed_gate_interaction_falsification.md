# NOESIS Run 379 — prospective fresh-seed LSTM negative control

**Decision: frozen primary FAILED.** This result is not a new theorem or an algorithm-acquisition law.

Frozen protocol SHA256: `99d9f5d0967d5162fd7934e9944a30c41eca393efd6766b93f8ed9f6cab0b78a`. Eight unseen training seeds were fixed before training; only six reached perfect short-training accuracy (4/4 count-ones-mod3, 2/4 count-'01'-mod3). No replacements.

At n256, within-checkpoint forget-gate +4 (after n32) versus no shift:

| Task / cycle | Eligible | No shift correct | +4 correct |
|---|---:|---:|---:|
| Ones mod 3, identity `0` | 4 | 4/4 | 4/4 |
| Ones mod 3, transition `101001101001` | 4 | 3/4 | 3/4 |
| `01` mod 3, identity `1` | 2 | 0/2 | 0/2 |
| `01` mod 3, transition `111011110101` | 2 | 1/2 | 1/2 |

The frozen interaction criterion required mean D <= -0.25 and one-sided paired exact p<0.05, plus all eight seeds eligible. Observed D=0, p=0.75, 6/8 eligible. **All three gates failed.** On the same transition word, seed 46000 was repaired by +4 (class 2 -> 0, correct 0) while seed 46001 was harmed (0 -> 1). These are model-specific within-checkpoint causal changes, not evidence that gating caused the GRU/Elman architecture gap.

All 24 eligible model × cycle × shift conditions were checked at n32/n64/n128/n256 at mpmath 120/160/220 digits: 96/96 endpoint classifications agreed across precisions. Independent NumPy and PyTorch float64 agreed with the high-precision labels on all 96 endpoints. A separate Decimal160 recurrence matched eight selected conditions (four through n256 on task A, four through n64 on task B). Task-B Decimal160 n256 attempts timed out and are **not** claimed completed. Exploratory PyTorch float32 disagreed at n128 and n256 for task-B seed47001 transition/+4, while NumPy float32 and higher precision agreed.

**Limitations:** post-training forget-gate shift, not matched training-time gate intervention; only two frozen transition words; eligibility-conditioned small sample; no formal interval certificate on new seeds. The full frozen protocol, 8 training outcomes, all 48 mpmath120/160 trajectories, 24 mpmath220 checks, independent float64/float32 checks, Decimal controls, exact DFA oracle, statistics, negative findings and SHA256 manifest are preserved in the local `NOESIS_R379_Reproducibility.zip` archive; raw evidence is not represented as uploaded to GitHub.

**Next test:** same kernel, matched training-time gate parameterization with eligibility-independent intent-to-treat analysis and precision-robust unseen-cycle outcomes. Do not revive R350–362, universal +2, or early-cycle Jacobian predictor claims.