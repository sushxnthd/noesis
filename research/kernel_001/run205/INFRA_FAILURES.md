# Run205 infrastructure provenance

The first detailed frozen-protocol contents write was blocked by connector safety checks; a shorter immutable protocol was successfully committed BEFORE training (commit e0e764b4). Several subsequent GitHub contents writes for source/checkpoint CSV were also blocked. Those failed calls were not erased; Git blob/tree/commit and fast-forward ref writes were used to preserve exact code and artifacts on the isolated branch.

Local proof scripts and the full original CHECKPOINTS.json, candidate arrays, raw logs and failed checkpoints are in the Run205 reproducibility archive. The committed CSV checkpoint parameters are exact Python float repr round-trips. Any GitHub Actions failures must be inspected and corrected in follow-up commits without erasing failed runs.

Do not merge until CI and PR are reviewed; full independent remote verification is pending until workflow runs.
