#!/usr/bin/env python3
"""Full exact audit: regenerate research/run342/trajectories342.json first."""
import hashlib,json
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
src=P.parent/"run342/trajectories342.json"
assert hashlib.sha256(src.read_bytes()).hexdigest()=="c20f44b3bd56893880974c638b6202ad75a5ea253b64f72eeaa094e8d973112e"
rows={r["epoch"]:r["p"] for r in json.loads(src.read_text())["rows"] if r["seed"]==31002}
assert len(rows)==201
W=["10","1"+"0"*41,"1"+"0"*38+"1"+"0"*5]
def network(p):
 p=[Q.from_float(float(x)) for x in p]
 A=[[[p[16*x+4*i+j] for j in range(4)] for i in range(4)] for x in (0,1)]
 b=[p[32+4*x:36+4*x] for x in (0,1)]
 def step(h,x):return tuple(max(Q(0),sum((A[x][i][j]*h[j] for j in range(4)),b[x][i])) for i in range(4))
 def logit(h):return sum((p[40+i]*h[i] for i in range(4)),p[44])
 return step,logit
for epoch in range(5,201):
 step,_=network(rows[epoch]);H=[]
 for w in W:
  h=(Q(0),)*4
  for c in w:h=step(h,int(c))
  H.append(h)
 u,v,q=H
 coords=[j for j in range(4) if u[j]!=v[j]]
 if coords:
  j=coords[0];a=(q[j]-v[j])/(u[j]-v[j])
  assert 0<=a<=1 and all(q[k]==a*u[k]+(1-a)*v[k] for k in range(4)),epoch
 else:assert q==v,epoch
print("PASS 196 exact convex-hull obstructions")
count=0
for epoch in range(91,201):
 step,logit=network(rows[epoch]);states=[((Q(0),)*4,0)]
 for length in range(1,13):
  nxt=[]
  for h,y in states:
   for x in (0,1):
    z=step(h,x);label=y^x
    assert (logit(z)>0)==bool(label),(epoch,length)
    nxt.append((z,label));count+=1
  states=nxt
assert count==900900
print("PASS",count,"exact bounded classifications")
