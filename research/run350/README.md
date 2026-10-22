# NOESIS Run 350 — new-seed exact readout transitions

Frozen protocol commit: edea92b80cdabaaf54703aa794345c47c338a4a3, before training.
Cohort: 192 new seeds (33000–33191), 200 Adam updates, width-three ReLU parity RNNs, exact-real interpretation of float64 checkpoint parameters.
Run350 confirms two exact representational-obstruction-to-repairability transitions:
- seed 33053, epoch 30 obstruction (five hidden states), epoch 31 exact affine separation for all 2,644 deep-family words through length 23; first unrestricted certificate epoch 76.
- seed 33068, epoch 55 obstruction (three hidden states), epoch 56 exact affine separation for the same 2,644-word family; first unrestricted certificate epoch 72.
Both early checkpoints are correct on all 510 nonempty binary inputs through length eight. Their original output heads fail on longer witness words. Both early checkpoints admit exact separators on the frozen 618-word shallow family, so shallow geometry misses the deeper obstruction.
Independent SymPy and Fraction calculations verify exact convex equalities. Two later endpoint support-cone certificates were checked independently. Across all 192 new models, 10 endpoints were certified at epoch 200. The deterministic training trajectory SHA256 is 52e57a99729da2a5710f55d09689d8730286d60798b25c33d841b3bd15905c64.
Full original 38,592 checkpoints and selected weights are generated and uploaded by the workflow artifact; they are not represented as permanent Git blobs. Source and exact verification are in reproduce350.py.
Scope: prospective new-cohort existence replication, but earlier checkpoints were searched retrospectively within endpoint-certified trajectories. No evidence of model-agnostic prediction or the exact epoch of unrestricted algorithm acquisition. Numerical LP false positives on other seeds must not be treated as proof.
