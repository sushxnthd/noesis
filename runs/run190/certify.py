"""Independent outward-interval all-length parity certificate for Run190 seed151."""
import json
from pathlib import Path
from fractions import Fraction
import numpy as np
from mpmath import iv
R=Path(__file__).resolve().parent
iv.dps=65
def q(x):
    f=Fraction.from_float(float(x))
    return iv.mpf(f.numerator)/iv.mpf(f.denominator)
def verify(epoch,k=6):
    data=json.loads((R/"TRAINED.json").read_text())
    row=next(r for r in data['rows'] if r['seed']==151 and r['epoch']==epoch)
    p={key:np.asarray(val,dtype=float) for key,val in row['params'].items()}
    n=1<<k;mask=n-1
    lo=np.full((2*n,8),np.inf);hi=np.full((2*n,8),-np.inf)
    h=np.zeros((1,8));par=np.zeros(1,dtype=int);suf=np.zeros(1,dtype=int)
    for _ in range(k+1):
        hh=np.empty((2*len(h),8));pp=np.empty(2*len(h),dtype=int);ss=np.empty(2*len(h),dtype=int)
        for bit in (0,1):
            hh[bit::2]=np.tanh(h@p['W'].T+p['U'][bit]+p['b'])
            pp[bit::2]=par^bit;ss[bit::2]=((suf<<1)|bit)&mask
        h,par,suf=hh,pp,ss
    ix=par*n+suf
    np.minimum.at(lo,ix,h);np.maximum.at(hi,ix,h)
    grid=1e-12
    lo=np.floor((lo-1e-13)/grid)*grid
    hi=np.ceil((hi+1e-13)/grid)*grid
    pos=np.maximum(p['W'],0);neg=np.minimum(p['W'],0)
    target=np.array([[(idx//n^bit)*n+(((idx%n)<<1|bit)&mask) for bit in (0,1)] for idx in range(2*n)])
    closed=False
    for step in range(1000):
        oldlo=lo.copy();oldhi=hi.copy()
        for bit in (0,1):
            tl=np.tanh(oldlo@pos.T+oldhi@neg.T+p['U'][bit]+p['b'])
            th=np.tanh(oldhi@pos.T+oldlo@neg.T+p['U'][bit]+p['b'])
            np.minimum.at(lo,target[:,bit],np.floor((tl-1e-13)/grid)*grid)
            np.maximum.at(hi,target[:,bit],np.ceil((th+1e-13)/grid)*grid)
        if np.array_equal(oldlo,lo) and np.array_equal(oldhi,hi):closed=True;break
    if not closed:raise AssertionError("grid candidate did not stabilize")
    low=[[format(x,'.15f') for x in r] for r in lo]
    high=[[format(x,'.15f') for x in r] for r in hi]
    box=[[iv.mpf([low[i][j],high[i][j]]) for j in range(8)] for i in range(2*n)]
    P={key:[[q(x) for x in rr] for rr in val] if isinstance(val,list) and isinstance(val[0],list) else [q(x) for x in val] if isinstance(val,list) else q(val) for key,val in row['params'].items()}
    def advance(h,bit):
        return [1-2/(1+iv.exp(2*sum((P['W'][i][j]*h[j] for j in range(8)),P['b'][i]+P['U'][bit][i]))) for i in range(8)]
    def output(h):return sum((P['v'][j]*h[j] for j in range(8)),P['c'])
    def good(y,parity):return bool(y.a>0 if parity else y.b<0)
    states=[([iv.mpf(0)]*8,0,0)]
    prefixes=0
    for depth in range(1,k+2):
        new=[]
        for h,par,suf in states:
            for bit in (0,1):
                nxt=advance(h,bit);pa=par^bit;su=((suf<<1)|bit)&mask
                assert good(output(nxt),pa),('short_prefix',epoch,depth,pa,su)
                new.append((nxt,pa,su));prefixes+=1
        states=new
    for h,par,suf in states:
        idx=par*n+suf
        for j in range(8):
            assert h[j].a>=box[idx][j].a and h[j].b<=box[idx][j].b,('base',epoch,idx,j)
    for idx,h in enumerate(box):
        assert good(output(h),idx//n),('output',epoch,idx)
        for bit in (0,1):
            nh=advance(h,bit);dest=target[idx,bit]
            for j in range(8):
                assert nh[j].a>=box[dest][j].a and nh[j].b<=box[dest][j].b,('closure',epoch,idx,bit,j)
    return {'verified':True,'seed':151,'epoch':epoch,'k':k,'boxes':2*n,'prefixes':prefixes,'closure_coordinate_checks':2*n*2*8,'train_loss':row['loss'],'torch_version':data['torch']}
if __name__=='__main__':
    result=[verify(300),verify(600)]
    (R/"CERTIFICATION.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
