# Run 142 smallest supported claim

Of four retrospectively selected 3-state ordinary gradient-trained ReLU RNN checkpoints, three satisfy an exact all-length binary hidden counting invariant absent at initialization. A one-point output-gain calibration (which modifies the model) makes those three exact on binary +/- words. The original readout is not exact, and all three retain nonzero neutral-token drift with a finite first failure within a specified word family. One float64 checkpoint fails the exact unit-coefficient test. Independent SymPy and remote CI tests support the restricted claim.

Not shown: exact original ternary algorithm, globally shortest ternary failures, general model-agnostic certificate, unseen-architecture validation, publication novelty.
