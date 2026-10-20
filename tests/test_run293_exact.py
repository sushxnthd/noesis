from pathlib import Path
import runpy

def test_run293_relational_quotient():
    p = Path(__file__).resolve().parents[1] / 'research/kernel_001/run293/test_run293.py'
    runpy.run_path(str(p))['test_trained_witness']()
