# NOESIS K001 — Run298 frozen targeted long-horizon falsification

Date: 2026-10-20. Parent: Run297 (frozen cross-task failure), PR #14.
This is one active kernel, not a new research direction.

1. **Question.** Do Run297's 58 unresolved, sampled-perfect gradient-trained latch networks fail on a cheap, predeclared family of long input words, despite passing exhaustive words of length <=12?
2. **Primary-literature frontier.** Finite-length accuracy cannot certify length generalization of neural formal-language learners; recurrent-network verification requires sound reachable-state reasoning. This run makes no priority/novelty claim.
3. **Scalar success.** At least 10 of the 58 previously unresolved epoch-80 networks have independently checked exact-real incorrectness witnesses of length 13–256 from the frozen pattern generator. Report every remaining unresolved network.
4. **Competing explanation.** The prior verifier was incomplete; unresolved networks may be genuinely correct, or the chosen patterns may miss their failures. A found witness proves incorrectness; no witness does not prove correctness.
5. **Cheapest decisive falsification.** Scan deterministic unary and one-switch prefix/tail families on stored trained checkpoints, then independently recompute every claimed witness using exact rational arithmetic.
6. **Publishable threshold.** >=25 new exact long-horizon witnesses, public reproduction, a mechanism-level classification of the failures, and no prior-art collision; a negative result is retained without a paper claim.
7. **Learning relevance.** >=5 new length>12 counterexamples from actual gradient-trained models with perfect sampled accuracy, not engineered post-training parameters.
8. **Kill condition.** If fewer than 3 new witnesses emerge after three substantively different frozen probes, stop long-horizon probing and reformulate around task-specific reachable-state certification.

**Frozen generator.** For each of 58 Run297 unresolved seed IDs, consider prefixes: empty; 0^k 1 for k=0..6; 1^k for k=1..6. Extend each prefix by all-0 or all-1 tails until total length 256. Retain the shortest failing word of length >=13, breaking ties lexicographically. If a float candidate fails exact checking, reject it and continue. No parameter tuning or model selection. Initial state all zeros, binary logit threshold strictly >0. Original Run297 checkpoints SHA256: `620d1852010a2889338752b8568689c709b22ba928b674a44c0b559d7b7fc473`.

**THEORY ledger.** This is a falsification-only diagnostic, not a correctness certificate. Long-horizon targeted search cannot prove unrestricted correctness.
**LEARNING ledger.** All tested parameters are actual Run297 gradient-trained epoch-80 checkpoints; no new training. Preserve unresolved outcomes.
**Provenance.** Freeze code and protocol on a research branch before running against the cohort; GitHub Actions public reproduction must retain raw rows and generated exact witnesses.
