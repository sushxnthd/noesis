# Run226 Phase B — frozen extension before search (2026-10-17)

Phase A found no newly resolvable labels by exhaustive float64 candidate enumeration through length 9. This is an unsuccessful candidate-discovery screen, NOT an exact proof of correctness.

**One decisive test:** seek additional epoch-200 counterexamples among the 18 previously unresolved trained Run220 checkpoints using multiple nonnested adversarial beam widths. The Run221 failure at width 384 makes single-beam non-detection unreliable.

Freeze beam widths {64,128,256,512,1024}; max length 256; all previously unresolved epoch-200 checkpoints; original Run220 checkpoints and original sign-only diagnostic scores immutable. Candidate selection deterministic with tie-breaking by original path order. Every candidate must be checked independently by directed Decimal and mpmath.iv before being labeled INCORRECT. Absence of a candidate remains UNRESOLVED.

**Primary scalar:** number of newly independently verified epoch-200 incorrect checkpoints (target >=3, which would bring PERSISTENT to >=4, subject to early epoch-50 verification). Secondary descriptive: new resolved-label AUROCs using original Run220 frozen scores, no refitting.

Strongest alternative: beams repeatedly rediscover only the previously known seed 1429, or produce floating-point artifacts. Kill Phase B if no new rigorously verified counterexamples under all frozen widths. Do not reinterpret no-beam-error as correctness. This is retrospective diagnostic auditing, not a new prospective architecture-transfer experiment.
