"""Frozen Run343 cohort search. Requires Run342 archive: ../run342/trajectories342.json and outcomes342.json."""
import json
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
rows=json.loads((P.parent/'run342/trajectories342.json').read_text())['rows']
out=json.loads((P.parent/'run342/outcomes342.json').read_text())['rows']
seeds=sorted(r['seed'] for r in out if r['endpoint_label']==1)
assert len(seeds)==88
models={r['seed']:r['p'] for r in rows if r['epoch']==200 and r['seed'] in seeds}
assert len(models)==88
result=[]
for start in range(0,88,8):
 ss=seeds[start:start+8];n=len(ss)
 p=np.array([models[s] for s in ss],dtype=np.float64)
 a=p[:,:32].reshape(n,2,4,4);b=p[:,32:40].reshape(n,2,4);v=p[:,40:44];c=p[:,44]
 state=np.zeros((n,1,4));par=np.array([0],dtype=np.int8)
 first={}
 for length in range(1,17):
  z0=np.maximum(np.einsum('nij,nkj->nki',a[:,0],state,optimize=True)+b[:,None,0,:],0)
  z1=np.maximum(np.einsum('nij,nkj->nki',a[:,1],state,optimize=True)+b[:,None,1,:],0)
  state=np.stack((z0,z1),axis=2).reshape(n,-1,4)
  par=np.stack((par,1-par),axis=1).reshape(-1)
  if length<=12:continue
  logits=np.einsum('nkj,nj->nk',state,v,optimize=True)+c[:,None]
  bad=(logits>0)!=(par[None,:]==1)
  for i,s in enumerate(ss):
   if s not in first and np.any(bad[i]):
    j=int(np.flatnonzero(bad[i])[0])
    first[s]={'length':length,'word':format(j,f'0{length}b'),'logit_float64':float(logits[i,j])}
 for s in ss:result.append({'seed':s,'first_failure':first.get(s)})
assert len(result)==88
print(json.dumps({'tested':88,'new_input_model_pairs':88*sum(2**n for n in range(13,17)),'failures':[r for r in result if r['first_failure']],'rows':result},indent=2))
