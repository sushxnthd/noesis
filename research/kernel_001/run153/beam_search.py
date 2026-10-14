"""Deterministic adversarial witness search. NOT a shortest-failure verifier."""
import json,itertools
from pathlib import Path
import numpy as np
HERE=Path(__file__).parent
def load(seed):
    return json.loads((HERE/'checkpoints'/f'{seed}.json').read_text())
def search(seed,max_depth=128,per_objective=4):
    p=load(seed); A=np.asarray(p['A']); E=np.asarray(p['E']); w=np.asarray(p['w'])
    h=np.zeros((1,4)); q=np.zeros(1,dtype=np.int32); words=[b'']
    for depth in range(1,max_depth+1):
        n=len(q)
        hnew=np.maximum(0,np.repeat(h,3,axis=0)@A.T+np.tile(E,(n,1)))
        qnew=np.maximum(0,np.repeat(q,3)+np.tile([1,-1,0],n))
        paths=[words[i]+bytes([t]) for i in range(n) for t in range(3)]
        err=hnew@w-qnew
        j=int(np.argmax(abs(err)))
        if abs(err[j])>.1:
            return dict(depth=depth,word=''.join(map(str,paths[j])),error=float(err[j]))
        selected=set()
        for target in np.unique(qnew):
            ix=np.flatnonzero(qnew==target)
            norm=np.sum(abs(hnew[ix]),axis=1)
            for score in (err[ix],-err[ix],norm,-norm):
                selected.update(map(int,ix[np.argsort(-score,kind='stable')[:per_objective]]))
        keep=sorted(selected)
        h=hnew[keep];q=qnew[keep];words=[paths[k] for k in keep]
    return None
def neutral_control(seed,max_depth=128):
    p=load(seed);A=np.asarray(p['A']);E=np.asarray(p['E']);w=np.asarray(p['w'])
    words=np.array(list(itertools.product(range(3),repeat=6)),dtype=np.int8)
    h=np.zeros((len(words),4));q=np.zeros(len(words),dtype=np.int32)
    for t in range(6):
        x=words[:,t];h=np.maximum(0,h@A.T+E[x]);q=np.maximum(0,q+(x==0)-(x==1))
    for depth in range(7,max_depth+1):
        h=np.maximum(0,h@A.T+E[2])
        err=h@w-q;j=int(np.argmax(abs(err)))
        if abs(err[j])>.1:
            return dict(depth=depth,word=''.join(map(str,words[j]))+'2'*(depth-6),error=float(err[j]))
    return None
if __name__=='__main__':
    for seed in range(208,216):
        try: print(seed,search(seed),neutral_control(seed))
        except FileNotFoundError: print(seed,'checkpoint not uploaded; regenerate with run150 training script')
