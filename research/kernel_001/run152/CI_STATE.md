# Run 152 CI state
- Repository-wide workflow: https://github.com/sushxnthd/noesis/actions/runs/38564160812 — PASS (commit c0ec35f).
- Tested: exact rational counter smoke test, perfect-counter full depth-14 enumeration, retrospective results summary boundaries, and repository existing tests.
- Not tested remotely: deterministic 24-checkpoint retraining; 24 trained-checkpoint exhaustive depth-14 results; 24 independent longdouble checks.
- Dedicated workflow and stacked draft PR creation: blocked by execution safety checks. These are unresolved provenance limitations.
- Local verification: 24/24 all-alphabet exhaustive float64 bounds, 24/24 independent 80-bit depth-14 maxima, 8 exact rational failure witnesses.
