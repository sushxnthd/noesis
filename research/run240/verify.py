"""Sound exact-reachability checker for RESET PARITY, dyadic floats as rationals."""
from fractions import Fraction as F
from collections import deque
import hashlib
def check(row,limit=2500,max_depth=15):
 p=row['params'];dim=row['dim'];exact=lambda x:F.from_float(float(x))
 W=[[[exact(a) for a in line] for line in mat] for mat in p['W']]
 b=[[exact(a) for a in vec] for vec in p['b']];v=[exact(a) for a in p['v']];c=exact(p['c'])
 initial=tuple([F(1,2),F(-1,2),F(1,4),F(1,8)])
 seen={(0,initial):()};queue=deque([(0,initial)]);edges=0
 while queue:
  q,h=queue.popleft();w=seen[(q,h)]
  if len(w)>=max_depth:return dict(status='ABSTAIN',reason='depth_limit',states=len(seen))
  for t in range(3):
   qq=0 if t==2 else (1-q if t==1 else q)
   hh=tuple(max(F(-1),min(F(1),sum((W[t][j][k]*h[k] for k in range(dim)),b[t][j]))) for j in range(dim))
   z=sum((v[j]*hh[j] for j in range(dim)),c);edges+=1
   if (qq==1 and z<=0) or (qq==0 and z>=0):
    return dict(status='INCORRECT',witness=list(w+(t,)),logit_sign=(z>0)-(z<0),edges_checked=edges)
   st=(qq,hh)
   if st not in seen:
    if len(seen)>=limit:return dict(status='ABSTAIN',reason='state_limit',states=len(seen))
    seen[st]=w+(t,);queue.append(st)
 return dict(status='CERTIFIED',states=len(seen),edges_checked=edges,graph_sha256=hashlib.sha256('\n'.join(sorted(str((q,tuple(str(x) for x in h))) for q,h in seen)).encode()).hexdigest())
