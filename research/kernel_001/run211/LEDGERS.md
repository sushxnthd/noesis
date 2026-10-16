# NOESIS Run 211 — THEORY and LEARNING ledgers

## THEORY
**Verified:** For the stored binary64 weights of the fully coupled 2D tanh RNN trained at seed 773, epoch 800, the input `010011001100100` has reset-parity label 0 but strictly positive output logit. The primary mpmath.iv and independent directed-Decimal interval implementations enclose the exact-real logit in positive intervals, both near 0.78649425024194519. This is a real counterexample, not an interval-box false positive.

**Numerical only:** Exhaustive float64 evaluation of all ternary words through length 14 found zero errors and a smallest length-14 signed margin of 1.7818091041612139. It supports but does not rigorously prove that the length-15 witness is globally shortest. The beam found the witness at length 15. The all-length behavior of seed 787 remains unresolved.

**Smallest claim:** An all-length inductive verifier's abstention on a gradient-trained 2D network can conceal a short, independently certifiable adversarial error beyond the finite training horizon and beyond the Run 210 length-10 probe. No new universal acquisition law is established.

## LEARNING
The network was trained by full-batch Adam for 800 epochs on every six-token ternary reset-parity word, supervising each prefix. It achieved 100% finite training accuracy, and Run 210 found no numerical errors through length 10. Nevertheless, it fails on a length-15 structured input. This demonstrates a concrete learned heuristic failure in a coupled recurrent model and reinforces the need for adversarial verification rather than interpreting invariant abstention as either correct or incorrect.

**Competing explanation:** The failure is a rare out-of-distribution path, not evidence of a generic long-zero memory-retention law. The word is not of the scalar `10^k1` family. Do not generalize this result to all coupled RNNs.

## Decision
Kernel 001 retained; architecture-universal scalar failure-signature hypothesis weakened. The next experiment should freeze a mechanism-derived signature on an unseen trained cohort rather than tuning this attack on the same checkpoint. No field-level breakthrough claim.

## Provenance
Run 210 original source and exact checkpoint remain in the parent research branch. Run 211 protocol was committed before search. Numerical beam, exhaustive enumeration, and both independent proof implementations are committed in this branch. Preserve failed workflow attempts and follow-up fixes.
