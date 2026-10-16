# Kernel 001 — post-Run-195 reformulation (one active kernel)

Status: ACTIVE. Retire absolute-logit-drift and deterministic stutter grammar as candidate general-purpose diagnostics; preserve their failures. No active wildcard kernel.

1. **Precise question.** Can an automatically synthesized, task-aligned inductive simulation certificate (reachable hidden-state sets indexed by abstract task state, closed under all inputs, with strict output separation) prospectively distinguish learned all-length algorithms from finite-horizon spoofs across unseen gradient-trained networks, without hand-tuned checkpoint-specific partitions?

2. **Primary-literature frontier.** Van Rossem & Saxe, ICML 2025, https://proceedings.mlr.press/v267/van-rossem25a.html already show parity-algorithm phase transitions and representational mergers. Ryou et al., CAV 2021, https://www.sri.inf.ethz.ch/publications/ryou2021scalable already establish polyhedral verification of trained RNNs. DFA extraction and inductive invariants are not novel alone. The open NOESIS question is prospective *certificate coverage and prediction of training transitions* under strong spoofs, not parity acquisition itself.

3. **One exact success criterion.** On a frozen held-out panel with at least two distinct task families or architectures, obtain >=2 independently checked positive all-length certificates for trained checkpoints, 0 false-positive certificates on adversarial finite-prefix spoofs, and >=1 prospectively predicted acquisition/retention/loss transition not resolved by matched finite-horizon metrics. Report abstentions and failures; no selective denominator.

4. **Strongest competing explanation.** Checkpoint-specific invariant engineering or lucky saturating tanh dynamics, with no transferable relation to actual gradient learning. Soundness alone is not novelty; lack of coverage would falsify practical usefulness.

5. **Cheapest decisive falsification.** Freeze an automatic invariant synthesis algorithm before new checkpoints; run it first on stored Run 189/190 certified and known-failing models and capped-neural spoofs, then on unseen seeds. Compare to finite-horizon accuracy and budget-matched interval/abstract-interpretation baselines. Preserve all failed proof attempts.

6. **Publishable threshold.** Independent verifier + automatic reproducible certificate synthesis, prospective transfer across at least two task/architecture families, meaningful coverage with no false-positive certificates, explicit mechanism-derived transition prediction, and primary-priority audit. A single model-specific proof is insufficient.

7. **Learning relevance threshold.** Every positive certificate must attach to unchanged weights obtained by ordinary gradient training, and the diagnostic must add predictive or causal information about acquisition/retention/loss beyond training loss and finite evaluation.

8. **Kill condition.** If three substantive attempts yield no transferable certificate coverage or no incremental predictive value, retire Kernel 001 and start a different single kernel. Do not replace it with unrelated finite automata theorems.

THEORY ledger: Inductive closure plus output separation is sufficient for the specified task under exact-real weights; a finite-horizon closure check is not. Open issue: automatic invariant construction and proof-checker generality.

LEARNING ledger: Runs 188-190 supply model-specific positive certificates, Runs 189/191-195 supply counterexamples and negative transfer. Run 195 prospective grammar score 0; seed 199 exact shortest separator length 14, demonstrating that search heuristics are not certificates.

Backup kernels: none. Wildcard effort <=10% and isolated from frozen holdouts.
