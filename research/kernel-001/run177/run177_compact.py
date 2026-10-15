"""Retrospective inductive interval gate; requires archived Run176 source/checkpoints."""
import numpy as np, json
from run176 import ROOT, load, state0, first_block_affine, WIDTHS, SEEDS, WORDS

def mm(X,Y):
 a,b=X;c,d=Y;n,m=a.shape;p=c.shape[1];lo=np.zeros((n,p));hi=lo.copy()
 for k in range(m):
  with np.errstate(invalid='ignore',over='ignore'):
   v=np.stack(np.broadcast_arrays(a[:,k,None]*c[k,None,:],a[:,k,None]*d[k,None,:],b[:,k,None]*c[k,None,:],b[:,k,None]*d[k,None,:]))
  if np.isnan(v).any():return np.full((n,p),-np.inf),np.full((n,p),np.inf)
  lo=np.nextafter(lo+np.nextafter(v.min(0),-np.inf),-np.inf)
  hi=np.nextafter(hi+np.nextafter(v.max(0),np.inf),np.inf)
 return lo,hi

def mv(M,v):
 l,u=mm(M,(v[0][:,None],v[1][:,None]));return l[:,0],u[:,0]

def run(A,E,word):
 n=len(A);h=(np.zeros(n),np.zeros(n))
 for _ in range(6):
  l,u=mv((np.column_stack((A,E[0])),)*2,(np.r_[h[0],1],np.r_[h[1],1]))
  h=(np.maximum(l,0),np.maximum(u,0))
 state=state0(A,E);_,masks=first_block_affine(A,E,state,word)
 I=np.eye(n+1);T=(I,I)
 for t,x in enumerate(word):
  S=np.zeros((n+1,n+1));S[-1,-1]=1
  for i in range(n):
   if masks[t,i]:S[i,:n]=A[i];S[i,n]=E[x,i]
  T=mm((S,S),T)
 B=(np.r_[h[0],1],np.r_[h[1],1]);P=T
 for _ in range(13):
  l,u=mv(P,B);B=(np.minimum(B[0],l),np.maximum(B[1],u));P=mm(P,P)
 h=(B[0][:n],B[1][:n])
 for t,x in enumerate(word):
  l,u=mv((np.column_stack((A,E[x])),)*2,(np.r_[h[0],1],np.r_[h[1],1]))
  active=masks[t].astype(bool)
  if not (np.all(l[active]>0) and np.all(u[~active]<0)):return False
  h=(np.where(active,l,0),np.where(active,u,0))
 return True

if __name__=='__main__':
 rows=[]
 for width in WIDTHS:
  for seed in SEEDS:
   A,E,w,mse,sha=load(width,seed)
   for word in WORDS:
    rows.append(dict(width=width,seed=seed,word=word,accept=run(A,E,np.array([int(x) for x in word],dtype=np.int64))))
 print('accepted',sum(x['accept'] for x in rows),'/',len(rows))
