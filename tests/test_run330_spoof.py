import runpy
from pathlib import Path

def test_run330_exact_spoof():
    root = Path(__file__).resolve().parents[1]
    runpy.run_path(str(root / "research" / "run330" / "spoof330.py"))
