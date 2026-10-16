# THEORY ledger — Run 191
KNOWN: For seed163 epoch300 stored binary64 parameters interpreted as exact real numbers, the exact output sign on input 0^k is negative for 1<=k<=180 and positive for ALL k>=181. Proof: interval replay through 201, then two alternating 8D rational boxes B0/B1 around the attracting 2-cycle, with F0(B0) subset B1, F0(B1) subset B0, and positive output on both boxes. Two independent local implementations passed. This is a restricted input-family counterexample, NOT a universal algorithm-acquisition theorem.
KNOWN: At epoch600 the output on 0^181 is negative by independent 100-digit interval replay; no all-k guarantee.
REJECTED: Zero-tail testing as a sufficient general algorithmicity diagnostic. The frozen primary criterion was not met and long random performance worsened for the model whose zero-tail behavior improved.
UNPROVEN: seed167 all-length correctness, cross-task transfer, a model-agnostic certificate, or a mechanism-derived prospective predictor.
