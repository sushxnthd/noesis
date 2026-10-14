import json
from pathlib import Path
from fractions import Fraction as Q
C={210:([0,3],Q(1),Q(3)),214:([0,1],Q(2),Q(9,2)),215:([0,2],Q(2,5),Q(1,2))}
def check(seed):
 p=Path(__file__).parent/'checkpoints'/f'{seed}.json'
 r=json.loads(p.read_text())
 A=[[Q(x) for x in row] for row in r['A']];e=list(map(Q,r['E'][0]))
 ids,l,u=C[seed]
 def inside(v):return v[0]>0 and l*v[0]<=v[1]<=u*v[0]
 assert inside([e[i] for i in ids])
 for ratio in (l,u):
  v=[Q(1),ratio]
  z=[sum(A[i][j]*v[k] for k,j in enumerate(ids)) for i in range(4)]
  assert inside([z[i] for i in ids])
  assert all(z[i]>=0 for i in ids)
  assert all(z[i]<=0 for i in range(4) if i not in ids)
 assert all(e[i]>0 for i in ids)
 assert all(e[i]<0 for i in range(4) if i not in ids)
 return True
