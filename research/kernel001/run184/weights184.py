import json
from fractions import Fraction as F
from pathlib import Path
p=json.loads(Path('research/kernel001/run183/reduced_checkpoint.json').read_text())
q=lambda x:F.from_float(float(x))
A=[q(x) for x in p['A1']]
B=[q(x) for x in p['A3']]
E=[[q(x) for x in p[k]] for k in ('E0','E1')]
w=q(p['w1'])
h=[max(F(0),x) for x in E[0]]
for _ in range(5):
 h=[max(F(0),A[i]*h[1]+B[i]*h[3]+E[0][i]) for i in range(7)]
assert all(h[i]==0 for i in range(7) if i!=1)
h0=h[1]
