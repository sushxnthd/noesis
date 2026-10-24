# NOESIS R386 — Matched neutral-word order and two-phase readout behavior

**Date:** 2026-10-24. **Kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **Decision:** frozen primary **FAILED**. This note summarizes a complete local 53-file reproducibility archive; raw trajectories and checkpoints are **not uploaded to GitHub**.

## Frozen protocol and training

Protocol SHA256: `ce0b2f5cfa9f88f5f54b1cb5928b2ce8cb2753573cafa1cd911a3daf12b0883d`. Frozen before training. Thirty-two new models: eight LSTM and eight GRU per task (count-ones mod3 and count-'01' mod3), 160 matched Adam updates, 196 matched length-8 training strings, 258 versus 273 parameters. All 32 short-perfect. Every complete DFA state had three independent 10-bit prefixes and six 12-bit full-state-neutral words with exactly six ones, six zeros, six transitions, and matching first/last bits. 2,592 full n0..512 trajectories, 1,296 frozen matched-order pairs.

## Frozen primary: FAILED

Among 1,710 task-B rows with correct n0 suffix-1 classification, the observed n8 suffix-1 class forecast the n256 class in **1,706/1,710 (99.7661%)**, versus **1,639/1,710 (95.8480%)** for the n0 forecast. LSTM n8 concordance 842/846; GRU 864/864. Improvement **+3.9181 percentage points** (seed bootstrap 95% [+1.1574,+8.7753] pp), exact eight-shared-seed one-sided sign-flip p=0.0078125. The PREDEFINED effect threshold was **>=8 pp** and therefore **FAILED**, regardless of the other passing gates. Do not round or change the threshold.

## Matched-order effects, exploratory

At n256, **48/432 LSTM** and **5/432 GRU** task-B matched-word pairs produced different suffix-1 classes, despite identical symbolic state, prefix, network, length, symbol composition, transition count, and endpoints. Four *post-hoc selected* pairs (two per architecture) retained different classes at 120/160/220-digit precision. This is model-specific causal sensitivity to word order, not a generalizable discovered law.

## Falsification of sampled-even-horizon stability inference

**Zero of 2,592** suffix-1 labels differed between n256 and n512. Yet the *full traces* contained late n33..512 consecutive-cycle class changes in **18/864 LSTM task-B rows** (6,894 flips) and **2/864 GRU task-B rows** (960 flips). Selected trajectories alternate every cycle while all even-horizon labels agree. One LSTM and one GRU example were independently evaluated at 120/160/220 digits for n32,33,34,255,256,257,511,512. LSTM alternates classes 0/1 with minimum selected readout margin 1.286; GRU alternates 2/0 with minimum margin 4.183. **This falsifies the inference that even-horizon endpoint equality establishes invariant classification or fixed-point capture.** It does not formally certify a period-two attracting orbit.

A retrospective reanalysis of R385 archived full traces likewise found late flips in 12/288 GRU task-B rich-word cases (4,319 flips), despite n256=n512 equality. This reanalysis is not prospective replication.

## Independent numerical checks

Independent NumPy versus Numba float64: **85,524/85,536** labels agree. All 12 discordances (three unique task-B LSTM cases) were arbitrated at 120/160/220 digits; one n128 case sided with NumPy, the rest with Numba. The prespecified high-precision subset plus arbitration comprised 990 comparisons, 981 matching Numba, with 450/450 classification groups precision-converged. All post-hoc period-two and matched-order examples agreed at 120/160/220 digits. No formal interval certificate or full-panel high-precision certification.

## Next scientific test

Prospectively predict **period-one versus period-two** readout response from complete learned neutral-cycle maps, rather than even-horizon endpoints. Freeze fresh seeds, odd/even horizons, matched word-order controls, training n-gram support, exact seed-cluster statistics, independent high-precision arbitration, and validated invariant-neighborhood verification before outcomes. This is the first failed confirmatory test of the early-map-capture family; no novelty claim.

**Archive:** `NOESIS_R386_Reproducibility.zip`, 53 files, SHA256 `ed9f290198e62c3168433d275af7ec2960ca086b569f353d76e883371b239d05`. Complete raw evidence remains in the local archive. Same branch and draft PR #21; no force-push or merge.