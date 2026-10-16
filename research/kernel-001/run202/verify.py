#!/usr/bin/env python3
"""NOESIS Run202: frozen, proof-producing heldout zero-tail transfer."""
import sys,json,hashlib,traceback
from pathlib import Path
import numpy as np
from mpmath import iv,mp
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"run200"))
import prove as b
SHA="5f2ea6c259cf07ae4cd1915cad3aea3ce85c20723401b33ef4e1197a67384c32"
CONFIGS=((240,14),(260,16))
R=iv.mpf("1e-9")
def numerical(row):
 p={k:np.asarray(v,dtype=np.float64) for k,v in row["params"].items()}
 h=np.zeros(12); states=[h.copy()]; labels=[];margins=[]
 for _ in range(320):
  h=np.tanh(p["W"]@h+p["U"][0]+p["b"]);states.append(h.copy())
  z=p["V"]@h+p["c"];i=int(np.argmax(z));labels.append(i)
  margins.append(float(z[i]-np.partition(z,-2)[-2]))
 delta=float(np.max(np.abs(states[320]-states[306])))
 return {"class320":labels[-1],"stable_last64":len(set(labels[-64:]))==1,
         "delta320_306":delta,"min_margin_last64":min(margins[-64:]),
         "candidate":len(set(labels[-64:]))==1 and delta<1e-7 and min(margins[-64:])>0.1}
def cls(h,p):
 z=b.z(h,p);g=[min((z[i]-z[j]).a for j in range(3) if j!=i) for i in range(3)]
 w=[i for i in range(3) if g[i]>0]
 if len(w)!=1:raise AssertionError("interval output undecidable")
 return w[0],str(g[w[0]].a)
def cert(row,N,P,expected):
 b.N=N;b.P=P
 p=b.pars(row);h=[iv.mpf(0)]*12; finite=[]
 for n in range(1,N+1):
  h=b.F(h,p);pred,_=cls(h,p);finite.append(pred)
 assert finite[-1]==expected
 centers=b.center(row);c=[[iv.mpf(v) for v in x] for x in centers]
 assert max(b.up(h[i]-c[0][i]) for i in range(12))<R.a
 A=[[iv.mpf(int(i==j)) for j in range(12)] for i in range(12)]
 E=[iv.mpf(0)]*12;minphase=None
 for t in range(P):
  d=[sum(b.up(A[i][j])*R for j in range(12))+E[i] for i in range(12)]
  box=[c[t][i]+iv.mpf([-1,1])*d[i].b for i in range(12)]
  pred,gap=cls(box,p)
  assert pred==expected,("phase mismatch",t,pred)
  minphase=gap if minphase is None else min(minphase,gap)
  f=b.F(c[t],p)
  J=[[(1-f[i]*f[i])*p["W"][i][j] for j in range(12)] for i in range(12)]
  beta=[b.up(f[i]-c[t+1][i]) for i in range(12)]
  rem=[sum(b.up(p["W"][i][j])*d[j] for j in range(12))**2 for i in range(12)]
  E=[sum(b.up(J[i][j])*E[j] for j in range(12))+rem[i]+beta[i] for i in range(12)]
  A=[[sum(J[i][k]*A[k][j] for k in range(12)) for j in range(12)] for i in range(12)]
 bound=max(b.up(c[P][i]-c[0][i])+sum(b.up(A[i][j])*R for j in range(12))+E[i] for i in range(12))
 assert bound<R.a,("closure",str(bound))
 changes=[n+1 for n in range(1,N) if finite[n]!=finite[n-1]]
 return {"N":N,"P":P,"radius":"1e-9","eventual_class":expected,
         "finite_change_lengths":changes,"finite_counts":{str(i):finite.count(i) for i in range(3)},
         "image_radius_upper":str(bound.b),"centers":centers,"status":"PASS"}
def main(source,out):
 raw=Path(source).read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
 rows=json.loads(raw)["rows"];results=[]
 for seed in (293,307,311):
  for epoch in (400,800):
   row=next(x for x in rows if x["seed"]==seed and x["epoch"]==epoch)
   gate=numerical(row);item={"seed":seed,"epoch":epoch,"gate":gate,"attempts":[],"certificate":None}
   if gate["candidate"]:
    for N,P in CONFIGS:
     try:
      proof=cert(row,N,P,gate["class320"]);item["certificate"]=proof
      item["attempts"].append({"N":N,"P":P,"status":"PASS"});break
     except Exception as e:
      item["attempts"].append({"N":N,"P":P,"status":"ABSTAIN","error":repr(e),"traceback":traceback.format_exc()})
   else:item["attempts"].append({"status":"ABSTAIN","reason":"frozen gate"})
   print(seed,epoch,"CERTIFIED" if item["certificate"] else "ABSTAIN",flush=True)
   results.append(item)
 Path(out).write_text(json.dumps({"source_sha256":SHA,"results":results},indent=2)+"\n")
if __name__=="__main__":
 assert len(sys.argv)==3
 main(*sys.argv[1:])
