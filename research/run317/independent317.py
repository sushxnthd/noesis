"""Independent SymPy vertex/ray certificate. No imports from exact317."""
import json
from pathlib import Path
from sympy import Rational, Integer
P=Path(__file__).resolve().parent
p=[Rational(*x.as_integer_ratio()) for x in json.loads((P/'seed22642_epoch80.json').read_text())]
p[0]=Rational(11,10);p[27]=-Rational(1,100)
Z=(Integer(0),)*3
def pre(h,x,i):return p[18+3*x+i]+sum(p[9*x+3*i+j]*h[j] for j in range(3))
def step(h,x):return tuple(max(Integer(0),pre(h,x,i)) for i in range(3))
V=[(Integer(1),Integer(0),Integer(0)),(Integer(1),Integer(0),Integer(3))]
assert step(Z,0)==Z and p[27]<0
e=step(Z,1)
assert e[1]==0 and e[0]>=1 and 0<=e[2]<=3*e[0]
for x in (0,1):
    for h in V:
        assert pre(h,x,1)<=0 and pre(h,x,0)>=1
        assert 3*pre(h,x,0)>=pre(h,x,2)
        assert pre(h,x,1)-p[18+3*x+1]<=0
        assert pre(h,x,0)-p[18+3*x]>=0
        assert 3*(pre(h,x,0)-p[18+3*x])>=pre(h,x,2)-p[18+3*x+2]
for h in V:
    assert p[27]+sum(p[24+i]*h[i] for i in range(3))>=Rational(1,100)
    assert sum(p[24+i]*h[i] for i in range(3))>=0
print('PASS independent SymPy all-length certificate')
