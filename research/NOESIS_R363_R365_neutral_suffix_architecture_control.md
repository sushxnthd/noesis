# NOESIS Runs 363–365: neutral-suffix state retention

Date: 2026-10-23. Research result, NOT a claim of publication-level novelty.

## R363: pilot-frozen gated-network early-warning diagnostic

On 96 unseen gated recurrent models (48 per task), 73 were eligible (at least two of three DFA-distinguishable prefixes correct at neutral suffix length 32). A pilot-selected hidden-distance contraction rule R=d32/d16<0.95 predicted a newly incorrect prefix at length 256 with contingency [[8,1],[25,39]], precision 8/9=88.9%, risk ratio 2.276, and one-sided Fisher p=0.00612. This passed the frozen gate. However, continuous raw distance d32 achieved AUROC 0.799, outperforming the R diagnostic (AUROC 0.666). Thus R is not an established superior mechanism.

## R363 third architecture: falsification

An independently trained 64-seed ungated Elman tanh RNN cohort (width 8, count-ones-mod3) had 57 eligible networks. The same frozen R<0.95 rule yielded [[0,5],[3,49]], precision 0 and one-sided Fisher p=1.0. The cross-architecture replication FAILED.

## R364: matched-input, near-matched-parameter architecture control

Train 48 new width-10 Elman networks (253 parameters) on the identical 196 length-8 training strings per seed used by 48 width-6 gated networks (273 parameters). At first-perfect training checkpoints, 34 seed pairs were jointly eligible at suffix length 32. The gated networks suffered 16 new failures by suffix length 256; Elman networks suffered 0. Paired risk difference 47.1 pp, bootstrap 95% CI [29.4,64.7] pp; exact one-sided discordance p=1.53e-5. The prespecified gate passed.

## R365: matched short cross-entropy control

Retrain the same 48 gated networks from original initialization and Adam state; select first checkpoint after perfect short training whose cross-entropy is no greater than the same-seed Elman first-perfect loss. All 48 matched. Original first-perfect epochs reproduced exactly (48/48). Among 36 jointly eligible seed pairs, CE-matched gated networks suffered 18 new failures at length 256; Elman networks suffered 0. Paired risk difference 50.0 pp, bootstrap 95% CI [33.3,66.7] pp; exact one-sided discordance p=3.81e-6. The prespecified gate passed. Mean gated CE 0.095 vs Elman target CE 0.117, so a weaker short loss does not explain the observed retention difference.

## Limits

This is one adversarial neutral-suffix family per task. Architecture, gate structure, hidden width, parameter count, learning rate, and optimization trajectory are not isolated. The Elman models and gated models are not identical-capacity or optimizer-matched causal interventions. The hidden-distance diagnostic is not architecture-invariant. No all-length correctness certificate or new general neural-learning law is claimed. Full raw artifacts, frozen protocols, source code, independent NumPy/PyTorch audits, and hashes are preserved in the accompanying local reproducibility package.