import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"research/kernel001/run303"
def test_run303_exact():
    d=json.loads((ROOT/"epoch80_22438.json").read_text())
    z=[Q.from_float(float(x)) for x in d["p"]]
    v=z[24:27];T=Q("71/25");mu=[Q("1127/1000"),Q("17/1000")]
    assert all(x>=0 for x in v) and z[27]<0<T+z[27]
    assert all(z[18+i]<=0 for i in range(3))
    assert sum(v[i]*max(Q(0),z[21+i]) for i in range(3))>=T
    for x in (0,1):
        assert all(sum(v[i]*z[9*x+3*i+j] for i in range(3))>=mu[x]*v[j] for j in range(3))
        assert mu[x]*T+sum(v[i]*z[18+3*x+i] for i in range(3))>=T
