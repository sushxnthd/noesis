"""NOESIS Run240 frozen holdout: reset parity, 48 newly gradient-trained hardtanh RNNs."""
import json,time
from pathlib import Path
import torch
R=Path(__file__).parent
SEEDS=range(6201,6225)
ARMS=('baseline','saturation')
EPOCHS=(0,100,200)
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
x=torch.tensor([[(n//3**(4-j))%3 for j in range(5)] for n in range(243)],dtype=torch.long)
q=torch.zeros(243,dtype=torch.long);ys=[]
for j in range(5):
 q=torch.where(x[:,j]==2,0,torch.where(x[:,j]==1,1-q,q));ys.append(q.clone())
y=torch.stack(ys,dim=1).double()
rows=[];start=time.time()
for seed in SEEDS:
 for arm in ARMS:
  torch.manual_seed(seed)
  W=torch.nn.Parameter(torch.randn(3,4,4,dtype=torch.double));b=torch.nn.Parameter(torch.randn(3,4,dtype=torch.double))
  v=torch.nn.Parameter(torch.randn(4,dtype=torch.double));c=torch.nn.Parameter(torch.randn((),dtype=torch.double))
  opt=torch.optim.Adam([W,b,v,c],lr=.03)
  for epoch in range(201):
   h=torch.tensor([.5,-.5,.25,.125],dtype=torch.double).repeat(243,1)
   zs=[];sat=[]
   for j in range(5):
    h=torch.clamp(torch.einsum('nij,nj->ni',W[x[:,j]],h)+b[x[:,j]],-1,1)
    zs.append(h@v+c);sat.append(h.abs().mean())
   z=torch.stack(zs,dim=1);bce=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
   avg=torch.stack(sat).mean()
   loss=bce+.1*(1-avg) if arm=='saturation' else bce
   if epoch in EPOCHS:
    p=dict(W=W.detach().tolist(),b=b.detach().tolist(),v=v.detach().tolist(),c=float(c.detach()))
    rows.append(dict(dim=4,seed=seed,arm=arm,epoch=epoch,train_accuracy=float(((z>0)==(y>.5)).double().mean().detach()),train_confidence=float(z.abs().mean().detach()),mean_abs_h=float(avg.detach()),bce=float(bce.detach()),params=p))
   if epoch==200:break
   opt.zero_grad();loss.backward();opt.step()
  print('trained',seed,arm,rows[-1]['train_accuracy'],round(time.time()-start,2),flush=True)
  (R/'CHECKPOINTS.json').write_text(json.dumps(dict(seeds=list(SEEDS),arms=ARMS,epochs=EPOCHS,rows=rows,torch=torch.__version__),indent=2)+'\n')
