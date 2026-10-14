"""Frozen Run154 local-affine task-cycle diagnostic. Requires numpy."""
import itertools
import numpy as np
def parameters(cp):
 p=cp["parameters"]
 return np.asarray(p["A"],float),np.asarray(p["E"],float),np.asarray(p["w"],float)
def prefixes(A,E):
 words=np.array(list(itertools.product(range(3),repeat=6)),dtype=int)
 h=np.zeros((729,A.shape[0]));q=np.zeros(729,dtype=int)
 for t in range(6):
  z=words[:,t];h=np.maximum(0,h@A.T+E[z])
  q=np.maximum(0,q+(z==0)-(z==1))
 return h,q
def affine(h,A,E,word):
 n,d=h.shape;x=h.copy();J=np.broadcast_to(np.eye(d),(n,d,d)).copy()
 for token in word:
  pre=x@A.T+E[token];mask=(pre>0).astype(float)
  J=np.einsum("ni,ij,njk->nik",mask,A,J,optimize=True)
  x=np.maximum(0,pre)
 b=x-np.einsum("nij,nj->ni",J,h)
 return J,b
def score(cp,include_increment=False):
 A,E,w=parameters(cp);h,q=prefixes(A,E)
 specs=[("neutral",(2,),32,0),("roundtrip",(0,1),16,0)]
 if include_increment:specs.append(("increment",(0,),32,32))
 parts={}
 for name,word,k,delta in specs:
  J,b=affine(h,A,E,word);x=h.copy()
  for _ in range(k):x=np.einsum("nij,nj->ni",J,x)+b
  errors=x@w-(q+delta);idx=int(np.argmax(abs(errors)))
  parts[name]={"score":float(abs(errors[idx])),"prefix_index":idx}
 return {"components":parts,"score":max(v["score"] for v in parts.values()),
         "predict_failure":max(v["score"] for v in parts.values())>0.1}
