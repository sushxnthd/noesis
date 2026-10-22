# NOESIS Run351 CI and provenance

**Latest verified branch workflow:** GitHub Actions 39821398121 PASSED on commit c4a21537a855ffd7c56bae8f3997c1b2b82e0f00. It downloaded the immutable original trajectory artifact, reproduced the frozen N=0/3 result (29 eligible seeds), independently exact-verified 12 checkpoint/intervention variants and the length-11 adversarial failure, and passed **3/3** regression tests. Standard repository CI 39821397825 PASSED. Artifact retention is limited.

**Original full public reproduction:** run 39820568214 PASSED, with full Run348 training regeneration, trajectory SHA256 c74d2821ae8ae6ea568c1fee80fa11f704efcc62d31416b0d436fc4d1ca60403, intervention results, and independent exact checker. Its full artifact ID 12444112106 expires 2027-01-20. Frozen protocol commit dff59294bdc4742beb39c1568918f513c18b48dd predates intervention evaluation.

**Preserved failed provenance:** generic CI 39820947163 failed because tests expected generated outcomes; fixed by conditional pytest skips, and subsequent generic CI passed. Dedicated replay 39821102555 failed with trajectory SHA256 1c118007cbcc4a70c5f0f4d88afd031e48e370f693ce5797495b582ce64c75bf, despite nominally matching software versions. This bitwise replay divergence is unresolved; the workflow now uses the frozen original artifact to avoid conflating changed weights with frozen intervention evaluation. No failure has been deleted or relabeled.

Two original checkpoint pairs are permanently committed. All 192 Run348 trajectories and Run351 raw outcomes are preserved in the original public workflow artifact and local archive, but public artifact retention is finite.

**Draft PR blocker:** create_pull_request was rejected repeatedly by connector safety checks. The research branch remains unmerged.
