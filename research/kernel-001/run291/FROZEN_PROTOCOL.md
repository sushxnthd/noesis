# NOESIS K001 — Run291 prospective width-3 architecture transfer (FROZEN)

Frozen before any Run291 training, early scores, or endpoint labels. Run290's normalized two-box LP distance is extended mechanically from 2 to 3 ReLU hidden units, with no outcome-dependent feature selection, task change, or hyperparameter fitting.

## Eight-field active kernel
1. **Question:** Does gauge-normalized invariant-feasibility distance measured at epoch 20 predict independently established unrestricted correctness at epoch 80 in a *new gradient-trained width-3* RESET/TOGGLE ReLU RNN, beyond early BCE?
2. **Primary frontier:** Inductive invariant verification of RNNs and positive-rescaling symmetries are known; Runs 288/290 provide only within-width-2 predictive evidence. Finite-horizon perfect accuracy is spoofable by gradient-trained RNNs.
3. **Single exact success criterion:** On resolved epoch-80 labels, ROC-AUC(normalized LP score) - ROC-AUC(-BCE) >= 0.10, with >=10 exact certificates and >=30 exact incorrectness witnesses. Unresolved endpoints abstain and are reported.
4. **Strongest competing explanation:** The predictor recognizes only a restrictive task-specific box-invariant geometry; changes in width or unresolved-case selection destroy its advantage.
5. **Cheapest decisive falsification:** 256 neutral-Gaussian width-3 RNNs, score at epoch20, independently verify epoch80 correctness/witnesses. Check against BCE and raw LP distance.
6. **Publishable threshold:** Frozen criterion passes, independent exact checker, gauge tests, public deterministic reproduction, primary-prior-art audit, no claim beyond width-3 transfer.
7. **Learning relevance threshold:** >=2 trajectories sampled-perfect but exactly incorrect at an earlier checkpoint become all-length certified after ordinary gradient training. Record failure if not met.
8. **Kill condition:** If this width-3 transfer fails or has inadequate resolved support, retire the claim that current normalized LP score is architecture-general. After three substantive failures to strengthen reformulated K001, kill/reformulate the active kernel.

## Frozen protocol
- Seeds: 21440..21695 inclusive (256); float64; torch deterministic; 3 hidden ReLU units; 28 scalar parameters (2*3*3+2*3+3+1); Gaussian N(0,0.5^2), generator seed+51000; no task-specific initialization.
- Task: RESET=0, TOGGLE=1; target parity after each token; 160 random binary sequences length 6 per seed, plus four fixed length-six padded 2-token prefixes; BCE over all tokens.
- Adam lr=0.025, 120 epochs; snapshots epochs 0,20,40,80,120. Use the same training and checkpoint semantics as Run290.
- Early diagnostic: canonicalize positive diagonal ReLU gauge using d_i=1/max_x|b[x,i]|; extend Run288 relaxed two-box LP to width 3 with all 2^3 parity-one zero masks, delta=0.05, box bounds [0,1000], nonnegative slack. Higher score = negative minimum slack. Early scores must be hashed and persisted before endpoint evaluation.
- Endpoint labels: independently verified strict all-length two-box inductive certificates (sufficient only), exact rational word counterexamples (incorrect), otherwise unresolved. Never label abstention incorrect. Use all 256 in denominators for coverage.
- Secondary controls: unnormalized score, early sampled accuracy, -parameter norm, gauge-equivalent representations. Secondary analyses cannot change the primary pass/fail.
- Exact-real semantics: stored float64 parameters interpreted as dyadic rationals, not indefinitely rounded IEEE-754 recurrence.
- Freeze random-witness generator separately from training and use reset-toggle plus deterministic mixed-word candidates. Exact verification must check all positive/negative claims.
- If early-score file is not committed before evaluating endpoints, mark the study **NOT PROSPECTIVELY FROZEN** even if script order is correct.

## THEORY ledger (before results)
Positive diagonal ReLU gauge symmetry applies to any width with nonzero per-unit bias maxima. Width-3 two-box LP soundness requires independent rational-arithmetic checking. Completeness not claimed.

## LEARNING ledger (before results)
New width-3 networks have not been trained at protocol freeze. No endpoint labels are known.

## Backup kernels (not active)
1. Representation-independent quotient-state simulation with sound abstention.
2. Cross-task prediction on a distinct reset-latch algorithm.

Wildcard effort capped to cheap probes only, outside the frozen cohort.
