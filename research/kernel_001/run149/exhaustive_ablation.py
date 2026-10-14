import json
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
CHECKPOINTS=HERE.parent/'run147'/'checkpoints'
def word(code,n):return ''.join(str((int(code)//3**i)%3) for i in range(n-1,-1,-1))
def scan(seed,clamp=None,depth=13):
    p=json.loads((CHECKPOINTS/f'{seed}.json').read_text())
    A,E,w=[np.array(p[k],dtype=np.float64) for k in ('A','E','w')]
    h=np.zeros((1,4));q=np.zeros(1,dtype=np.int16);codes=np.zeros(1,dtype=np.int64)
    rows=[];first_failure=None
    for n in range(1,depth+1):
        nh=np.empty((3*len(q),4),dtype=np.float64)
        for tok in range(3):
            z=np.maximum(0,h@A.T+E[tok])
            if tok==2 and clamp is not None:z[:,clamp]=0
            nh[tok::3]=z
        h=nh;q=np.maximum(0,np.repeat(q,3)+np.tile(np.array([1,-1,0],dtype=np.int16),len(q)))
        codes=np.repeat(codes,3)*3+np.tile(np.arange(3,dtype=np.int64),len(codes))
        err=np.abs(h@w-q);i=int(np.argmax(err));fails=int(np.sum(err>0.1))
        if first_failure is None and fails:first_failure=n
        rows.append(dict(n=n,max_abs_error=float(err[i]),argmax=word(codes[i],n),num_failing=fails))
    return dict(seed=seed,clamp=clamp,first_failure=first_failure,rows=rows)
if __name__=='__main__':
    results=[]
    for seed in [214,210,215]:
        for clamp in [None,3,0,1,2]:
            r=scan(seed,clamp);print(seed,clamp,r['first_failure'],r['rows'][-1],flush=True);results.append(r)
    (HERE/'FLOAT64_OUTCOMES.json').write_text(json.dumps(results,indent=2)+'\n')
