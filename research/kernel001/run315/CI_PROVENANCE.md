# Run315 reproducibility and failed-workflow provenance

Frozen protocol: 4f9d7431c1ff45fdba4d27a3f3ff2445905a4288. Frozen early-score SHA256: 2a540bbcefba298bf159a93c71345c48a0586244180562af8fbe2e8954a74d43.

Failed public run 39577740551: strict raw byte-hash mismatch due cross-CPU floating-point variation; original artifact 12334453809 preserved. Failed follow-up run 39578321439: a second raw score hash differed from both earlier hashes; artifact 12334722882 preserved. Checkpoint trajectories and 57/96 sampled-perfect count were reproducible, while small floating-point retention differences (at most approximately 1.8e-15) altered byte hashes.

Portable remedy: round all 96 frozen early score triples to eight decimal places *for integrity verification only*. The SHA256 of canonical JSON is 55227737526cab6fac9f51bc2300a22ab6e8cf39413939d2c25d12cfe68d06ad on local and both remote runs. The scientific predictor and raw AUROC values remain unrounded and unchanged. Independent exact certificate/witness checks remain required. Failed workflow histories are not deleted. No PR creation success is claimed.