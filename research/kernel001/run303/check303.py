import json
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
d=json.loads((P/'epoch80_22438.json').read_text())
z=[Q.from_float(float(t)) for t in d['p']]
v=z[24:27];c=z[27];T=Q('71/25');mu=[Q('1127/1000'),Q('17/1000')]
assert c<0 and T+c>0 and all(w>=0 for w in v) and any(v)
assert all(z[18+i]<=0 for i in range(3))
assert sum(v[i]*max(Q(0),z[21+i]) for i in range(3))>=T
for x in (0,1):
    assert mu[x]>=0
    for j in range(3):
        assert sum(v[i]*z[9*x+3*i+j] for i in range(3))>=mu[x]*v[j]
    assert mu[x]*T+sum(v[i]*z[18+3*x+i] for i in range(3))>=T
print('EXACT_ALL_LENGTH_CERTIFIED',d['seed'])
