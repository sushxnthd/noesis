"""Run333 regression tests for exact certificates and corrupted controls."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from proof333 import prove
from independent333 import verify

p=Path(__file__).resolve().parent
raw=json.loads((p/'newly_certified.json').read_text())['rows']
assert len(raw)==5
for row in raw:
    w=row['p']
    assert len(w)==28
    assert prove(w) and verify(w),row['seed']
    a=w.copy();a[27]=abs(a[27])+0.1
    assert not prove(a) and not verify(a)
    a=w.copy();a[18]=abs(a[18])+0.1
    assert not prove(a) and not verify(a)
    a=w.copy();a[21:24]=[-10.,-10.,-10.]
    assert not prove(a) and not verify(a)
print('5 exact certificates; 15 mutated controls rejected by two independent methods')
