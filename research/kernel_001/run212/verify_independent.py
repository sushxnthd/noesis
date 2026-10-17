"""Run 212 independent directed-Decimal checker: no mpmath or numpy."""
import json
from pathlib import Path
from decimal import Decimal as D,Context,ROUND_FLOOR,ROUND_CEILING,localcontext
R=Path(__file__).resolve().parent
p=json.loads((R.parent/"run210/checkpoints/seed_787.json").read_text())["params"]
cert=json.loads((R/"CANDIDATE.json").read_text())
P=90;F=Context(prec=P,rounding=ROUND_FLOOR);C=Context(prec=P,rounding=ROUND_CEILING)
class I:
 def __init__(self,a,b=None):
  self.a=D(a);self.b=D(b) if b is not None else self.a
  assert self.a<=self.b
 def __add__(self,o):
  o=o if isinstance(o,I) else I(o)
  return I(F.add(self.a,o.a),C.add(self.b,o.b))
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,o):return self+-o
 def __mul__(self,o):
  o=o if isinstance(o,I) else I(o)
  return I(min(F.multiply(a,b) for a in (self.a,self.b) for b in (o.a,o.b)),max(C.multiply(a,b) for a in (self.a,self.b) for b in (o.a,o.b)))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=o if isinstance(o,I) else I(o)
  assert o.a>0
  return I(min(F.divide(a,b) for a in (self.a,self.b) for b in (o.a,o.b)),max(C.divide(a,b) for a in (self.a,self.b) for b in (o.a,o.b)))
def ex(x):
 n,d=float(x).as_integer_ratio()
 return I(F.divide(D(n),D(d)),C.divide(D(n),D(d)))
def exp_pt(x):
 with localcontext(Context(prec=P)):
  z=x.exp()
 eps=D(2).scaleb(z.adjusted()-P+1)
 return I(F.subtract(z,eps),C.add(z,eps))
def tanh(z):
 def f(x):
  e=exp_pt(x);return (e-I(1))/(e+I(1))
 lo=f(F.multiply(D(2),z.a));hi=f(C.multiply(D(2),z.b))
 return I(lo.a,hi.b)
W=[[[ex(x) for x in row] for row in M] for M in p["W"]]
b=[[ex(x) for x in row] for row in p["b"]]
v=[ex(x) for x in p["v"]];c=ex(p["c"])
def step(box,t):
 return [tanh(sum((W[t][j][k]*box[k] for k in range(2)),I(0))+b[t][j]) for j in range(2)]
def advance(B):
 out={}
 for (q,last),box in B.items():
  for t in range(3):
   dest=(0 if t==2 else q^(t==1),t);z=step(box,t)
   if dest in out:
    out[dest]=[I(min(z[j].a,out[dest][j].a),max(z[j].b,out[dest][j].b)) for j in range(2)]
   else:out[dest]=z
 return out
def margin(key,box):
 z=sum((v[j]*box[j] for j in range(2)),c)
 return -z.b if key[0]==0 else z.a
B={(int(t==1),t):step([I(".5"),I("-.5")],t) for t in range(3)}
min_prefix=D("Infinity")
for n in range(1,cert["base_depth"]+1):
 for k,box in B.items():
  m=margin(k,box)
  assert m>0,("prefix",n,k,m)
  min_prefix=min(min_prefix,m)
 if n<cert["base_depth"]:B=advance(B)
J={tuple(map(int,k.split(":"))):[I(val["lo"][j],val["hi"][j]) for j in range(2)] for k,val in cert["boxes"].items()}
assert set(B)==set(J)
min_base=D("Infinity");min_closure=D("Infinity");min_output=D("Infinity")
for k,box in B.items():
 for j in range(2):
  a=box[j].a-J[k][j].a;z=J[k][j].b-box[j].b
  assert a>0 and z>0,("base",k,j,a,z)
  min_base=min(min_base,a,z)
for k,box in J.items():
 m=margin(k,box);assert m>0,("output",k,m)
 min_output=min(min_output,m)
 for t in range(3):
  dest=(0 if t==2 else k[0]^(t==1),t);z=step(box,t)
  for j in range(2):
   a=z[j].a-J[dest][j].a;h=J[dest][j].b-z[j].b
   assert a>0 and h>0,("closure",k,t,j,a,h)
   min_closure=min(min_closure,a,h)
print(json.dumps({"status":"CERTIFIED","seed":787,"epoch":800,"checker":"directed Decimal","prefix_depth":cert["base_depth"],"cells":len(J),"edges":len(J)*3,"min_prefix_margin":str(min_prefix),"min_base_slack":str(min_base),"min_closure_slack":str(min_closure),"min_output_margin":str(min_output)},indent=2))
