"""Independent exact dyadic verification of adversarial full-latch prefix."""
import json
from fractions import Fraction
from pathlib import Path
models=json.loads((Path(__file__).parent/'SEED18453_CHECKPOINTS.json').read_text())
p=next(x['params'] for x in models if x['epoch']==100)
R=lambda z:Fraction(*float(z).as_integer_ratio())
A=[[R(z) for z in row] for row in p['A']]
e=[[R(p['E'][symbol][i])+R(p['b'][i]) for i in range(2)] for symbol in (0,1)]
v=[R(z) for z in p['v']];bias=R(p['c'])
scale=1<<60
assert all((scale*z).denominator==1 for z in [*sum(A,[]),*sum(e,[]),*v,bias])
A=[[int(scale*z) for z in row] for row in A]
e=[[int(scale*z) for z in row] for row in e]
v=[int(scale*z) for z in v];bias=int(scale*bias)
x0=x1=0;den=1;first=None
for step in range(1,2875):
    symbol=int(step==1)
    t0=A[0][0]*x0+A[0][1]*x1+e[symbol][0]*den
    t1=A[1][0]*x0+A[1][1]*x1+e[symbol][1]*den
    x0=max(0,t0);x1=max(0,t1)
    den*=scale
    numerator=v[0]*x0+v[1]*x1+bias*den
    if numerator<=0:
        first=step
        break
assert first==2874
print('PASS exact full-latch counterexample 1 followed by 2873 holds')
