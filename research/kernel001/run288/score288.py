#!/usr/bin/env python3
"""Frozen early LP-slack score; endpoint-blind. Run after train288.py."""
import json,hashlib,math
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
def relaxed_margin(p,delta=0.05):
 A=np.array(p[:8]).reshape(2,2,2);b=np.array(p[8:12]).reshape(2,2);v=p[12:14];c=p[14]
 best=float('inf')
 for maskbits in range(4):
  mask=[[False,False],[bool(maskbits&1),bool(maskbits&2)]]
  aub=[];bub=[];eq=[];beq=[]
  def row():return np.zeros(9)
  for s in (0,1):
   for x in (0,1):
    y=0 if x==0 else 1-s
    for i in (0,1):
     r=row();r[4+2*y+i]-=1;r[8]=-1
     for j in (0,1):r[(4 if A[x,i,j]>=0 else 0)+2*s+j]+=A[x,i,j]
     aub.append(r);bub.append(-b[x,i])
     if mask[y][i]:
      r=row();r[2*y+i]+=1;r[8]=-1
      for j in (0,1):r[(0 if A[x,i,j]>=0 else 4)+2*s+j]-=A[x,i,j]
      aub.append(r);bub.append(b[x,i])
  for s in (0,1):
   r=row();r[8]=-1
   if s==0:
    for i in (0,1):r[(4 if v[i]>=0 else 0)+i]+=v[i]
    aub.append(r);bub.append(-c-delta)
   else:
    for i in (0,1):r[(0 if v[i]>=0 else 4)+2+i]-=v[i]
    aub.append(r);bub.append(c-delta)
  for s in (0,1):
   for i in (0,1):
    r=row();r[2*s+i]=1;r[4+2*s+i]=-1;aub.append(r);bub.append(0)
  for i in (0,1):
   r=row();r[i]=1;eq.append(r);beq.append(0)
  for s in (0,1):
   for i in (0,1):
    if not mask[s][i]:
     r=row();r[2*s+i]=1;eq.append(r);beq.append(0)
  obj=np.zeros(9);obj[8]=1
  sol=linprog(obj,A_ub=aub,b_ub=bub,A_eq=eq,b_eq=beq,bounds=[(0,1000)]*8+[(0,None)],method='highs')
  if sol.success:best=min(best,sol.x[8])
 return best
if __name__=='__main__':
 d=json.loads((P/'checkpoints288.json').read_text())
 assert d['config']['seeds']==list(range(20928,21184))
 r={(x['seed'],x['epoch']):x for x in d['rows']}
 scores=[]
 for seed in range(20928,21184):
  x=r[(seed,20)]
  scores.append(dict(seed=seed,score=-relaxed_margin(x['p']),bce_baseline=-x['bce'],accuracy_baseline=x['accuracy'],parameter_norm_baseline=-math.fsum(v*v for v in x['p'])**.5))
 out=P/'FROZEN_EARLY_SCORES.json';out.write_text(json.dumps(scores,indent=2,sort_keys=True)+'\n')
 digest=hashlib.sha256(out.read_bytes()).hexdigest()
 print('EARLY_SCORE_SHA256',digest)
 assert digest=='d1fa94298a74ae79f59da22fc239d3e451cc2432a970e0d533bc4bb3245fed8a'
