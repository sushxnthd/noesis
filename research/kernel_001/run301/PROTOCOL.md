# NOESIS Kernel 001 — Run 301 protocol (retrospective selection audit)

Status: **RETROSPECTIVE**, not prospectively frozen. The Run300 outcomes and exploratory candidate completions were inspected before this protocol was committed. Do not describe the resulting test as preregistered or as an empirical finding about unresolved networks.

## Precise question
Does the reported Run300 superiority of epoch-20 negative BCE over gauge-LP identify superiority over the **full** 384-network gradient-trained latch cohort, or can two evidence-compatible resolutions of the 192 unclassified checkpoints reverse the ranking?

## Frontier and competing explanation
Partial verification yields labels that are missing not at random: a sufficient cone certificate finds a subset of correct networks, while bounded counterexample search finds a subset of incorrect networks. AUC computed only on the resolved subset may be unrepresentative. Alternative explanation: BCE genuinely predicts all-word correctness, and unknown labels will preserve its advantage.

## One exact success criterion
Fix the 17 certified correct and 175 witnessed incorrect outcomes. Assign exactly **40** of the 192 unresolved as correct, remaining 152 as incorrect, in each of two hypothetical completions:
- G-completion: rank unresolved by descending Run300 gauge score (ties: ascending seed), mark top 40 correct.
- L-completion: rank unresolved by descending epoch-20 negative BCE (ties: ascending seed), mark top 40 correct.

Compute exact Mann–Whitney ROC-AUC with 1/2 credit for ties. **Success:** G-completion gives AUC(gauge) > AUC(loss), while L-completion gives AUC(loss) > AUC(gauge). Both must retain every established exact outcome and the same hypothetical prevalence.

## Cheapest decisive falsification
A standalone deterministic Python implementation reading Run300 rows, and a second independent implementation reading the same raw scores and statuses, must agree on integer twice-concordance counts and both AUCs for both completions. Verify source SHA256 before evaluation.

## Publishable threshold
Only if paired with an exact or prospectively evaluated strategy for resolving enough of the 192 unknowns; the selection audit alone is an evaluation-validity warning, not a new neural-learning law.

## Learning-system relevance threshold
All 384 are genuine unmodified gradient-trained checkpoints; do not claim any of the 192 hypothetical labels represent ground truth. Separately compute resolved-only AUC among 35 sampled-perfect networks (17 certified, 18 witnessed wrong) to expose dependence on easy-negative composition.

## Kill condition
If both completions yield the same score ranking, this identifiability attack fails. Do not claim a model-agnostic predictor without genuinely new trained-model validation.

## Evidence handling
Preserve original Run300 hashes, labels, unknowns, exact-score arrays, alternative completions, per-pair integer counts, tests, and THEORY/LEARNING ledgers. Do not rewrite Run300 or merge main. This audit is downstream of the already inspected Run300 results.

Backups (inactive): (A) exact checkpoint acquisition transitions; (B) task-observable relational quotient.
