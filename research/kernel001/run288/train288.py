import itertools,json,hashlib,torch
from pathlib import Path
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
S=list(range(20928,21184));T=6;X=[];Y=[];init=[]
for seed in S:
 g=torch.Generator().manual_seed(seed)
 x=torch.cat([torch.randint(0,2,(160,T),generator=g),torch.tensor([list(w)+[0]*4 for w in itertools.product(range(2),repeat=2)])])
 q=torch.zeros(len(x),dtype=torch.long);ys=[]
 for t in range(T):
  q=torch.where(x[:,t]==0,0,1-q);ys.append(q.clone())
 X.append(x);Y.append(torch.stack(ys,1).double())
 init.append(torch.randn(15,generator=torch.Generator().manual_seed(seed+51000),dtype=torch.float64)*.5)
X=torch.stack(X);Y=torch.stack(Y);N=len(S)
p=torch.nn.Parameter(torch.stack(init));o=torch.optim.Adam([p],lr=.025);rows=[]
for epoch in range(121):
 a=p[:,:8].reshape(N,2,2,2);b=p[:,8:12].reshape(N,2,2);v=p[:,12:14];c=p[:,14]
 h=torch.zeros((N,X.shape[1],2),dtype=torch.float64);zs=[]
 for t in range(T):
  symbol=X[:,:,t];ii=torch.arange(N)[:,None]
  h=torch.relu(torch.einsum('nmij,nmj->nmi',a[ii,symbol],h)+b[ii,symbol])
  zs.append((h*v[:,None,:]).sum(-1)+c[:,None])
 z=torch.stack(zs,2);loss=torch.nn.functional.binary_cross_entropy_with_logits(z,Y,reduction='none').mean((1,2))
 acc=((z>0)==(Y>.5)).double().mean((1,2))
 if epoch in (0,20,40,80,120):
  for k,seed in enumerate(S):rows.append(dict(seed=seed,epoch=epoch,accuracy=float(acc[k].detach()),bce=float(loss[k].detach()),p=p[k].detach().tolist()))
 if epoch<120:o.zero_grad();loss.sum().backward();o.step()
data=dict(config=dict(seeds=S,length=T,random_sequences=160,enumerated_prefixes=4,epochs=120,snapshots=[0,20,40,80,120],lr=.025,dtype='float64',torch=torch.__version__,width=2,init_sigma=.5),rows=rows)
blob=json.dumps(data,sort_keys=True,separators=(',',':'))+'\n'
Path('checkpoints288.json').write_text(blob)
print(hashlib.sha256(blob.encode()).hexdigest())

torch.save({'optimizer':o.state_dict(),'parameters':p.detach().clone(),'config':data['config']},Path('optimizer288.pt'))
