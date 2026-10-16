"""Independent directed-Decimal proof; no mpmath, numpy, or float propagation."""
import json
from pathlib import Path
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
p=json.loads((Path(__file__).resolve().parent.parent/"run210/checkpoints/seed_773.json").read_text())["params"]
N=90;F=Context(prec=N,rounding=ROUND_FLOOR);C=Context(prec=N,rounding=ROUND_CEILING)
class I:
 def __init__(self,a,b=None):
  self.a=D(a);self.b=D(b) if b is not None else self.a
  assert self.a<=self.b
 def __add__(self,y):
  y=I(y) if not isinstance(y,I) else y
  return I(F.add(self.a,y.a),C.add(self.b,y.b))
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,y):return self+-y
 def __mul__(self,y):
  y=I(y) if not isinstance(y,I) else y
  return I(min(F.multiply(a,b) for a in (self.a,self.b) for b in (y.a,y.b)),max(C.multiply(a,b) for a in (self.a,self.b) for b in (y.a,y.b)))
 __rmul__=__mul__
 def __truediv__(self,y):
  y=I(y) if not isinstance(y,I) else y
  assert y.a>0
  return I(min(F.divide(a,b) for a in (self.a,self.b) for b in (y.a,y.b)),max(C.divide(a,b) for a in (self.a,self.b) for b in (y.a,y.b)))
def ex(x):
 n,d=float(x).as_integer_ratio()
 return I(F.divide(D(n),D(d)),C.divide(D(n),D(d)))
def exp_pt(x):
 with localcontext(Context(prec=N)):
  z=x.exp()
 eps=D(2).scaleb(z.adjusted()-N+1)
 return I(F.subtract(z,eps),C.add(z,eps))
def th(x):
 lo=F.multiply(D(2),x.a);hi=C.multiply(D(2),x.b)
 def f(z):
  e=exp_pt(z)
  return (e-I(1))/(e+I(1))
 a,b=f(lo),f(hi)
 return I(a.a,b.b)
W=[[[ex(x) for x in r] for r in M] for M in p["W"]]
B=[[ex(x) for x in r] for r in p["b"]]
h=[ex(.5),ex(-.5)]
q=0
for t in map(int,"010011001100100"):
 q=0 if t==2 else q^(t==1)
 h=[th(sum((W[t][j][k]*h[k] for k in range(2)),I(0))+B[t][j]) for j in range(2)]
z=sum((ex(p["v"][j])*h[j] for j in range(2)),ex(p["c"]))
assert q==0 and z.a>0
print("PASS: independent directed-Decimal trained-model counterexample",z.a,z.b)
