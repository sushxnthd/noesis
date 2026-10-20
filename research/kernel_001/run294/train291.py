#!/usr/bin/env python3
"""Exact Run291 cohort generator reused for Run294 public reproduction."""
import hashlib,itertools,json,time
from pathlib import Path
import torch
P=Path(__file__).resolve().parent
D=torch.float64;W=3;N=256;T=6;SEEDS=list(range(21440,21696));SNAP=(0,20,40,80,120)
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
xs=[];ys=[];init=[]
for seed in SEEDS:
 g=torch.Generator().manual_seed(seed)
 x=torch.randint(0,2,(160,T),generator=g)
 fixed=torch.tensor([list(w)+[0]*(T-2) for w in itertools.product((0,1),repeat=2)],dtype=torch.long)
 x=torch.cat([x,fixed]);q=torch.zeros(len(x),dtype=torch.long);targets=[]
 for t in range(T):
  q=torch.where(x[:,t]==0,0,1-q);targets.append(q.clone())
 xs.append(x);ys.append(torch.stack(targets,dim=1).to(D))
 g=torch.Generator().manual_seed(seed+51000)
 init.append(torch.randn(2*W*W+2*W+W+1,generator=g,dtype=D)*.5)
X=torch.stack(xs);Y=torch.stack(ys);params=torch.nn.Parameter(torch.stack(init))
opt=torch.optim.Adam([params],lr=.025);rows=[];t0=time.time()
for epoch in range(121):
 a=params[:,:2*W*W].reshape(N,2,W,W)
 b=params[:,2*W*W:2*W*W+2*W].reshape(N,2,W)
 v=params[:,2*W*W+2*W:-1];c=params[:,-1]
 h=torch.zeros((N,X.shape[1],W),dtype=D);logits=[]
 for t in range(T):
  sym=X[:,:,t];ii=torch.arange(N)[:,None]
  h=torch.relu(torch.einsum('nmij,nmj->nmi',a[ii,sym],h)+b[ii,sym])
  logits.append((h*v[:,None,:]).sum(-1)+c[:,None])
 z=torch.stack(logits,dim=2)
 bce=torch.nn.functional.binary_cross_entropy_with_logits(z,Y,reduction='none').mean((1,2))
 acc=((z>0)==(Y>.5)).to(D).mean((1,2))
 if epoch in SNAP:
  for k,seed in enumerate(SEEDS):
   rows.append({'seed':seed,'epoch':epoch,'accuracy':float(acc[k].detach()),'bce':float(bce[k].detach()),'p':params[k].detach().tolist()})
  print('epoch',epoch,'sampled_perfect',int((acc==1).sum()),flush=True)
 if epoch<120:
  opt.zero_grad();bce.sum().backward();opt.step()
raw={'config':{'seeds':SEEDS,'length':T,'random_sequences':160,'enumerated_prefixes':4,'epochs':120,'snapshots':SNAP,'lr':.025,'dtype':'float64','torch':torch.__version__,'width':W,'init_sigma':.5},'rows':rows}
blob=json.dumps(raw,sort_keys=True,separators=(',',':'))+'\n'
(P/'checkpoints291.json').write_text(blob)
print('CHECKPOINT_SHA256',hashlib.sha256(blob.encode()).hexdigest(),'seconds',round(time.time()-t0,2),flush=True)
