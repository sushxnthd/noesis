# THEORY ledger — Run 186
Hypothesis falsified: saturation-aware 32-cycle forecasting cannot improve on linear forecasting in the frozen cohort, because all 464 binary prediction pairs are identical.
Observed 8192-horizon labels: 110 pass, 354 fail. Both diagnostics make three false-fail and zero false-safe predictions.
Exact witness: one previously unmined gradient-trained width-3 seed-409 epoch-800 checkpoint, three balanced words 011100, 101010, 110001. Independent 80-digit outward-rounded Decimal interval checker interprets stored binary64 parameters as exact rationals and verifies all 8622 preceding block boundaries satisfy absolute error <= 0.1, then proves the first failure at cycle 8623.
All three apparent baseline errors at horizon 8192 disappear as errors when the evaluation horizon is increased to 8623. They share a checkpoint and are not independent replications.
No unbounded counting algorithm or model-agnostic law was established. Existing neural-counting and finite-horizon indistinguishability literature remains the priority boundary.
