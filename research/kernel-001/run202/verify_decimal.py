#!/usr/bin/env python3
"""Independent directed-Decimal checker for NOESIS Run202."""
import json,sys,hashlib
from pathlib import Path
from decimal import Decimal as D
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"run201"))
import independent_decimal as d
SOURCE_HASH="5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32"
def check(row,c):
 n,p=c["N"],c["P"];target=c["eventual_class"];radius=D(c["radius"])
 w=d.params(row);centers=[[d.I(D(v)) for v in x] for x in c["centers"]]
 h=[d.I(0)]*12;classes=[]
 for _ in range(n):
  h=d.step(h,w,0);cls,gap=d.classify(h,w);assert cls is not None;classes.append(cls)
 assert classes[-1]==target
 assert [i+1 for i in range(1,n) if classes[i]!=classes[i-1]]==c["finite_change_lengths"]
 assert max((h[i]-centers[0][i]).absup() for i in range(12))<radius
 A=[[d.I(int(i==j)) for j in range(12)] for i in range(12)];E=[D(0)]*12
 for t in range(p):
  delta=[d.upadd(d.upsum(d.upmul(A[i][j].absup(),radius) for j in range(12)),E[i]) for i in range(12)]
  box=[centers[t][i]+d.I(-delta[i],delta[i]) for i in range(12)]
  cls,gap=d.classify(box,w);assert cls==target
  f=d.step(centers[t],w,0)
  J=[[(d.I(1)-f[i]*f[i])*w["W"][i][j] for j in range(12)] for i in range(12)]
  beta=[(f[i]-centers[t+1][i]).absup() for i in range(12)]
  rem=[]
  for i in range(12):
   v=d.upsum(d.upmul(w["W"][i][j].absup(),delta[j]) for j in range(12));rem.append(d.upmul(v,v))
  E=[d.upadd(d.upadd(d.upsum(d.upmul(J[i][j].absup(),E[j]) for j in range(12)),rem[i]),beta[i]) for i in range(12)]
  A=[[sum((J[i][k]*A[k][j] for k in range(12)),d.I(0)) for j in range(12)] for i in range(12)]
 final=[d.upadd(d.upadd((centers[p][i]-centers[0][i]).absup(),d.upsum(d.upmul(A[i][j].absup(),radius) for j in range(12))),E[i]) for i in range(12)]
 assert max(final)<radius
 return {"seed":row["seed"],"epoch":row["epoch"],"class":target,"status":"PASS","radius_upper":str(max(final))}
def main(source,proof,out):
 raw=Path(source).read_bytes();assert hashlib.sha256(raw).hexdigest()==SOURCE_HASH
 rows={(x["seed"],x["epoch"]):x for x in json.loads(raw)["rows"]}
 items=json.loads(Path(proof).read_text())["results"];results=[]
 for x in items:
  if x["certificate"] is None:continue
  y=check(rows[x["seed"],x["epoch"]],x["certificate"]);results.append(y)
  print("INDEPENDENT PASS",y["seed"],y["epoch"],flush=True)
 assert len(results)==5
 Path(out).write_text(json.dumps(results,indent=2)+"\n")
if __name__=="__main__":
 assert len(sys.argv)==4
 main(*sys.argv[1:])
