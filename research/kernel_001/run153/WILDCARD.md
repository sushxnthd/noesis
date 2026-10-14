# Run 153 isolated wildcard: activation-mask novelty
Seed 208: five distinct ReLU masks observed during length-six training; its 25-token adversarial failure never enters a new mask.
Seed 210: three distinct masks observed during training; its 20-token adversarial failure never enters a new mask.
Seed 214: five masks observed; its 10-token failure enters a new mask at positions 9 and 10.
Conclusion: novel activation-mask visitation is not necessary for these observed long-horizon failures. This does not establish a sufficient algorithm-acquisition diagnostic.
Provenance: initial local JSON serialization failed on numpy.int64, then corrected and rerun; both traces retained in local Run 153 archive. The wildcard did not modify the frozen primary evaluation.
