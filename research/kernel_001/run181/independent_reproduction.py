"""Independent, human-readable reproduction of NOESIS Run181.
The original frozen experiment source and raw weights are archived separately.
This checker regenerates trained snapshots and evaluates the same observables.
"""
import itertools, json
from pathlib import Path
import numpy as np
import torch

torch.set_num_threads(1)
S=(0,20,50,100,200,400,800,1200)
W=('000111','001011','111000','001101')
X=torch.tensor(list(itertools.product(range(3),repeat=6)),dtype=torch.long)
T=torch.zeros(729,6)
q=torch.zeros(729)
delta=torch.tensor([1.,-1.,0.])
for t in range(6):
    q=(q+delta[X[:,t]]).clamp(min=0)
    T[:,t]=q

def apply(h,a,e,s):
    for x in s:
        h=np.maximum(a@h+e[int(x)],0)
    return h

def metrics(a,e,w):
    h=apply(np.zeros(len(w)) ,a,e,'000000')
    d=0.
    for neutral in ('01','0011'):
        z=apply(h.copy(),a,e,neutral)
        for suffix in ('','0','1','2','00','01','10'):
            d=max(d,abs(w@apply(z.copy(),a,e,suffix)-w@apply(h.copy(),a,e,suffix)))
    b=0.;z=h.copy()
    for _ in range(32):
        z=apply(z,a,e,'01')
        b=max(b,abs(w@z-6))
    clocks=[]
    for word in W:
        z=h.copy();first=None
        for k in range(1,2049):
            z=apply(z,a,e,word)
            error=w@z-6
            if not np.isfinite(error) or abs(error)>.1:
                first=k;break
        clocks.append(first)
    return d,b,clocks

def train(width,seed):
    torch.manual_seed(seed)
    A=torch.nn.Parameter(torch.eye(width)*.75+torch.randn(width,width)*.17)
    E=torch.nn.Parameter(torch.randn(3,width)*.4)
    v=torch.nn.Parameter(torch.randn(width)*.35+.5)
    opt=torch.optim.Adam([A,E,v],lr=.025)
    result=[]
    for epoch in range(1201):
        if epoch in S:
            with torch.no_grad():
                h=torch.zeros(729,width);mse=0.
                for t in range(6):
                    h=torch.relu(h@A.T+E[X[:,t]])
                    mse+=float(((h@v-T[:,t])**2).mean())/6
            a=A.detach().numpy().astype('float64')
            e=E.detach().numpy().astype('float64')
            w=v.detach().numpy().astype('float64')
            d,b,clocks=metrics(a,e,w)
            result.append(dict(width=width,seed=seed,epoch=epoch,mse=mse,D=d,B=b,
                               clocks=clocks,pass_all=all(c is None for c in clocks),
                               parameters=dict(A=a.tolist(),E=e.tolist(),w=w.tolist())))
        if epoch==1200:break
        opt.zero_grad();h=torch.zeros(729,width);loss=torch.zeros(());reg=torch.zeros(())
        for t in range(6):
            h=torch.relu(h@A.T+E[X[:,t]])
            loss+=((h@v-T[:,t])**2).mean()/6
            z=torch.relu(h@A.T+E[2])
            reg+=((z-h)**2).sum(dim=1).mean()/6
        (loss+.1*reg).backward();opt.step()
    return result

if __name__=='__main__':
    out=[]
    for width in (3,7):
        for seed in (401,405,409):
            out+=train(width,seed)
    path=Path(__file__).with_name('REPLAY_RAW.json')
    if path.exists():raise RuntimeError('Refusing to overwrite prior results')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('snapshots',len(out),'passes',sum(r['pass_all'] for r in out))
