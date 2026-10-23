# NOESIS R382 — prospective readout-silent observability intervention (negative primary)

Date: 2026-10-24. Kernel: learned DFA-state retention under neutral cycles. This is one failed confirmatory attempt of the newly reformulated basin/observability mechanism. The uniform gate-offset and gradient-mask family remains retired.

## Frozen design
Protocol SHA256: `f19506a5d212ea7b9c085e189d80a962568d96bfbcaecc6ab3137201663511f9`.
Frozen directions/predictions SHA256: `03c59ffcc2f42270c4b2df962542fdf01906b3188ea4b50fb5f3d625cb164970`.
Both frozen before their corresponding training/outcome stages.

Trained 16 **new** width-5 symbol-conditioned LSTMs (258 parameters), eight per task, 160 Adam updates, matched R381 control training schedule; all 16 achieved perfect short-training accuracy. Six held-out, full-DFA-state-preserving neutral-cycle contexts per task/seed. At cycle 32, injected norm-0.20 perturbations to h alone, holding c fixed. Directions: maximal/minimal one-cycle local readout observability within approximate readout nullspace, random nullspace, rowspace and baseline, with both signs. Total 96 model-cycle cases, 864 long trajectories. The readout-nullspace is a float64 SVD approximation (not exact rational), with immediate readout change below 3e-15.

**Frozen primary:** top nullspace vs bottom nullspace increases n256 oracle error by >=10 percentage points, exact one-sided seed-cluster sign-flip p<0.05, intent-to-treat all 16 seed clusters.

## Result: FAILED
Top-minus-bottom loss difference **+2.083 percentage points**, seed-bootstrap 95% CI **[0, 4.688] percentage points**, exact one-sided paired sign-flip **p=0.125**. Both thresholds failed. Count-ones task: 48/48 retained for every arm (ceiling). Count-'01' task: baseline 39/48, top 37/48, bottom 39/48, random nullspace 37/48; top does not outperform the random-nullspace control.

The local one-cycle derivative separated top from bottom directions (median predicted readout norm ~2.23e-4 vs 6.29e-6), but did not yield the prespecified general long-horizon failure law.

## Independent checks and post-hoc witnesses
Numba/PyTorch float64 n256 classifications agreed **864/864**. Independent mpmath 120/160-digit recurrences from zero state agreed on **24/24** stratified conditions and with float64. This is not full-panel precision certification or a formal interval proof.

Two **post-hoc selected**, model-specific witnesses on count-'01' mod 3, prefix `01011`, had unperturbed/bottom-plus class 2 (oracle correct) and top-plus class 0 at n256: seed 63001 with cycle `011111001011`, seed 63002 with cycle `100001110101`. All 6 baseline/top/bottom conditions agreed at 120, 160, 220 digits. These witnesses demonstrate a within-checkpoint delayed classification effect but are not prospective replication and cannot rescue the failed primary.

## Decision and limits
No new theorem, architecture-general law, or publication-grade discovery. Retain the negative result; do not tune epsilon post hoc or reverse the hypothesis. Next independent attempt should use exact rational readout-null perturbations, a pilot-frozen nonlinear basin-boundary forecast, fresh seeds, and a different gated architecture. Classical observability is prior art.

Complete 48-file reproducibility archive, including frozen protocols, checkpoints, raw trajectories, independent implementations, high-precision data, exact statistics, negatives and SHA256 manifest, is preserved outside GitHub:
`NOESIS_R382_Reproducibility.zip` SHA256 `db570fd1906dc5d0ab897a944650cb174af47b03a021ff015a90b202fafd00c1`.

**The complete raw archive is NOT uploaded to GitHub.** No merge or force push.
