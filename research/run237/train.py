import torch,json
from pathlib import Path
R=Path(__file__).parent
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
ARMS=('baseline','saturation','confidence')
x=torch.tensor([[(n//3**(5-j))%3 for j in range(6)] for n in range(729)],dtype=torch.long)
q=torch.zeros(729,dtype=torch.long);ys=[]
for j in range(6):
 q=torch.where(x[:,j]==2,0,torch.where(x[:,j]==1,1-q,q));ys.append(q.clone())
y=torch.stack(ys,dim=1).double()
rows=[]
for dim,seeds in [(3,range(3601,3625)),(4,range(3701,3713))]:
 for seed in seeds:
  for arm in ARMS:
   torch.manual_seed(seed)
   W=torch.nn.Parameter(torch.randn(3,dim,dim,dtype=torch.double));b=torch.nn.Parameter(torch.randn(3,dim,dtype=torch.double))
   v=torch.nn.Parameter(torch.randn(dim,dtype=torch.double));c=torch.nn.Parameter(torch.randn((),dtype=torch.double))
   opt=torch.optim.Adam([W,b,v,c],lr=.03)
   for epoch in range(201):
    h=torch.tensor([.5,-.5,.25]+([.125] if dim==4 else []),dtype=torch.double).repeat(729,1)
    zs=[];sat=[]
    for j in range(6):
     h=torch.clamp(torch.einsum('nij,nj->ni',W[x[:,j]],h)+b[x[:,j]],-1,1)
     zs.append(h@v+c);sat.append(h.abs().mean())
    z=torch.stack(zs,dim=1);bce=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
    if arm=='saturation':loss=bce+.1*(1-torch.stack(sat).mean())
    elif arm=='confidence':loss=bce+.1*torch.nn.functional.softplus(-z.abs()).mean()
    else:loss=bce
    if epoch in (0,50,100,200):
     p=dict(W=W.detach().tolist(),b=b.detach().tolist(),v=v.detach().tolist(),c=float(c.detach()))
     rows.append(dict(dim=dim,seed=seed,arm=arm,epoch=epoch,train_accuracy=float(((z>0)==(y>.5)).double().mean().detach()),mean_abs_h=float(torch.stack(sat).mean().detach()),bce=float(bce.detach()),params=p))
    if epoch==200:break
    opt.zero_grad();loss.backward();opt.step()
   print('trained',dim,seed,arm,flush=True)
   (R/'CHECKPOINTS.json').write_text(json.dumps(dict(rows=rows,torch=torch.__version__),indent=2)+'\n')
