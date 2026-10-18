"""NOESIS Run233 prospectively frozen CPU-only reset-latch training."""
import torch,json,time
from pathlib import Path
R=Path(__file__).parent
SEEDS=list(range(2501,2517))+list(range(2601,2605))
EPOCHS=(0,50,100,200)
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
 lr=.03 if seed<2600 else .001
 opt=torch.optim.Adam([W,b,v,c],lr=lr)
 for epoch in range(201):
  h=torch.tensor([.5,-.5,.25],dtype=torch.double).repeat(729,1);zs=[]
  for j in range(6):
   h=torch.tanh(torch.einsum('nij,nj->ni',W[x[:,j]],h)+b[x[:,j]])
   zs.append(h@v+c)
  z=torch.stack(zs,dim=1)
  loss=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
  if epoch in EPOCHS:
   p=dict(W=W.detach().tolist(),b=b.detach().tolist(),v=v.detach().tolist(),c=float(c.detach()))
   rows.append(dict(seed=seed,epoch=epoch,loss=float(loss.detach()),train_accuracy=float(((z>0)==(y>.5)).double().mean().detach()),params=p,lr=lr))
  if epoch==200:break
  opt.zero_grad();loss.backward();opt.step()
 print('trained',seed,'acc',rows[-1]['train_accuracy'],flush=True)
 (R/'CHECKPOINTS.json').write_text(json.dumps(dict(seeds=SEEDS,epochs=EPOCHS,rows=rows,architecture='3D tanh reset-latch',torch=torch.__version__,elapsed=time.time()-start),indent=2)+'\n')
