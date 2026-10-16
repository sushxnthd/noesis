# NOESIS Kernel 001 — Run 201 prospective suffix-transfer test
Status: **FROZEN BEFORE SUFFIX EVALUATION**, 2026-10-16.
Parent evidence: Run 200 post-hoc all-zero invariant; seed 283, width-12 tanh RNN, epochs 400/800.
This is a new within-checkpoint prediction test, **not** an unseen-seed or unseen-architecture holdout.

## Eight-field active kernel
1. **Question:** Does the certified infinite all-zero regression reflect a task-relevant persistent state alias, observable after *nonzero* suffix perturbations, rather than a zero-only anomaly?
2. **Frontier:** Existing RNN formal verification/invariant synthesis and parity/modular counting studies already establish general possibilities; do not claim new universal theory. Run 200 certifies zero tails only. The relevant new evidence is whether the learned mechanism persists under previously unevaluated suffixes.
3. **Single exact success criterion:** At least **one suffix containing a 1**, with length 1–4, has certified final-output classification CORRECT at epoch 400 and WRONG at epoch 800, **for every** zero-run length k>=240. Only strict interval proofs count. Count is the primary scalar.
4. **Strongest competing explanation:** The all-zero error is an isolated trajectory; appending any 1 restores correct behavior, so the pathology has no robust suffix extension.
5. **Cheapest decisive falsification:** Enumerate the 30 nonempty binary suffixes of lengths 1–4. For each suffix, check all 14 invariant phases and both epochs with exact-parameter interval enclosures. Mark uncertified as ABSTAIN, never as correct.
6. **Publishable threshold:** Independent proof checker, frozen protocol, strong alternative controls, and a genuine unseen learning-transition prediction; this one experiment alone is not sufficient.
7. **Learning relevance threshold:** At least one certified nonzero suffix that converts a previously correct infinite input family to an incorrect infinite family after continued gradient training, with no architecture-coded task transition.
8. **Kill condition:** If no such suffix certifies, retire this suffix-persistence mechanism; if 3 substantive attempts to improve Kernel 001 fail, reformulate or kill.

## Frozen method and boundary
- Freeze exact two checkpoint parameter sets from Run 200; no retraining or parameter selection.
- Zero prefix k>=240. Return-map period P=14 and rational initial radius r=1e-9; use the Run 200 Taylor enclosure to cover each of the 14 phases, then interval-propagate the suffix.
- Suffix set: lexicographically all binary strings of lengths 1,2,3,4 (30 total). Primary subset: 26 suffixes containing at least one '1'. No post-hoc exclusion.
- Ground truth: count of ones mod 3. Classification is the strict maximum logit, no tie-breaking accepted.
- Primary scalar = number of suffixes with independently verified epoch400 correct and epoch800 wrong for every k>=240. Success if >=1.
- Secondary descriptive results: all certified epoch-pair classifications, minimum logit gap, abstentions, local finite-k checks; no threshold tuning after evaluation.
- Do not infer that any checkpoint globally learns or loses an algorithm. This is a certified infinite **subfamily**.
- Required independent implementation: directed Decimal interval propagation or another distinct arithmetic backend. Any checker disagreement is a blocker.
- Preserve the Run 200 archive source SHA and existing failed attempts. Do not alter frozen criteria after results.

THEORY ledger: precise all-k suffix classification obligations, closure inheritance from Run 200, strict interval margins, independent verification.
LEARNING ledger: frozen two training checkpoints, exact suffix regression count, limits, and whether the nonzero perturbation changes the inference about learned behavior.
