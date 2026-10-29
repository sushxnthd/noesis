# R424: early-output parameter identifiability in archived learned RNNs — frozen negative

**Kernel:** causal transition dynamics of learned DFA-state retention under full-state-neutral cycles. Retrospective, no new training. **Frozen primary FAILED (0/24)**. No publication-grade neural novelty.

## Frozen experiment

Pre-outcome protocol SHA256 `2b9e0ad21340ac1b9e931d52d120c3486155dffb5252e60eaed9a4d6cfcced00`. All 24 immutable R418 float64 networks (LSTM/GRU/MGU × TaskA/TaskB × seeds 99960–99963) retained. One outcome-independent rotated complete-DFA-state context per model was evaluated (24); the remaining 84/108 contexts are **unevaluated**, not silently ITT-positive or negative. All nine complete DFA states represented in the measured set.

Early observations: 14 real oracle-vs-other-class logit gaps at seven neutral-word continuations of depth 0–2 after the exact-zero prefix plus u^16. Heldout: 36 gaps at u^d, v^d, alternating uv, depths 3–8. Differentiated the complete 248–273-parameter recurrent computation through prefix, entry, continuation, suffix1 using Torch float64 autograd. SHA-seeded random directions projected off the early Jacobian rowspace and exact common-logit gauge; four directions × frozen L2 scales 0.1,0.3,0.6,1.0 per model. Matched-norm random direction control. No heldout-gradient selection.

Primary required early oracle correctness and maximum early gap drift <=0.05, a heldout classification flip plus frozen late-effect condition, and >=6 cases spanning both tasks, >=2 architectures, >=3 seeds with >=6 negatives.

## Results

**0/24 primary successes; frozen conjunctive primary FAILED.** 18/24 baseline contexts were early-correct. Of 384 projected perturbations, **287 preserved the early readout/gap tolerance, 0 of those flipped a late class**. Ten late flips occurred only after early preservation failed. Of 96 matched random perturbations, 19 preserved early outputs, 0 of those flipped late classes; five late flips occurred with early failure. Largest heldout gap drift among early-preserving projected perturbations was 0.044499, below the 0.15 late-effect gate. No threshold retuning or case selection.

Numerical early Jacobian rank under frozen max(1e-9,1e-8*smax) cutoff: rank 4 (2 cases), 5 (2), 6 (2), 8 (18), with 14 observed gaps and 248–273 parameters. These are **approximate, cutoff-dependent ranks**, not rigorous exact-real rank certificates or proof of a new learned symmetry. Some near-zero singular values may reflect saturation and redundant early traces.

## Exact and independent controls

Classical exact gauge: `R_i -> R_i+a, O_i -> O_i+b` adds the same scalar to every logit and preserves all gaps and argmaxes for all histories. Fraction and independent SymPy tangent checks passed for widths 5,6,7. Rank-nullity gives at least p-14 linearized null directions; an implicit-function-theorem exact early-output level curve requires an unverified full-row-rank hypothesis. None of this is novel neural theory.

Separately frozen independent selection SHA256 `fc01ac3430da0639ccc2ab73ebafd49633e05a31b4536b4dcc36e39377d94bec`: Torch/Numba 24/24 selected early/future gap-vector comparisons passed (max difference 2.80e-14); six central-difference derivative checks passed (max difference 1.09e-9); 12/12 exact-gauge early/future checks passed. Independent mpmath 120/160/220-digit pointwise calculations agreed on **108/108 selected classification labels**; maximum gap discrepancy 3.55e-15. No directed interval proof of exact neural parameter Jacobian rank or IEEE execution behavior.

## Interpretation and preservation

This falsifies **only** the predeclared random gauge-quotiented early-null intervention's ability to produce late classification flips while preserving early readouts in these 24 contexts. It does not prove general future-output identifiability, non-identifiability, or learned causal mechanisms; interventions are off the training manifold. Do not rebrand R382–383, R408–409, R410–411, or R423 as new findings.

Full source, frozen protocols, 24 per-case raw perturbation records, negatives, independent audits, logs, and immutable R423 checkpoint dependency are preserved in the 49-entry SHA256-verified archive `NOESIS_R424_Reproducibility.zip`, SHA256 `03a893b72d0b773e7ad21d995cba0871c7fdc9326c1afabe6db65c700cf3d53d`. Raw not committed to GitHub.

**Next:** R425 should change mechanism rather than retune R424. Any new input-intervention alphabet must first pass exact symbolic feasibility across both tasks and be distinguished from retired R396–397 adversarial words and R419 third-word impossibility. No new neural cohort without frozen non-ceiling feasibility.

No personal spending or user laptop. Same authorized branch; PR #22 remains draft/unmerged.
