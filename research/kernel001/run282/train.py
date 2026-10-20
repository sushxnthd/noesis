#!/usr/bin/env python3
"""Run282: held-out parity training, two matched initialization arms; CPU-only."""
import torch,itertools,json,hashlib,time
from pathlib import Path
P=Path(__file__).resolve().parent
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
D=torch.float64
SEEDS=range(20496,20592); T=10; SNAP=(0,20,40,80,120,160)
xs=[];ys=[];starts=[];meta=[]
for arm in ('biased','neutral'):
 for seed in SEEDS:
  g=torch.Generator().manual_seed(seed)
  x=torch.randint(0,2,(256,T),generator=g)
  prefix=torch.tensor([list(w)+[0]*(T-2) for w in itertools.product(range(2),repeat=2)],dtype=torch.long)
  x=torch.cat([x,prefix]); q=torch.zeros(len(x),dtype=torch.long); targets=[]
  for t in range(T):
   q=torch.where(x[:,t]==0,0,1-q);targets.append(q.clone())
  xs.append(x);ys.append(torch.stack(targets,dim=1).to(D))
  if arm=='biased':
   g=torch.Generator().manual_seed(seed+17000)
   starts.append((torch.tensor([-.2,-1.2],dtype=D)+torch.randn(2,generator=g,dtype=D)*torch.tensor([.2,.35],dtype=D),
                  torch.tensor([-.03,1.],dtype=D)+torch.randn(2,generator=g,dtype=D)*torch.tensor([.06,.15],dtype=D),
                  torch.randn((),generator=g,dtype=D)*.4+2.,torch.randn((),generator=g,dtype=D)*.15-.8))
  else:
   g=torch.Generator().manual_seed(seed+31000); p=torch.randn(6,generator=g,dtype=D)*.5
   starts.append((p[:2].clone(),p[2:4].clone(),p[4].clone(),p[5].clone()))
  meta.append((arm,seed))
N=len(meta);X=torch.stack(xs);Y=torch.stack(ys);idx=torch.arange(N)[:,None]
A=torch.nn.Parameter(torch.stack([s[0] for s in starts]))
B=torch.nn.Parameter(torch.stack([s[1] for s in starts]))
V=torch.nn.Parameter(torch.stack([s[2] for s in starts]))
C=torch.nn.Parameter(torch.stack([s[3] for s in starts]))
opt=torch.optim.Adam([A,B,V,C],lr=.025)
rows=[]
for epoch in range(161):
 h=torch.zeros((N,X.shape[1]),dtype=D); logits=[]
 for t in range(T):
  x=X[:,:,t];h=torch.relu(A[idx,x]*h+B[idx,x]);logits.append(V[:,None]*h+C[:,None])
 z=torch.stack(logits,dim=2)
 bce=torch.nn.functional.binary_cross_entropy_with_logits(z,Y,reduction='none').mean((1,2))
 acc=((z>0)==(Y>.5)).to(D).mean((1,2))
 if epoch in SNAP:
  for k,(arm,seed) in enumerate(meta):
   rows.append({'arm':arm,'seed':seed,'epoch':epoch,'accuracy':float(acc[k].detach()),'bce':float(bce[k].detach()),
    'p':[float(A[k,0].detach()),float(A[k,1].detach()),float(B[k,0].detach()),float(B[k,1].detach()),float(V[k].detach()),float(C[k].detach())]})
  print('epoch',epoch,'perfect',int((acc[:96]==1).sum()),int((acc[96:]==1).sum()),flush=True)
 if epoch<160:
  opt.zero_grad();bce.sum().backward();opt.step()
raw={'config':{'seeds':list(SEEDS),'arms':['biased','neutral'],'length':T,'random_sequences':256,'enumerated_prefixes':4,'epochs':160,'snapshots':SNAP,'lr':.025,'dtype':'float64','torch':torch.__version__},'rows':rows}
blob=json.dumps(raw,sort_keys=True,separators=(',',':'))+'\n'
(P/'checkpoints282.json').write_text(blob)
torch.save({'epoch':160,'params':[p.detach().clone() for p in (A,B,V,C)],'optimizer':opt.state_dict()},P/'optimizer282.pt')
print('CHECKPOINT_SHA256',hashlib.sha256(blob.encode()).hexdigest(),flush=True)
