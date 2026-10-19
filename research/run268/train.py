"""NOESIS Run268: deterministic 2D/3D ReLU RNN latch training; no private compute."""
import json,itertools,hashlib,time,sys
from pathlib import Path
import torch
P=Path(__file__).resolve().parent
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
dim=int(sys.argv[1]);assert dim in (2,3)
start=18501 if dim==2 else 18601
seeds=list(range(start,start+16))
N=len(seeds);seqs=[];ys=[];inits=[]
for seed in seeds:
 torch.manual_seed(seed)
 randomseq=torch.randint(0,3,(512,20),dtype=torch.long)
 short=torch.tensor([list(w)+[0]*17 for w in itertools.product(range(3),repeat=3)],dtype=torch.long)
 seq=torch.cat([randomseq,short],dim=0)
 q=torch.zeros(len(seq),dtype=torch.long);target=[]
 for j in range(20):
  q=torch.where(seq[:,j]==2,0,torch.where(seq[:,j]==1,1,q));target.append(q.clone())
 seqs.append(seq);ys.append(torch.stack(target,dim=1).double())
 torch.manual_seed(seed+9999)
 inits.append((torch.randn(dim,dim,dtype=torch.double)*.25,torch.randn(3,dim,dtype=torch.double)*.3,
  torch.zeros(dim,dtype=torch.double),torch.randn(dim,dtype=torch.double)*.3,torch.zeros((),dtype=torch.double)))
seq=torch.stack(seqs);y=torch.stack(ys);B=seq.shape[1]
A=torch.nn.Parameter(torch.stack([i[0] for i in inits]))
E=torch.nn.Parameter(torch.stack([i[1] for i in inits]))
b=torch.nn.Parameter(torch.stack([i[2] for i in inits]))
v=torch.nn.Parameter(torch.stack([i[3] for i in inits]))
c=torch.nn.Parameter(torch.stack([i[4] for i in inits]))
opt=torch.optim.Adam([A,E,b,v,c],lr=.03)
rows=[];st=time.time();idx=torch.arange(N)[:,None]
for epoch in range(601):
 h=torch.zeros((N,B,dim),dtype=torch.double);zs=[]
 for j in range(20):
  h=torch.relu(torch.bmm(h,A.transpose(1,2))+E[idx,seq[:,:,j],:]+b[:,None,:])
  zs.append((h*v[:,None,:]).sum(dim=2)+c[:,None])
 z=torch.stack(zs,dim=2)
 losses=torch.nn.functional.binary_cross_entropy_with_logits(z,y,reduction='none').mean(dim=(1,2))
 if epoch in (0,100,300,600):
  for i,seed in enumerate(seeds):
   rows.append({'seed':seed,'dimension':dim,'epoch':epoch,'train_accuracy':float(((z[i]>0)==(y[i]>.5)).double().mean().detach()),
    'bce':float(losses[i].detach()),'params':{'A':A[i].detach().tolist(),'E':E[i].detach().tolist(),
    'b':b[i].detach().tolist(),'v':v[i].detach().tolist(),'c':float(c[i].detach())}})
  print('dimension',dim,'epoch',epoch,'perfect',sum(r['train_accuracy']==1 for r in rows if r['epoch']==epoch),'elapsed',round(time.time()-st,2),flush=True)
 if epoch==600:break
 opt.zero_grad();losses.sum().backward();opt.step()
out=P/f'CHECKPOINTS_dim{dim}.json'
out.write_text(json.dumps({'torch':torch.__version__,'rows':rows,'training_seeds':seeds,'dimension':dim,'deterministic':True},separators=(',',':'))+'\n')
print('SHA256',hashlib.sha256(out.read_bytes()).hexdigest())
