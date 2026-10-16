import torch,json,numpy as np,sys
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
SEEDS=(751,757,761,769,773,787,797,809)
x=torch.tensor([[(n//3**(5-j))%3 for j in range(6)] for n in range(729)])
q=torch.zeros(729,dtype=torch.long);ys=[]
for j in range(6):
 q=torch.where(x[:,j]==2,0,q^(x[:,j]==1).long());ys.append(q.clone())
y=torch.stack(ys,dim=1).double()
rows=[]
for seed in SEEDS:
 torch.manual_seed(seed)
 W=torch.nn.Parameter(torch.randn(3,2,2,dtype=torch.double));b=torch.nn.Parameter(torch.randn(3,2,dtype=torch.double))
 v=torch.nn.Parameter(torch.randn(2,dtype=torch.double));c=torch.nn.Parameter(torch.randn((),dtype=torch.double))
 opt=torch.optim.Adam([W,b,v,c],lr=.03)
 for epoch in range(801):
  h=torch.tensor([.5,-.5],dtype=torch.double).repeat(729,1);zs=[]
  for j in range(6):
   h=torch.tanh(torch.einsum('nij,nj->ni',W[x[:,j]],h)+b[x[:,j]])
   zs.append(h@v+c)
  z=torch.stack(zs,dim=1)
  loss=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
  if epoch in (0,50,100,200,400,800):
   rows.append(dict(seed=seed,epoch=epoch,loss=float(loss.detach()),train_accuracy=float(((z>0)==(y>.5)).double().mean().detach()),params=dict(W=W.detach().tolist(),b=b.detach().tolist(),v=v.detach().tolist(),c=float(c.detach()))))
  if epoch==800:break
  opt.zero_grad();loss.backward();opt.step()
 print(seed,rows[-1]['train_accuracy'],flush=True)
 open(sys.argv[1] if len(sys.argv)>1 else 'RUN210_CHECKPOINTS.json','w').write(json.dumps(dict(seeds=SEEDS,rows=rows,torch=torch.__version__),indent=2)+'\n')
