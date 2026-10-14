# NOESIS Run 147 reproduction
Frozen protocol: FROZEN_PROTOCOL.md. All eight final float32 trained checkpoints: checkpoints/*.json. Training recipe: train.py (requires torch). Run the exact verifier and invariant-cone checks without torch using:
python -m pytest -q tests/test_run147.py
The test uses Python Fraction for all 512-step nonlinear trajectories and rational inequalities for cones; no hardware float32 long rollout is claimed.
Local complete artifact additionally contains full initialization tensors, raw prediction log, independent checker, independent SymPy checker, tests and failure provenance.
Results: 7/8 exact frozen forecast matches, 3/3 genuinely prospective matches; two-dimensional invariant cones certified for seeds 210,214,215; mask-only sufficiency falsified by exact cap spoof.
