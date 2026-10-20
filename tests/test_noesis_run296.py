"""Public pytest hook for NOESIS Run296 exact trained-checkpoint regression."""
from pathlib import Path
import subprocess
import sys

def test_run296_exact_witness_and_mutation_controls():
    root = Path(__file__).resolve().parents[1]
    subprocess.run(
        [sys.executable, str(root / "research/kernel_001/run296/test_reachability296.py")],
        cwd=root, check=True, timeout=60,
    )
