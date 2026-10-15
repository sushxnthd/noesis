# Run 187 learning ledger

Four generic width-8 tanh RNNs were trained with Adam on all 64 length-six binary strings and prefix-wise parity labels. Seeds 101, 103, 107, 109; checkpoints 0, 100, 300, 600, 1200. Heldout evaluation was exhaustive for length 12 (4096 words) and deterministic for 128 length-128 words. Seed 101 at epoch 600 transitioned from <1% full-word accuracy at epoch 300 to 100% at both heldout lengths; seed 107 likewise transitioned to 100% at epoch 600. Seed 109 remained ~46%-50% on length 128 despite ~98% on length 12. No claim of all-length correctness; two-box certificate failed on every checkpoint.

Source, raw checkpoints and exact outcomes are in Run 187 archive; remote evidence upload remains pending.
