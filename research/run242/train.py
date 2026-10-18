"""Frozen NOESIS Run242 reset-parity training; do not modify after holdout."""
import torch,json,time
from pathlib import Path
R=Path(__file__).parent
SEEDS=list(range(8101,8149)); EPOCHS=(0,50,200)
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
x=torch.tensor([[(n//3**(4-j))%3 for j in range(5)] for n in range(243)],dtype=torch.long)
q=torch.zeros(243,dtype=torch.long);ys=[]
for j in range(5):
 q=torch.where(x[:,j]==2,0,torch.where(x[:,j]==1,1-q,q));ys.append(q.clone())
y=torch.stack(ys,dim=1).double();rows=[];start=time.time()
for seed in SEEDS:
 torch.manual_seed(seed)
 W=torch.nn.Parameter(torch.randn(3,4,4,dtype=torch.double))
 b=torch.nn.Parameter(torch.randn(3,4,dtype=torch.double))
 v=torch.nn.Parameter(torch.randn(4,dtype=torch.double))
 c=torch.nn.Parameter(torch.randn((),dtype=torch.double))
 opt=torch.optim.Adam([W,b,v,c],lr=.03)
 for epoch in range(201):
  h=torch.tensor([.5,-.5,.25,.125],dtype=torch.double).repeat(243,1);zs=[]
  for j in range(5):
   h=torch.clamp(torch.einsum('nij,nj->ni',W[x[:,j]],h)+b[x[:,j]],-1,1)
   zs.append(h@v+c)
  z=torch.stack(zs,dim=1)
  loss=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
  if epoch in EPOCHS:
   p=dict(W=W.detach().tolist(),b=b.detach().tolist(),v=v.detach().tolist(),c=float(c.detach()))
   rows.append(dict(seed=seed,epoch=epoch,train_accuracy=float(((z>0)==(y>.5)).double().mean().detach()),train_confidence=float(z.abs().mean().detach()),loss=float(loss.detach()),params=p))
  if epoch==200:break
  opt.zero_grad();loss.backward();opt.step()
 print('trained',seed,'acc',rows[-1]['train_accuracy'],'elapsed',round(time.time()-start,2),flush=True)
 (R/'CHECKPOINTS.json').write_text(json.dumps(dict(seeds=SEEDS,epochs=EPOCHS,rows=rows,task='reset parity',dim=4,train_length=5,torch=torch.__version__),indent=2)+'\n')
