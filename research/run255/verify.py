import json
from pathlib import Path
from fractions import Fraction as Q
P=Path(__file__).resolve().parent
witnesses=json.loads((P/'EXACT_WITNESSES.json').read_text())
rows=json.loads((P/'CHECKPOINTS.json').read_text())['rows']
for m in rows:
 if m['epoch']!=200:continue
 p=m['params'];A=[[Q.from_float(t) for t in r] for r in p['A']]
 E=[[Q.from_float(t) for t in r] for r in p['E']]
 b=list(map(Q.from_float,p['b']));v=list(map(Q.from_float,p['v']))
 c=Q.from_float(p['c']);h=[Q(0)]*4;q=0
 for ch in witnesses[m['task']][str(m['seed'])]:
  s=int(ch)
  q=0 if s==2 else (q^(s==1) if m['task']=='parity' else (1 if s==1 else q))
  h=[max(Q(0),sum((A[i][j]*h[j] for j in range(4)),E[s][i]+b[i])) for i in range(4)]
 z=sum((v[i]*h[i] for i in range(4)),c)
 if int(z>0)==q:raise AssertionError(m['seed'])
print('PASS: 16 exact rational witnesses')
