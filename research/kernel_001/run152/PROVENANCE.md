# Run 152 provenance and failure retention
- Source cohort: Run 150 training protocol; Run 151 seed-214 exact all-alphabet audit.
- Exploratory all-seed enumeration first stopped at depth 12; follow-up increased to depth 14. No training, threshold, or seeds were changed. This is retrospective, not a prospectively frozen result.
- Independent 80-bit alternate-traversal checker timed out after seeds 208..214. Stdout preserved locally; seed 215 verified in a second execution. All 24 depth-14 maxima agreed within 4e-15.
- All 24 original unchanged trained checkpoints, detailed histories, exact witness checks, and both independent execution logs are preserved in the Run 152 local reproducibility archive. The repository contains executable code and derived summary; the binary checkpoint upload was rejected by execution safety checks.
- Repository-wide CI at commit c0ec35f383993f37400a1b2e8ca71c2b4a46f9c9 passed, including Run152 smoke tests. This does NOT constitute remote reproduction of all 24 trained checkpoints or independent all-word verification.
- A dedicated workflow creation and draft PR creation were rejected by execution safety checks. Keep branch unmerged. Full remote research CI remains pending.
- No user laptop or paid APIs used.
