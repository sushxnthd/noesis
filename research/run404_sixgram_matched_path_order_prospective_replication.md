# NOESIS R404 — Prospective sixgram-matched DFA-path-order sensitivity

**Date:** 2026-10-25. **Scope:** one kernel, complete-DFA-state-neutral learned transition maps. **Verdict:** separately frozen pilot PASS; fresh prospectively frozen latent-transition primary PASS across all three architectures and both DFA tasks; prospectively frozen cross-task readout-retention secondary FAIL. **Novelty/publication:** not established. No general theorem, invariant-set proof, or external replication.

## Frozen before fresh outcomes

Pilot symbolic design SHA256 `0fa0b4e412aed57c07b9bc4127497302b27016daac00f58772c7b7692f02db11`; pilot quantitative protocol `b617be46faed18af8dd171642ab4aeafea7e46ad20d3e2289504b99e3986a760`. Fresh confirmatory symbolic design `d857313c0f36b4f32551a861aeb31f68d1d879f58ee5f0dc158fe4073c74125d`; fresh confirmatory protocol `6c55ca6da96850d57fd1fc41c24052b3395d10cddec16ddfdf7d509e820675fe`. No model outcomes inspected before corresponding design and thresholds froze; no retuning or exclusion of failed seeds.

## Separate pilot

36 NEW LSTM/GRU/MGU-style models × two DFA tasks × six shared seeds 99600–99605, 100 matched Adam steps, 196 length-8 training strings, 36/36 short-perfect, all ITT. 648 paired cases, 997,272 n0–512 suffix1 labels, novel 32-bit complete-DFA-neutral word triples with exact overlapping 1–5gram and boundary matching, matched Hamming, high/low selected ONLY by symbolic intermediate complete-DFA-path divergence. Frozen feasibility gates passed: 69 class-discordant oracle-error cases through n64, both tasks, three architectures, five seeds; seed-cluster mean log10(high/low full neural-state endpoint displacement) +0.535641, exact six-seed one-sided signflip p=.015625. A separately frozen post-outcome/pre-HP selection of 12 cases × 3 arms had 36/36 n0–8 labels agree across 120/160/220-digit mpmath, pure NumPy and Numba.

## Fresh confirmatory experiment

48 NEW networks, disjoint eight shared seeds 99620–99627, 47/48 short-perfect, all ITT. Novel unseen 32-bit neutral word triples and unseen 10/14-bit prefixes for all complete DFA states. All three words in each triple match exact overlapping **1–6gram histograms** and five-bit boundaries; base-to-low and base-to-high **Hamming distances exactly equal**, mismatch-center difference <=2. All words have identical complete symbolic DFA transformation for both tasks. 864 paired cases, 2,592 full n0–512 trajectories, **1,329,696 raw suffix1 classifications**, all hidden/cell endpoints, all checkpoints and source archived.

**FROZEN LATENT PRIMARY PASSED:** compare from identical prefix-end state `||F_high(x)-F_base(x)||_inf` vs `||F_low(x)-F_base(x)||_inf`, high/low determined from exact intermediate symbolic DFA-path divergence before training. Eight shared-seed cluster means of log10(high/low): `[.64935047,.79218573,.71030124,.47797918,.57721326,.62835802,.72482592,1.05898429]`. Mean **+.7023997654 log10**, geometric displacement ratio **5.03964×**; exact 2^8 one-sided signflip **p=.00390625**; deterministic seed-block bootstrap 95% **[+.6007,+.8242]**. Frozen gates were >=+.10, p<.05 and all six architecture×task means >0. All six passed: LSTM taskA +1.263593, taskB +.531938; GRU taskA +.841519, taskB +.616876; MGU taskA +.657808, taskB +.630526. Descriptive only: 632/864 high>low, median log10 +.4431; trimming 10% leaves +.5925.

**FROZEN READOUT SECONDARY FAILED:** 102/864 high/low class-discordant oracle-error cases by n64, all taskB (LSTM49, GRU37, MGU16), all eight seeds; taskA 0/288 oracle errors and 0/288 high/low class discordances through n512. Frozen both-task gate failed. Float64 n256/n512 labels are NOT exact-real long-horizon certificates.

## Independent verification and exact boundary

Independent standard-library audit passed 864/864 exact overlapping 1–6gram, Hamming, neutral/oracle and intermediate-path checks, plus 13,824 aggregate positional checks. A checker-only initial taskA previous-bit-state bug yielded 96 spurious failures; invalid output preserved and checker fixed, model outcomes unchanged. Independently preselected 108 n1 endpoints recomputed with pure NumPy, 108/108 agree with Numba (max abs difference 2.665e-15). Independently preselected 12 cases × three word arms: 36/36 n0–8 labels agree at 120/160/220 digits, pure NumPy and Numba; 12/12 n1 high/low displacement signs stable at 120/160/220 digits (max binary64-vs-HP absolute displacement difference 3.522e-13). Interrupted evaluation resumed by reloading 648 completed cases and evaluating only remaining 216; preserved logs and code change, no threshold changes.

Exact elementary identifiability fact: for fixed starting state, full intermediate taskA residue path determines each input bit from residue increments; taskB complete state stores previous bit. Thus **distinct words cannot have identical complete DFA-state paths**. Sixgram/boundary-equivalent words induce the same final DFA transformation but can traverse different intermediate paths. This is classical de Bruijn/transition-monoid mathematics, NOT a novel theorem.

**Causal scope:** high/low substitution changes word order at identical weights and identical initial neural state, but intermediate symbolic path is not isolated from 7gram+ and positional lexical structure. Aggregate position balancing is possible by reversing high/low assignments across two prefixes; **not** individually position-matched. The +5× is a preselected-contrast association under strong lexical controls, not a general law. Pointwise high precision is not directed interval certification. No complete prior-art audit. Relevant literature includes Merrill2019, Muškardin et al ACL2024, Svete et al ACL2024, Dave et al 2025, classical de Bruijn Euler trails/Myhill–Nerode.

## Reproducibility and next test

**200-entry SHA256-verified complete local archive:** `/mnt/data/NOESIS_R404_Reproducibility.zip`, SHA256 `60b00010852c300f9847d33d3c297ae244319ff43dd9b29a1cc9e64e7b34b909`. Contains frozen protocols, raw labels/endpoints, all 84 new checkpoints, all source, independent checks, failures, and all negatives; full raw NOT uploaded to GitHub.

Next: second decisive prospectively frozen path-order mechanism test, seek non-ceiling taskA retention, distinguish higher-order lexical effects, preserve all failures. If two primaries fail change mechanism, after three kill/reformulate. Existing branch `research/kernel-001-causal-generalization`, authorized DRAFT PR #22 only; no new branches/PRs, force-push or merge.
