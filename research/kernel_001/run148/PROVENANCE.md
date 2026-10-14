# Protocol, exploratory failures, provenance
Date: 2026-10-14. Hosted CPU; no user laptop, no paid API or hardware.
Starting artifact: Run147 trained seed 214, branch research/kernel-001-run147-complete, file research/kernel_001/run147/checkpoints/214.json. Frozen training protocol/checkpoints belong to Run147.

**Exploratory:** A float64 beam heuristic (beam width 400) found candidate word 0022222222222 at length 13. Beam search is NOT an exact shortest-failure proof and is not used in the final certificate.

**Decisive:** Exhaustive ternary interval enumeration to n=13, with directed rounding at every scalar operation; 531441 words at n=12, 1594323 at n=13. Independent Python Fraction rollout verifies both failure witnesses. This analysis was NOT prospectively frozen; avoid claims of predictive discovery.

**Arithmetic:** The input parameters are stored float32 numbers exactly embedded in float64; each floating-point primitive is enlarged by nextafter toward both infinities. Results concern exact-real mathematical recurrence, not hardware float32 execution. A conservative <0.099 guard certifies prefix errors are below exact 0.1 despite representation of decimal tolerance.

**CI:** Run148 tests need numpy + pytest. Keep all failed CI runs if any; do not erase history.
