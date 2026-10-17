# NOESIS Run226 frozen protocol (2026-10-17)
Active Kernel 001 only.
1. Question: Is seed1301 epoch100 wrong on a finite word, or certifiably all-length correct?
2. Literature frontier: Ryou et al. CAV2021 RNN verification; van Rossem & Saxe ICML2025 learned infinite generalization.
3. Success: independent rigorous proof of one incorrect prefix OR independent inductive all-length certificate.
4. Competing explanation: interval-box abstraction may fail despite correctness; finite probes miss late errors.
5. Cheapest falsification: exhaustive ternary words length 1..12, length-lexicographic, using vectorized float64 as untrusted generator; independently check shortest wrong candidate by directed Decimal and mpmath.iv. If none, attempt k=4,5 inductive boxes at eps=0 and 0.003, independently verify.
6. Publishable threshold: not publishable alone; require novel prospective cross-model predictor or causal mechanism, independent verification, spoofs and primary audit.
7. Learning relevance: same gradient-trained RNN wrong at epoch50, robust all-length correct at epoch200.
8. Kill: no rigorous wrong word through 12 and no inductive proof k<=5 -> mark UNRESOLVED and stop.
Frozen checkpoint: run223/CHECKPOINTS.json seed1301 epoch100. Task reset parity q'=0 for 2 else q xor (token==1), q0=0. Negative logit for q0, positive for q1. No retraining.
