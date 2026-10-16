"""Outward interval proof for trained Run 210 seed 773."""
import json
from pathlib import Path
from mpmath import iv
p=json.loads((Path(__file__).resolve().parent.parent/"run210/checkpoints/seed_773.json").read_text())["params"]
iv.dps=90
def ex(x):
 n,d=float(x).as_integer_ratio()
 return iv.mpf(n)/iv.mpf(d)
def th(x):
 def f(y):
  e=iv.exp(2*y)
  return (e-1)/(e+1)
 a,b=f(x.a),f(x.b)
 return iv.mpf([a.a,b.b])
W=[[[ex(x) for x in r] for r in M] for M in p["W"]]
B=[[ex(x) for x in r] for r in p["b"]]
h=[ex(.5),ex(-.5)]
q=0
for t in map(int,"010011001100100"):
 q=0 if t==2 else q^(t==1)
 h=[th(sum(W[t][j][k]*h[k] for k in range(2))+B[t][j]) for j in range(2)]
z=sum(ex(p["v"][j])*h[j] for j in range(2))+ex(p["c"])
assert q==0 and z.a>0
print("PASS: trained-model misclassification",z)
