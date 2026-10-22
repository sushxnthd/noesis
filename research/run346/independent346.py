#!/usr/bin/env python3
"""Independent SymPy reimplementation of the original checkpoint proof."""
import json
from pathlib import Path
import sympy as s
p=[s.Rational(float(x)) for x in json.loads((Path(__file__).parent/"model_epoch200.json").read_text())["p"]]
A=[[[p[16*x+4*i+j] for j in range(4)] for i in range(4)] for x in (0,1)]
b=[p[32+4*x:36+4*x] for x in (0,1)]
def state(w):
 h=[s.Integer(0)]*4
 for c in w:
  x=int(c)
  h=[max(s.Integer(0),sum((A[x][i][j]*h[j] for j in range(4)),b[x][i])) for i in range(4)]
 return h
u,v,q=[state(w) for w in ["10","1"+"0"*41,"1"+"0"*38+"1"+"0"*5]]
j=next(j for j in range(4) if u[j]!=v[j])
a=s.cancel((q[j]-v[j])/(u[j]-v[j]))
assert 0<a<1 and all(s.cancel(q[k]-a*u[k]-(1-a)*v[k])==0 for k in range(4))
print("PASS independent SymPy exact collision",float(a))
