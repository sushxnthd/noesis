# NOESIS Run 333 — frozen two-class interval inductive synthesis

Kernel: 001-S, learned-state inductive certificates. Active question: Can an automatically synthesized task-conditioned inductive invariant certify unrestricted persistent-latch correctness of original gradient-trained width-3 ReLU RNNs?

## Frozen algorithm
For each epoch-80 checkpoint in the immutable Run326 384-seed cohort (seed 24000..24383), solve a linear feasibility problem for two axis-aligned nonnegative state boxes N (no 1 seen) and P (1 seen). Require initial zero state in N; for input 0, N maps into N; for input 1, N maps into P; and both inputs map P into P. Require strictly negative logit over N and strictly positive logit over P with margin >= 1/1000000. Use outward interval bounds of each affine ReLU transition, with linear inequalities. Candidate LP boxes are NOT certificates until an independent checker replays all inequalities using exact rational arithmetic from the original float64 weights and exact candidate box endpoints. Treat infeasible/solver errors as unresolved, not incorrect. No checkpoint modifications or training.

## Frozen criterion
>=3 NEW exact all-length certificates among the 173 unresolved Run329 endpoints, with zero false positives on the 193 witnessed-incorrect controls. Report coverage of 18 previously certified controls, and preserve every failure and solver status. Any false positive is a soundness bug, not a scientific result. Three failed synthesis families kill/reformulate Kernel 001-S; this is the first.

## Limits
Two boxes cannot represent disconnected reachable sets, output-sign correlations, or unbounded positive trajectories. Passing a box certificate is a theorem about the fixed-parameter real-arithmetic network, not evidence of when training acquired the algorithm. Existing abstract interpretation and neural verification predate this experiment. Frozen input: Run332 archive checkpoints326.json SHA256 628493d45ba6468144e4a771a8d73c01786333eca26fa8afaf25336da480fe1e; Run329 outcomes SHA256 108d462f64cbc925b0420db3fa10f121926506623062518976d02d96c355782f.
