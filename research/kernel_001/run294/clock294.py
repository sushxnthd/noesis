"""NOESIS Run294: exact rational clock augmentation and backward-observability pruning."""
from fractions import Fraction as F
import diagnostic291 as D
def unpack(p,w):
 z=[F.from_float(float(x)) for x in p]
 assert len(z)==2*w*w+3*w+1
 a=[[[z[x*w*w+i*w+j] for j in range(w)] for i in range(w)] for x in range(2)]
 b=[[z[2*w*w+x*w+i] for i in range(w)] for x in range(2)]
 return a,b,z[2*w*w+2*w:-1],z[-1]
def pack(a,b,v,c):
 return [t for ax in a for row in ax for t in row]+[t for bx in b for t in bx]+list(v)+[c]
def augment(p,gain):
 a,b,v,c=unpack(p,3)
 aa=[[[F(0)]*4 for i in range(4)] for x in range(2)]
 bb=[[F(0)]*4 for x in range(2)]
 for x in range(2):
  for i in range(3):
   aa[x][i][:3]=a[x][i];bb[x][i]=b[x][i]
  aa[x][3][3]=gain;bb[x][3]=F(1)
 return pack(aa,bb,v+[F(0)],c)
def exact_projection(p,q):
 a,b,v,c=unpack(p,3);aa,bb,vv,cc=unpack(q,4)
 return (c==cc and v==vv[:3] and vv[3]==0 and
  all(aa[x][i][:3]==a[x][i] and aa[x][i][3]==0 and bb[x][i]==b[x][i]
      for x in range(2) for i in range(3)))
def prune(p,w):
 a,b,v,c=unpack(p,w)
 keep={i for i in range(w) if v[i]!=0}
 while True:
  nxt=keep|{j for i in keep for j in range(w) if any(a[x][i][j]!=0 for x in range(2))}
  if nxt==keep:break
  keep=nxt
 indices=sorted(keep)
 assert indices
 assert all(v[j]==0 for j in range(w) if j not in keep)
 assert all(a[x][i][j]==0 for x in range(2) for i in keep for j in range(w) if j not in keep)
 aa=[[[a[x][i][j] for j in indices] for i in indices] for x in range(2)]
 bb=[[b[x][i] for i in indices] for x in range(2)]
 return pack(aa,bb,[v[i] for i in indices],c),indices
def score(p,w):
 D.W=w
 return -float(D.lp(D.canonical([float(x) for x in p])))
