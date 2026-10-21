# NOESIS Kernel 001-R — Run 329 frozen protocol (2026-10-22)

**Question.** Can score-blind adversarial continuation expose a new output-level failure in the 174 original gradient-trained RNN checkpoints left unresolved after Run 328, without using the frozen predictor scores?

**Input lock.** The Run 328 archive's `input/checkpoints326.json` and `results/updated_outcomes328.json`; checkpoint SHA256 `628493d45ba6468144e4a771a8d73c01786333eca26fa8afaf25336da480fe1e`. Only epoch-80 weights, unmodified.

**Algorithm lock.** Evaluate (a) all-zero and initial-one zero-tail words to length 512; (b) one-bit-at-a-time beam search for words that have already contained 1, maximizing negative readout excursions, with deterministic width 48 and depth 256. Preserve activation-pattern and state-norm diversity; use seeds 329 and 1337 for deterministic exploration. Candidate errors are *only* valid after exact binary64-as-rational replay of the complete witness. Minimize valid words by deterministic deletion. An independent implementation must recheck the final witnesses. No access to frozen early predictor scores during search.

**Scalar success.** At least one previously unresolved original network acquires a new exact failure witness (otherwise a negative search result, not a correctness certificate).

**Competing explanation.** Search heuristics are finite and biased; lack of a witness cannot imply correctness. Observed late failures may be simple readout instabilities rather than algorithm acquisition.

**Publishable threshold.** A new mechanism-derived predictive invariant with independent verification, cross-architecture tests and selection-bias accounting; this search alone cannot meet it.

**Learning relevance.** All targets are real original gradient-trained epoch-80 networks, no post-training calibration.

**Kill.** No newly adjudicated failures => stop this beam/tail search family rather than increasing horizon again; retain Kernel 001-R until three predictor failures.

**Evidence.** Commit the full script, exact witness JSON, independent checker, negative outcomes, both ledgers, hashes and CI state on this isolated research branch. Do not merge or claim field-level breakthrough.
