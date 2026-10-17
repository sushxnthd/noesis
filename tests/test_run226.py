"""Remote regression: independently recheck Run226's trained transition."""
from pathlib import Path
import importlib.util
def test_run226_inductive_certificate():
    path=Path(__file__).resolve().parents[1]/"research"/"kernel_001"/"run226"/"check_decimal.py"
    spec=importlib.util.spec_from_file_location("run226_decimal",path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.verify()
