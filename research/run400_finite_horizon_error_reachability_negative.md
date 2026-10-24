# NOESIS R400 — Prospective finite-horizon neutral-cycle error reachability (negative primary)

**Date:** 2026-10-24. **Kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. **Frozen conjunctive primary: FAILED.** No novel general theorem or publication readiness is claimed.

## Frozen separation
- Independent three-seed pilot 99300–99302, protocol SHA256 `9923759e85e54dff7211a1f830e2edbe5fc45a439c2ed2ce8dfb553fa670e244`. Pilot selected 80 Adam updates, with only 1 first n3–8 error among 541 early-correct trajectories; sparse pilot and weak power. Pilot-selection SHA256 `0230b43494b98014816735f715cd7e5d96ea89950e9ac30e1781920c6d59ffbf`.
- Fresh symbolic design SHA256 `486aca7e292c6783f927179b5dc19f79b55fc7d26743ef82f18fa7c8b9a62a4f`, and **confirmatory protocol frozen before fresh training** SHA256 `d4a4000a5d9cab621e30499e24635e5db66342ae1748700bdcfdee783e365c2a`.
- Trained **48 fresh** LSTM/GRU/MGU-style networks, both DFA tasks, 8 shared seeds 99310–99317, 196 length-8 training strings, 80 Adam steps; **44/48 short-perfect**, all intention-to-treat.
- Evaluated **1,296 paired cases**, **2,592 full n0–512 trajectories**, **1,329,696 suffix-one classifications**. Paired 40-bit neutral compositions were exactly matched on overlapping 1–5grams and four-bit endpoints, with aggregate (not per-instance) positional balance. Complete DFA oracle verified independently.

## Frozen primary result
Eligible population: both arms oracle-correct at n0, n1, n2. **1/1,019** eligible pairs first erred at n3–8. The single event was **MGU-style, task B, seed 99311, n3**. Zero qualifying events in the other five architecture/task cells. Frozen gates required >=5 events, >=2 architectures, both tasks, >=3 shared seeds and >=90% full finite-horizon directed interval certification. At the frozen 100-digit setting, **12/14** selected arms had all n0–8 labels certified (**85.71%**). **Conjunctive primary failed**; no thresholds were changed, no holdout retuned.

## Narrow finite-word witness
MGU-style task B seed 99311, prefix `1101110000`, complete DFA state (1, previous 0), suffix-one oracle class 2. The two exact-fivegram-matched, full-state-neutral 40-bit words:
- `0010101111010001011000101000101111010110`
- `0010101111010001011000101111010001010110`

From the **same exact-zero recurrent state and same prefix**, their n0–8 suffix-one classes are respectively `[2,2,2,1,1,1,1,1,1]` and `[2,2,2,2,2,2,2,2,2]`. Frozen 100-digit `mpmath.iv` directed intervals strictly certify the causal class difference at n3 and all n0–7, but **not n8** due natural interval wrapping. Explicitly post-primary 160/220-digit interval reruns certify all n0–8 labels of both arms; they **do not rescue the primary**. These are conditional finite-string certificates, not invariant-set proofs.

## Independent numerical audit
- Pure standard-library complete-DFA and overlapping-gram checks passed on the full design and all 1,296 evaluated pairs.
- Predeclared selected seven cases (one positive, six negative controls): independent NumPy/Numba **252/252** sampled classifications agree through n512.
- Three selected cases, two arms each, at 120/160/220 digits: **18/18** high-precision finite n0–8 continuations match early labels.
- Separately outcome-selected long-horizon cases exposed numerical instability. LSTM/task B seed99314 n256: Numba class **1**, pure NumPy **0**, 120/160/220-digit point recurrence **0**. MGU/task B seed99311 n256: Numba **0**, NumPy **2**, 120-digit point **1**; higher precision attempt timed out. No unverified n256/n512 oscillation is treated as a theorem.

## Decision and preservation
This is the **first failed primary** of the finite-horizon reachability mechanism. The next separate pilot must demonstrate adequate post-n2 onset incidence and cross-seed diversity before a second fresh prospective test; if that also fails, change mechanism. Prior-art novelty audit remains incomplete.

Complete **77-entry SHA256-verified** hosted-runtime archive: `NOESIS_R400_Reproducibility.zip`, SHA256 `561349cf68cc622027e9354b851c214b9ebc169e3271e82ca317bd327fb58f73`. It contains frozen protocols, every pilot/fresh checkpoint, all raw n0–8 logits, all n0–512 labels, negative results, independent checks, source, logs, failed precision attempts and full report. Raw data are not on GitHub. Zero user spend, no user laptop. Only existing `research/kernel-001-causal-generalization` branch and authorized continuing draft PR #22; no merge, force-push or new branch/PR.
