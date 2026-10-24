# NOESIS R391: prospective causal quotient regularization FAILED (24 October 2026)

**Scientific kernel:** causal transition dynamics of learned DFA-state retention under complete-state-neutral cycles. **Status:** frozen conjunctive primary FAILED; second consecutive failure of finite-word quotient-consistency mechanism (R390, R391), triggering a change of mechanism. No theorem or publication-grade discovery.

## Frozen protocol
- Pilot freeze SHA256 `965d077074afe6985fcb8479b495a544da5f8dcc1d6ac704ca9759658225838f`; separate two-seed pilot selected regularization weight 0.20 using only short accuracy and auxiliary CE, without holdout inspection.
- Unseen neutral-word design SHA256 `a23d663bd2795a93875b0debc1b1d2ccaf31b3972971dcf96193312f693608ce`.
- Confirmatory freeze SHA256 `149855a373ce551f2080ed6cfe81e7adc5ef441fc0c328832c34539893123433`, before fresh confirmatory training.
- 216 trained models: LSTM, GRU, MGU-style; 8 shared seeds on count-ones-mod3 and 16 on count-'01'-mod3; three seed-matched arms (CE-only, SAME-state response consistency, RANDOM different-state alignment). Same initial parameters, 196 realized length-8 training strings, 160 Adam steps, common CE and auxiliary CE, all seeds ITT.
- New 10-bit prefixes and 14-bit full-state-neutral word pairs matched on 1–4-grams, counts, transitions and endpoints. Enumerated all u/v compositions depth 0–4 and suffixes empty, 0, 1. Fixed task-B denominator **1,728 cases per arm**, without dropping post-training failures.

## Primary results

| Task-B arm | New depth-2–4 strict quotient violations | Early oracle-correct | All-depth oracle response accuracy |
|---|---:|---:|---:|
| CE-only | 11/1728 | 1494/1728 | 90.9654% |
| SAME | 6/1728 | 1509/1728 | 91.0096% |
| RANDOM | 26/1728 | 171/1728 | 36.0103% |

SAME minus CE = **−0.28935 percentage points**, below frozen ≥0.5-point absolute improvement. Exact one-sided 16-shared-seed sign test vs CE: **p=0.8125** (2 favorable, 3 unfavorable, 11 ties); vs RANDOM: **p=0.11328125**. Seed-block bootstrap 95% CI for CE-minus-SAME: **[−0.5787,+1.5625] percentage points**. Architecture-specific CE/SAME/RANDOM positives, each /576: LSTM 8/2/1; GRU 3/0/7; MGU 0/4/18. Only GRU improved against BOTH controls. Multiple frozen gates failed. **No threshold changed.**

RANDOM damaged symbolic performance and is an adverse negative control, not a strong replacement for CE-only. SAME preserved short accuracy and oracle accuracy but showed no statistically reliable improvement over CE-only.

## Verification and long-horizon secondary
- Pure Python symbolic oracle **602,640/602,640** checks passed.
- Independent NumPy/Numba float64 **96,720/96,720** sampled classifications agreed (520 cases; reproducible hash stratum plus outcome-selected).
- **41/41** selected case paths converged at 120/160 decimal digits, including **29/29** outcome-selected positive witnesses. Three selected finite-string witnesses, one per architecture, additionally agreed at 220 digits and were conditionally certified by mpmath.iv at 100 digits. These are finite-word classifications, **not** n256 invariant-set certificates.
- Independent pure-Python exact binomial checker reproduced counts and seed-cluster p-values.
- Exploratory 1,080-trajectory n256/n512 secondary: task B n256 suffix-1 accuracy **CE 259/288, SAME 259/288, RANDOM 92/288**. No overall long-horizon gain.

## Decision and reproducibility
Retire finite-word quotient-consistency prediction/regularization as the flagship after **two failed confirmatory tests** (R390–R391). Same single kernel continues, with next candidate **causal DFA-transition-edge coverage and support-conditioned retention**: prospective edge-specific prediction and seed-matched symbolic-edge-balanced curriculum versus original i.i.d. and lexical-support-matched controls. Classical automata/state-supervision prior art prevents a novelty claim without sharper mediation, cross-task replication, and validated verification.

Complete raw evidence, fresh parameters, frozen protocols, source, checkers, negative results, 69-file SHA256-verified archive **NOESIS_R391_Reproducibility.zip** remains local (not uploaded to GitHub). Archive SHA256 `ce9d44626c6c45d1fb632cd869a31adf1bd2b1937fe6aeaf4dbcf3cafed5beb0`.

Limitations: low positive base rate, shared-seed clustering, post-treatment eligibility handled by fixed ITT denominator and noninferiority gates, random-pair control collapse, incomplete full-panel high precision and no invariant-set theorem. Prior art includes Dan/Bastani/Roth 2022, Merrill/Tsilivis 2022, and Brandoit et al. 2026.
