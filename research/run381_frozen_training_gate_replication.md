# NOESIS Run 381 — prospectively frozen anti-persistence replication

**Original local protocol SHA256:** `76e3835ea916dd7cb383ebc0da1013dcd2e360c01093ff6db4b2b138dab737f8`. Frozen **before** any Run381 training or long-horizon evaluation; a pre-training symbolic-oracle check corrected two invalid *secondary* words before final freezing. No outcome-based protocol changes.

This is a new hypothesis prompted by Run380 exploratory state geometry. Run380's primary remained failed (p=.0625). It is not retroactively rescued.

- Fresh seeds: count-ones-mod3 50000–50007, count-'01'-mod3 51000–51007. No replacements.
- Each seed: three identical-initialization width-5 LSTMs, 258 parameters, identical 196 length-eight training strings, Adam .035 for 240 epochs. Arms baseline, persistence pressure `0.5 mean((f-.9)^2)`, anti-persistence pressure `0.5 mean((f-.1)^2)`. Final epoch240 intent-to-treat, including imperfect short-trained seeds.
- Primary DFA representatives: ones `0`, `1`, `11`; substring01 `1`, `011`, `01011`. New 12-bit primary cycles: `010100100111` and `111011011001` respectively. Symbolic oracle verifies state preservation for these representatives; the task-B word is not a global six-state identity.
- Primary outcome: at n256, per-seed mean correctness across three representatives, anti-persistence minus persistence; 16 independent seeds are statistical units.
- **Conjunctive success criteria:** mean difference >=.25; exact paired one-sided sign-flip p<.05; mean difference >.1 in each task; *every* model short-training accuracy >=.995; |mean short-CE difference| <=.03; mean forget-gate activation persistence minus anti-persistence >=.05; and agreement at 120/160 digits for every primary label. No post-hoc threshold changes.
- Strong controls: baseline arm, seed-matched training strings/initialization/optimizer/width/parameters, exact DFA oracle, two independent float64 recurrences, n32/n64/n128 failure onset, full training-state coverage and raw d32/readout margin. Independent Decimal and 220-digit selected checks planned if resources permit.
- Limitations: regularizer changes the optimization objective, not only a single gate; even success would not establish architecture-general causality, a new theorem, or publication-ready novelty.

One persistent branch and existing draft PR #21; no merge or force-push.
