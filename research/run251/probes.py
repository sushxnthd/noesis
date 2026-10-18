"""Frozen deterministic probe families for Run251; no target-label access in model-conditioned selection."""
import numpy as np
LENGTHS=(6,8,10,12,16,20,24,32,40,48,64,80,96,128,192,256)
PREF=((1,),(1,1),(1,2),(2,1),(1,0,1),(1,1,2),(2,1,1),(1,2,1))
TAIL=((0,),(1,0),(0,1),(1,1,0),(2,0,0))
PERIOD=((1,0),(1,1),(1,2),(2,1))
PLENS=(8,12,20,32,48,80,128,256)
def motif(prefix,tail,n):
    return tuple(prefix+tuple(tail[i%len(tail)] for i in range(n-len(prefix))))
def model_score(row,w):
    p=row['params'];A=np.array(p['A']);E=np.array(p['E']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
    h=np.zeros(len(v));prev=np.zeros(len(v),dtype=bool);switches=0;flips=0;oldz=c
    for t in w:
        z=A@h+E[t]+b;mask=z>0
        switches+=int(np.count_nonzero(mask!=prev));prev=mask;h=np.maximum(0,z)
        newz=float(h@v+c);flips+=int((newz>0)!=(oldz>0));oldz=newz
    return switches/len(w)+.20*flips/len(w)+.05/(1+abs(oldz))
def arms(row):
    pool=[]
    for i,p in enumerate(PREF):
      for j,t in enumerate(TAIL):
        for n in LENGTHS[2:]:
          w=motif(p,t,n)
          pool.append((model_score(row,w),i,j,n,w))
    pool.sort(key=lambda x:(-x[0],x[1],x[2],x[3]))
    selected=[]; per_motif={};per_length={}
    for _,i,j,n,w in pool:
        if per_motif.get((i,j),0)>=2 or per_length.get(n,0)>=5:continue
        selected.append(w);per_motif[i,j]=per_motif.get((i,j),0)+1;per_length[n]=per_length.get(n,0)+1
        if len(selected)==32:break
    assert len(selected)==32
    fixed=[motif((s,),(0,),n) for n in LENGTHS for s in (1,2)]
    periodic=[motif((),m,n) for m in PERIOD for n in PLENS]
    rng=np.random.default_rng(451000+row['seed'])
    random=[tuple(map(int,rng.choice(3,size=len(w),p=(.85,.075,.075)))) for w in selected]
    assert len(fixed)==len(periodic)==len(random)==32
    return {'switching':selected,'fixed_tail':fixed,'periodic':periodic,'hold_biased':random}
