"""NOESIS Run289 function-preserving diagonal gauge and canonicalization."""
from fractions import Fraction as F
import itertools
import numpy as np
def gauge(p,d):
 a=np.asarray(p[:8]).reshape(2,2,2);b=np.asarray(p[8:12]).reshape(2,2);v=np.asarray(p[12:14]);d=np.asarray(d)
 return (a*d[None,:,None]/d[None,None,:]).ravel().tolist()+(b*d[None,:]).ravel().tolist()+(v/d).tolist()+[p[14]]
def canonical(p):
 b=np.asarray(p[8:12]).reshape(2,2);norm=np.max(np.abs(b),axis=0)
 if not np.all(norm>0):raise ValueError("zero bias column")
 return gauge(p,(1/norm).tolist())
def auc(vals):
 pos=[s for s,y in vals if y];neg=[s for s,y in vals if not y]
 return float(sum(float(p>n)+.5*float(p==n) for p in pos for n in neg)/(len(pos)*len(neg)))
def exact_check(p,d,limit=0):
 q=gauge(p,d);D=[F.from_float(float(x)) for x in d]
 for x in range(2):
  for i in range(2):
   assert F.from_float(q[8+2*x+i])==D[i]*F.from_float(p[8+2*x+i])
   assert F.from_float(q[12+i])*D[i]==F.from_float(p[12+i])
   for j in range(2):
    assert F.from_float(q[4*x+2*i+j])*D[j]==D[i]*F.from_float(p[4*x+2*i+j])
 def step(pp,h,x):
  return [max(F(0),sum(F.from_float(pp[4*x+2*i+j])*h[j] for j in range(2))+F.from_float(pp[8+2*x+i])) for i in range(2)]
 for n in range(limit+1):
  for w in itertools.product((0,1),repeat=n):
   h=[F(0),F(0)];hh=h.copy()
   for x in w:
    h=step(p,h,x);hh=step(q,hh,x)
    assert all(hh[i]==D[i]*h[i] for i in range(2))
   z=sum(F.from_float(p[12+i])*h[i] for i in range(2))+F.from_float(p[14])
   zz=sum(F.from_float(q[12+i])*hh[i] for i in range(2))+F.from_float(q[14])
   assert z==zz
 return True
