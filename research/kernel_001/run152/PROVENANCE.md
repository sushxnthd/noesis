# Run 152 provenance and failure retention
- Source cohort: Run 150 training protocol; Run 151 exact all-alphabet seed 214.
- Initial exploratory all-seed enumeration stopped at depth 12. Follow-up increased to 14; no training, threshold, or seeds were changed.
- Independent 80-bit alternate-traversal verifier timed out after completing seeds 208..214; its stdout was preserved. A second execution for seed 215 completed verification of all 24 checkpoints. This is an infrastructure timeout, not a scientific negative result.
- The code regenerates archived checkpoints deterministically using Run 150 training source if a cached CHECKPOINTS.json is not present. GitHub Actions uploads regenerated checkpoint JSON as a research artifact.
- 24 first-failure classifications have conservative float64 roundoff envelopes and rational exact failure-witness checks. Independent longdouble max-error verification is not a formal all-words proof.
- No user laptop or paid APIs used.
