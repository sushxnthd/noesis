# Run315 CI provenance

Original public workflow run 39577740551 failed at strict byte SHA256 comparison. The training itself completed with identical 57/96 sampled-perfect count. Public artifact 12334453809 preserved the remote raw checkpoint and scores.

Local frozen score SHA256: 2a540bbcefba298bf159a93c71345c48a0586244180562af8fbe2e8954a74d43. Remote CPU score SHA256: 446ea8779a30e08b523ec27689ef18332518d905079b65ecd9f56ddfd51fcd00. Direct comparison found maximum absolute retention-score difference approximately 5.1e-16. The original protocol and score function are unchanged. A separate follow-up workflow evaluates the independently generated remote cohort without replacing the original frozen local scores or rewriting the original failed run.

The same exact outcome counts and AUROC values were reproduced locally using the remote checkpoint artifact. No scientific success is claimed: the frozen criterion failed.