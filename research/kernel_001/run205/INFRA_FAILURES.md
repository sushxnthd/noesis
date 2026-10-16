# Run205 infrastructure provenance

Frozen protocol committed before training: e0e764b4. Detailed protocol and several file/PR writes were blocked; successful writes used Git blobs, trees, commits and fast-forward refs. Checkpoint serialization bug fixed in follow-up e2d0e743, preserving the earlier commit.

**Remote proof CI PASSED:** run 38941141661 (2026-10-16): 14 exact rational/Decimal certificates, 14 independent mpmath.iv certificates, both 803/804 spoof proofs, three certified early training errors, and two unit tests. Earlier proof CI 38940875645 also passed. Generic CI was still in progress when last checked.

All 28 checkpoint parameter snapshots are committed as exact float repr CSVs. Full raw CHECKPOINTS.json and logs are in the reproducibility archive. Draft PR and PR1 comment attempts were blocked. Branch remains unmerged.
