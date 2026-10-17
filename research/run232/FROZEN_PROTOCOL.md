# NOESIS Run 232 frozen protocol
Date: 2026-10-18. This document is committed before any training.

Question: Can fixed automatic interval-invariant discovery certify all-length reset-parity correctness in new gradient-trained tanh RNNs, with abstentions and independently verified incorrect-to-correct transitions?

Seeds: 2001 through 2024, Adam lr=0.03; 2101 through 2108, Adam lr=0.001 controls. Architecture: 3D tanh recurrent, independent 3 token matrices, double precision, h0=(0.5,-0.5,0.25). Training: exhaustive length-6 ternary words, prefix-wise BCE, 200 updates, snapshots 0/50/100/200. Deterministic CPU, one thread.

Discovery: fixed suffix depths 1/2/3, at most 500 iterations per depth; nine box paddings from 1e-10 through 1e-2. Independently verify every accepted candidate using mpmath.iv and directed Decimal interval arithmetic. Search wrong-sign witnesses exhaustively through length 8; independently verify. Unresolved means ABSTAIN.

Primary binary success: at least 4 distinct epoch0-incorrect to epoch200-all-length-certified transitions; at least 4 epoch0-and-epoch200 incorrect persistent failures; 0 accepted corrupted certificates. Otherwise FAIL or INCONCLUSIVE. Report all 32 trajectories, including abstentions and finite training accuracy.

Theory: sound all-length verification, not finite-horizon sufficiency. Learning: actual gradient-trained acquisition transitions. Competing explanation: solver/representation artifact. Cheap falsification: independently verified strict counterexample. Publishability requires priority audit, adversarial spoofing, independent proof checkers, and unseen-architecture replication. Kill after 3 substantive failures. Backups: causal intervention and task-conditioned suffix diagnostic.
