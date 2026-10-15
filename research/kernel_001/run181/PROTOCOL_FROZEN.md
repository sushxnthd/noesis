# NOESIS Kernel 001 — Run 181: frozen training-trajectory transition test

Status: PRE-EVALUATION PROTOCOL. This file is committed before training trajectories and held-out evaluation. Do not change it after observing outcomes; corrections must be separate append-only amendments.

1. **Precise question.** Does a task-observable neutral-composition distinguishability score, measured during actual gradient training, predict held-out long-horizon balanced-word correctness better than training MSE and a 32-cycle drift baseline?
2. **Primary-literature frontier.** Weiss, Goldberg & Yahav (ACL 2018) demonstrate counting/finite-precision limitations of RNNs; neural algorithmic generalization and recurrent verification have extensive prior art. A generic compositional-probe score is NOT presumed novel.
3. **Single success scalar.** On training-fit-matched snapshots (train MSE <= 1e-3), ROC AUC of -log10(D+1e-15) for all-four-held-out-words correct at 2,048 cycles must exceed max(AUC of -log10(train MSE+1e-15), AUC of -log10(B+1e-15)) by >=0.05, with >=8 positives, >=8 negatives and >=2 within-seed fail-to-pass transitions. Otherwise FAILURE/INCONCLUSIVE; no post-hoc threshold changes.
4. **Strongest competitor.** Training MSE; B=max absolute output error over the first 32 repetitions of 01, evaluated after prefix 000000. A trivial training-progress explanation must be rejected.
5. **Cheapest decisive falsification.** Train six ReLU recurrent cells on all 3^6 sequences using frozen Run169 protocol (Adam lr=.025, 1200 steps, regularizer .1, float32 torch CPU, one thread). Widths [3,7], seeds [401,405,409]. Record snapshots at steps [0,20,50,100,200,400,800,1200]. Evaluate unseen repeated balanced words 000111, 001011, 111000, 001101 after prefix 000000 for 2048 repetitions; failure when |output-6|>0.1. A snapshot passes only if all four words pass every repetition.
6. **Publishable threshold.** Surviving frozen superiority on unseen training seeds, architectures and a distinct task family, independent implementation, adversarial spoof resistance and priority audit.
7. **Learning relevance threshold.** Real gradient-trained model snapshots, not just exact automata. A positive result needs within-seed learning transitions and improved predictive information beyond the baselines.
8. **Kill condition.** If no improvement, kill the neutral-composition scalar as an acquisition predictor; keep bounded verification infrastructure only. After three substantive failures of any reformulated active kernel, kill/reformulate kernel.

**Probe D:** Starting from the model's hidden state after 000000, for each neutral word in {01,0011} and each suffix in {empty,0,1,2,00,01,10}, take the maximum absolute difference between the output after suffix from the neutral-word successor and the output after the same suffix from the original state. This is output-based, not a hidden-coordinate norm.

**Baseline B:** max_{1<=k<=32}|output(000000(01)^k)-6|.

**Evaluation semantics:** torch CPU float32 for gradient updates; float64 NumPy evaluation using stored float32 parameter values; strict >0.1 failure threshold. No hyperparameter tuning, cohort selection or score fitting using held-out outcomes. Use exact rank-based ROC AUC with average ties; when class counts insufficient report inconclusive.

**Raw provenance:** Preserve each snapshot's A,E,w and train MSE; full per-word first-failure clocks, scores, exact config, code, package versions, hashes, independent checker, failures, and CI state.

**Theory ledger:** Output-probe equivalence over finitely many suffixes is necessary on sampled states but cannot certify an unbounded algorithm. No positive theorem claimed.
**Learning ledger:** Training-epoch association is not causal acquisition. This run asks whether a discriminating empirical transition signature exists at all.

No spending; compute in assistant environment only. Main branch remains untouched.
