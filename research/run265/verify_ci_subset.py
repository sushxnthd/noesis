"""Exact dyadic integer witness replay; three trained checkpoints."""
import json
from pathlib import Path
rows=json.loads((Path(__file__).parent/'CI_REPRESENTATIVE_WITNESSES.json').read_text())
assert len(rows)==3
for r in rows:
 p=r['params']
 z=[*sum(p['A'],[]),*sum(p['E'],[]),*p['b'],*p['v'],p['c']]
 D=1<<max(float(t).as_integer_ratio()[1].bit_length()-1 for t in z)
 def q(t):
  a,b=float(t).as_integer_ratio()
  return a*(D//b)
 A=[[q(t) for t in row] for row in p['A']]
 E=[[q(t) for t in row] for row in p['E']]
 b=[q(t) for t in p['b']]
 v=[q(t) for t in p['v']]
 c=q(p['c'])
 h=[0,0]
 scale=1
 first=None
 expected=int(r['prefix']==1)
 for j in range(r['hold_index']+1):
  x=r['prefix'] if j==0 else 0
  h=[max(0,A[i][0]*h[0]+A[i][1]*h[1]+(E[x][i]+b[i])*scale) for i in range(2)]
  scale*=D
  if int(v[0]*h[0]+v[1]*h[1]+c*scale>0)!=expected:
   first=j
   break
 assert first==r['hold_index'],(r['seed'],first)
 print('PASS',r['seed'],r['epoch'],r['prefix'],first)
