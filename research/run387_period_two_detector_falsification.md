# NOESIS Run 387 — prospective period-two detector: frozen primary FAILED

Date: 24 October 2026. Same scientific kernel, persistent branch and draft PR #21. No novelty or publication-grade claim.

## Frozen experiment

Protocol frozen **before training**, SHA256 `7db2d222f8a67a466e075d1312bd760455fa3beed93aa95ce76964e3c242368c`. R386 was the **separate pilot**, not part of the confirmatory sample. R387 trained 32 NEW LSTM/GRU networks (8 per architecture and DFA task), 160 Adam steps, 196 matched length-eight training strings per paired seed, 258 vs 273 parameters. All 32 achieved perfect short-training accuracy; all training sets covered complete DFA states. Three new prefixes and six new, fully DFA-neutral 12-bit words per state, excluded from R386, gave 2,592 full n0..512 trajectories. Words were matched on symbol counts, transition counts and endpoints.

At cycle n16, compute complete-state cycle map x, y=F(x), z=F(y). Predict late period-two suffix-1 classifications iff ||z-x||/(||y-x||+1e-30)<0.1, ||y-x||>0.1, the x/y suffix-1 classes differ, and both margins exceed 0.1. Late target: strict alternating class for all cycles 384..512. All detector thresholds were calibrated on R386 and frozen before the R387 models were trained.

**Frozen conjunctive primary** on task B: >=4 late period-two trajectories, >=1 in EACH architecture, PPV >=90%, recall >=75%, and one-sided Fisher exact p<.05 on 16 architecture-seed clusters.

## Result: FAILED

There were only **3/1,728** task-B late period-two trajectories, all from **one LSTM seed (75103)**, with **0 GRU positives**. The detector found all three, with no false positives, but all are correlated trajectories from one seed and word. Seed-cluster contingency table [[1,0],[0,15]], one-sided Fisher **p=0.0625**. The required event count, cross-architecture replication, and p<.05 all **FAILED**. Do not turn 3/3 trajectory-level performance into a general result.

Task-B n256 one-bit oracle errors: LSTM 215/864; GRU 61/864. Within exact symbol/transition-count matched word-order pairs, n256 suffix-1 classes differed in 122/432 LSTM and 40/432 GRU task-B pairs; **only 3/27** word pairs had identical trigram histograms, so n-gram support remains a confounder. Neither task-A architecture exhibited late period-two classifications.

## Independent checks and numerical caution

Independent vectorized NumPy versus Numba: **116,635/116,640** sampled immediate/suffix0/suffix1 classifications agreed. Five disagreements came from one task-B LSTM trajectory, all independently arbitrated. **36 mpmath 120/160/220-digit runs** yielded 1,308/1,332 comparisons matching Numba and **576/576** precision-converged groups. All 24 disagreements involved that single arbitration trajectory. Eight additional 160/220-digit complete n384..512 runs converged for **all four selected cases** (three detector positives and one arbitration case). The positives alternated with minimum suffix-1 margin 4.638; the arbitration case disagreed with Numba on 41/129 late cycles per precision. These are numerical convergence checks, NOT interval certificates or exact attracting-orbit proofs.

Independent standard-library exact-statistics, symbolic DFA neutrality, no-pilot-reuse, detector and precision checker PASSED.

## Decision and prior art

R386 and R387 are TWO failed confirmatory attempts. **Retire the early period-two detector as the flagship**; do not tune n16 or thresholds on these holdouts. Next mechanistic target within the SAME kernel: **neutral-word map noncommutativity**, comparing F_u∘F_v with F_v∘F_u under symbol-, boundary-, n-gram- and complete-state-matched controls on new seeds. Freeze a quantitative predictor and cluster-level gate before unseen outcomes.

Classical RNN/DFA dynamical systems and attractor literature already exists (Casey 1996; Tino, Horne & Giles 1995/1998; Omlin & Giles 1995/1998; Merrill & Tsilivis 2022; Weiss 2018). This is not a new theorem. No publication-level claim.

**Raw evidence is NOT on GitHub.** Full 50-entry SHA256-verified local reproducibility archive: `NOESIS_R387_Reproducibility.zip`, SHA256 `10ef9ef879a622f6823d12fbfe3f44a76c247ac4741d0496859ba539ddab5321`. Contains frozen protocol, R386 pilot archive, 32 checkpoints, 2,592 full traces, all source, independent checkers, raw precision records and figures. Keep PR draft; never merge or force-push.
