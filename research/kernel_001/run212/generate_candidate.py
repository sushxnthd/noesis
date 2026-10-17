"""Untrusted numerical candidate generator. Final soundness comes from independent interval checkers."""
import numpy as np,json,itertools
from pathlib import Path
from scipy.optimize import linprog
R=Path(__file__).resolve().parent
p=json.loads((R.parent/"run210/checkpoints/seed_787.json").read_text())["params"]
W=np.array(p["W"]);b=np.array(p["b"]);v=np.array(p["v"]);c=p["c"]
def step(lo,hi,t):
 w=W[t]
 return np.tanh(np.maximum(w,0)@lo+np.minimum(w,0)@hi+b[t]),np.tanh(np.maximum(w,0)@hi+np.minimum(w,0)@lo+b[t])
m=1
boxes={}
for word in itertools.product(range(3),repeat=m):
 q=0;h=np.array([.5,-.5])
 for t in word:
  q=0 if t==2 else q^(t==1);h=np.tanh(W[t]@h+b[t])
 boxes[(q,word)]=(h,h)
for L in range(m+1,121):
 nxt={}
 for (q,s),(lo,hi) in boxes.items():
  for t in range(3):
   qn=0 if t==2 else q^(t==1);k=(qn,s[1:]+(t,));a,z=step(lo,hi,t)
   if k in nxt:
    oldlo,oldhi=nxt[k];nxt[k]=(np.minimum(oldlo,a),np.maximum(oldhi,z))
   else:nxt[k]=(a,z)
 boxes=nxt
keys=sorted(boxes);ix={k:i for i,k in enumerate(keys)};rows=[];rhs=[]
for key,(lo,hi) in boxes.items():
 q,s=key
 for t in range(3):
  qn=0 if t==2 else q^(t==1);dest=(qn,s[1:]+(t,));dl,du=boxes[dest];a,z=step(lo,hi,t)
  za=np.maximum(W[t],0)@lo+np.minimum(W[t],0)@hi+b[t]
  zb=np.maximum(W[t],0)@hi+np.minimum(W[t],0)@lo+b[t]
  closest=np.where(za>0,za,np.where(zb<0,zb,0))
  Lmat=(1-np.tanh(closest)**2)[:,None]*abs(W[t])
  for j in range(2):
   row=np.zeros(2*len(keys));row[2*ix[key]:2*ix[key]+2]=Lmat[j];row[2*ix[dest]+j]-=1
   rows.append(row);rhs.append(-max(dl[j]-a[j],z[j]-du[j],0)-1e-8)
res=linprog(np.ones(2*len(keys)),A_ub=np.array(rows),b_ub=np.array(rhs)*1e6,bounds=[(1,1e5)]*(2*len(keys)),method="highs")
assert res.success,res.message
e=res.x*1e-6
out={}
for i,(q,s) in enumerate(keys):
 lo,hi=boxes[(q,s)]
 out[f"{q}:{s[0]}"]={"lo":[format(float(lo[j]-e[2*i+j]-1e-10),".17g") for j in range(2)],"hi":[format(float(hi[j]+e[2*i+j]+1e-10),".17g") for j in range(2)]}
candidate={"seed":787,"epoch":800,"base_depth":120,"boxes":out}
(R/"CANDIDATE_REGENERATED.json").write_text(json.dumps(candidate,indent=2)+"\n")
print("Untrusted candidate regenerated; run both proof checkers before any claim.")
