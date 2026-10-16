"""Numerical exhaustive check of all 7,174,453 words through length 14.

IMPORTANT: Float64 enumeration does NOT prove global shortest counterexample.
"""
import json, numpy as np
from pathlib import Path
P=Path(__file__).resolve().parent
p=json.loads((P.parent/"run210/checkpoints/seed_773.json").read_text())["params"]
W=np.array(p["W"]);b=np.array(p["b"]);v=np.array(p["v"]);c=p["c"]
H=np.array([[.5,-.5]],dtype=np.float64)
Q=np.array([0],dtype=np.int8)
rows=[]
for n in range(1,15):
 children=[];labels=[]
 for t in range(3):
  children.append(np.tanh(H@W[t].T+b[t]))
  labels.append(np.zeros(len(Q),dtype=np.int8) if t==2 else Q^(t==1))
 H=np.concatenate(children);Q=np.concatenate(labels)
 z=H@v+c
 margins=np.where(Q==0,-z,z)
 row={"length":n,"words":len(Q),"min_float64_margin":float(margins.min()),"num_float64_errors":int(np.sum(margins<=0))}
 rows.append(row)
 print(row,flush=True)
 assert row["num_float64_errors"]==0, "earlier numerical counterexample found"
(P/"EXHAUSTIVE_FLOAT64.json").write_text(json.dumps({"scope":"numerical only, not rigorous minimality","rows":rows},indent=2)+"\n")
