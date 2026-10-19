"""Run266 frozen complete-alphabet prefix enumeration; numerical discovery only."""
from pathlib import Path
import itertools,json,hashlib
import numpy as np
P=Path(__file__).resolve().parent
models={}
for f in P.glob("checkpoints_part*.json"):models.update(json.loads(f.read_text()))
words=[w for n in range(2,6) for w in itertools.product(range(3),repeat=n) if 1 in w and 2 in w]
assert len(words)==244 and len(models)==16
out=[]
for key,p in sorted(models.items()):
 A=np.asarray(p["A"]);E=np.asarray(p["E"]);b=np.asarray(p["b"]);v=np.asarray(p["v"]);c=p["c"]
 H=np.zeros((244,2));target=np.zeros(244,dtype=np.int8);first=np.full(244,-1,dtype=int)
 for i,w in enumerate(words):
  h=np.zeros(2);q=0
  for j,s in enumerate(w,1):
   h=np.maximum(0.,A@h+E[s]+b)
   q=1 if s==1 else (0 if s==2 else q)
   if first[i]<0 and int(h@v+c>0)!=q:first[i]=j
  H[i]=h;target[i]=q
 for k in range(1,2049):
  H=np.maximum(0.,H@A.T+E[0]+b)
  z=H@v+c
  ix=np.where((first<0)&((z>0).astype(int)!=target))[0]
  for i in ix:first[i]=len(words[i])+k
 candidates=[(int(n),list(words[i])) for i,n in enumerate(first) if n>0]
 candidates.sort(key=lambda z:(z[0],z[1]))
 out.append({"key":key,"candidate_count":len(candidates),"first":candidates[0] if candidates else None,"positions":first.tolist()})
 print(key,len(candidates),candidates[0] if candidates else None,flush=True)
assert sum(r["first"] is not None for r in out)==10
(P/"REPRODUCED_FLOAT64.json").write_text(json.dumps(out,separators=(",",":"))+"\n")
print("PASS 244 prefixes x 16 checkpoints, 2048 holds; numerical only")
