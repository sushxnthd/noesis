from pathlib import Path
import importlib.util
from itertools import product
spec=importlib.util.spec_from_file_location("relu_spoof",Path(__file__).resolve().parents[1]/"research"/"run246"/"relu_spoof.py")
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def test_finite_horizon_spoof():
    assert all(m.ok(w) for n in range(1,9) for w in product(range(3),repeat=n))

def test_length_nine_failure():
    assert not m.ok([1]*8+[2])
