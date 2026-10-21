# NOESIS Run317 — frozen original-head finite-range falsification

**Parent:** Kernel 001; prior Run316 exact delayed hidden-state collision. This is an original-checkpoint evaluation, not a post-hoc readout-calibrated hybrid.

1. **Question:** Among the 57 epoch-80 sampled-perfect gradient-trained Run315 networks, do untouched trained checkpoints classify every nonempty binary word through length 6 correctly but fail at lengths 7–10?
2. **Frontier:** Weiss et al., ICML 2018 (automata extraction); Jacoby et al., ATVA 2020 (invariant verification); prior NOESIS Runs 315–316 (retention predictor falsified, exact delayed collision with bias-adjusted head). No novelty is claimed for the basic finite-horizon impossibility.
3. **Exact success criterion:** Count of previously unresolved, untouched epoch-80 checkpoints with *all* 126 words of lengths 1..6 correct and at least one exact signed-logit error at length 7..10 is >=1. This is a retrospective, seed-fixed failure-mode audit, **not** a prospective predictor.
4. **Strongest competitor:** Failure could be due only to output-head calibration rather than recurrent memory loss.
5. **Cheapest falsification:** Exact rational breadth-first prefix enumeration of original parameters, first failure witness and signed margin; search same-length opposite-label hidden-state collisions for each qualifying seed, reporting absence if none found.
6. **Publishable threshold:** Independent checker, immutable checkpoint provenance, exact minimal witnesses, adversarial tests, and evidence that the result is not already established by existing neural generalization literature. A mere finite-range counterexample is insufficient for a field-level claim.
7. **Learning threshold:** At least one actual gradient-trained untouched checkpoint must satisfy the exact success criterion; record its original training BCE/accuracy and all earlier checkpoint statuses.
8. **Kill condition:** If no original checkpoint satisfies the criterion, mark this probe failed; if three substantive attempts fail to strengthen K001 beyond training loss/finite horizon, reformulate or kill K001.

**Frozen cohort:** Exactly the 57 seed IDs whose epoch-80 sampled training accuracy equals 1.0 in the original Run315 `checkpoints315.json`, no endpoint-based selection. Use the original epoch-80 `p` vectors and no modifications.

**Exact arithmetic:** Decode each stored Python JSON float into `fractions.Fraction.from_float`, ReLU = exact max(0,z), output threshold positive iff logit > 0. Correct label is OR of all input bits. Enumerate all words in length/lexicographic order through 10, stopping early per model only after recording whether all <=6 are correct. Track smallest failing word and first task-opposed equal-length hidden-state collision through 10, if computationally feasible. If resource-limited, explicitly report incomplete, never extrapolate.

**Precommitted scope:** No fitting, no new training, no modifying checkpoints, no changing horizon after outcome inspection. Archive raw per-seed results, independent reimplementation, mutation tests, SHA256 provenance, THEORY and LEARNING ledgers. No merge until GitHub public reproduction.
