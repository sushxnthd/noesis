#!/usr/bin/env python3
"""Public CPU replay of frozen NOESIS Run315: run train315.py first."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
P=Path(__file__).resolve().parent
HASH='2a540bbcefba298bf159a93c71345c48a0586244180562af8fbe2e8954a74d43'
def cone(p):
 z=list(map(F.from_float,p));v=z[24:27];c=z[27]
 if c>=0 or any(z[18+i]>0 for i in range(3)) or any(x<0 for x in v) or not any(v):return None
 T=sum(v[i]*max(F(0),z[21+i]) for i in range(3));lo=max(F(0),-c);mu=[]
 for x in (0,1):
  q=[sum(v[i]*z[9*x+3*i+j] for i in range(3)) for j in range(3)]
  if any(v[j]==0 and q[j]<0 for j in range(3)):return None
  m=min(q[j]/v[j] for j in range(3) if v[j]>0)
  if m<0:return None
  mu.append(m);beta=sum(v[i]*z[18+3*x+i] for i in range(3))
  if m==1:
   if beta<0:return None
  elif m>1:lo=max(lo,-beta/(m-1))
  else:T=min(T,beta/(1-m))
 if lo>T or T<=-c or T<=0:return None
 return {'T':str(T),'mu':[str(x) for x in mu]}
def exact_wrong(p,s):
 z=list(map(F.from_float,p));h=[F(0)]*3;y=0
 for bit in s:
  x=int(bit);y|=x
  h=[max(F(0),sum(z[9*x+3*i+j]*h[j] for j in range(3))+z[18+3*x+i]) for i in range(3)]
  if (sum(z[24+i]*h[i] for i in range(3))+z[27]>0)!=bool(y):return True
 return False
def witness(p):
 z=np.asarray(p);a=z[:18].reshape(2,3,3);b=z[18:24].reshape(2,3);v=z[24:27];c=z[27]
 h=np.zeros((1,3));y=np.zeros(1,dtype=np.int8);words=np.zeros(1,dtype=np.int64)
 for n in range(1,13):
  hs=[];ys=[];ws=[]
  for x in (0,1):
   hh=np.maximum(0,h@a[x].T+b[x]);yy=np.maximum(y,x);ww=words*2+x
   for i in np.flatnonzero(((hh@v+c)>0)!=yy)[:32]:
    s=format(int(ww[int(i)]),f'0{n}b')
    if exact_wrong(p,s):return s
   hs.append(hh);ys.append(yy);ws.append(ww)
  h=np.concatenate(hs);y=np.concatenate(ys);words=np.concatenate(ws)
 return None
def auc(pos,neg,key):
 return sum((a[key]>b[key])+.5*(a[key]==b[key]) for a in pos for b in neg)/(len(pos)*len(neg))
def main():
 assert hashlib.sha256((P/'FROZEN_EARLY_SCORES315.json').read_bytes()).hexdigest()==HASH
 ck=json.loads((P/'checkpoints315.json').read_text());scores=json.loads((P/'FROZEN_EARLY_SCORES315.json').read_text())
 by={(r['seed'],r['epoch']):r for r in ck['rows']};e={r['seed']:r for r in scores};rows=[]
 for seed in range(22600,22696):
  p=by[seed,80]['p'];proof=cone(p);word=None if proof else witness(p)
  rows.append({'seed':seed,'outcome':'certified' if proof else 'incorrect' if word else 'unresolved','certificate':proof,'witness':word,**e[seed]})
 pos=[r for r in rows if r['outcome']=='certified'];neg=[r for r in rows if r['outcome']=='incorrect']
 assert (len(pos),len(neg),len(rows)-len(pos)-len(neg))==(4,43,49)
 ar=auc(pos,neg,'retention_score');al=auc(pos,neg,'negative_bce');delta=ar-al
 assert abs(ar-0.627906976744186)<1e-12 and abs(al-0.9011627906976745)<1e-12
 out={'correct':len(pos),'incorrect':len(neg),'unresolved':49,'auc_retention':ar,'auc_loss':al,'delta':delta,'decision':'FAIL','rows':rows}
 (P/'reproduced315.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print('RUN315_FROZEN_FAILURE',json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
