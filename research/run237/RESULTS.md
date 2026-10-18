# NOESIS Run 237 — frozen unseen reset-parity mechanism test

**FROZEN PRIMARY FAILED.** Pretraining manifest commit: 6e57c6db76f6473de6e11d021ec09361d6112fad. Holdout seeds 3601–3624 (3D) and 3701–3712 (4D), three matched-initialization arms: baseline, saturation regularizer, generic output-confidence regularizer.

| Final checkpoint | Baseline certified/wrong/abstain | Saturation | Confidence |
|---|---|---|---|
| 3D (24 seeds) | 7/8/9 | 9/11/4 | 5/9/10 |
| 4D (12 seeds) | 4/2/6 | 7/3/2 | 3/2/7 |

The primary 3D criterion required at least 3 baseline-wrong to saturation-all-length-certified rescues and at least 2 more rescues than confidence. Observed: **1 vs 0**. The single 3D rescue (seed 3616) has baseline training accuracy 86.67%, versus saturation 100%; this is NOT a matched-perfect-fit beyond-horizon rescue. No 4D baseline-wrong to saturation-certified rescue.

3D certificate gains/losses 3/1, exact one-sided sign p=0.3125. 4D 4/1, p=0.1875. Not significant. Hidden saturation increased but mechanism-specific learned algorithmicity did not replicate prospectively.

Two independent exact-dyadic checkers agreed on 216/216 endpoint classifications; 4/4 corrupted-readout controls rejected. A trained 4D baseline (seed 3709) had perfect length-six training accuracy but a verified wrong-sign witness at length ten. ABSTAIN is unknown, not incorrect. Certificates are exact-real hardtanh statements with binary64 parameters treated as dyadic rationals.

**Smallest supported claim:** This prospective transfer experiment failed to establish a general saturation-mediated algorithm-acquisition improvement on reset parity. Prior Run236 reset-latch improvement remains task-specific. Mark mechanism-transfer attempt 1/3 failed; retain Kernel 001, do not merge or claim breakthrough.

Primary-literature collisions: van Rossem & Saxe ICML 2025 (streaming parity), Wang & Niepert ICML 2019, Oliva & Lago-Fernández 2020 (state/saturation regularization), Dankowiakowski & Ronca NeurIPS 2025 (metric automata).
