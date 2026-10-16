# Run203 — Frozen reachable output-quotient falsification

Primary (seed 307, epoch 400): **PASS** for falsification, not for positive certification. Exhaustive breadth-first search over actual states of the gradient-trained width-12 tanh RNN found the shortest nonempty-prefix transition-congruence violation at maximum prefix length **7**.

| word | true count mod 3 | model prediction |
|---|---:|---:|
| `1` | 1 | 1 |
| `1110001` | 1 | 1 |
| `10` | 1 | 1 |
| `11100010` | 1 | **2 (wrong)** |

Both first words predict class 1, but appending the same symbol 0 yields different predicted classes. The last word is an actual reachable error at length 8. The output-class quotient is therefore not transition-congruent on reachable states.

Secondary (seed 307, epoch 800): shortest max-prefix depth **8**; `1` and `11010001` predict 1, whereas `10` predicts 1 and `110100010` predicts 2 (incorrect).

Exact-binary64 mpmath outward interval proof classified all nonempty words through lengths 8 (primary: 510 words) and 9 (secondary: 1,022 words), establishing shortest collision depth. A separate directed-Decimal interval checker confirmed strict output labels for all eight witness evaluations. Numerical screens are not themselves certificates.

**Interpretation:** Both seed307 checkpoints previously had all-length *zero-only* correctness certificates. That does not transfer to mixed-symbol input; indeed the primary model fails at length 8. This kills the unrefined three-output-class quotient. It does not refute task-state quotient simulation with additional reachable-state refinement and does not prove the model lacks an algorithm on other tasks.

**Kernel status:** One active Kernel001. Next refinement must split output classes by transition behavior and prove inductive reachable closure on both symbols, or abstain. No new breakthrough claim. Original checkpoint SHA256: `5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32`. Source checkpoint data are preserved in the Run202 archive and GitHub Run199 evidence artifact 12043032970.
