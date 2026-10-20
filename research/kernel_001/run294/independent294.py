"""Independent Run294 structural proof; no imports from diagnostic or clock implementation."""
import json
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).resolve().parent
ck={(r['seed'],r['epoch']):r['p'] for r in json.loads((P/'checkpoints291.json').read_text())['rows']}
res=json.loads((P/'results294.json').read_text())
def split(p,n):
 z=[F.from_float(float(t)) for t in p]
 a=[[[z[x*n*n+i*n+j] for j in range(n)] for i in range(n)] for x in range(2)]
 b=[[z[2*n*n+x*n+i] for i in range(n)] for x in range(2)]
 return a,b,z[2*n*n+2*n:-1],z[-1]
def expand(p,g):
 a,b,v,c=split(p,3)
 aa=[[[F(0)]*4 for _ in range(4)] for _ in range(2)]
 bb=[[F(0)]*4 for _ in range(2)]
 for x in range(2):
  for i in range(3):
   for j in range(3):aa[x][i][j]=a[x][i][j]
   bb[x][i]=b[x][i]
  aa[x][3][3]=g;bb[x][3]=F(1)
 return aa,bb,v+[F(0)],c
count=0
for r in res['rows']:
 a,b,v,c=split(ck[(r['seed'],20)],3)
 for label,g in [('stable',F(1,2)),('divergent',F(2))]:
  aa,bb,vv,cc=expand(ck[(r['seed'],20)],g)
  assert vv[3]==0 and cc==c and vv[:3]==v
  assert all(aa[x][i][:3]==a[x][i] and aa[x][i][3]==0 and bb[x][i]==b[x][i] for x in range(2) for i in range(3))
  assert r[label]['restored_score']==r['original']
  count+=1
assert count==490
assert sum(abs(r['divergent']['delta'])>1e-6 for r in res['rows'])==192
print('PASS 490 exact all-word projection checks and 192 changed scores')
