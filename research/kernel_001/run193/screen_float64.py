"""Exploratory float64 screening only; NOT a proof or prospective evaluation."""
import json,numpy as np
from pathlib import Path
R=Path(__file__).resolve().parent
p=[]
for epoch in (300,600):
 path=R.parent/("run192/seed163_epoch600_params.json" if epoch==600 else "run191/seed163_epoch300_params.json")
 p.append({k:np.asarray(v,dtype=np.float64) for k,v in json.loads(path.read_text()).items()})
h=[np.zeros((1,8)),np.zeros((1,8))]
for d in range(1,18):
 for i in range(2):
  q=p[i]
  a=np.repeat(h[i]@q["W"].T+q["b"],2,axis=0)
  a[::2]+=q["U"][0];a[1::2]+=q["U"][1]
  h[i]=np.tanh(a)
 y=[h[i]@p[i]["v"]+p[i]["c"] for i in range(2)]
 idx=np.flatnonzero(np.signbit(y[0])!=np.signbit(y[1]))
 print(d,len(idx),[format(int(j),f"0{d}b") for j in idx[:10]])
