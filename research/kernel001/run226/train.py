"""Run220 deterministic training: frozen 24-seed 3D tanh RNN."""
import json
from pathlib import Path
import torch
SEEDS=(1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483)
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
x=torch.tensor([[(n//3**(5-j))%3 for j in range(6)] for n in range(729)],dtype=torch.long)
q=torch.zeros(729,dtype=torch.long)
ys=[]
for j in range(6):
    q=torch.where(x[:,j]==2,0,q^(x[:,j]==1).long())
    ys.append(q.clone())
y=torch.stack(ys,dim=1).double()
rows=[]
for seed in SEEDS:
    torch.manual_seed(seed)
    W=torch.nn.Parameter(torch.randn(3,3,3,dtype=torch.double))
    b=torch.nn.Parameter(torch.randn(3,3,dtype=torch.double))
    v=torch.nn.Parameter(torch.randn(3,dtype=torch.double))
    c=torch.nn.Parameter(torch.randn((),dtype=torch.double))
    opt=torch.optim.Adam([W,b,v,c],lr=.03)
    for epoch in range(201):
        h=torch.tensor([.5,-.5,.25],dtype=torch.double).repeat(729,1)
        zs=[]
        for j in range(6):
            h=torch.tanh(torch.einsum('nij,nj->ni',W[x[:,j]],h)+b[x[:,j]])
            zs.append(h@v+c)
        z=torch.stack(zs,dim=1)
        loss=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
        if epoch in (0,50,100,200):
            p=dict(W=W.detach().tolist(),b=b.detach().tolist(),v=v.detach().tolist(),c=float(c.detach()))
            rows.append(dict(seed=seed,epoch=epoch,loss=float(loss.detach()),train_accuracy=float(((z>0)==(y>.5)).double().mean().detach()),params=p))
        if epoch==200:break
        opt.zero_grad();loss.backward();opt.step()
    print(seed,rows[-1]['train_accuracy'],flush=True)
Path('RUN220_CHECKPOINTS.json').write_text(json.dumps(dict(seeds=SEEDS,epochs=(0,50,100,200),rows=rows,architecture='fully coupled 3D tanh',torch=torch.__version__),indent=2)+'\n')
