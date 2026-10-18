"""Exact state graph size at epoch100, capped after 1000."""
from fractions import Fraction as F
def graph_size(row,cap=1000,depth=7):
 p=row['params'];d=row['dim'];f=lambda x:F.from_float(float(x))
 W=[[[f(a) for a in line] for line in mat] for mat in p['W']]
 b=[[f(a) for a in vec] for vec in p['b']]
 h=(F(1,2),F(-1,2),F(1,4),F(1,8));seen={h};cur={h}
 for _ in range(depth):
  nxt=set()
  for h in cur:
   for t in range(3):
    hh=tuple(max(F(-1),min(F(1),sum((W[t][j][k]*h[k] for k in range(d)),b[t][j]))) for j in range(d))
    if hh not in seen:nxt.add(hh)
    if len(seen)+len(nxt)>cap:return cap+1
  seen|=nxt;cur=nxt
  if not cur:break
 return len(seen)
