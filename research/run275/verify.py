"""Exact rational verification of four naturally acquired algorithms, with all-future negative family proof."""
import json
from pathlib import Path
from fractions import Fraction as F
def q(x): return F.from_float(float(x))
def unpack(p): return list(map(q,p["a"])),list(map(q,p["b"])),q(p["v"]),q(p["c"])
def positive(p):
 a,b,v,c=unpack(p);L=max(F(0),b[2]);U=b[1]
 return all((v>0,U>L,v*L+c<0,v*U+c>0,a[0]>=0,a[0]*L+b[0]<=L,
             a[0]*U+b[0]>=U,a[1]>=0,b[1]>=U,a[2]<=0,b[2]<=L))
def negative(p,sym,n):
 a,b,v,c=unpack(p);h=max(F(0),b[sym]);target=(sym==1)
 for i in range(n+1):
  assert ((v*h+c>0)==target)==(i<n),(i,n)
  if i<n:h=max(F(0),a[0]*h+b[0])
 # Show wrong persists under all future HOLD steps, not just at this n.
 if sym==2:
  assert b[0]>0 and a[0]>0 and a[0]*h+b[0]>h and v>0
 else:
  assert 0<a[0]<1 and b[0]<0 and a[0]*h+b[0]<h and v>0
 return True
if __name__=="__main__":
 rows=json.loads((Path(__file__).parent/"four_pairs.json").read_text())
 for r in rows:
  assert not positive(r["early_params"])
  assert negative(r["early_params"],1 if r["family"]=="SET" else 2,r["n"])
  assert positive(r["late_params"])
  print(r["seed"],"earlier",r["earlier_epoch"],"exact false after",r["n"],"HOLDs; later",r["later_epoch"],"certified")
 assert len(rows)==4
 print("PASS 4/4 exact acquisition pairs")
