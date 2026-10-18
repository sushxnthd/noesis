# Run246 public independent replay — PASSED
GitHub Actions run: https://github.com/sushxnthd/noesis/actions/runs/39136800432
Artifact: https://github.com/sushxnthd/noesis/actions/runs/39136800432/artifacts/12140406154
Date: 2026-10-18. Pinned torch 2.10.0 CPU; GitHub-hosted Ubuntu/Python 3.12; no user laptop.
The remote workflow retrained all 48 networks, reran exact rational state enumeration, the sound interval verifier, and independent dyadic witness checks. Frozen summary matches local exactly, including CHECKPOINTS.json SHA256 b0a31428609da72d9aef54606d61d47d2e22c2bd70dc9412df4f5b3ac7237991.
Outcome: 0 new certificates (frozen criterion FAILED); 30 incorrect endpoints, 18 unresolved, 31 perfect finite train; 13 perfect-finite networks provably wrong at lengths 6–9. Independent witness replay 123/123; 1D tied-ReLU horizon spoof passes 9,840 strings then fails at length9. Public artifact holds full checkpoints, outcomes and summary; retention until 2026-11-17. Full local evidence archive also preserved.
Draft PR creation still blocked by connector; leave branch isolated. Failure count 1/3, active K001 retained. No breakthrough claimed.
