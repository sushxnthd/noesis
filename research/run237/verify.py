from fractions import Fraction as F
from collections import deque
from pathlib import Path
import json
R=Path(__file__).parent
def check(row,limit=2500,max_depth=15):
 p=row['params'];dim=row['dim']
 exact=lambda x:F.from_float(float(x))
 W=[[[exact(a) for a in line] for line in mat] for mat in p['W']]
 b=[[exact(a) for a in vec] for vec in p['b']];v=[exact(a) for a in p['v']];c=exact(p['c'])
 initial=tuple([F(1,2),F(-1,2),F(1,4)]+([F(1,8)] if dim==4 else []))
 seen={(0,initial):()};queue=deque([(0,initial)])
 while queue:
  q,h=queue.popleft();w=seen[(q,h)]
  if len(w)>=max_depth:return dict(status='ABSTAIN',reason='depth_limit',states=len(seen))
  for t in range(3):
   qq=0 if t==2 else (1-q if t==1 else q)
   hh=tuple(max(F(-1),min(F(1),sum((W[t][j][k]*h[k] for k in range(dim)),b[t][j]))) for j in range(dim))
   z=sum((v[j]*hh[j] for j in range(dim)),c)
   if (qq==1 and z<=0) or (qq==0 and z>=0):
    return dict(status='INCORRECT',witness=list(w+(t,)))
   st=(qq,hh)
   if st not in seen:
    if len(seen)>=limit:return dict(status='ABSTAIN',reason='state_limit',states=len(seen))
    seen[st]=w+(t,);queue.append(st)
 return dict(status='CERTIFIED',states=len(seen))
if __name__=='__main__':
 D=json.load(open(R/'CHECKPOINTS.json'));out=[]
 for row in D['rows']:
  if row['epoch'] not in (0,200):continue
  r=check(row);out.append({k:row[k] for k in ['dim','seed','arm','epoch']}|r)
  print(row['dim'],row['seed'],row['arm'],row['epoch'],r['status'],flush=True)
 (R/'EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
