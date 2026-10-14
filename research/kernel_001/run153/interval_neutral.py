import itertools,numpy as np
from .beam_search import load
def dn(x):return np.nextafter(x,-np.inf)
def up(x):return np.nextafter(x,np.inf)
def step(lo,hi,A,e):
 n=len(lo);nl=np.empty_like(lo);nh=np.empty_like(hi)
 for i in range(4):
  l=np.full(n,float(e[i]));u=l.copy()
  for j in range(4):
   a=float(A[i,j]);pl=lo[:,j]*a if a>=0 else hi[:,j]*a;ph=hi[:,j]*a if a>=0 else lo[:,j]*a
   l=dn(l+dn(pl));u=up(u+up(ph))
  nl[:,i]=np.maximum(0,l);nh[:,i]=np.maximum(0,u)
 return nl,nh
def certify(seed,depth):
 p=load(seed);A=np.asarray(p['A']);E=np.asarray(p['E']);w=np.asarray(p['w'])
 words=np.array(list(itertools.product(range(3),repeat=6)),dtype=np.int8)
 lo=np.zeros((729,4));hi=lo.copy();q=np.zeros(729,dtype=np.int32)
 for t in range(6):
  for s in range(3):
   ix=np.where(words[:,t]==s)[0]
   lo[ix],hi[ix]=step(lo[ix],hi[ix],A,E[s])
   q[ix]=np.maximum(0,q[ix]+(1 if s==0 else -1 if s==1 else 0))
 for d in range(7,depth+1):
  lo,hi=step(lo,hi,A,E[2]);l=np.zeros(729);u=l.copy()
  for j in range(4):
   a=float(w[j]);pl=lo[:,j]*a if a>=0 else hi[:,j]*a;ph=hi[:,j]*a if a>=0 else lo[:,j]*a
   l=dn(l+dn(pl));u=up(u+up(ph))
  l=dn(l-q);u=up(u-q);upper=np.maximum(abs(l),abs(u))
  if d<depth:assert np.max(upper)<.1
  else:
   i=int(np.argmax(upper));lower=0 if l[i]<=0<=u[i] else min(abs(l[i]),abs(u[i]))
   assert lower>.1
   return float(lower)
