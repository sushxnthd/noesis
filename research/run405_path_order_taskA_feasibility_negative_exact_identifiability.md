# NOESIS R405 — Path-order task-A feasibility negative; exact identifiability audit

**25 October 2026.** Same kernel, existing `research/kernel-001-causal-generalization` branch, draft PR #22. Independent prospectively frozen pilot **FAILED**; no fresh confirmatory cohort was justified. This does not reverse R404's narrowly successful latent primary.

## Pre-outcome freezes

- New symbolic design SHA256 `c8f7e7e27def966c00ff273c10ed18e4eb0009576a6f0a4c84a9a2224eb14575`.
- Pilot protocol SHA256 `df37f1d5deb39711c01f6073ce39da2d2e105d1493cd2213914f1d41c72eb17e`.
- Independent exact combinatorial protocol SHA256 `bc94f62fc9edd8f38c5d4b9bb6cf40b4d83b4af4e89f7c883047a4911193ef14`.
- Outcome-selected HP manifest, frozen before HP, SHA256 `a7364e7e6f726236c9519fe4e7fabfc241c8bdf3f974ed10af02432c43e49a5d`.
- Exploratory late extension, frozen before n65..512 outcomes, SHA256 `9a4cb7ed3d3d48429cbe9f1ae3ce3ab4784a02e95974d7901d1d63db51f056bb`.

## New independent pilot

36 new LSTM/GRU/MGU-style networks, both DFA tasks, six disjoint shared seeds 99700–99705, 196 matched length-8 training strings, four checkpoints at Adam updates 50/75/100/125. All seeds/snapshots intention-to-treat. New 32-bit full-DFA-neutral word triples, identical overlapping 1–6gram histograms and 5-bit boundaries, matched base-to-low/high Hamming distance, mismatch-center difference <=2, and unseen 10/14-bit prefixes across all complete DFA states. Symbolic high/low path divergence fixed **before** training. 648 paired cases per snapshot, 2,592 total.

Frozen conjunctive feasibility required task-A >=12 eligible low/high class-discordant oracle-error pairs, >=2 architectures, >=3 seeds, and >=2 task-A architectures each with >=2 positive seeds, plus task-B >=8 pairs across >=2 architectures/3 seeds and short accuracy >=95% for positive models. Results:

| Snapshot | Task-A eligible positives | Task-A positive seeds | Task-B eligible positives | Frozen feasibility |
|---|---:|---|---:|---|
| 50 | 6 (LSTM 2, MGU 4) | only 99701 | 160 | **FAIL** |
| 75 | 0 | none | 128 | **FAIL** |
| 100 | 0 | none | 103 | **FAIL** |
| 125 | 0 | none | 97 | **FAIL** |

Task-A networks were 18/18 short-perfect at all snapshots. Task B remained non-ceiling across architectures and seeds. No threshold changes, no confirmatory training, no cross-task retention claim.

An exploratory, **non-preregistered** latent high/low endpoint displacement analysis gave pooled log10 ratios +.279/+ .400/+.327/+.351 by snapshot, but is not new confirmatory evidence. Higher lexical order remains confounded: across 18 symbolic groups, 7gram base-to-high distance exceeded/tied/fell below base-to-low in 8/4/6 groups.

## Independent verification and full trajectories

Independent standard-library symbolic checker: 2,592/2,592 pairs passed full-state neutrality, suffix1 oracle, Hamming, boundaries, exact 1–6gram and symbolic path-gap checks. Eight frozen-selected cases (four task-A positives, two task-B positives, two negative controls), 24 word arms, all n0..8 labels agree in independent pure NumPy, Numba and pointwise 120/160/220-digit mpmath. **Not directed interval proof.**

Separately frozen exploratory extension preserved **7,776 full n0..512 trajectories, 3,989,088 float64 classifications**, with all n0..64 labels exactly reproduced. Late float64 discordances/errors are not exact-real arbitration or invariance claims. Initial execution stopped at 1,296 rows; resume skipped completed keys. Logs and both scripts preserved.

## Exact combinatorial boundary (classical, not novel)

Independent exhaustive binary-word enumeration for k=5,6,7 and lengths k..17 established that the shortest distinct words with identical overlapping kgram counts and (k-1)-bit boundaries have length **2k**. Proof: common boundaries restrict possible mismatches to positions k..n-k+1, requiring n>=2k-1; at n=2k-1 a sole middle-bit mismatch contradicts equal total ones implied by kgram counts and common prefix. Sharp example `0^k 1 0^(k-1)` versus `0^(k-1) 1 0^k`.

At this minimum, both-DFA-neutral matched examples exist:
- k5 n10: `0010010100` / `0010100100`;
- k6 n12: `001000100100` / `001001000100`;
- k7 n14: `00010001001000` / `00010010001000`.

At n17, exact both-neutral unordered pair counts were 3931/635/141 for k5/k6/k7. A **separate rolling-bitmask implementation** reproduced all 36 k/length count cells. Its initial previous-bit-zero checker bug and corrected results are both preserved. For these DFA tasks, complete intermediate symbolic state paths recover each input bit; nonidentical same-path controls are impossible. Exact per-position bit matching also forces identical words. Lexical and symbolic path order are therefore not separately manipulable by a single deterministic word swap.

Two descriptive-only audit bugs (half-L1 7gram distance and incorrect case-weighted short-perfect count) were independently corrected without changing any frozen pilot outcomes or raw data.

## Decision and reproducibility

R405's **prospective feasibility gate FAILED**, so no second path-order confirmatory primary was run. R404's latent sensitivity remains narrowly replicated, but path-order mediation of readout errors and task-A generalization remain unsupported. Next work should pursue identifiable operator-level causal experiments or rigorous finite-word transition-semigroup bounds, rather than force task-A errors. No novel universal law, publication-grade priority or invariant-set theorem.

Complete **44-entry SHA256-verified local archive**, including all raw/checkpoints/seeds/source/negative results/independent checks and exact R404 dependency ZIP: `NOESIS_R405_Reproducibility.zip`, SHA256 `3a5092554cabea69e558c5d127bc599122cf648d4fd61259f7d019817f3a9ff9`. Full raw data are **not on GitHub**. Zero user spend; no user-laptop access.
