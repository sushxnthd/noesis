# NOESIS R392 — exact-four-gram DFA-edge curriculum intervention (negative)

Date: 24 October 2026. One kernel: learned DFA-state retention under complete-state-neutral cycles. This is the first prospective failure of the edge-coverage mechanism, not a new general law.

## Frozen design

Pilot SHA256 `5eb05882004e2622b75adc146a315dda036199e65e6fa1b979e7f6e082526247`; training/test design SHA256 `323fd1e108faa0759567fd47a4d5aed53659bb8537ca6dd4cd1a7489029b4652`; protocol SHA256 `7ea8d62aca3caf5008553f52eacc89925fd968255dcb51e97deccb1bb4ee5409`; evaluation index SHA256 `b20c22cda4016d87cf3c64b02ff2d1d8789c6b99e63db18c63e6351d6f8b19de`. These were frozen before their relevant unseen outcomes. No holdout threshold tuning.

Trained 144 NEW networks (LSTM, GRU, MGU-style; two DFA tasks; eight shared seeds; three arms: iid, lexical-equivalent random, edge-balanced). All 144 attained perfect 196×12 short-training accuracy after 160 matched Adam updates. Lexical and balanced arms preserve the exact per-word 1–4-gram histograms and boundary three-grams. All seeds retained. The balanced arm reduced task-B symbolic-edge imbalance from 0.046877 to 0.028102 (40.05%), improving all 8 seed curricula.

## FROZEN PRIMARY FAILED

Task-B high-edge-exposure n256 suffix-1 correct: iid 429/432; lexical 423/432; balanced 420/432. Balanced−lex **−0.6944 percentage points** (8-seed bootstrap 95% [−4.8611,+2.7778] pp; frozen one-sided exact p=0.75); balanced−iid **−2.0833 pp** (p=1.0). Frozen gates required +5pp vs lexical, +3pp vs iid, p<.05 both, nonnegative each architecture. Architecture high-risk iid/lex/balanced: LSTM 141/138/132 of 144, GRU 144/144/144, MGU-style 144/141/144. **No causal generalization advantage established.**

3,888 complete neutral-cycle trajectory cases through n512 at selected horizons; 18 preselected full 0..512 traces; 648 finite-word quotient cases at depths0..4. Independent NumPy vs Numba 640/640 sampled labels agree. 19 selected n256 paths converge at 120/160 decimal digits; 3 at 220 digits. Three outcome-selected n2 arm differences conditionally certified by 100-digit `mpmath.iv` intervals (finite-string only; NOT n256/invariant-set certification). Pure Python symbolic checks 15,734 passed; exhaustive length1..14 counting lemma checks 32,766 per task passed. Independent stdlib exact seed sign-flip test reproduced p=0.75 and p=1.0.

## Structural limitation

For count-ones mod3, the j-th `1` edge must leave residue (j−1) mod3; for count-`01` mod3, the j-th `01` edge likewise leaves residue (j−1) mod3 with previous bit zero. Thus event-triggering edge counts are **invariant under unigram/bigram-matched reorderings**. The intervention can only redistribute other edges. This is an elementary counting observation, not a novel theorem. Higher-order 5+-gram and positional support were not matched; edge-count mediation is not identified.

## Next

One failed prospective test of the edge-coverage family. Next independent test should isolate movable non-event edges, pre-freeze edge-specific predictions, strengthen positional/higher-order lexical controls, and replicate across architectures and both tasks. A second substantive failure triggers mechanism change; a third kills/reformulates. No post-hoc reversal of R392.

Complete source, trained parameters, frozen protocols, raw data, independent checkers, negative results, figures, logs and manifest are in the SHA256-verified **101-file** assistant-side archive `NOESIS_R392_Reproducibility.zip`, SHA256 `c27876ebdf43ce8a8492d4e64681d761f88236a3c2a9e80eb7cef450cbd31213`. Full raw evidence is not uploaded to GitHub. No user laptop, hardware or paid API used. Draft PR #21 remains unmerged.