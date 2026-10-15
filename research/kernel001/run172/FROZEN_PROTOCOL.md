# NOESIS Run 172 — Frozen protocol (before new evaluation)

Date: 2026-10-15. Active Kernel 001 only. Source is the **unchanged gradient-trained** width-3 seed-415 checkpoint from archived Run 169/171; SHA256 must be checked against Run 171 manifest. No retraining or weight editing.

1. **Question.** Does the Run 171 IEEE-754 binary32 all-length pass on the single neutral cycle `(01)^k` survive changing only the *balanced neutral block*, or can a short unseen block expose an execution-semantics-specific failure in the same trained network?
2. **Frontier.** Weiss, Goldberg & Yahav, ACL 2018 (finite-precision recurrent counting); Korsky & Berwick 2019 (finite-precision RNN automata); NOESIS Run 171 exact precision reversal. Neither generic finite-state limitations nor floating-point rounding are claimed novel.
3. **Exact success criterion.** Find the lexicographically first shortest balanced block B of length 2,4,6,8, with |B|_0=|B|_1, for which IEEE binary32 scalar execution of `0^6 B^k` has a first terminal output error >0.1 for some 1<=k<=20,000, while `0^6(01)^k` retains the archived bitwise fixed point. Use token 0 increment, 1 decrement. The primary outcome is the *minimum B length*; secondary is first k. All blocks are enumerated, not selected by hand.
4. **Competing explanation.** Apparent failures are caused by hidden activation switches, incorrect floating-point operation order, or a task-label mismatch, rather than neutral-block rounding.
5. **Cheapest falsification.** Exact integer IEEE-binary32 RNE step checker on the candidate and all shorter blocks; independently reproduce with NumPy binary32 and compare bit patterns and full 3-neuron ReLU masks. Verify original checkpoint SHA.
6. **Publishable threshold.** New prospective gradient-trained checkpoints, across architectures and independent checker, priority audit and a predictive learning transition; one trained checkpoint alone is not publishable.
7. **Learning relevance.** Demonstrate a changed long-range generalization outcome without changing a gradient-trained checkpoint, solely by switching a neutral input composition that should preserve the true counter value.
8. **Kill condition.** If no balanced block <=8 fails by 20,000 cycles, or independent checks disagree, record negative result and do not broaden search within this run.

**Theory ledger:** exact statements about arithmetic semantics and restricted words only.
**Learning ledger:** checkpoint origin, training fit, whether the test changes actual learned generalization, no causal acquisition claim.
**Frozen details:** original float32 parameter values, exact scalar IEEE RNE after each addition, ReLU after each token, output float32 multiplication, terminal error threshold strict >0.1. Lexicographic enumeration over blocks in {0,1}^L, L=2,4,6,8. Check full-network masks. No parameter tuning, no change to training.
**Controlled serendipity:** only inspect unexpected mask changes within these frozen blocks; do not change primary metric.
