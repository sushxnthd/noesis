# NOESIS Kernel 001 — Run 234 frozen hardtanh architecture-transfer protocol

Frozen before training, inspection, or selection of any Run 234 checkpoint. This is an **unseen activation architecture** (piecewise-linear hardtanh, not tanh) on the same reset-latch task as Run 233.

## Active kernel (eight mandatory fields)
1. **Question:** Does the existing sound, abstaining suffix-box algorithm-acquisition verifier transfer from trained smooth tanh recurrence to gradient-trained hardtanh recurrence, without confusing finite accuracy with an all-length certificate?
2. **Primary frontier:** Ryou et al., CAV 2021 (RNN verification); van Rossem and Saxe, ICML 2025 (learned infinite generalization); representation-sensitive verification is established prior art. No universal novelty is assumed.
3. **Exact scalar success:** >=2 distinct networks with independently verified incorrect epoch-0 checkpoints and all-length-correct epoch-200 checkpoints, >=4 distinct networks with rigorous incorrect epoch-200 witnesses, and zero false acceptances of deliberately corrupted certificates.
4. **Competing explanation:** Prior results depend on tanh smoothness and selected seeds; hardtanh saturation or proof-search incompleteness prevents transferable acquisition certificates.
5. **Cheapest falsification:** Rigorous wrong-sign witness against a claimed positive, a corrupted proof accepted, or <2 verified transitions in the frozen cohort. Abstentions are neither negative nor positive.
6. **Publishable threshold:** A new architecture-transfer result plus prospective predictive value and spoof-resistant, independently checked certification beyond existing verification prior art. This run alone cannot establish model-agnostic law.
7. **Learning relevance:** Actual Adam-trained hardtanh networks with wrong-sign epoch-0 witnesses and sound inductive all-length epoch-200 certificates.
8. **Kill condition:** Three substantive unsuccessful attempts after this reformulation trigger retirement or a new hypothesis; do not keep retuning a failed suffix-box generator indefinitely.

## Frozen experiment
- Task: ternary reset latch; token 2 sets q=0, token 1 sets q=1, token 0 leaves q unchanged. Supervise every nonempty prefix.
- Architecture: **3-dimensional hardtanh RNN** h_{t+1}=clip(W_{x_t}h_t+b_{x_t},-1,1), z_t=v^T h_t+c. Independent token-specific matrices; initial h=(0.5,-0.5,0.25).
- Seeds: 2701..2712 with Adam lr=0.03; 2801..2804 with Adam lr=0.001. Fixed 16 networks, no post hoc filtering. 200 full-batch updates, BCEWithLogits, all 729 ternary words of length 6, float64 PyTorch CPU deterministic, one thread. Save 0,50,100,200.
- Discovery: suffix depths k=1,2,3, 500 iterations maximum; same padding grid (1e-10 through 1e-2) as Run 233. Candidate generator uses floating-point intervals and is untrusted.
- **Independent exact checkers:** Python Fraction rational intervals and Decimal directed-rounding intervals (90 digits), both treat saved binary64 parameters as exact rationals and clip exactly at +/-1. Verify base words through k, strict output signs, and all closure obligations. Neither checker imports candidate generator.
- Negative controls: exhaustive finite float witness search through length 8, then rigorous wrong-sign confirmation by both exact checkers. No observed witness => ABSTAIN.
- Corrupt at least one bound in each accepted certificate, and require both checkers to reject. Never claim that finite-horizon perfection proves an algorithm.
- Freeze primary criteria and all seeds before training; archive every checkpoint, raw outcomes, failed hypotheses, code, controls, and tests.
- Separate wildcard <=10% exploratory budget cannot change primary evaluation.

## THEORY / LEARNING
THEORY: all-length correctness requires a sound inductive proof. Certificate non-discovery means ABSTAIN.
LEARNING: only actual gradient-trained checkpoint transitions from rigorous incorrectness to independently certified correctness count as acquisition.
