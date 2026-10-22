"""Run333 exact proof regression tests; optional SymPy checker."""
import json,sys,importlib.util
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from proof333 import prove
verify=None
if importlib.util.find_spec("sympy") is not None:
    from independent333 import verify
p=Path(__file__).resolve().parent
raw=json.loads((p/'newly_certified.json').read_text())['rows']
assert len(raw)==5
for row in raw:
    w=row['p']
    assert len(w)==28 and prove(w),row['seed']
    if verify is not None:assert verify(w),row['seed']
    a=w.copy();a[27]=abs(a[27])+0.1
    assert not prove(a)
    if verify is not None:assert not verify(a)
    a=w.copy();a[18]=abs(a[18])+0.1
    assert not prove(a)
    if verify is not None:assert not verify(a)
    a=w.copy();a[21:24]=[-10.,-10.,-10.]
    assert not prove(a)
    if verify is not None:assert not verify(a)
print('Five certificates and fifteen mutated controls verified')
