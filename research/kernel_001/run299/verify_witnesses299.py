from pathlib import Path
from fractions import Fraction as F
import json
d=json.loads((Path(__file__).parent/"certified_weights299.json").read_text())
cert={"21832":("9/4","21/16","7/5"),"21903":("1","9/5","1/2"),"21926":("5/4","3/2","6/5")}
for seed,(t,m0,m1) in cert.items():
 p=list(map(F.from_float,d[seed]));v=p[24:27];c=p[27];T=F(t);mu=[F(m0),F(m1)]
 assert all(x>=0 for x in v) and any(v) and all(p[18+i]<=0 for i in range(3)) and c<0
 assert T+c>0 and sum(v[i]*max(F(0),p[21+i]) for i in range(3))>=T
 for x in (0,1):
  assert mu[x]>=0
  assert all(sum(v[i]*p[9*x+3*i+j] for i in range(3))>=mu[x]*v[j] for j in range(3))
  assert mu[x]*T+sum(v[i]*p[18+3*x+i] for i in range(3))>=T
 print("EXACT_CERTIFIED",seed)
