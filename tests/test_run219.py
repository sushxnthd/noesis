"""Ensure generic CI actually runs Run219 frozen reproduction."""
import runpy
from pathlib import Path
def test_run219_remote():
    root=Path(__file__).resolve().parents[1]
    result=runpy.run_path(str(root/"research"/"kernel_001"/"run219"/"reproduce.py"))
    assert result["A"]["suffix"]==0.75
    assert abs(result["A"]["shuffle"]-2/3)<1e-12
    assert len(result["P"])==3 and len(result["N"])==4
