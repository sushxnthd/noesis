# R454: Exact finite-corpus DFA/lexical controls and prospective seed-power gate

2026-10-27. Kernel: causal transition dynamics of learned DFA-state retention under per-designated-complete-state-neutral cycles. **Classical training-design feasibility, not a neural breakthrough or prospective replication.**

## Frozen physical-corpus result

Pre-outcome protocol SHA256 `8cdc02a7ba7517f51766112be14802f23b5692eb3bb24e2a3a2a9af7d8e6dfa0`; primary source SHA256 `c231838b8b987855a6133f5275ab2cc16ba89d9fe8979b5d92892285d98bfd30`. Both original R418 DFAs, TaskB initial previous bit 1, L=15, predeclared N=48/96/192. Integer time-expanded DFA+last-three-bit flows must exactly match all 15 per-position bit marginals, all aggregate binary 1..4gram counts, all three post-token DFA class totals, and uniform occupancy of 24 terminal joint states. Six of six integer feasibility cases passed with zero exact linear residual; 241/252/261 positive edges for TaskA, 238/256/234 for TaskB.

A separately frozen independent checker decomposed all flows into literal physical words and replayed the DFAs: **36/36 exact corpus tests passed** across both tasks, N=48/96/192, and L=15/16/35/55/335/655. All literal words, sources, original errors, negative results and independent checks are archived.

**Classical constructive extension:** If N is divisible by 48 and the joint complete-DFA/last3-bit state has N/24 words at length L, append bit 0 to half and bit 1 to half at each joint state. Every one of the 48 edges then has N/48 words, every successor state N/24, and each appended position preserves exact balanced bit, 1..4gram and DFA-class counts. The frozen N48 prefix witnesses therefore construct a nested, exactly balanced **finite corpus at every length L>=15** for both tasks. N48 is minimal for this *particular* uniform-state/equal-edge construction, not a universal minimum. At L15, the N48 witnesses have 41 unique TaskA and 40 unique TaskB strings, reaching 48 unique by L16. Samples are deterministically coupled, not iid.

## Frozen independent-seed power and compute gate

For a hypothetical independent nonzero paired seed-sign model, the exact two-sided six-stratum Bonferroni threshold is 1/120. At k=8, unanimous signs are required and power under P(positive)=0.8 is only 16.78%; k=24 yields 65.59%, k=32 yields 82.54%. Conditional 80% per-stratum power needs 47 seeds at p=0.75, 32 at p=0.8, 15 at p=0.9, and >128 at p=0.65. These are *assumed* sign probabilities, not empirical R418 effect rates or joint six-stratum replication power. All 44 exact power scenarios passed independent 80-digit mpmath checks.

Original R418 per-checkpoint exposure: 196x8=1,568 tokens. A 192-sequence equal length-mixture over L=15/35/55/335/655 needs 42,048 tokens (26.816x); 192 sequences **at each length** need 210,240 tokens (134.082x), excluding training overhead. No neural training was initiated without a viable pre-frozen non-ceiling hypothesis.

## Interpretation, preservation and next gate

R453 proved expectation-level moment feasibility; R454 proves **exact finite realized-corpus feasibility**, not neural state retention or a causal mechanism. R425, R438, R441, R442, R449 and R451 remain negative; R443's four-seed pseudoreplication warning remains binding. Original independent literal replay timed out because of quadratic DFA reparsing; a frozen implementation-only caching erratum passed 36/36. Original exact-power replay was accelerated with cached binomial rejection sets; output SHA remained identical. The clean archive replay passed 39/39 payload SHA256, 42 nested R453 payload hashes and three deterministic output hashes.

Reproducibility archive: `NOESIS_R454_Reproducibility.zip` SHA256 `dae2def56437cb072fdada4809f80e7bb9ae361583aa8a637afabb419fc49e6f` (local verified archive, not committed binary). Prior art: Dankowiakowski/Ronca NeurIPS2025 Metric Automata; Brandoit et al arXiv:2609.32447; Terzic et al NeurIPS2025 structured sparse state tracking. No new branch, PR, merge, force push, personal spend or user-laptop use.

Next R455: independently audit effective corpus diversity, deterministic coupling and disjoint holdout leakage; require prospective non-ceiling neural-specific causal hypothesis and independent checkpoint power before any training.
