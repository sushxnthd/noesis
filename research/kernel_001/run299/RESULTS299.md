# NOESIS K001 Run299 — exact trained-latch certificates
Date: 2026-10-20. Parent: Run298. Active kernel: task-conditioned reachable-state correctness.

**Frozen primary threshold PASSED**: 3/54 previously unresolved trained networks certified correct for every finite binary input: seeds 21832, 21903, 21926. Seed 21903 was not among the two numerically inspected pilot seeds (21832, 21926). Remaining unresolved: 51. All 74 known incorrect trained models rejected. Five negative proof mutations rejected. No new training performed.

For h'=ReLU(A_x h+b_x), y=1[v^T h+c>0], latch target q'=q OR x:
If b_0<=0 and c<0, q=0 remains h=0. For q=1, choose v>=0, T>0 and mu_x>=0 with v^T A_x >= mu_x v^T, mu_x T+v^T b_x>=T, v^T ReLU(b_1)>=T, T+c>0. Then the cone h>=0, v^T h>=T is inductive for every future input. Exact Fraction arithmetic treats stored float64 parameters as dyadic rationals.

Compact rational witnesses (independently exact-checked):
- 21832: T=9/4, mu_0=21/16, mu_1=7/5.
- 21903: T=1, mu_0=9/5, mu_1=1/2.
- 21926: T=5/4, mu_0=3/2, mu_1=6/5.

**THEORY ledger.** An exact inductive scalar-cone certificate establishes unrestricted correctness for three specific trained models that the prior box verifier left unresolved. It is not a novel general theorem or universal algorithmicity law. Inductive-invariant RNN verification is established prior art (Jacoby et al., ATVA 2020).

**LEARNING ledger.** All three checkpoints were trained with gradients in Run297; they were not engineered after training. The finding distinguishes genuine all-length correctness from finite-range heuristic behavior on this task. It does not explain the training transition or transfer to other tasks/architectures.

**Competing explanation.** The proof selects a monotone readout-growth subfamily of the latch-trained ReLU architecture. Selection bias and representation dependence remain. Public reproduction and complete artifact mirroring must be checked separately from local verification.

**Decision.** Retain K001, now with a nonzero certified-positive cross-task cohort. Next decisive run: freeze an early diagnostic before labels and evaluate its discrimination on these certified positives versus exact wrong checkpoints, or develop a stronger relational invariant for the remaining 51. Do not call this a field-level breakthrough.
