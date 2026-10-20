#!/usr/bin/env python3
"""Run291 frozen gauge-normalized relaxed LP score, reused without modification."""
import hashlib,itertools,json,math
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
W=3
def unpack(p):
 a=np.asarray(p[:2*W*W],dtype=float).reshape(2,W,W)
 b=np.asarray(p[2*W*W:2*W*W+2*W],dtype=float).reshape(2,W)
 v=np.asarray(p[2*W*W+2*W:-1],dtype=float)
 return a,b,v,float(p[-1])
def canonical(p):
 a,b,v,c=unpack(p)
 d=1/np.max(np.abs(b),axis=0)
 if not np.isfinite(d).all():raise ValueError('zero bias gauge')
 a=a*d[None,:,None]/d[None,None,:]
 b=b*d[None,:];v=v/d
 return a.ravel().tolist()+b.ravel().tolist()+v.tolist()+[c]
def lp(p,delta=.05,certificate=False):
 a,b,v,c=unpack(p);best=float('inf');bestcert=None
 M=4*W+1;slack=4*W; aub=[];bub=[];eq=[];beq=[]
 for bits in range(1<<W):
  aub.clear();bub.clear();eq.clear();beq.clear()
  mask=[[False]*W,[(bits>>i)&1==1 for i in range(W)]]
  def row():return np.zeros(M)
  for s,x,i in itertools.product((0,1),(0,1),range(W)):
   y=0 if x==0 else 1-s
   r=row();r[2*W+W*y+i]-=1
   if not certificate:r[slack]-=1
   for j in range(W):r[(2*W if a[x,i,j]>=0 else 0)+W*s+j]+=a[x,i,j]
   aub.append(r);bub.append(-b[x,i]-(1e-6 if certificate else 0))
   if mask[y][i]:
    r=row();r[W*y+i]+=1
    if not certificate:r[slack]-=1
    for j in range(W):r[(0 if a[x,i,j]>=0 else 2*W)+W*s+j]-=a[x,i,j]
    aub.append(r);bub.append(b[x,i]-(1e-6 if certificate else 0))
  for s in (0,1):
   r=row()
   if s==0:
    for i in range(W):r[(2*W if v[i]>=0 else 0)+i]+=v[i]
    r[slack]+=(1 if certificate else -1)
    aub.append(r);bub.append(-c-(0 if certificate else delta))
   else:
    for i in range(W):r[(0 if v[i]>=0 else 2*W)+W+i]-=v[i]
    r[slack]+=(1 if certificate else -1)
    aub.append(r);bub.append(c-(0 if certificate else delta))
  for s,i in itertools.product((0,1),range(W)):
   r=row();r[W*s+i]=1;r[2*W+W*s+i]=-1;aub.append(r);bub.append(0)
  for i in range(W):
   r=row();r[i]=1;eq.append(r);beq.append(0)
  for s,i in itertools.product((0,1),range(W)):
   if not mask[s][i]:
    r=row();r[W*s+i]=1;eq.append(r);beq.append(0)
  obj=np.zeros(M);obj[slack]=-1 if certificate else 1
  bounds=[(0,1000)]*(4*W)+([(0,100)] if certificate else [(0,None)])
  sol=linprog(obj,A_ub=aub,b_ub=bub,A_eq=eq,b_eq=beq,bounds=bounds,method='highs')
  if sol.success:
   if certificate and sol.x[slack]>1e-6:
    return {'L':sol.x[:2*W].reshape(2,W).tolist(),'U':sol.x[2*W:4*W].reshape(2,W).tolist(),'margin_lp':float(sol.x[slack]),'mask':mask}
   if not certificate:best=min(best,float(sol.x[slack]))
 return best if not certificate else None
