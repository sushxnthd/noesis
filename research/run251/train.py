import json,time,torch
from pathlib import Path
R=Path(__file__).resolve().parent
SEEDS=list(range(13001,13049)); EPOCHS=(0,50,100,200)
torch.set_num_threads(1); torch.use_deterministic_algorithms(True)
x=torch.tensor([[(n//3**(4-j))%3 for j in range(5)] for n in range(243)],dtype=torch.long)
q=torch.zeros(243,dtype=torch.long); ys=[]
for j in range(5):
 q=torch.where(x[:,j]==2,0,torch.where(x[:,j]==1,1-q,q));ys.append(q.clone())
y=torch.stack(ys,dim=1).double()
rows=[]; start=time.time()
for seed in SEEDS:
 torch.manual_seed(seed)
 A=torch.nn.Parameter(torch.randn(4,4,dtype=torch.double)*.25)
 E=torch.nn.Parameter(torch.randn(3,4,dtype=torch.double)*.3)
 b=torch.nn.Parameter(torch.zeros(4,dtype=torch.double))
 v=torch.nn.Parameter(torch.randn(4,dtype=torch.double)*.3)
 c=torch.nn.Parameter(torch.zeros((),dtype=torch.double))
 opt=torch.optim.Adam([A,E,b,v,c],lr=.03)
 for epoch in range(201):
  h=torch.zeros((243,4),dtype=torch.double);zs=[]
  for j in range(5):
   h=torch.relu(h@A.T+E[x[:,j]]+b)
   zs.append(h@v+c)
  z=torch.stack(zs,dim=1)
  bce=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
  if epoch in EPOCHS:
   rows.append({'seed':seed,'epoch':epoch,'train_accuracy':float(((z>0)==(y>.5)).double().mean().detach()),'bce':float(bce.detach()),'params':{'A':A.detach().tolist(),'E':E.detach().tolist(),'b':b.detach().tolist(),'v':v.detach().tolist(),'c':float(c.detach())}})
  if epoch==200:break
  opt.zero_grad();bce.backward();opt.step()
 print('TRAIN',seed,'accuracy',rows[-1]['train_accuracy'],'seconds',round(time.time()-start,2),flush=True)
 (R/'CHECKPOINTS.json').write_text(json.dumps({'protocol':'run251 frozen reset-parity switching cohort','torch':torch.__version__,'seeds':SEEDS,'epochs':EPOCHS,'rows':rows},indent=2)+'\n')
