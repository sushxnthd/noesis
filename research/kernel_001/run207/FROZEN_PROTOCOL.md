# NOESIS Run 207 — Frozen prospective pre-certificate prediction

**Status:** Frozen before any Run 207 holdout training or endpoint labels are examined. Branch `research/kernel-001-run207-precertificate-prediction` is isolated from main.

## Active kernel — exactly one

1. **Question:** Does a low-cost, task-state transition geometry score measured at epoch 50 predict which *gradient-trained* reset-parity RNNs will admit all-length, all-symbol inductive certificates at epoch 800?
2. **Primary-literature frontier:** Neural algorithm acquisition and recurrent verification are established (van Rossem & Saxe, ICML 2025; Ryou et al., CAV 2021). No claim of a novel verification paradigm or of a general algorithm-acquisition law is made.
3. **One scalar success criterion:** On 48 previously unused seeds, `AUC(geometry_score, verified_epoch800_certificate) >= 0.70` **and** exceeds the larger AUC of the epoch-50 negative BCE-loss and negative heldout64 error-rate baselines by at least 0.05. Both classes must contain at least five checkpoints; otherwise FAIL/inconclusive. Ties count 0.5.
4. **Strongest competing explanation:** Ordinary loss or long-sequence heldout accuracy predicts eventual certificate just as well; input-gated scalar architecture is unusually favorable.
5. **Cheapest falsification:** Freeze predictor and baseline definitions, train the 48 seeds, independently verify all positive endpoint certificates; compare the exact AUCs without retuning.
6. **Publishable threshold:** Frozen success plus independent replication, meaningful effect beyond matched baselines, spoof controls, unseen architecture/task, and comprehensive priority audit.
7. **Learning relevance:** Early-training scalar score must prospectively predict later all-length correctness certificates on actual gradient-trained checkpoints, not merely correlate with finite accuracy.
8. **Kill condition:** If this fails, count it as one substantive failure of the prediction subkernel. Kill/reformulate after three failures. Never relabel abstentions as incorrect models.

## Locked experiment

- Architecture/training: reuse Run206 `train.py` exactly: scalar input-gated tanh, resettable parity alphabet {0,1,2}, all 729 length-six training words, all-prefix BCE, Adam lr .03, float64, 800 epochs, initial hidden state 0.5.
- Seeds: 353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647.
- Early feature: epoch-50 checkpoint only. Enumerate all 729 length-six words; group final hidden states by target parity. Let `mu_q` be the median hidden state in group q; `D=abs(mu_1-mu_0)`. For q in {0,1}, a in {0,1,2}, `residual=max(abs(tanh(w_a*mu_q+b_a)-mu_delta(q,a)))/D`; `J=max(abs(w_a)*(1-tanh(w_a*mu_q+b_a)**2))`. Readout normalized separation `M=min(-(v*mu_0+c), v*mu_1+c)/(abs(v)*D+1e-12)`. **Frozen geometry score** `G=min(0.5-residual, M)-max(0,J-1)`. If `D<1e-10`, G=-1e6. Higher predicts certification. No fitting, feature selection, or tuning.
- Baselines at epoch 50: negative train BCE loss; negative error count from frozen 128 x length64 heldout stream. Higher predicts certification.
- Endpoint label 1 only for a successfully independently verified Run206-style two-interval, all-three-symbol inductive certificate at epoch 800. Label 0 means **uncertified**, NOT proven incorrect.
- All endpoints get synthesis attempt; every candidate acceptance must pass both Run206 independent proof implementations. Record generator abstentions, checker failures, raw checkpoint parameters, heldout errors, seeds, software versions, hashes, and smallest claims.
- No decisions from intermediate epochs may alter the locked primary score. Preserve negative results. Same-architecture finite-horizon cap spoof remains a mandatory adversarial control; a high score on it invalidates interpretation of G as a certificate, but not its explicitly predictive interpretation.

## Interpretation guardrail

Even success would show only **predictive association with certifiability in this architecture/task**, not algorithm acquisition across architectures, and not a sufficient finite-query certificate.
