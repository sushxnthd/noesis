"""Independent Fraction-based gauge identity audit."""
import json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
r={(x['seed'],x['epoch']):x for x in json.loads((P.parent/'run288'/'checkpoints288.json').read_text())['rows']}
z=json.loads((P/'results289.json').read_text())
assert len(z['rows'])==1280
for seed in range(20928,21184):
 a=[F.from_float(float(x)) for x in r[(seed,20)]['p']]
 for g in (F(8),F(1,8),F(64),F(1,64)):
  d=[g,1/g]
  A=[a[4*x+2*i+j]*d[i]/d[j] for x in range(2) for i in range(2) for j in range(2)]
  B=[a[8+2*x+i]*d[i] for x in range(2) for i in range(2)]
  V=[a[12+i]/d[i] for i in range(2)]
  assert all(F.from_float(float(q))==q for q in A+B+V)
  assert all(A[4*x+2*i+j]*d[j]==a[4*x+2*i+j]*d[i] for x in range(2) for i in range(2) for j in range(2))
  assert all(V[i]*d[i]==a[12+i] for i in range(2))
assert z['summary']['8_0.125']['max_change']>1e-6
print('INDEPENDENT EXACT CONJUGACY: PASS')
