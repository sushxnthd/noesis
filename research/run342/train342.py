import hashlib,json,platform,time
from pathlib import Path
import torch
P=Path(__file__).resolve().parent
SEEDS=list(range(31000,31128));N=len(SEEDS);W=4;T=8;EPOCHS=200;D=torch.float64
PARAMS=2*W*W+3*W+1
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
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
 initial.append(torch.randn(PARAMS,generator=g,dtype=D)*.5)
X=torch.stack(xs);Y=torch.stack(ys)
params=torch.nn.Parameter(torch.stack(initial));opt=torch.optim.Adam([params],lr=.025)
rows=[];start=time.time();ii=torch.arange(N)[:,None]
for epoch in range(EPOCHS+1):
 a=params[:,:2*W*W].reshape(N,2,W,W)
 b=params[:,2*W*W:2*W*W+2*W].reshape(N,2,W)
 v=params[:,2*W*W+2*W:2*W*W+3*W];c=params[:,-1]
 h=torch.zeros((N,X.shape[1],W),dtype=D);logits=[]
 for t in range(T):
  h=torch.relu(torch.einsum('nmij,nmj->nmi',a[ii,X[:,:,t]],h)+b[ii,X[:,:,t]])
  logits.append((h*v[:,None,:]).sum(-1)+c[:,None])
 z=torch.stack(logits,dim=2)
 bce=torch.nn.functional.binary_cross_entropy_with_logits(z,Y,reduction='none').mean((1,2))
 acc=((z>0)==(Y>.5)).to(D).mean((1,2))
 for k,seed in enumerate(SEEDS):
  rows.append({'seed':seed,'epoch':epoch,'accuracy':float(acc[k].detach()),'bce':float(bce[k].detach()),'p':params[k].detach().tolist()})
 if epoch%40==0:print('epoch',epoch,'train-perfect',int((acc==1).sum()),'elapsed',round(time.time()-start,2),flush=True)
 if epoch<EPOCHS:
  opt.zero_grad();bce.sum().backward();opt.step()
out={'frozen_protocol_commit':'d6ed8e1a362d3eabb7c6c8b98c359eb1131dde34','task':'prefix parity','torch':torch.__version__,'python':platform.python_version(),'seeds':SEEDS,'width':W,'rows':rows}
payload=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
(P/'trajectories342.json').write_text(payload)
(P/'training342_summary.json').write_text(json.dumps({'n':N,'epochs':EPOCHS+1,'num_rows':len(rows),'elapsed_s':round(time.time()-start,3),'sha256':hashlib.sha256(payload.encode()).hexdigest()},indent=2)+'\n')
