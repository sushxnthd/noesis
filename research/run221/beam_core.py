import json,numpy as np
from pathlib import Path
p=json.loads((Path(__file__).parent/"SEED1429_E200.json").read_text())["params"]
W=np.asarray(p["W"]);b=np.asarray(p["b"]);v=np.asarray(p["v"]);c=p["c"]
def search(width):
 h=np.array([[.5,-.5,.25]]);q=np.array([0],dtype=np.int8);words=[""]
 for depth in range(1,9):
  old=len(h)
  H=np.vstack([np.tanh(h@W[t].T+b[t]) for t in range(3)])
  Q=np.concatenate([np.zeros_like(q) if t==2 else q^(t==1) for t in range(3)])
  margin=(2*Q-1)*(H@v+c)
  candidates=[words[i%old]+str(i//old) for i in range(len(H))]
  ix=np.where(margin<0)[0]
  if len(ix):return [candidates[i] for i in ix]
  keep=[]
  for qq in (0,1):
   inds=np.where(Q==qq)[0]
   if not len(inds):continue
   quota=max(1,width//2)
   selected=list(inds[np.argsort(margin[inds])[:quota//2]])
   for dim in range(3):
    selected.extend(inds[np.argsort(H[inds,dim])[:quota//12]].tolist())
    selected.extend(inds[np.argsort(-H[inds,dim])[:quota//12]].tolist())
   selected.extend(inds[np.argsort(np.abs(H[inds]).sum(axis=1))[:quota//8]].tolist())
   bins={tuple(np.round(H[i],6)) for i in selected}
   for i in inds[np.argsort(margin[inds])]:
    key=tuple(np.round(H[i],6))
    if key not in bins:bins.add(key);selected.append(int(i))
    if len(selected)>=quota:break
   keep.extend(dict.fromkeys(selected[:quota]))
  h,q,words=H[keep],Q[keep],[candidates[i] for i in keep]
 return []
