# NOESIS Kernel 001 — Run 182 (frozen before held-out evaluation)

**Question.** Does the Run 180/181 32-cycle short-horizon drift extrapolator misclassify long-horizon neutral-composition correctness in a new *gradient-trained gated residual recurrent* architecture?

**Literature frontier.** Weiss, Goldberg & Yahav, ACL 2018 (https://aclanthology.org/P18-2117/) establish important differences between finite-precision recurrent counting architectures, including limitations of conventional GRUs; Merrill et al., ACL 2020 (https://aclanthology.org/2020.acl-main.43/) formalize architectural expressivity hierarchies. A gated *residual* ReLU recurrence is NOT a standard GRU and must not be described as one.

**Primary scalar.** Count baseline classification mistakes on 64 prespecified model-snapshot observations (2 widths × 8 seeds × 4 checkpoints), each labeled correct iff all four held-out balanced compositions pass 2,048 cycles. Eligibility requires training MSE <= 1e-3. Success requires >=8 mistakes among >=32 eligible observations; otherwise negative/inconclusive.

**Strongest competing explanation.** Any observed failures are explained by training MSE, initial 32-cycle drift, or the architecture's saturation/finite-precision behavior rather than acquired algorithms.

**Cheapest falsification.** Train all 16 small networks with fixed seeds, freeze all checkpoints and baseline predictions before 2,048-cycle replay; compare against labels and a training-MSE baseline. The primary 32-cycle extrapolator is least-squares affine prediction from per-composition signed output errors at repetitions 8, 16, 24, 32; forecast extrema over repetitions 1..2048; predicted correct iff all four compositions stay within absolute error <=0.1. Baseline fit uses NO held-out repetition >32.

**Publishable threshold.** >=8 errors on eligible observations, independent replay and prospective replication on unseen seeds, multiple architecture families, and a mechanism-derived improvement. A mere failure of this baseline is not a breakthrough.

**Learning relevance.** Models must be trained by gradient descent on all 3^6 length-six reflected-counter sequences, checkpointed without modification; record training MSE and held-out outcomes. Training is done on assistant-side CPU, no user hardware.

**Kill condition.** Fewer than 32 eligible observations or <8 baseline errors kills the architecture-transfer challenge as presently formulated. Three substantive failures kill/reformulate this kernel.

**Architecture.** h_next = ReLU(h + sigmoid(h G^T + GE[x]) * (2 tanh(h A^T + E[x]))); y = h·w. Parameters A,E,G,GE,w optimized with Adam, width in {3,7}, seeds 401..408, 1,200 epochs, lr=.025; checkpoints at {200,400,800,1200}. Training target: reflected count, 6-token exhaustive ternary words; regularizer 0.1 on noop transition. Fixed prefix 000000; held-out neutral blocks 000111, 001011, 111000, 001101; threshold 0.1, horizon 2048. float32 stored parameters, float64 numerical replay. Seed generation and all parameters archived.

**THEORY ledger.** The frozen test is finite-horizon and has no positive universal theorem. Numerical execution semantics must be explicit.

**LEARNING ledger.** An observed fail-to-pass training transition is bounded behavior, not proof of an unbounded algorithm.

**Provenance.** Run 181 negative remains immutable. CI workflow must test executable research checks, not merely generic placeholder tests.
