"""NOESIS Run272 exact deterministic paired training generator."""
import json,itertools,hashlib,time
from pathlib import Path
import torch
ROOT=Path(__file__).resolve().parent
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
D=torch.float64;seeds=list(range(19300,19324));N=len(seeds);T=20
seqs=[];tgts=[];starts=[]
for seed in seeds:
 g=torch.Generator().manual_seed(seed)
 x=torch.randint(0,3,(256,T),generator=g)
 short=torch.tensor([list(w)+[0]*17 for w in itertools.product(range(3),repeat=3)],dtype=torch.long)
 x=torch.cat([x,short]);q=torch.zeros(len(x),dtype=torch.long);y=[]
 for t in range(T):
  q=torch.where(x[:,t]==1,1,torch.where(x[:,t]==2,0,q));y.append(q.clone())
 seqs.append(x);tgts.append(torch.stack(y,dim=1).to(D))
 g=torch.Generator().manual_seed(seed+13000)
 starts.append((torch.randn(3,generator=g,dtype=D)*.25+.1,
  torch.randn(3,generator=g,dtype=D)*.25,
  torch.randn((),generator=g,dtype=D)*.3,
  torch.randn((),generator=g,dtype=D)*.3))
X=torch.stack(seqs).repeat(2,1,1);Y=torch.stack(tgts).repeat(2,1,1)
A=torch.nn.Parameter(torch.stack([s[0] for s in starts]*2))
B=torch.nn.Parameter(torch.stack([s[1] for s in starts]*2))
V=torch.nn.Parameter(torch.stack([s[2] for s in starts]*2))
C=torch.nn.Parameter(torch.stack([s[3] for s in starts]*2))
opt=torch.optim.Adam([A,B,V,C],lr=.03)
idx=torch.arange(2*N)[:,None];rows=[]
for epoch in range(501):
 h=torch.zeros((2*N,X.shape[1]),dtype=D);zs=[]
 for t in range(T):
  x=X[:,:,t];h=torch.relu(A[idx,x]*h+B[idx,x]);zs.append(V[:,None]*h+C[:,None])
 Z=torch.stack(zs,dim=2)
 bce=torch.nn.functional.binary_cross_entropy_with_logits(Z,Y,reduction='none').mean((1,2))
 if epoch in (0,100,300,500):
  for k in range(2*N):
   rows.append({'seed':seeds[k%N],'arm':'baseline' if k<N else 'amplification',
    'epoch':epoch,'train_accuracy':float(((Z[k]>0)==(Y[k]>.5)).to(D).mean().detach()),
    'train_bce':float(bce[k].detach()),
    'params':{'a':A[k].detach().tolist(),'b':B[k].detach().tolist(),
     'v':float(V[k].detach()),'c':float(C[k].detach())}})
 if epoch==500:break
 loss=bce.sum()+10.0*((A[N:,2]-2.0**(-12))**2).sum()
 opt.zero_grad();loss.backward();opt.step()
out={'schema':'noesis_run272','torch':torch.__version__,'seeds':seeds,
 'config':{'epochs':500,'N':256,'T':T,'lr':.03,'baseline_aux':False,
 'intervention_reset_gain_prior':{'weight':10.0,'target':2.0**(-12)},
 'dtype':'float64'},'rows':rows}
p=ROOT/'checkpoints.json';p.write_text(json.dumps(out,indent=2)+'\n')
print('sha256',hashlib.sha256(p.read_bytes()).hexdigest())
