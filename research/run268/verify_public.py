import json
from pathlib import Path
from fractions import Fraction as Q
rows=json.loads((Path(__file__).parent/'PUBLIC_EXACT_MODELS.json').read_text())
for r in rows:
 p=r['params']
 A=[[Q.from_float(x) for x in row] for row in p['A']]
 E=[[Q.from_float(x) for x in row] for row in p['E']]
 b=list(map(Q.from_float,p['b']))
 v=list(map(Q.from_float,p['v']))
 c=Q.from_float(p['c'])
 h=[Q(0)]*len(b)
 q=0
 first=None
 word=[r['head']]+[0]*r['holds']+[r['tail']]
 for t,s in enumerate(word,1):
  q=1 if s==1 else 0 if s==2 else q
  h=[max(Q(0),sum(A[i][j]*h[j] for j in range(len(b)))+E[s][i]+b[i]) for i in range(len(b))]
  z=sum(v[j]*h[j] for j in range(len(b)))+c
  if first is None and int(z>0)!=q:first=t
 assert first==r['first_error_position'],(r['seed'],first)
 print('EXACT PASS',r['seed'],first)
