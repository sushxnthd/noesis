# THEORY — Run 148
The prior Run147 invariant-cone proof for seed 214 is valid **only** for the repeated-plus transition. It does not imply complete ternary counting.

A rigorous exhaustive interval calculation branches over all three tokens at every step. Each multiplication and addition is rounded outward by one adjacent binary64 value. ReLU preserves interval inclusion. Because all trained parameters are exactly binary32 values stored as binary64, induction encloses every exact-real trajectory.

For all lengths n <= 12, every possible ternary word has |y_n-q_n| < 0.094712 < 0.1. At n=13, the lexicographically first word 0022222222222 has exact-rational error in [0.11199123726423954, 0.11199123726428084], and 0202222222222 has error in [0.1008466502637253, 0.1008466502637635]. Independent Fraction rollout confirms both exceed exact 1/10. Thus the global first failure is 13.

No universal certificate or novel mathematical theorem is claimed. The result is a learned-model counterexample to promoting single-token inductive structure into task-level algorithm acquisition.
