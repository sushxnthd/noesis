# Run 215 infrastructure provenance

- Frozen protocol commit: `774460d80d203e9df7a3f5f0ff1d27fb9e756d4c`.
- Initial dedicated GitHub Actions run `38998980408` **FAILED**: the branch's Run214 source lacked `verify_decimal.py` and `verify_run214.py`, and its `verify_run210.py` exported `check`, not `certify`. The original local checkpoint JSON was also absent from the repository. This was an infrastructure failure, not a mathematical refutation.
- Follow-up fix `94f0d805da23aae5f967053fdabb3924ae43462e` uses GitHub-hosted retraining, the available interval checker, and independent reproduction of the frozen score. GitHub Actions run `38999093676` **PASSED**: 15 strict epoch100 wrong-word witnesses, six epoch100 two-state positives, and Run214/Run215 AUROC reproduction.
- Eight epoch100 five-cell positives were independently verified locally using mpmath.iv and directed Decimal but are **not** rechecked by the GitHub-hosted workflow. The three epoch100 abstentions remain unresolved.
- Draft-PR creation and updating PR #1 were blocked by the connector. Branch remains unmerged. Full local source, proof candidates, independent checks, logs, and checkpoints are preserved in the Run215 reproducibility archive.
