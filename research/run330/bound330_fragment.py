# Append to rank330.py or import its ranks()
from fractions import Fraction as Q
def sharp_bounds(group):
 rs=ranks([r["score"] for r in group]);rl=ranks([r["loss"] for r in group])
 d=[a-b for a,b in zip(rs,rl)]
 p=[i for i,r in enumerate(group) if r["outcome"]=="certified"]
 u=[i for i,r in enumerate(group) if r["outcome"]=="unresolved"]
 base=sum((d[i] for i in p),Q(0));ans=[]
 for rev in (False,True):
  order=sorted(u,key=lambda i:d[i],reverse=rev)
  total=base;best=None
  for k in range(len(u)+1):
   val=total/((len(p)+k)*(len(group)-len(p)-k))
   if best is None or (val>best if rev else val<best):best=val
   if k<len(u):total+=d[order[k]]
  ans.append(best)
 return ans
