# NOESIS R474 — physical neutral-cycle order commutator and neural DFA-state quotient falsification

**Status:** Frozen neural-checkpoint falsification, primary strong gate FAILED. Not a novel neural causal mechanism, independent-seed replication, or population claim. No new training/spending/user-device access.

## Frozen experiment

Protocol SHA256 `680cc29df02a30ad8d579945e23415c8ee8a33128b0c76387c0e654c9cfad107`. Original source SHA256 `8779c022472326c16020b4ad28aedb9dd1811204e3968547430370b640210fae`. Independent Torch source SHA256 `a27e241741539b8f3448b1176e79c083da2e01f76d10e344f689cb15c435fb3e`.

All 24 original R418 checkpoints, Task A all 256 length-eight prefixes, Task B all 128 length-eight prefixes ending in zero. For each prefix p, compare physical paths pABs and pBAs with two individually complete-DFA-state-neutral seven-bit cycles, same length and same total unigrams, for all 15 suffixes s of lengths 0..3. Task A A=0000000, B=0111000, q-changing C=0000001. Task B A=0000000, B=0101010, q-changing C=0011100; Task B AC preserves unigrams and terminal bit relative to AB. The compared physical words have lengths 22..25, beyond original training length eight.

**Necessary condition:** If the neural predictor's output is an exact function only of the true complete DFA state, its predicted label must agree on pABs and pBAs for every suffix. A disagreement is a finite natural-input counterexample to that exact quotient, but not a causal hidden-state mediation result.

## Neural results

- Task A: 2,110/46,080 same-q neutral-cycle prediction discordances; 43,207/46,080 pairs both oracle-correct; 42,877/46,080 q-changing controls both correct.
- Task B: 4,986/23,040 same-q neutral-cycle prediction discordances; 13,414/23,040 pairs both oracle-correct; 10,182/23,040 q-changing controls both correct.
- **Total 7,096/69,120 discordant pairs, across 15/24 checkpoints.** Input pairs are correlated and not independent seed replicates. Prespecified behavioral and strong geometry cross-architecture gates both FAILED (Task A 2/3 architectures; Task B 0/3).
- Exact physical witness for Task B LSTM seed 99960: `0000001000000000101010` and `0000001001010100000000` have the same complete DFA state (1,0), same length and unigrams, but frozen neural predictions are 0 and 1. Minimum literal binary64 winning margin 2.12105536.
- Independent Torch float64 recurrence checked 207,360 logits and 13,824 cycle-end hidden states against primary NumPy (maximum logit error 6.04e-13, hidden error 1.49e-13, zero class flips); all 207,360 literal DFA labels checked. All 15 finite counterexamples separately verified using exact rational arithmetic on archived binary64 logits (minimum winner margin 0.00428686). This is not an exact-real transcendental RNN certificate.

## Separately frozen postprimary controls

Protocol SHA256 `f0f79ca9cac5dd32965a3f21a9f5769ee39bc939512d9858669646747515ab8d`. All 48/48 Task A original-training-length (eight-bit) neutral-cycle order pairs were both correct, with zero discordances. No analogous Task B two-cycle test fits in original length eight (R461). At length 15 some Task B checkpoints already lose oracle accuracy after one neutral cycle. Thus length shift, training exposure, and lexical effects remain unresolved; no claim that the second cycle uniquely caused failures.

## Boundary and next step

Prior art: Metric Automata Theory (NeurIPS 2025); Buitrago/Gu (ICML 2025); Brandoit et al. arXiv:2609.32447; Geiger et al. (JMLR 2025); *The Automaton Underneath* arXiv:2609.18966. The quotient condition is classical, not a new general theorem. R472's nonrecurrent parallel scan and R473's nonrecurrent threshold circuit can both satisfy the behavioral oracle, so this does not identify recurrence as a necessary mechanism.

Next R475: do not repeat static/suffix/lexical surrogate probes. Only train a new cohort after a non-ceiling pre-frozen neural-specific transition intervention, at least 32 independent seed clusters, exact seed-level power, disjoint exposure-balanced corpora, and feasible free CPU are demonstrated. Otherwise pursue a distinct neural-specific necessary condition. Preserve all raw outcomes, source, independent checks, negatives and immutable historical artifacts in the local reproducibility archive.
