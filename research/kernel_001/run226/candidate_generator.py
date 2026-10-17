"""Untrusted interval-box candidate generator, preserving NO_CLOSED failures."""
import json,numpy as np
from pathlib import Path
R=Path(__file__).resolve().parent
row=next(r for r in json.loads((R/'CHECKPOINTS.json').read_text())['rows'] if r['epoch']==100)
def step(lo,hi,W,b,t,eps):
 A=W[t]-eps;B=W[t]+eps
 vals=np.stack((A*lo,A*hi,B*lo,B*hi))
 lower=np.min(vals,axis=0).sum(axis=1)+b[t]-eps
 upper=np.max(vals,axis=0).sum(axis=1)+b[t]+eps
 return np.nextafter(np.tanh(lower),-np.inf),np.nextafter(np.tanh(upper),np.inf)
def candidate(row,k,eps,maxiter=600):
 p=row['params'];W=np.array(p['W']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
 init=np.array([.5,-.5,.25]);boxes={}
 def target(word):
  q=0
  for t in word:q=0 if t==2 else q^(t==1)
  return q
 for n in range(3**k):
  word=tuple((n//3**(k-1-j))%3 for j in range(k))
  lo=hi=init.copy()
  for t in word:lo,hi=step(lo,hi,W,b,t,eps)
  boxes[(target(word),word)]=(lo,hi)
 for iteration in range(maxiter):
  nxt={key:(lo.copy(),hi.copy()) for key,(lo,hi) in boxes.items()}
  for (q,word),(lo,hi) in boxes.items():
   for t in range(3):
    qq=0 if t==2 else q^(t==1);dest=(qq,word[1:]+(t,))
    a,z=step(lo,hi,W,b,t,eps)
    if dest in nxt:
     l,h=nxt[dest];nxt[dest]=(np.minimum(l,a),np.maximum(h,z))
    else:nxt[dest]=(a,z)
  diff=max(max(float(np.max(np.abs(nxt[key][j]-boxes[key][j]))) for j in (0,1)) for key in boxes)
  boxes=nxt
  if any(np.max(hi-lo)>2.01 for lo,hi in boxes.values()):return dict(status='DIVERGED',iteration=iteration)
  if diff<1e-12:break
 else:return dict(status='NO_CONVERGENCE')
 gap=None;minmargin=float('nan')
 for pad in (1e-11,1e-10,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3):
  inv={key:(np.maximum(-1,lo-pad),np.minimum(1,hi+pad)) for key,(lo,hi) in boxes.items()}
  minmargin=1e9
  for (q,word),(lo,hi) in inv.items():
   vals=np.stack(((v-eps)*lo,(v-eps)*hi,(v+eps)*lo,(v+eps)*hi))
   zlo=np.min(vals,axis=0).sum()+c-eps
   zhi=np.max(vals,axis=0).sum()+c+eps
   minmargin=min(minmargin,zlo if q else -zhi)
  if minmargin<=0:continue
  gap=0
  for (q,word),(lo,hi) in inv.items():
   for t in range(3):
    dest=(0 if t==2 else q^(t==1),word[1:]+(t,))
    a,z=step(lo,hi,W,b,t,eps);l,h=inv[dest]
    gap=max(gap,float(np.max(l-a)),float(np.max(z-h)))
  if gap<=0:return dict(status='CANDIDATE',k=k,eps=eps,pad=pad,iterations=iteration+1,margin=minmargin,boxes={str(q)+':'+''.join(map(str,word)):{'lo':[format(x,'.17g') for x in lo],'hi':[format(x,'.17g') for x in hi]} for (q,word),(lo,hi) in inv.items()})
 return dict(status='NO_CLOSED',iteration=iteration+1,margin=minmargin,gap=gap)
if __name__=='__main__':
 for k in (4,5):
  for eps in (0.,0.003):
   r=candidate(row,k,eps)
   print(k,eps,r['status'],r.get('gap'),flush=True)
