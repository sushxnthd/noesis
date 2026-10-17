# Kernel 001 — reformulated after Run 218

Exactly one active kernel: **behavioral, output-gauge-invariant prediction of neural algorithm acquisition**.

1. **Question.** Can task-derived, sign-only counterfactual suffix challenges predict which gradient-trained networks transition from verified incorrect behavior to certified all-length correct behavior, across an unseen architecture?
2. **Primary frontier.** RNN invariant verification and automata extraction; Chen–Goodfellow–Shlens (Net2Net, ICLR 2016) on function-preserving transformations; Guo–Pleiss–Sun–Weinberger (ICML 2017) on posthoc calibration. No novel general impossibility theorem is claimed.
3. **One frozen scalar criterion for next run.** Held-out AUROC improvement >=0.10 over the strongest equal-budget sign-only random-prefix accuracy baseline, with at least four independently verified incorrect-to-all-length-correct training transitions and at least four persistent failures. Unresolved certificates are abstentions, never negatives.
4. **Strongest competing explanation.** Any advantage is ordinary finite-test coverage rather than mechanism-derived algorithm acquisition; task-specific suffix challenges merely overfit parity.
5. **Cheapest decisive falsification.** Before new training, define fixed challenge pairs and equal-budget random baselines; freeze generator and seeds; evaluate one unseen gated recurrent architecture using only binary decisions; independently certify outcome labels or abstain.
6. **Publishable threshold.** Prospective transfer, adversarial finite-horizon spoof controls, independent mathematical checker, held-out task family, primary-prior-art audit and bounded claims.
7. **Learning relevance.** Only actual gradient-trained checkpoint trajectories with verified transition labels count toward the AUROC. Pure finite-state examples do not.
8. **Kill.** After three substantive attempts failing the frozen predictor improvement, retire this kernel; do not tune on the same cohort.

**THEORY ledger:** Naive finite-horizon closure was spoofed in PR #1. Raw margins (Run 216), L2-normalized margins (Run 217), and output ratio (Run 218) are not intrinsic to the binary decision function. Finite sign-only probes can be predictive but cannot be sufficient all-length certificates without additional inductive obligations.

**LEARNING ledger:** Earlier runs established certified incorrect-to-correct transitions in trained RNNs, but none of the posthoc margin diagnostics has prospectively survived a cross-architecture acquisition test. Run 218 reused 12 trained models and does not add new transitions.

Backups (inactive, max two): proof-guided transition localization; task-suffix intervention study. Do not run them until active kernel is killed or yields stronger evidence.
