"""Exact rational checker and adversarial witness search; no LP trust."""
import random
from fractions import Fraction as F
def check(p,box):
 q=[F.from_float(float(x)) for x in p]
 L=[[F.from_float(float(x)) for x in row] for row in box['L']]
 U=[[F.from_float(float(x)) for x in row] for row in box['U']]
 if not all(L[0][i]<=0<=U[0][i] for i in (0,1)):return False
 for s in (0,1):
  for x in (0,1):
   y=0 if x==0 else 1-s
   for i in (0,1):
    a=q[4*x+2*i:4*x+2*i+2];b=q[8+2*x+i]
    lo=b+sum(a[j]*(L[s][j] if a[j]>=0 else U[s][j]) for j in (0,1))
    hi=b+sum(a[j]*(U[s][j] if a[j]>=0 else L[s][j]) for j in (0,1))
    if max(F(0),lo)<L[y][i] or max(F(0),hi)>U[y][i]:return False
 for s in (0,1):
  v=q[12:14];c=q[14]
  low=c+sum(v[i]*(L[s][i] if v[i]>=0 else U[s][i]) for i in (0,1))
  high=c+sum(v[i]*(U[s][i] if v[i]>=0 else L[s][i]) for i in (0,1))
  if s==0 and not high<0:return False
  if s==1 and not low>0:return False
 return True
def exact_witness(p,word):
 q=[F.from_float(float(x)) for x in p];h=[F(0),F(0)];s=0
 for t,x in enumerate(word,1):
  h=[max(F(0),q[4*x+2*i]*h[0]+q[4*x+2*i+1]*h[1]+q[8+2*x+i]) for i in (0,1)]
  s=0 if x==0 else 1-s
  if ((q[12]*h[0]+q[13]*h[1]+q[14])>0)!=bool(s):return t
 return None
def step(p,h,x):
 return [max(0.,p[4*x+2*i]*h[0]+p[4*x+2*i+1]*h[1]+p[8+2*x+i]) for i in (0,1)]
def find_witness(p,seed):
 h=step(p,[0.,0.],0);s=0
 for n in range(1,257):
  h=step(p,h,1);s=1-s
  if ((p[12]*h[0]+p[13]*h[1]+p[14])>0)!=bool(s):
   word=[0]+[1]*n;e=exact_witness(p,word)
   if e is not None:return {'kind':'reset_toggle','length':e,'word':''.join(map(str,word[:e]))}
   break
 rng=random.Random(286000+seed)
 for L in (64,128):
  for k in range(256):
   word=[0 if rng.random()<.2 else 1 for _ in range(L)]
   h=[0.,0.];s=0;t=None
   for j,x in enumerate(word,1):
    h=step(p,h,x);s=0 if x==0 else 1-s
    if ((p[12]*h[0]+p[13]*h[1]+p[14])>0)!=bool(s):t=j;break
   if t is not None:
    e=exact_witness(p,word[:t])
    if e is not None:return {'kind':f'mixed_{L}_{k}','length':e,'word':''.join(map(str,word[:e]))}
 return None
