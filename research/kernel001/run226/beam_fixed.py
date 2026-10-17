"""Run226 deterministic, multi-width counterexample discovery; NEVER a proof."""
import json, hashlib, numpy as np
from pathlib import Path
R=Path(__file__).resolve().parent
D=json.loads((R/"RUN220_CHECKPOINTS.json").read_text())
UNRESOLVED=(1303,1307,1321,1361,1367,1373,1381,1399,1423,1433,1439,1447,1453,1459,1471,1481,1483)
WIDTHS=(64,128,256,512,1024)
MAXLEN=256

def search(p,width,maxlen=MAXLEN):
    W=np.asarray(p["W"]);b=np.asarray(p["b"]);v=np.asarray(p["v"]);c=p["c"]
    h=np.array([[.5,-.5,.25]]);q=np.array([0],dtype=np.int8);words=[""]
    for length in range(1,maxlen+1):
        oldn=len(h)
        H=np.concatenate([np.tanh(h@W[t].T+b[t]) for t in range(3)])
        Q=np.concatenate([np.zeros_like(q) if t==2 else q^(t==1) for t in range(3)])
        margin=(2*Q-1)*(H@v+c)
        ix=np.flatnonzero(margin<0)
        if len(ix):
            i=int(ix[np.argmin(margin[ix])])
            return dict(status="CANDIDATE",length=length,word=words[i%oldn]+str(i//oldn),margin=float(margin[i]))
        keep=[]
        for qq in (0,1):
            inds=np.flatnonzero(Q==qq)
            if not len(inds):continue
            quota=max(1,width//2)
            order=np.argsort(margin[inds],kind="stable")
            selected=list(inds[order[:quota//2]])
            for dim in range(3):
                selected.extend(inds[np.argsort(H[inds,dim],kind="stable")[:quota//12]].tolist())
                selected.extend(inds[np.argsort(-H[inds,dim],kind="stable")[:quota//12]].tolist())
            selected.extend(inds[np.argsort(np.abs(H[inds]).sum(axis=1),kind="stable")[:quota//8]].tolist())
            bins=set(tuple(np.round(H[i],6)) for i in selected)
            for i in inds[order]:
                key=tuple(np.round(H[i],6))
                if key not in bins:bins.add(key);selected.append(int(i))
                if len(selected)>=quota:break
            keep.extend(dict.fromkeys(selected[:quota]))
        h=H[keep];q=Q[keep];words=[words[i%oldn]+str(i//oldn) for i in keep]
    return dict(status="NO_CANDIDATE",length=maxlen)

def main():
    rows={r["seed"]:r for r in D["rows"] if r["epoch"]==200}
    outcomes=[]
    for width in WIDTHS:
        for seed in (*UNRESOLVED,1429):
            r=search(rows[seed]["params"],width)
            outcomes.append(dict(seed=seed,width=width,**r))
            print(seed,width,r["status"],r["length"],flush=True)
    assert len(outcomes)==90
    assert not [r for r in outcomes if r["seed"]!=1429 and r["status"]=="CANDIDATE"]
    controls={r["width"]:r for r in outcomes if r["seed"]==1429}
    assert controls[64]["word"]=="200011100"
    assert controls[128]["status"]=="NO_CANDIDATE"
    for w in (256,512,1024):assert controls[w]["word"]=="20011100"
    (R/"BEAM_OUTCOMES.json").write_text(json.dumps(dict(archived_checkpoint_sha256="4cc24de3636fa8aaf98bbd96470d8e9f3509b2c16b7fcce021cd6d681b542dd8",widths=WIDTHS,maxlen=MAXLEN,results=outcomes),indent=2)+"\n")
if __name__=="__main__":main()
