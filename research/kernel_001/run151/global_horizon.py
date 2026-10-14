"""Exhaustive ternary first-failure check with conservative roundoff bounds."""
import json
from pathlib import Path
import numpy as np
from certified_horizon import bounds

HERE=Path(__file__).resolve().parent
def check(name,depth=13):
    p=json.loads((HERE/"checkpoints"/(name+".json")).read_text())
    A=np.array(p["A"]); E=np.array(p["E"]); w=np.array(p["w"])
    h=np.zeros((1,len(w)));q=np.zeros(1,dtype=int)
    norms=[]; history=[]
    for n in range(1,depth+1):
        old=float(np.max(np.abs(h)))
        h=np.stack([np.maximum(0,h@A.T+E[s]) for s in range(3)],axis=1).reshape(-1,len(w))
        q=np.stack([np.maximum(0,q+d) for d in (1,-1,0)],axis=1).reshape(-1)
        norms.append((old,float(np.max(np.abs(h)))))
        err=h@w-q; idx=int(np.argmax(np.abs(err))); m=float(abs(err[idx]))
        b=bounds(A,E,w,norms)[-1]
        history.append((m,b))
        if m-b>0.1:
            assert all(v+e<0.1 for v,e in history[:-1])
            digits=[]
            for _ in range(n): digits.append(str(idx%3));idx//=3
            return n,''.join(reversed(digits)),m,b
        assert m+b<0.1, "Ambiguous boundary; use exact intervals"
    return None
if __name__=="__main__":
    for variant in ("baseline","latent","output"):
        print(variant,check(variant))
