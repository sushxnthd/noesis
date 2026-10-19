"""Run258 frozen independent-initialization cohort. Public CPU only."""
import json, hashlib, time
from pathlib import Path
import torch
P=Path(__file__).resolve().parent
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
seq=torch.tensor([[(n//3**(4-j))%3 for j in range(5)] for n in range(243)],dtype=torch.long)
q=torch.zeros(243,dtype=torch.long); ys=[]
for j in range(5):
    q=torch.where(seq[:,j]==2,0,torch.where(seq[:,j]==1,1-q,q))
    ys.append(q.clone())
y=torch.stack(ys,dim=1).double()
rows=[];start=time.time()
for seed in range(17001,17065):
    torch.manual_seed(seed)
    A=torch.nn.Parameter(torch.randn(4,4,dtype=torch.double)*.25)
    E=torch.nn.Parameter(torch.randn(3,4,dtype=torch.double)*.3)
    b=torch.nn.Parameter(torch.zeros(4,dtype=torch.double))
    v=torch.nn.Parameter(torch.randn(4,dtype=torch.double)*.3)
    c=torch.nn.Parameter(torch.zeros((),dtype=torch.double))
    opt=torch.optim.Adam([A,E,b,v,c],lr=.03)
    for epoch in range(201):
        h=torch.zeros((243,4),dtype=torch.double); zs=[]
        for j in range(5):
            h=torch.relu(h@A.T+E[seq[:,j]]+b)
            zs.append(h@v+c)
        z=torch.stack(zs,dim=1)
        loss=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
        if epoch in (0,50,100,200):
            rows.append({'task':'parity','seed':seed,'epoch':epoch,
              'train_accuracy':float(((z>0)==(y>.5)).double().mean().detach()),
              'loss':float(loss.detach()),'params':{
              'A':A.detach().tolist(),'E':E.detach().tolist(),
              'b':b.detach().tolist(),'v':v.detach().tolist(),
              'c':float(c.detach())}})
        if epoch==200:break
        opt.zero_grad();loss.backward();opt.step()
    print(seed,rows[-1]['train_accuracy'],round(time.time()-start,2),flush=True)
(P/'CHECKPOINTS.json').write_text(json.dumps({'torch':torch.__version__,'rows':rows},separators=(',',':'))+'\n')
print('sha256',hashlib.sha256((P/'CHECKPOINTS.json').read_bytes()).hexdigest())
