# NOESIS R370–R371: prospective diagnostic and fresh-seed intervention (23 Oct 2026)

**Scientific status: two stronger prespecified mechanism gates failed; no field-level discovery claimed.** The single active kernel remains gate-mediated DFA-state retention under neutral cycles. Earlier Run350–362 single-coordinate claim remains retired. Prior R363–R369 within-network findings are retained as bounded evidence.

## Run 370: prospective neutral-cycle transfer
- Protocol SHA256: `e9a2c62c081db9c092b33090bd7c69d8f5b0071c2fa585c0197520a2c40936e0`.
- 80 previously trained GRUs, 22 new neutral words (10 same-composition nontrivial + 1 identity control per task), fixed three DFA-state representatives, eligibility >=2 correct at n32.
- Frozen predictor: sign of the true-class margin difference after four cycles of update-logit +4 vs unmodified continuation from identical n32 state.
- After 80-digit arbitration: 1,396 discordant opportunities, 1,385 harms and 11 improvements. Directional accuracy **99.07%**, clustered 95% CI **[98.26%, 99.62%]**. Prespecified directional criterion passed.
- **Mechanism criterion failed:** pooled AUROC for harm on same-composition nontrivial cycles **0.725**, below the frozen 0.80 threshold. A privileged identity/nontrivial symbolic rule achieved **99.57%** directional accuracy, better than the learned predictor.
- Independent batched PyTorch float64 checked all **5,280** n256 predictions: **27** disagreements plus **one** n32 disagreement. **28** targeted 80-digit high-precision replays included six cases in which both float64 implementations disagreed with high precision. Main conclusion robust to arbitration.
- **Decision:** do not claim a novel predictive transition mechanism; near-perfect sign accuracy is largely explained by extreme outcome imbalance.

## Run 371: independent fresh-seed selective-gate intervention
- Protocol SHA256: `6742aff7e4df36bbbb3a1a0abad1a3ed2881f34cfe38a4075eb8fccf58f412f5`.
- **32 independently trained GRUs**, 16 per task, seeds 38000–38015 and 39000–39015, all reached perfect short-training accuracy. First-perfect checkpoint selected without long-sequence outcomes. Same width-six 273-parameter cell; not a third architecture.
- Fixed within-network variants from identical n32 hidden states: baseline, uniform z+4, local-residual selective z+4 (only if unperturbed single-step residual <=0.05), and privileged symbolic oracle.
- **Nontrivial neutral cycles:** 588 previously correct opportunities; baseline **98.30%**, uniform z+4 **33.67%**, selective **98.47%**, symbolic oracle **98.30%**. Selective-minus-baseline **+0.17 pp**, clustered CI **[0,+0.54]**; selective policy triggered on 3.46% of nontrivial steps.
- **Identity cycles:** task A baseline **94.44%** vs selective **100%** (36 opportunities, nine eligible seed models); task B baseline **85.71%** vs selective **100%** (28 opportunities, seven eligible seed models). Both bootstrap CIs for improvement have **lower bound zero**.
- **Conjunctive primary failed:** identity improvements lacked positive lower confidence bounds. Selective intervention essentially reproduced a privileged oracle abstention policy; do not claim a general repair law.
- Independent NumPy/SciPy recurrence agreed with Numba on **160/160** stratified n32, n256, and n512 predictions.
- Classical spectral sanity check: 33 exact SymPy rational permutation-interpolation cases passed. This is not a novel theorem about nonlinear GRUs.

## Reproducibility
Complete local archive: `NOESIS_R370_R371_Reproducibility.zip`, SHA256 `62057b6bf4a0b61779fb011721b426b40e928d0554d13b987ffd8eb36414d7db`. Includes frozen protocols, 32 fresh checkpoints, prior cohort checkpoints, all raw outcomes, independent PyTorch and NumPy checks, 28 high-precision arbitrations, exact symbolic checker, full research note, vector figures, and a validated 75-file SHA256 manifest. The full raw archive is preserved outside GitHub pending durable upload; this commit does **not** pretend the raw archive is in the repository.

## Decision and next experiment
Two consecutive mechanism-strengthening attempts failed their stronger predefined gates. Retire the four-cycle predictor as a flagship mechanism and local-residual gate modulation as a general repair claim. **Reformulate the same kernel around the learned full-cycle map and its Jacobian cocycle/spectral stability**, then freeze an unseen-seed failure-horizon prediction and compare against short CE, readout margin, raw d32, state coverage, local Jacobian, and symbolic oracle. Next require a matched training-time gate intervention and third architecture. Do not revive the R350–362 single-coordinate claim, auto-merge this PR, or assert novelty without priority and causal controls.

Primary priority sources: Weiss et al. ICML 2018; Dan et al. ICML 2022; Muskardin et al. ACL Findings 2024; Buitrago & Gu ICML 2025; Dankowiakowski & Ronca NeurIPS 2025; Brandoit et al. 2026 (metadata/full text needs verification).
