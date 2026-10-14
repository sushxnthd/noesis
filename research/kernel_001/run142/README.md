# Run 142: learned binary latent counter and neutral drift

Retrospective analysis of four ordinary gradient-trained 3-state ReLU checkpoints from Run 138. Reproduce from repository root:

- `python -m pytest -q research/kernel_001/run142/test_run142.py` (standard library and pytest)
- `python research/kernel_001/run142/independent_check.py` (requires SymPy)

The full local reproducibility archive additionally preserves original Run 138 record metadata, verifier logs, SHA-256 manifest, and a repository application patch. All exact failure horizons are mathematical predictions under exact rational arithmetic of stored float coefficients, not float32/float64 hardware rollouts at those lengths.
