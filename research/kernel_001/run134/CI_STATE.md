# CI provenance
Before run 134, draft PR #1 head 0a1b49a748c7f1aed34c5aafb1128663d4f74093, existing workflow .github/workflows/ci.yml executes pytest and finite-horizon spoof. Local full package: 4 main tests and 4 independent tests passed; repository CI now exercises two run134 tests if push succeeds. Preserve earlier failed workflow attempts.
