#!/usr/bin/env python3
"""Run346 exact trained-network three-word readout-impossibility certificate."""
import json
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
m=json.loads((P/"model_epoch200.json").read_text())
assert m["seed"]==31002 and m["epoch"]==200
p=[Q.from_float(float(x)) for x in m["p"]]
assert len(p)==45
A=[[[p[16*x+4*i+j] for j in range(4)] for i in range(4)] for x in (0,1)]
b=[p[32+4*x:36+4*x] for x in (0,1)]
def state(w):
 h=(Q(0),)*4
 for c in w:
  x=int(c)
  h=tuple(max(Q(0),sum((A[x][i][j]*h[j] for j in range(4)),b[x][i])) for i in range(4))
 return h
W=["10","1"+"0"*41,"1"+"0"*38+"1"+"0"*5]
assert [w.count("1")%2 for w in W]==[1,1,0]
u,v,q=[state(w) for w in W]
j=next(j for j in range(4) if u[j]!=v[j])
a=(q[j]-v[j])/(u[j]-v[j])
assert 0<a<1
assert all(q[k]==a*u[k]+(1-a)*v[k] for k in range(4))
# A convex combination of positive odd states equals an even state.
# Therefore no affine readout can strictly separate these three words.
w="1"+"0"*37
h=state(w);z=sum((p[40+i]*h[i] for i in range(4)),p[44])
assert z<0 and w.count("1")%2==1
for k in range(37):
 h=state("1"+"0"*k)
 assert sum((p[40+i]*h[i] for i in range(4)),p[44])>0
print("PASS exact 3-state collision; alpha",float(a),"first W1 failure length",len(w))
