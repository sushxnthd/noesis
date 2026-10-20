# Run294 public reproduction audit — 2026-10-20

- **First run:** https://github.com/sushxnthd/noesis/actions/runs/39419498355 — false green. Training checkpoint SHA mismatch, evaluation failed, downstream outputs absent, but the workflow used piped Python commands without pipefail and reported success. Failure and partial artifact retained.
- **Follow-up run:** https://github.com/sushxnthd/noesis/actions/runs/39420569387 — independently inspected full job log: regenerated training completed, all 245 evaluations completed, metrics matched local exactly, and independent checker printed PASS for 490 all-word projection identities.
- **Public raw artifact:** https://github.com/sushxnthd/noesis/actions/runs/39420569387/artifacts/12263019468 .
- Local vs public checkpoint hashes differ because the public wheel identifies Torch 2.10.0+cu128 versus local 2.10.0+cpu. Max epoch-20 parameter difference observed <=5e-16. Scores differ by at most 1.78e-15; frozen outcomes match 192 changed, 245 stable unchanged, 490 recoveries.
- **Open CI plumbing defect:** Workflow still lacks pipefail; the update attempt was blocked by connector safety checks. Do not infer success from status alone until this is corrected. The specific follow-up run has been checked by log and artifact contents.
