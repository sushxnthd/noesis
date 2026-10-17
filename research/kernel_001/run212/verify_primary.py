"""Run 212: independently check five-cell task/last-symbol invariant with mpmath.iv."""
import json
from pathlib import Path
from mpmath import iv
R=Path(__file__).resolve().parent
iv.dps=90
p=json.loads((R.parent/"run210/checkpoints/seed_787.json").read_text())["params"]
cert=json.loads((R/"CANDIDATE.json").read_text())
def ex(x):
 n,d=float(x).as_integer_ratio()
 return iv.mpf(n)/iv.mpf(d)
def tanh(z):
 def f(y):
  e=iv.exp(2*y);return (e-1)/(e+1)
 return iv.mpf([f(z.a).a,f(z.b).b])
W=[[[ex(x) for x in row] for row in M] for M in p["W"]]
b=[[ex(x) for x in row] for row in p["b"]]
v=[ex(x) for x in p["v"]];c=ex(p["c"])
def step(box,t):
 return [tanh(sum(W[t][j][k]*box[k] for k in range(2))+b[t][j]) for j in range(2)]
def advance(B):
 out={}
 for (q,last),box in B.items():
  for t in range(3):
   dest=(0 if t==2 else q^(t==1),t)
   z=step(box,t)
   if dest in out:
    out[dest]=[iv.mpf([min(z[j].a,out[dest][j].a),max(z[j].b,out[dest][j].b)]) for j in range(2)]
   else:out[dest]=z
 return out
def margin(key,box):
 z=sum(v[j]*box[j] for j in range(2))+c
 return float((-z.b).a if key[0]==0 else z.a)
B={(int(t==1),t):step([ex(.5),ex(-.5)],t) for t in range(3)}
min_prefix=1e100
for n in range(1,cert["base_depth"]+1):
 for k,box in B.items():
  m=margin(k,box)
  assert m>0,("prefix",n,k,m)
  min_prefix=min(min_prefix,m)
 if n<cert["base_depth"]:B=advance(B)
I={tuple(map(int,k.split(":"))):[iv.mpf([val["lo"][j],val["hi"][j]]) for j in range(2)] for k,val in cert["boxes"].items()}
assert set(B)==set(I)
min_base=1e100;min_closure=1e100;min_output=1e100
for k,box in B.items():
 for j in range(2):
  a=float((box[j].a-I[k][j].a).a);z=float((I[k][j].b-box[j].b).a)
  assert a>0 and z>0,("base",k,j,a,z)
  min_base=min(min_base,a,z)
for k,box in I.items():
 m=margin(k,box);assert m>0,("output",k,m)
 min_output=min(min_output,m)
 for t in range(3):
  dest=(0 if t==2 else k[0]^(t==1),t);z=step(box,t)
  for j in range(2):
   a=float((z[j].a-I[dest][j].a).a);h=float((I[dest][j].b-z[j].b).a)
   assert a>0 and h>0,("closure",k,t,j,a,h)
   min_closure=min(min_closure,a,h)
print(json.dumps({"status":"CERTIFIED","seed":787,"epoch":800,"checker":"mpmath.iv","prefix_depth":cert["base_depth"],"cells":len(I),"edges":len(I)*3,"min_prefix_margin":min_prefix,"min_base_slack":min_base,"min_closure_slack":min_closure,"min_output_margin":min_output},indent=2))
