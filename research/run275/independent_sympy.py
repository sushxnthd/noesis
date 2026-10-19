"""Independent SymPy implementation, does not import primary verifier."""
import json
from pathlib import Path
from sympy import Rational
def q(x):
 n,d=float(x).as_integer_ratio()
 return Rational(n,d)
for r in json.loads((Path(__file__).parent/"four_pairs.json").read_text()):
 p=r["early_params"];a=[q(x) for x in p["a"]];b=[q(x) for x in p["b"]];v=q(p["v"]);c=q(p["c"])
 sym=1 if r["family"]=="SET" else 2
 h=max(0,b[sym]);want=(sym==1)
 for i in range(r["n"]+1):
  assert ((v*h+c>0)==want)==(i<r["n"])
  if i<r["n"]:h=max(0,a[0]*h+b[0])
 if sym==2: assert b[0]>0 and a[0]>0 and a[0]*h+b[0]>h
 else: assert 0<a[0]<1 and b[0]<0 and a[0]*h+b[0]<h
 p=r["late_params"];a=[q(x) for x in p["a"]];b=[q(x) for x in p["b"]];v=q(p["v"]);c=q(p["c"])
 L=max(0,b[2]);U=b[1]
 assert v>0 and U>L and v*L+c<0 and v*U+c>0
 assert a[0]>=0 and a[0]*L+b[0]<=L and a[0]*U+b[0]>=U
 assert a[1]>=0 and b[1]>=U and a[2]<=0 and b[2]<=L
 print(r["seed"],"independent exact verification PASSED")
print("PASS 4/4 independent SymPy pairs")
