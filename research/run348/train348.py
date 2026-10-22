#!/usr/bin/env python3
"""Frozen Run348: width-3 parity training, independent seeds, no post-hoc changes."""
import hashlib, json, platform, time
from pathlib import Path
import torch
P=Path(__file__).resolve().parent
SEEDS=list(range(32000,32192)); N=len(SEEDS); W=3; T=8; EPOCHS=200; D=torch.float64
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
xs=[];ys=[];initial=[]
fixed=torch.tensor([[0]*T,[1]*T,[i%2 for i in range(T)],[(i+1)%2 for i in range(T)]],dtype=torch.long)
for seed in SEEDS:
    g=torch.Generator().manual_seed(seed)
    x=torch.cat([torch.randint(0,2,(192,T),generator=g),fixed])
    q=torch.zeros(len(x),dtype=torch.long);targets=[]
    for t in range(T):
        q=torch.bitwise_xor(q,x[:,t]);targets.append(q.clone())
    xs.append(x);ys.append(torch.stack(targets,dim=1).to(D))
    g=torch.Generator().manual_seed(seed+51000)
    initial.append(torch.randn(28,generator=g,dtype=D)*.5)
X=torch.stack(xs);Y=torch.stack(ys)
params=torch.nn.Parameter(torch.stack(initial))
opt=torch.optim.Adam([params],lr=.025)
rows=[];start=time.time()
for epoch in range(EPOCHS+1):
    a=params[:,:18].reshape(N,2,W,W);b=params[:,18:24].reshape(N,2,W)
    v=params[:,24:27];c=params[:,27]
    h=torch.zeros((N,X.shape[1],W),dtype=D);logits=[]
    ii=torch.arange(N)[:,None]
    for t in range(T):
        h=torch.relu(torch.einsum('nmij,nmj->nmi',a[ii,X[:,:,t]],h)+b[ii,X[:,:,t]])
        logits.append((h*v[:,None,:]).sum(-1)+c[:,None])
    z=torch.stack(logits,dim=2)
    bce=torch.nn.functional.binary_cross_entropy_with_logits(z,Y,reduction='none').mean((1,2))
    acc=((z>0)==(Y>.5)).to(D).mean((1,2))
    for k,seed in enumerate(SEEDS):
        rows.append({'seed':seed,'epoch':epoch,'accuracy':float(acc[k].detach()),'bce':float(bce[k].detach()),'p':params[k].detach().tolist()})
    if epoch%40==0:
        print('epoch',epoch,'train-perfect',int((acc==1).sum()),'elapsed',round(time.time()-start,2),flush=True)
    if epoch<EPOCHS:
        opt.zero_grad();bce.sum().backward();opt.step()
out={'protocol_sha256':hashlib.sha256((P/'FROZEN_PROTOCOL.md').read_bytes()).hexdigest(),
     'task':'prefix parity','torch':torch.__version__,'python':platform.python_version(),
     'seeds':SEEDS,'rows':rows}
payload=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
(P/'trajectories348.json').write_text(payload)
(P/'training348_summary.json').write_text(json.dumps({'seeds':SEEDS,'epochs':EPOCHS+1,'num_rows':len(rows),
 'elapsed_s':round(time.time()-start,3),'trajectories_sha256':hashlib.sha256(payload.encode()).hexdigest()},indent=2)+'\n')
