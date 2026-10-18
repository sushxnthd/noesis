# NOESIS Kernel 001 — Run 240 frozen prospective predictor
Frozen before any Run 240 holdout training. Development-only data: Run 239 reset-latch 4D hardtanh checkpoints, epochs 100/200; no Run 240 seed or task labels used to choose formula.

## Eight-field active-kernel contract
1. **Question:** Does an early, task-conditioned recurrent state-graph growth plus behavioral margin score predict later all-length algorithm acquisition in a new gradient-trained task, beyond finite training accuracy and confidence?
2. **Primary-literature frontier:** Wang & Niepert (ICML 2019) state regularization; Oliva & Lago-Fernandez (2020) state stability; van Rossem & Saxe (ICML 2025) neural algorithm development. Finite-state emergence is prior art. No universal or priority claim.
3. **Exact success criterion:** At epoch 100, held-out resolved-endpoint ROC-AUC >= 0.80, exceeding both early finite training accuracy and early mean absolute logit confidence ROC-AUC by >=0.15, with >=70% of endpoints independently resolved (CERTIFIED or INCORRECT) and >=3 of each class. All requirements must hold. No retrospective threshold changes.
4. **Strongest competitor:** Early score is a proxy for generic optimization/saturation or certificate discovery, not actual future correctness. Compare both baselines and strict incorrect witnesses; count abstentions separately.
5. **Cheapest falsification:** 48 entirely new 4D hardtanh RNNs trained on RESET PARITY, not reset latch; 24 fixed seeds 6201..6224, each with baseline and saturation arm; independently exact-classify epoch-200 endpoints. Same architecture, unseen task family.
6. **Publishable threshold:** Independent checker, public CI, frozen transfer, spoof controls and prior-art collision; this single experiment alone cannot establish field-level novelty.
7. **Learning relevance:** Genuine Adam-trained models with epoch100 prediction of epoch200 all-length correctness vs strict wrongness, not symbolic automata alone. Include every trained model and report abstentions.
8. **Kill condition:** Three failed prospective strengthening attempts, or a function-preserving representation attack that reverses the claimed prediction; no other active kernel. Inactive backup: relational quotient verifier.

## Frozen score and baselines
At epoch100, for each network, enumerate all 3^7 ternary words of length 7; target RESET PARITY has state q_0=0, q' = 0 on token 2, q'=1-q on token 1, q'=q on token 0. Let m = min over length-7 words of signed output logit, i.e. z for q=1 and -z for q=0. Let a=mean(abs(z)) on those words. Enumerate *exact rational* hidden states reachable from fixed initial h=(1/2,-1/2,1/4,1/8) through depth seven, including initial state; cap unique count at 1001 if >1000 states. Let N be the unique state count (or 1001 if capped). Frozen predictor:
    S = m/(a + 0.01) - 0.3*log2(1+N)
Higher predicts final CERTIFIED. This was chosen on Run239 development data; no claim of independent discovery.
Baselines at epoch100: (i) train_accuracy on all 3^5 length-5 training sequences and all prefixes, (ii) mean absolute logit on the same training prefixes. Higher predicts CERTIFIED. ROC-AUC uses average ranks for ties; endpoints ABSTAIN excluded from AUC but included in coverage denominator. Primary result FAILS if AUC undefined.
## Training/evaluation protocol
Torch float64, torch.use_deterministic_algorithms(True), torch.set_num_threads(1), torch.manual_seed(seed), 4D hardtanh recurrent h'=clamp(W_token h+b_token,-1,1), z=v dot h+c, initial h as above. Adam lr=0.03; 200 updates; all 243 ternary length-5 sequences and prefix BCE. Baseline BCE only; saturation arm BCE+0.1*(1-mean abs hidden activation). Store checkpoints epochs 0,100,200. Exact dyadic interpretation of serialized float64 parameters. Independent Fraction and integer-dyadic reachability checkers on all epoch200 endpoints; no unsound positive claims, depth limit 15 and state cap 2500, abstain if unresolved. Strict incorrectness witness must be exact. Freeze outcome file hash after training.
## Controls
Two corrupted-readout controls on certified networks must be rejected; test representation invariance for a signed coordinate permutation using identical exact graph cardinalities and output logits. A positive predictive AUC is association, not causality or a universal law.
## Decision
Pass only if every primary condition passes. If failed, count one strengthening failure; preserve all negative evidence. Do not merge main.
