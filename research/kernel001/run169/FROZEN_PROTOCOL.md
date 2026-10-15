# NOESIS Kernel 001 — Run 169 prospective protocol (frozen before training)

**Question.** Does a positive-diagonal-gauge-invariant, task-observable cycle-defect amplification score predict delayed cancellation failures in *unchanged, newly gradient-trained* recurrent ReLU counters after controlling for training fit and finite probe error?

**One active kernel.** Kernel 001; no new kernel. THEORY and LEARNING ledgers required. Backups: task-quotient bisimulation; interval multi-token gain.

**Source protocol.** Reuse Run 167 `train167.py` architecture, optimizer, target, regularizer and 1,200 steps unchanged, replacing seeds 300..307 with seeds 400..415, widths 3 and 7, 32 checkpoints total. CPU torch float32 training; NumPy float64 inference. Do not choose checkpoints based on outcomes.

**Task.** Tokens 0 increment, 1 decrement, 2 neutral. Prefix `0^6`; repeat cancellation cycle `01`. Target counter remains 6 after every cycle. Evaluate failures through k=8192, strict threshold |output-6|>0.1. Score uses *only* the trained weights and the prefix and first cycle, not outcome traces after cycle 1.

**Candidate scalar.** At h_0 after six increments, compute h_1=F_1(F_0(h_0)) and `delta=h_1-h_0`. Freeze ReLU masks along that first cycle. Let M=B_1 B_0 be the associated cycle Jacobian. Set S=max_{k in {16,64,256,1024}} log1p(|w M^k delta|). Handle nonfinite as +infinity; record all components and mask switches. This is an exact-real gauge-invariant *linearized* observable defect score, not an all-length certificate. No fitting, normalization tuning or outcome-dependent modifications.

**Baselines.** Absolute initial output error |w h0-6|, absolute one-cycle output error |w h1-6|, training MSE, and absolute 32-cycle output error from a direct 32-cycle forward probe. Use the strongest ROC AUC of training MSE, one-cycle error and 32-cycle probe as comparator. ROC AUC computed with tie=0.5. Larger score predicts failure.

**Matching.** Primary evaluation restricted to checkpoints with training MSE<=1e-8 AND absolute one-cycle output error<=1e-4. If this subset has fewer than 5 failures and 5 nonfailures overall, primary result is INCONCLUSIVE, not success. No data-dependent rematching. Report both width-specific and pooled results, including unmatched descriptive results. Check initial 32-cycle probe is not label leakage: labels begin at k=33, i.e., delayed failure after passing first 32 cycles; exclude early failures from the matched primary subset but report them as early failures. To avoid collider ambiguity, primary subset is all checkpoints passing both fit criteria and 32-cycle threshold; use 33..8192 delayed failure as outcome.

**One scalar success criterion.** On the primary subset with >=5 failures and >=5 nonfailures, ROC AUC(S) >=0.85 and >=max(AUC(train MSE),AUC(one-cycle),AUC(32-cycle probe))+0.10. Additionally each width must have >=2 of each label and AUC(S) >=0.75; otherwise inconclusive. If the full primary is adequately powered but fails these inequalities, candidate is falsified as incremental diagnostic on this protocol.

**Strongest competing explanation.** Training fit, local error or direct 32-cycle behavior predicts every failure, or frozen-mask amplification diverges from true ReLU trajectories due mask switches.

**Cheapest decisive falsification.** Execute the fixed 32 checkpoint CPU cohort, inspect matched counts and AUC. Independent implementation must recompute scores, labels and verify gauge invariance on at least 8 checkpoints under D_ii in {1,1000} using float64 with relative tolerance 1e-5 (not claiming float32 equivalence). Any mismatch is a validation failure.

**Publishable threshold.** Independent primary-priority audit; stronger cap/delayed-switch spoofs; second unseen task and architecture; numerical-semantics audit; frozen incremental prediction; explicit limits. A success here alone is not a breakthrough.

**Learning relevance threshold.** All scores/labels evaluated on newly gradient-trained unchanged checkpoints. The result must add predictive information beyond the best simple baseline, not just restate earlier known instabilities.

**Kill condition.** This is the first matched prospective attempt. Retire this scalar if adequately powered primary cohort fails criterion; if inconclusive do not claim success and move to more informative design without retrospective optimization. If three substantive attempts to strengthen this active kernel fail, reformulate it.

**Provenance.** This protocol must be committed to an isolated research branch before training or outcome evaluation. Record training log, checkpoints, SHA256, scripts, results, tests, and any infrastructure failures. Do not merge into main.
