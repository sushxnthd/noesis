"""Run153-style beam witness search and independent rational checker."""
import numpy as np
from fractions import Fraction as F
try:
 from .score import parameters
except ImportError:
 from score import parameters
def beam(cp,depth_limit=128):
 A,E,w=parameters(cp);h=np.zeros((1,len(w)));q=np.zeros(1,dtype=int);words=[b""]
 for depth in range(1,depth_limit+1):
  n=len(q);z=np.maximum(0,np.repeat(h,3,axis=0)@A.T+np.tile(E,(n,1)))
  tq=np.maximum(0,np.repeat(q,3)+np.tile([1,-1,0],n))
  err=z@w-tq;i=int(np.argmax(abs(err)))
  if abs(err[i])>0.1:
   return {"found":True,"depth":depth,"word":list(words[i//3]+bytes([i%3])),"float_error":float(err[i])}
  keep=set()
  for target in np.unique(tq):
   ix=np.flatnonzero(tq==target);norm=np.sum(abs(z[ix]),axis=1)
   for s in (err[ix],-err[ix],norm,-norm):
    keep.update(map(int,ix[np.argsort(-s,kind="stable")[:4]]))
  ix=sorted(keep);h=z[ix];q=tq[ix];words=[words[j//3]+bytes([j%3]) for j in ix]
 return {"found":False,"depth":None,"word":None}
def exact(cp,word):
 p=cp["parameters"];f=lambda x:F(str(x))
 A=[[f(v) for v in row] for row in p["A"]]
 E=[[f(v) for v in row] for row in p["E"]];w=[f(v) for v in p["w"]]
 d=len(w);h=[F(0)]*d;q=0
 for t in word:
  h=[max(F(0),sum(A[i][j]*h[j] for j in range(d))+E[t][i]) for i in range(d)]
  q=max(0,q+(1 if t==0 else -1 if t==1 else 0))
 error=sum(w[i]*h[i] for i in range(d))-q
 return {"error":float(error),"failure":abs(error)>F(1,10)}
