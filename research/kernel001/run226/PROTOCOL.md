# NOESIS Run 226 — frozen label-resolution protocol (2026-10-17)

Active kernel: 001 (functionally invariant behavioral acquisition diagnostic). This run is **not** a new prospective architecture transfer; it is a pre-specified falsification of the Run220 diagnostic using additional independent labels from already frozen 3D gradient-trained checkpoints.

## Precise question
Do exact short-word counterexamples resolve enough previously unclassified Run220 networks to establish whether the frozen Run220 task-derived suffix score outperforms both equal-budget sign-only baselines?

## Frozen inputs and analyses
- Input: immutable `CHECKPOINTS.json` and `EVALUATION.json` from Run220 archive, verified by SHA-256; use epoch 50 and epoch 200 parameters without retraining.
- Enumerate all 3^n ternary words for each n=1,...,9 in increasing n and lexicographic order for every checkpoint, with float64 **only for candidate discovery**.
- For every candidate wrong word, independently verify its sign using (a) mpmath interval arithmetic with exact binary64 parameter conversion and (b) directed Decimal interval arithmetic; do not count float64-only wrong words.
- Enumerate all words shorter than each claimed minimal witness using both independent checkers; if full rigorous enumeration is infeasible, label witness as *verified counterexample, minimality unverified*.
- Preserve all earlier independently proven positive all-length certificates; **absence** of a witness is UNRESOLVED, never CORRECT.
- For any seed, define ACQUIRED iff epoch50 INCORRECT and epoch200 CORRECT; PERSISTENT iff both INCORRECT; EARLY_CORRECT iff epoch50 CORRECT; otherwise UNRESOLVED.
- Reuse frozen Run220 challenge/uniform/shuffled words and accuracy scores verbatim; do not tune diagnostic.
- Scalar success criterion: >=4 ACQUIRED, >=4 PERSISTENT, <=8 UNRESOLVED, and AUROC(challenge) - max(AUROC(uniform), AUROC(shuffled)) >= 0.10. Otherwise record failure or inconclusive exactly as appropriate.
- Competing explanation: target suffix probes merely select harder words or benefit from sample composition.
- Cheapest falsification: rigorous verification of previously unknown epoch50/200 counterexamples.
- Publishable threshold: independent checks, all evidence, frozen score re-evaluation, novelty audit, unseen-architecture validation.
- Learning relevance: all labels are checkpoints of gradient-trained networks, not abstract machines.
- Kill: third unsuccessful *prospective* transfer/causal test kills or reformulates Kernel 001; this retrospective label audit does not substitute for one.

No personal spend or user-device compute. No change to `main`. Preserve negative results and failed checks. No breakthrough claim from this retrospective analysis.
