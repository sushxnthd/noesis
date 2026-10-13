# Kernel 001: shortest-witness dead-gradient
Negative result on a gradient-trained recurrent parameter. The shortest provable zero-test failure has **positive final count-regression loss but exactly zero gradient** to the finite-cap parameter. Prefix supervision shifts, but never eliminates, the failure frontier.

Run from repository root:
    python research/kernel_001/dead_gradient/run.py
    python research/kernel_001/dead_gradient/independent_check.py research/kernel_001/dead_gradient/RESULTS.json
    python -m pytest -q tests/test_dead_gradient.py

PROTOCOL.json is frozen; RESULTS.json preserves exact rational outcomes. No GPU or API spend. No claim of learned unbounded algorithmicity or publication novelty.

