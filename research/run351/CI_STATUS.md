# Run351 CI and provenance status

Frozen protocol commit: dff59294bdc4742beb39c1568918f513c18b48dd (before local intervention evaluation). Source Run348 trajectory SHA256: c74d2821ae8ae6ea568c1fee80fa11f704efcc62d31416b0d436fc4d1ca60403.

Public GitHub Actions run **39820568214** completed SUCCESS on commit 45060d5f856baaea526eacb0f64476429a93ad9d. Its job regenerated the original 192-seed Run348 trajectory under Python 3.13.5 / torch 2.10.0+cpu, matched the frozen source SHA256, reproduced Run351 N=0 with 29 eligible seeds, and independently exact-verified 12 cases plus the length-11 adversarial word. The full trajectory and outcome files were uploaded as artifact ID **12444112106**, expiring 2027-01-20. The standard repository CI also passed.

A later commit added two permanent original checkpoint pairs and a subsequent commit adds explicit pytest regressions. Check the latest workflow status before asserting that the *latest* commit passed. No previous failure was overwritten. Local independent checker initially failed on conversion of a SymPy Boolean; the error log is retained in the local evidence archive and the corrected checker passed.

**Draft PR blocker:** multiple create_pull_request connector attempts were rejected by connector safety checks; no draft PR was created. Research branch remains unmerged. This is an infrastructure limitation, not scientific evidence.

**Data retention:** all original Run348 checkpoints are in the reproducible GitHub Actions artifact and local archive. Two selected checkpoint pairs are committed permanently on the branch. Artifact retention is limited to 90 days.
