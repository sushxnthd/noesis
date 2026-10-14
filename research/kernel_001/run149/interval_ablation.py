from pathlib import Path
import json
import numpy as np
HERE=Path(__file__).resolve().parent
CHECKPOINTS=HERE.parent/'run147'/'checkpoints'
def down(x):return np.nextafter(x,-np.inf)
def up(x):return np.nextafter(x,np.inf)
def word(code,n):return ''.join(str((int(code)//(3**i))%3) for i in range(n-1,-1,-1))
def scan(seed=214,clamp=3,depth=13):
    p=json.loads((CHECKPOINTS/f'{seed}.json').read_text())
    A,E,w=[np.array(p[k],dtype=np.float64) for k in ('A','E','w')]
    assert all(float(np.float32(v))==float(v) for v in np.r_[A.ravel(),E.ravel(),w.ravel()])
    lo=np.zeros((1,4));hi=lo.copy();q=np.zeros(1,dtype=np.int16);codes=np.zeros(1,dtype=np.int64)
    rows=[]
    for n in range(1,depth+1):
        count=len(q)
        nl=np.zeros((3*count,4));nh=np.zeros_like(nl)
        for i in range(4):
            for tok in range(3):
                if tok==2 and i==clamp:continue
                sl=np.zeros(count);sh=np.zeros(count)
                for j in range(4):
                    a=A[i,j];vl=lo[:,j] if a>=0 else hi[:,j];vh=hi[:,j] if a>=0 else lo[:,j]
                    sl=down(sl+down(a*vl));sh=up(sh+up(a*vh))
                nl[tok::3,i]=np.maximum(0,down(sl+E[tok,i]))
                nh[tok::3,i]=np.maximum(0,up(sh+E[tok,i]))
        lo,hi=nl,nh
        q=np.maximum(0,np.repeat(q,3)+np.tile(np.array([1,-1,0],dtype=np.int16),count))
        codes=np.repeat(codes,3)*3+np.tile(np.arange(3,dtype=np.int64),count)
        yl=np.zeros(len(q));yh=yl.copy()
        for j in range(4):
            a=w[j]
            yl=down(yl+down(a*(lo[:,j] if a>=0 else hi[:,j])))
            yh=up(yh+up(a*(hi[:,j] if a>=0 else lo[:,j])))
        elo=down(yl-q);ehi=up(yh-q)
        err=np.maximum(np.abs(elo),np.abs(ehi));idx=int(np.argmax(err))
        definitely_bad=(elo>up(0.1))|(ehi<-up(0.1))
        possibly_bad=err>down(0.1)
        rows.append(dict(n=n,words=3**n,max_error_upper=float(err[idx]),argmax=word(codes[idx],n),definitely_bad=int(definitely_bad.sum()),possibly_bad=int(possibly_bad.sum())))
        print(seed,clamp,n,rows[-1],flush=True)
    return dict(seed=seed,clamp=clamp,semantics='exact real with binary32-stored parameters and outward-binary64 bounds',rows=rows)
if __name__=='__main__':
    r=scan();(HERE/'INTERVAL_OUTCOME.json').write_text(json.dumps(r,indent=2)+'\n')
