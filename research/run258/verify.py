import json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
rows=json.loads((P/'CHECKPOINTS.json').read_text())['rows']
models={r['seed']:r['params'] for r in rows if r['epoch']==200}
w=json.loads((P/'MINIMIZED_WITNESSES.json').read_text())['witnesses']
assert len(models)==64 and len(w)==20
for seed,word in w.items():
 p=models[int(seed)];A=[[F.from_float(x) for x in row] for row in p['A']]
 E=[[F.from_float(x) for x in row] for row in p['E']]
 b=list(map(F.from_float,p['b']));v=list(map(F.from_float,p['v']))
 h=[F(0)]*4;q=0
 for x in word:
  s=int(x);h=[max(F(0),sum((A[i][j]*h[j] for j in range(4)),E[s][i]+b[i])) for i in range(4)]
  q=0 if s==2 else q^(s==1)
 z=sum((v[i]*h[i] for i in range(4)),F.from_float(p['c']))
 assert (z>0)!=bool(q),seed
 print('PASS',seed,len(word))
