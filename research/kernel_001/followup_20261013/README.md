# NOESIS Kernel 001 follow-up (2026-10-13)

**Status:** restricted trained-model diagnostic, not a breakthrough or novelty claim.

16 CPU float64 gradient-trained two-ReLU recurrent counters, seeds 100–115, 350 Adam steps, exhaustive six-token supervised traces. Initial cap M=16. Under explicit post-training nearest-integer quantization and cap removal, exact unit-scale count certificates increased from 5/16 before training to 16/16 afterward. Gauge-aware zero-test certificates increased from 8/16 to 16/16: three untrained models already had a valid k=2 representation. With cap retained, every post-training model fails zero testing for the first time at exactly 33 tokens. All cap gradients were zero. Max final training MSE 7.59478382662917e-6.

**Exact restricted theorem.** For integer k>=1, nearest-integer recurrence h'=round(min(M,max(0,h+b_s))) with b+ in (k-1/2,k+1/2), b- in (-k-1/2,-k+1/2) implements h=k*n for every input word when M=infinity, so zero testing is all-length correct. With finite integer cap M, the globally shortest zero-test failure has length 2*ceil(M/k)+1, witnessed by +^(ceil(M/k)+1) followed by -^ceil(M/k). Exact-rational BFS verified k=1,2,3 and M=1..8, and all 16 posttraining k=1, M=16 models.

**Critical limit:** Quantization, identity skip and cap removal are supplied architecturally; gradient training learns only token biases. Original unquantized capped networks remain finite-range heuristics. No model-agnostic certificate or spontaneous algorithm acquisition is demonstrated.

**Theory ledger:** literal hidden-state equality is not necessary for zero-test correctness; gauge-aware simulation accepts k=2. **Learning ledger:** 11/16 entered the k=1 certified region during training, but 8/16 were already zero-test correct under a gauge-aware certificate before training. Strongest competing explanation is architectural supply.

**Active kernel:** Output-coupled gauge-invariant inductive simulation. Success requires accepting a genuinely trained unbounded algorithm while rejecting every finite-cap spoof, independent proof, unseen transfer, and no hardcoded target transition. Cheapest falsification: add an unbounded auxiliary latent state disconnected from decoder. Kill/reformulate after three failed substantive attempts. Backups: counterexample-guided intervention and robustness-margin boundary.

**Prior art:** https://proceedings.mlr.press/v217/el-naggar23a.html ; https://arxiv.org/abs/1808.00508 . Novelty not established. Prior successful CI: https://github.com/sushxnthd/noesis/actions/runs/38381902723 . Preserve failures; draft PR remains unmerged.
