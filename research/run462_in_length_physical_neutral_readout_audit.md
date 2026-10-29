# NOESIS R462: eight-bit physical neutral-word readout audit

**Status:** Frozen original-checkpoint neural experiment; primary multi-model discovery gate FAILED. No neural breakthrough, no new training, no mediation claim.

**Frozen before neural outcomes:** symbolic design SHA256 `15657b2f8c13cbce257660e0fb96a9818632b33c362ec9e0d28252a156c48041`; protocol SHA256 `f25d2968dd2b3cfe80d0805497edb9519b253ca6170f7176812444d06de5fdd9`. Original R418 training SHA256 `4eedb30560a39b01ec26547b66c4c0cc960411538d32989066ba0dd817f9f6b8`. Both tasks, all three architectures, all four seeds 99960–99963, all 256 physical eight-bit inputs per model, 6,144 total readouts. No training or hardware spend.

**Physical neutral interventions:** Task A: prefixes 000/111, all four length-four designated-neutral words with three ones, suffix 1 (12 same-prefix/same-unigram pairs/model, oracle 1). Task B: empty prefix with initial previous bit 1, all eight length-seven complete-state-neutral words, suffix 1 (nine same-unigram pairs/model, oracle 0). This is a **single-cycle**, within-training-length intervention, not a late-onset or two-cycle test.

| Outcome | Task A | Task B |
|---|---:|---:|
| Panel word errors, 96 readouts | 0 | 14 |
| Same-q class-discordant pairs | 0/144 | 3/108 |
| Full eight-bit universe errors | 1/3072 | 121/3072 |
| Frozen strong cross-task/architecture/seed gate | FAIL | FAIL |

All 14 Task B panel errors occurred in original LSTM seed 99961 (7) and 99962 (7). All three class-discordant pairs occurred in seed 99962; none had both arms in its training set. These original checkpoints were undertrained: their archived eight-token training accuracies were 95.47% and 95.73%, while exact replay found final-token training accuracies 76.53% and 80.61%. Therefore the observed within-length errors cannot be separated from ordinary short-training underfitting. Other ten Task B checkpoints and all twelve Task A checkpoints made zero panel errors. No cross-architecture or cross-task discovery.

**Independent verification:** Separate NumPy per-token recurrence matched all 6,144 Torch float64 readouts, max absolute logit error 1.821e-14, zero class flips. All 252 literal same-DFA-state/same-unigram pairs, all 6,144 DFA labels, 24 training-support checks and 192 identical-input controls passed. Original training X/Y hashes and all 24 archived training accuracy/CE records replayed exactly (max discrepancy zero). Five deterministic clean output SHA replays passed. Original JSON serialization error and implementation-only correction preserved without retuning.

**Caveats:** Seed ID is the replication unit, not pairs; four seeds cannot support population significance (two-sided exact sign-flip p floor 1/8). Same-unigram matching does not isolate path order or higher-order lexical effects. Training length match does not imply training exposure. No prospective external checkpoint replication.

**Reproducibility:** complete local `NOESIS_R462_Reproducibility.zip` SHA256 `0ffff4003565b9efa75ef85d70dbefe830ef937ec5db5b7c8ca585b536961cb8`, including original frozen protocols, original and corrected sources, all logits/labels/seeds/negative cases, independent checker, replay, and immutable nested R461->R404 checkpoint archive. Verified 38/38 local payloads, 23/23 nested R461 payloads, five deterministic replay outputs.

**Prior art:** Dankowiakowski & Ronca, Metric Automata Theory (NeurIPS 2025); Brandoit et al., Length-Independent State Tracking (arXiv:2609.32447); Buitrago Ruiz & Gu, Understanding and Improving Length Generalization (ICML 2025).

**R463:** Retire R462 as breakthrough candidate. Audit Task B LSTM final-token underfitting without retuning prior models; seek a distinct non-ceiling neural-specific physical hypothesis with independently trained seeds, disjoint balanced corpora, feasible free compute and adequate seed-level power. Do not infer DFA-path mediation.
