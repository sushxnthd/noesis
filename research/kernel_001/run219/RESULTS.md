# NOESIS Run219 — Frozen scalar sign-only suffix transfer (negative)

Frozen before scoring at commit b485ac20eb8085be572055113393ec81745b9862. Existing Run209 models were trained and their endpoint outcomes classified earlier; **not** a prospective new-training result.

112 suffix probes per network, 2,156 recurrent steps. Length-matched uniform and histogram-matched shuffled baselines each use 2,156 steps. Epoch100 scores predict independently established epoch800 all-length status. Earlier epoch100 classifications were established by exact-real interval methods.

| Seed | Epoch100 classification | Epoch800 | Suffix | Uniform | Shuffle |
|---|---|---|---:|---:|---:|
|659|certified correct|correct|1.000000|1.000000|1.000000|
|661|certified incorrect L2|correct|1.000000|1.000000|1.000000|
|673|certified correct|correct|1.000000|1.000000|1.000000|
|677|certified incorrect L2|incorrect|0.250000|0.794643|0.616071|
|683|certified incorrect L2|incorrect|0.250000|0.982143|0.642857|
|691|certified incorrect L5|incorrect|0.303571|1.000000|0.776786|
|701|certified incorrect L2|correct|0.250000|0.839286|0.526786|
|709|certified correct|correct|1.000000|1.000000|1.000000|
|719|certified correct|correct|1.000000|1.000000|1.000000|
|727|certified correct|correct|1.000000|1.000000|1.000000|
|733|certified incorrect L2|correct|0.750000|1.000000|0.955357|
|739|certified incorrect L5|incorrect|0.303571|1.000000|0.758929|

Eligible acquisition seeds: 661,701,733 (3). Persistent failures: 677,683,691,739 (4). Stable all-length correct already at epoch100: 659,673,709,719,727 (5).

**AUROC** suffix=0.750000; uniform=0.583333; shuffle=0.666667. **Delta over strongest equal-budget baseline = 0.083333**, below preregistered 0.10. Only 3 acquisitions vs minimum 4. **FROZEN CRITERION FAILED on both requirements.**

Independent NumPy scorer matched 36/36 scores. Independent 95-digit Decimal witness/minimality checker passed 7/7, and both independent Decimal and mpmath interval invariant checkers passed five epoch100 all-length certificates. Minimum absolute probe logit exceeded 1e-8 for every model/probe set, excluding floating-point sign ambiguity in reported scores. Previously frozen Run209 endpoint proofs were reused.

Local primary source SHA256 83c6b276dd0dd19cb03b500d5580af3d7374b6784d2cf9238de8a259d0ee8968; local independent source SHA256 f82f64d969b6e691490d9ed8e46664d7a482cee914100829fda9d72c316d8def. Full raw probe words, witnesses, proof logs and original 84 checkpoints are preserved in the accompanying archival package. Repo includes the exact epoch100 parameters and deterministic scoring generator.

Smallest claim: **a frozen sign-only suffix diagnostic did not outperform the strongest equal-budget sign-only baseline by the prespecified amount in a previously trained scalar-RNN cohort; five networks had already acquired the algorithm by epoch100.** No universal predictor established.
