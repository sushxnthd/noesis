"""Run 212 frozen width-2048 deterministic numerical beam; failure to find an error is not proof."""
import json,numpy as np
from pathlib import Path
R=Path(__file__).resolve().parent
p=json.loads((R.parent/"run210/checkpoints/seed_787.json").read_text())["params"]
W=np.array(p["W"]);b=np.array(p["b"]);v=np.array(p["v"]);c=p["c"]
K=2048;MAX_DEPTH=256
beam={0:(np.array([[.5,-.5]]),[b""])}
for n in range(1,MAX_DEPTH+1):
 candidates={0:([],[]),1:([],[])}
 for q,(H,words) in beam.items():
  for t in range(3):
   dest=0 if t==2 else q^(t==1)
   candidates[dest][0].append(np.tanh(H@W[t].T+b[t]))
   candidates[dest][1].extend([w+bytes([t]) for w in words])
 beam={}
 for q in (0,1):
  H=np.concatenate(candidates[q][0]);words=candidates[q][1]
  wrong=(1 if q==0 else -1)*(H@v+c)
  if np.max(wrong)>=0:
   j=int(np.argmax(wrong))
   print(json.dumps({"status":"NUMERIC_WITNESS","length":n,"word":"".join(map(str,words[j])),"logit":float(H[j]@v+c),"true_state":q}))
   raise SystemExit(0)
  priority=np.argsort(-wrong,kind="stable")
  bins=np.clip(((H+1)*48).astype(np.int64),0,95)
  ids=bins[:,0]*96+bins[:,1]
  _,ix=np.unique(ids[priority],return_index=True)
  selected=list(dict.fromkeys(np.concatenate((priority[:K//2],priority[ix])).tolist()))[:K]
  seen=set(selected)
  for j in priority:
   if len(selected)>=K:break
   if int(j) not in seen:selected.append(int(j));seen.add(int(j))
  beam[q]=(H[selected],[words[i] for i in selected])
print(json.dumps({"status":"NO_COUNTEREXAMPLE_IN_BEAM","depth":MAX_DEPTH,"width":K,"scope":"numerical only, no correctness inference"}))
