# NOESIS R429 — exact neutral-word lexical-alphabet identifiability obstruction

**2026-10-26 | Canonical scientific kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles.

**Pre-outcome protocol SHA256:** `da1e120467313d017f808a606c35b246541d689a8340fb06dfc87d88b87e65f4`. **Result:** classical exact obstruction independently verified; frozen TaskB-only retrospective exploratory neural gates **FAILED (6/8)**. No prospective training, IEEE execution theorem, external replication, or publication-grade neural novelty.

## Exact construction and its limits

For each specified complete DFA state q, let W_q be all 20-bit words returning q to itself and matching the original R418 u/v words in exact 1–5-gram multiplicities and first/last four bits. State-conditioned neutrality is *not* a global DFA identity on every state. Two independent enumerations (all 2^12 internal-bit patterns and Euler trails of the fixed 5-gram multigraph) gave:

| Task | States | Lexical class sizes | Original u/v state-word pairs | Missing pairs |
| --- | --- | --- | ---: | ---: |
| A, ones mod 3 | 0,1,2 | 2,2,2 | 6 | 0 |
| B, substring 01 mod 3 | 0|0,0|1,1|0,1|1,2|0,2|1 | 8,2,8,9,6,8 | 12 | 29 |
| Total | 9 | 47 words | 18 | 29 |

**Proposition (classical finite-state counterexample).** For any state q and any missing word w in W_q\{u,v}, construct two deterministic transducers with the same oracle DFA component. In the second, add a 20-phase aligned exact-word monitor armed at block starts in q. It sets a persistent hidden trap only upon reading the entire w, after which the output is shifted by +1 modulo 3. The models agree on every concatenation of u/v and all proper within-word suffix-1 probes, at arbitrary block depth, yet disagree after w. The first/last-four-bit matching rules out the only possible suffix-1 completion at cut 19. This is a finite-state **observational non-identifiability witness**, not an exact learned-RNN result.

In the **one-state/one-word per reset** query model, an adversarial single-word deviation cannot be ruled out without exposing all 29 missing state-word pairs. The count is sharp for one-step table coverage only. It is *not* a 29-query lower bound for arbitrary-length queries, and complete single-word coverage does *not* identify arbitrary infinite mixed-word semigroup dynamics. The result is an elementary classical consequence of the R419 lexical classes and the explicit monitor construction, not a new automata-learning theorem.

The original exact witness implementation verified 1,827 complete u/v histories, 73,080 within-block suffix-1 probes and 29 heldout interventions. An independent integer-bit DFA/aligned-block checker verified 36,864 candidates, 47 state returns, 3,683 complete histories, 147,320 within-block probes and 29 distinguishability witnesses. All passed. Finite checks audit the proof; the arbitrary-depth conclusion follows by the per-block invariant.

## Frozen actual-neural retrospective pilot

All **108 R418 contexts** tracked: 24 immutable LSTM/GRU/MGU float64 checkpoints, two tasks, four seeds 99960–99963, all complete states. Task A's 36 contexts have no extra lexical word, so a non-ceiling cross-task new-word challenge is **mathematically unavailable**. Task B's 72 contexts were tested on every exact class word. There were **348 additional state-word/network combinations** beyond u/v, **3,384** suffix-1 classifications over n=0,1,2,16,32,512. All source/checkpoints/raw logits, signed margins, CE and d32 preserved.

A frozen late event requires both u and v to classify correctly at the same late n while some additional w fails. A frozen late-onset event additionally requires *all* extra words to be correct at n0–2. Gates included >=6 late cases across >=2 architectures and >=3 seeds, >=2 late-onset, >=6 negative controls, and full ITT/saturation.

**Frozen exploratory primary FAILED (6/8 gates):** only **5/72** TaskB contexts had late extra-word failures (GRU 4, LSTM 1; all four seeds), versus >=6 required. **0** late-onset cases, versus >=2 required. All five failures were already detectable using early extra-word probes. There were **38** late extra-word negative-control contexts and **22/72** contexts with some early extra-word error. Four of the five late-positive contexts had all original u/v early probes correct, illustrating that lexical interventions add finite diagnostic information, but not a late-emergent causal mechanism. By state, late failures: 0|0=2, 0|1=0, 1|0=2, 1|1=0, 2|0=0, 2|1=1. No prospective cohort or retuning.

**Independent audits:** 3,384/3,384 exact streaming-oracle labels; 1,296/1,296 unchanged R425 u/v boundary labels and shifted logits (max difference 0); six SHA-selected TaskB cases, independent NumPy/Torch 12/12 and mpmath 120/160/220-digit 18/18, max selected logit difference <3e-15. These are finite numerical checks, not directed MPFR infinite-horizon certificates.

**Prior art:** Chow 1978 FSM conformance testing (DOI 10.1109/TSE.1978.231496); Angluin 1987 membership/equivalence-query automata learning (DOI 10.1016/0890-5401(87)90052-6); Moore/Myhill–Nerode distinguishability. No neural mechanism novelty claimed.

## Preservation and decision

**Complete archive:** `NOESIS_R429_Reproducibility.zip`, SHA256 `df7d4878f3449870973c84012c98b841f555661a4504363591b8306cc7d576fd`. **143 ZIP entries**, 142 SHA256-manifested payloads; full 108 raw cases, frozen/source, all negatives, independent/error logs, immutable R428 dependency and nested R418 checkpoints. Recursive verification passed through 20 dependency ZIPs (16 SHA256 manifests; four older unmanifested ZIPs checked by CRC and parent dependency hashes). Full raw is local, not GitHub.

**Decision:** Retire a cross-task new-lexical-word hypothesis for these exact R418 20-bit 5-gram classes; do not relax R419 matching, retune R420/R422 geometry, or reuse R428 probe thresholds. A future candidate needs a genuinely distinct causal neural mechanism and a disjoint pre-frozen prospective replication design. No personal spending or user-laptop access.
