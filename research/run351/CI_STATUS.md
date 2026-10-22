# Run351 CI and provenance status

Frozen protocol commit: dff59294bdc4742beb39c1568918f513c18b48dd. Original Run348 trajectory SHA256: c74d2821ae8ae6ea568c1fee80fa11f704efcc62d31416b0d436fc4d1ca60403.

**Successful original public reproduction:** GitHub Actions 39820568214, commit 45060d5f856baaea526eacb0f64476429a93ad9d. It regenerated original training, matched the source SHA256, reproduced N=0, and exact-verified 12 model variants plus the adversarial word. Artifact ID 12444112106 expires 2027-01-20 and contains the full original trajectories and outcomes.

**Preserved failures:** Generic repository CI 39820947163 failed because the new pytest tests expected generated outcome files not available in generic CI. Follow-up commit 8443982d9670caa2a636eda136356dcde3b422e2 skips generated-output tests in that context; generic CI 39821102649 then PASSED. Dedicated reproduction 39821102555 failed on a different regenerated trajectory SHA256 (1c118007cbcc4a70c5f0f4d88afd031e48e370f693ce5797495b582ce64c75bf), despite identical training code and nominal Python/Torch versions. This replay divergence is an unresolved portability issue, not a scientific counterexample; no failed run has been deleted.

**Reproducibility plumbing correction:** The dedicated workflow now downloads the immutable successful frozen trajectory artifact from run 39820568214 before rerunning all interventions, independent Fraction checks, and pytest. This preserves exact original weights instead of assuming bitwise-identical gradient training on different public runner hardware. Full fresh training remains available as a separate, non-guaranteed replay via research/run348/train348.py. Reverify the new workflow status; do not claim success until it completes.

Two original selected checkpoint pairs are permanently committed. Complete trajectories remain in retention-limited artifact and local evidence archive.

**Draft PR:** GitHub connector rejected multiple create_pull_request attempts; no PR created. Research branch remains unmerged.
