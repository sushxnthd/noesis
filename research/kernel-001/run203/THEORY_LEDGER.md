# THEORY ledger — Run203
**Exact falsification:** the output-class partition of a real gradient-trained width-12 tanh RNN is not a right congruence on its reachable states. At epoch 400, seed307, prefixes `1` and `1110001` both predict residue 1, yet their `0` successors predict 1 and 2. The second successor is wrong for the task. Maximum prefix depth 7 is minimal, checked by exhaustive outward interval evaluation of all words through length 8. Epoch800 has the analogous minimum depth 8.

**Claim boundary:** this disproves the *coarse three-output-region quotient*, not refined reachable-state partitions, not the possibility of an all-length neural algorithm, and not all task-quotient inductive simulations. The Run202 all-zero certificates remain valid and are insufficient for mixed-input correctness.

**Next obligation:** construct and independently verify a refinement of each task-state region by its 0/1 successor signature, then prove reachable inductive closure rather than extrapolating a finite quotient.
