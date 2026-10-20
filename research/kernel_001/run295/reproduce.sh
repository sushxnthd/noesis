#!/usr/bin/env bash
set -euo pipefail
python -m pip install numpy scipy==1.17.0
python -m pip install torch==2.10.0 --index-url https://download.pytorch.org/whl/cpu
python research/kernel_001/run294/train291.py
cp research/kernel_001/run294/checkpoints291.json research/kernel_001/run295/checkpoints291.json
cd research/kernel_001/run295
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
RUN295_START=0 RUN295_STOP=80 python evaluate295.py
RUN295_START=80 RUN295_STOP=160 python evaluate295.py
RUN295_START=160 RUN295_STOP=242 python evaluate295.py
python evaluate295.py --finalize
python independent295.py
