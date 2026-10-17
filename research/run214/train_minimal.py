import torch,json,numpy as np
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
SEEDS=(953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171)
x=torch.tensor([[(n//3**(5-j))%3 for j in range(6)] for n in range(729)])
q=torch.zeros(729,dtype=torch.long);ys=[]
for j in range(6):
 q=torch.where(x[:,j]==2,0,q^(x[:,j]==1).long());ys.append(q.clone())
y=torch.stack(ys,1).double();rows=[]
for seed in SEEDS:
 torch.manual_seed(seed)
 W=torch.nn.Parameter(torch.randn(3,2,2,dtype=torch.double));b=torch.nn.Parameter(torch.randn(3,2,dtype=torch.double))
 v=torch.nn.Parameter(torch.randn(2,dtype=torch.double));c=torch.nn.Parameter(torch.randn((),dtype=torch.double))
 opt=torch.optim.Adam([W,b,v,c],lr=.03)
 for epoch in range(201):
  h=torch.tensor([.5,-.5],dtype=torch.double).repeat(729,1);z=[]
  for j in range(6):
   h=torch.tanh(torch.einsum('nij,nj->ni',W[x[:,j]],h)+b[x[:,j]]);z.append(h@v+c)
  z=torch.stack(z,1);loss=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
  if epoch in (0,50,100,200):
   rows.append(dict(seed=seed,epoch=epoch,loss=float(loss.detach()),train_accuracy=float(((z>0)==(y>.5)).double().mean()),params=dict(W=W.detach().tolist(),b=b.detach().tolist(),v=v.detach().tolist(),c=float(c.detach()))))
  if epoch==200:break
  opt.zero_grad();loss.backward();opt.step()
json.dump(dict(seeds=SEEDS,rows=rows),open('RUN214_CHECKPOINTS.json','w'),indent=2)
