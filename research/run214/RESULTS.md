# NOESIS Run 214 — frozen matched-budget transfer FAIL (2026-10-17)

Frozen before training: `research/run214/FROZEN_PROTOCOL.md`, commit `d42735d548d98fa4948282d913d88090ace23f2d`. Thirty-two new 2D coupled tanh RNN seeds, epoch-100 predictors, epoch-200 independently checked behavioral labels. All 32 were trained; 30 achieved 100% finite training accuracy. Two (1093,1151) did not, and are retained as prespecified.

## Frozen outcome
21 **CORRECT** (14 two-state plus 7 five-cell all-length inductive proofs); 8 **INCORRECT** (strict interval wrong-word witnesses); 3 **UNRESOLVED** (953,1091,1153). Every resolved local outcome passed two independent arithmetic implementations (mpmath.iv and directed Decimal). No incorrect inference from abstention.

AUROC (29 resolved endpoints):
- Task-conditioned zero-retention margin: **0.892857**
- Generic final-logit minimum, 9 words, 54 recurrent steps: **0.922619**
- Generic prefix-logit minimum, same 9 words, 54 recurrent steps: **0.952381**
- Negative epoch-100 training loss: **0.910714**
- Negative heldout prefix-error count: **0.866071**

Frozen improvement over strongest baseline = **-0.059524** (required >= +0.10). **FAIL.** The generic *final* score also beats retention at exactly equal 54 recurrent steps and nine scored endpoints; the generic prefix score uses the same steps but more logits.

Stratified bootstrap (10,000 resamples, exploratory): retention minus generic-prefix 95% percentile interval [-0.226,0.095]; retention minus generic-final [-0.190,0.131]. This is a falsification of the prespecified superiority criterion, not a statistically established universal ranking.

Exploratory perfect-finite-training subset: 21 correct, 6 incorrect, 3 unresolved; retention AUROC 0.904762, generic final 0.912698, generic prefix 0.952381. The failure is not driven solely by the two imperfect training endpoints.

## Scientific decision
Retire **task-conditioned retention superiority** as a prospective acquisition predictor. Run 213's apparent advantage over conventional baselines does not survive a frozen, matched-budget generic-margin challenge. Keep retention probes as useful adversarial tests, not laws or certificates. Do not tune this predictor on the Run 214 holdout.

Inductive all-length proof remains a sufficient but incomplete certificate. Invariant inference and formal-language learning are prior art, so no novel universal theorem is claimed.

## Provenance / limitations
Local exact checkpoints: SHA256 `1833b17c2c31ce9da4c78885a4996069a8111df7f3cb80d3fe1110b75f5e3b59` for the local checkpoint JSON. The remote minimal trainer generates an independently structured JSON; compare parameter tensors, not whole-file SHA. Remote verification is not considered passed until Actions job logs are checked. Seven five-cell certificates are currently local-only. Preserve three abstentions. GitHub Actions may require workflow plumbing fixes; retain failures.

**Smallest supported claim:** In one preregistered 32-seed cohort of gradient-trained coupled 2D tanh RNNs, task-conditioned zero-retention margin did not outperform equally recurrent-step-budgeted generic signed-margin probes for predicting independently verified all-length reset-parity behavior.
