# THEORY ledger — K001 Run288
1. The two-box invariant remains a **sound sufficient** certificate for all binary strings, established by exact rational interval enclosure and output sign separation. Noncertification is not incorrectness.
2. New prospective result: early minimal LP relaxation slack predicts later *discovery of that certificate* in fresh gradient-trained width-two models, AUC 0.81594; BCE baseline 0.43256, delta +0.38339, frozen primary passed. This is a correlation with a future verifier outcome, not a general acquisition law.
3. Independent SymPy corner checker verified 141 certificates; independent rational simulation verified 378 wrong-word witnesses across checkpoints, with no contradiction.
4. Strongest spoof/alternative: predictor and endpoint share the same invariant family; eight historical finite-horizon spoofs have nonzero slack, but such a result is expected and not proof of generality. Full-label completeness and cross-architecture prediction remain unresolved.
5. Primary literature priority remains open: Butoi et al. ICLR 2025; Dankowiakowski & Ronca NeurIPS 2025; Dave et al. NeSy 2025.
6. Kill/reformulate if the same predictor fails on an unseen architecture or if it does not outperform BCE on genuinely correctness-labeled future endpoints. No claim of necessity or model-agnostic sufficiency.
