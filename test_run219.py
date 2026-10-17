"""Run219 frozen diagnostic remote regression: import executes all preregistered assertions."""
import runpy
from pathlib import Path
def test_run219_frozen_scalar_transfer():
    script=Path(__file__).resolve().parent/"research"/"kernel_001"/"run219"/"reproduce.py"
    r=runpy.run_path(str(script))
    assert len(r["W"])==112
    assert abs(r["A"]["suffix"]-0.75)<1e-12
    assert abs(r["A"]["shuffle"]-2/3)<1e-12
    assert len(r["P"])==3 and len(r["N"])==4
