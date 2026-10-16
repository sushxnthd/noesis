import json,numpy as np
from run197 import params,advance,logits,WIDTH
from pathlib import Path
rows=json.loads(Path('CHECKPOINTS.json').read_text())['rows']
p=params(next(r for r in rows if r['seed']==257 and r['epoch']==800))
h=np.zeros((1,WIDTH));res=np.zeros(1,dtype=np.int8)
for depth in range(1,16):
    h=np.concatenate((advance(h,p,0),advance(h,p,1)))
    res=np.concatenate((res,(res+1)%3))
    z=logits(h,p)
    scores=z[np.arange(len(res)),res][:,None]-z
    scores[np.arange(len(res)),res]=np.inf
    margin=np.min(scores,axis=1)
    j=int(np.argmin(margin))
    print(depth,len(res),float(margin[j]),int(j),flush=True)