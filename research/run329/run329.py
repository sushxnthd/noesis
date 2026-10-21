"""NOESIS K001-R Run329. Frozen seed 32924000; original epoch80 models only."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
root=Path(__file__).resolve().parent
raw=(root/"checkpoints326.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="628493d45ba6468144e4a771a8d73c01786333eca26fa8afaf25336da480fe1e"
old=json.loads((root/"updated_outcomes328.json").read_text())
models={r["seed"]:r["p"] for r in json.loads(raw)["rows"] if r["epoch"]==80}
seeds=[r["seed"] for r in old["rows"] if r["outcome"]=="unresolved"]
assert len(seeds)==174
rng=np.random.default_rng(32924000);words=[];seen=set()
for n in (16,32,64,128):
    for k in (1,2,3,5,8,n//2):
        for _ in range(64):
            pos=rng.choice(n,size=k,replace=False)
            w="".join("1" if i in pos else "0" for i in range(n))
            if w not in seen:seen.add(w);words.append(w)
assert len(words)==1399
assert hashlib.sha256(("\n".join(words)+"\n").encode()).hexdigest()=="d646769be6deb31db579bba1907aeeafeca5e643498ec5c2d1af2d86b2ec37a3"
P=np.array([models[s] for s in seeds]);A=P[:,:18].reshape(-1,2,3,3);b=P[:,18:24].reshape(-1,2,3);v=P[:,24:27];c=P[:,27]
def exact(seed,w):
    p=list(map(F.from_float,models[seed]));h=[F(0)]*3;label=False
    for t,ch in enumerate(w,1):
        x=int(ch);label|=bool(x)
        h=[max(F(0),sum(p[9*x+3*i+j]*h[j] for j in range(3))+p[18+3*x+i]) for i in range(3)]
        z=sum(p[24+i]*h[i] for i in range(3))+p[27]
        if bool(z>0)!=label:return t,z
    return None
def minimize(seed,w):
    step=max(1,len(w)//2)
    while step:
        changed=True
        while changed:
            changed=False
            for i in range(len(w)-step+1):
                z=w[:i]+w[i+step:]
                if z and exact(seed,z) is not None:w=z;changed=True;break
        step//=2
    return w
found={};screened=0;skipped=0
for wi,w in enumerate(words):
    h=np.zeros((len(seeds),3));label=False;done=np.array([s in found for s in seeds])
    for t,ch in enumerate(w,1):
        x=int(ch);label|=bool(x)
        with np.errstate(over="ignore",invalid="ignore"):
            h=np.maximum(0,np.einsum("nij,nj->ni",A[:,x],h)+b[:,x])
            z=np.einsum("ni,ni->n",h,v)+c
        finite=np.isfinite(z)&np.isfinite(h).all(axis=1)
        skipped+=int((~finite&~done).sum())
        for j in np.flatnonzero(((z>0)!=label)&finite&~done):
            seed=seeds[int(j)];screened+=1;hit=exact(seed,w[:t])
            if hit is None:continue
            witness=minimize(seed,w[:hit[0]])
            assert exact(seed,witness) is not None
            found[seed]={"witness":witness,"candidate_index":wi,"first_prefix_length":hit[0]}
            done[j]=True
assert len(found)==1 and 24108 in found
assert found[24108]["witness"]=="11101000000000111111110"
print(json.dumps({"candidates":len(words),"new_exact_witnesses":len(found),"found":found,"float_candidates":screened,"overflow_skips":skipped},indent=2))
