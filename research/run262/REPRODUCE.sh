#!/usr/bin/env bash
set -euo pipefail
python train_vectorized.py
python predict_frozen.py
python independent_sympy.py
python independent_hold_replay.py
