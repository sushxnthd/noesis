import json,time
from pathlib import Path
import torch
R=Path(__file__).parent
SEEDS=range(7101,7149)
EPOCHS=(0,50,200)
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
x=torch.tensor([[(n//3**(5-j))%3 for j in range(6)] for n in range(729)],dtype=torch.long)
q=torch.zeros(729,dtype=torch.long);ys=[]
for j in range(6):
 q=torch.where(x[:,j]==2,0,torch.where(x[:,j]==1,1,q));ys.append(q.clone())
y=torch.stack(ys,dim=1).double()
rows=[];start=time.time()
for seed in SEEDS:
 torch.manual_seed(seed)
 W=torch.nn.Parameter(torch.randn(3,3,3,dtype=torch.double))
 b=torch.nn.Parameter(torch.randn(3,3,dtype=torch.double))
 v=torch.nn.Parameter(torch.randn(3,dtype=torch.double))
 c=torch.nn.Parameter(torch.randn((),dtype=torch.double))
 opt=torch.optim.Adam([W,b,v,c],lr=.03)
 for epoch in range(201):
  h=torch.tensor([.5,-.5,.25],dtype=torch.double).repeat(729,1);zs=[]
  for j in range(6):
   h=torch.clamp(torch.einsum('nij,nj->ni',W[x[:,j]],h)+b[x[:,j]],-1,1)
   zs.append(h@v+c)
  z=torch.stack(zs,dim=1)
  loss=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
  if epoch in EPOCHS:
   p=dict(W=W.detach().tolist(),b=b.detach().tolist(),v=v.detach().tolist(),c=float(c.detach()))
   rows.append(dict(seed=seed,epoch=epoch,loss=float(loss.detach()),train_accuracy=float(((z>0)==(y>.5)).double().mean().detach()),train_confidence=float(z.abs().mean().detach()),params=p,lr=.03))
  if epoch==200:break
  opt.zero_grad();loss.backward();opt.step()
 print('trained',seed,'acc',rows[-1]['train_accuracy'],'elapsed',round(time.time()-start,2),flush=True)
 (R/'CHECKPOINTS.json').write_text(json.dumps(dict(seeds=list(SEEDS),epochs=EPOCHS,rows=rows,architecture='3D fully coupled hardtanh; reset-latch task',torch=torch.__version__,elapsed=time.time()-start),indent=2)+'\n')
