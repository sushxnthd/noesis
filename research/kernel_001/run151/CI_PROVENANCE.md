# Run 151 CI provenance
- Initial targeted run 38557800573: passed.
- Initial repository-wide run 38557800499: failed test collection.
- After independent checker: targeted run 38557999506 passed; repository-wide run 38557999605 failed.
- Cause: tests/test_run151.py imported the cached run148 independent_exact module instead of Run151.
- Repair: unique module name run151_exact, commit 2a458ed9d14fecd6dd8613ca26dc699e9c3e3d1a.
- Repaired targeted run 38558078684: passed, including 80-bit exhaustive check.
- Repaired repository-wide run 38558078681: passed.
- Failed runs preserved; no history rewritten. Draft PR creation blocked by execution safety checks.
