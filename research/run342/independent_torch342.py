import json,numpy as np,torch
from pathlib import Path
P=Path(__file__).resolve().parent
D=json.loads((P/'trajectories342.json').read_text())['rows']
out=json.loads((P/'outcomes342.json').read_text())['rows']
late={r['seed']:r for r in D if r['epoch']==200};N=len(out);W=4
p=np.array([late[r['seed']]['p'] for r in out])
a=torch.tensor(p[:,:32].reshape(N,2,W,W));b=torch.tensor(p[:,32:40].reshape(N,2,W))
v=torch.tensor(p[:,40:44]);c=torch.tensor(p[:,44]);h=torch.zeros((N,1,W),dtype=torch.float64)
par=np.array([0],dtype=np.int8);correct=np.ones(N,dtype=bool)
torch.set_num_threads(1)
for length in range(1,13):
 s0=torch.relu(torch.einsum('nij,nkj->nki',a[:,0],h)+b[:,None,0,:])
 s1=torch.relu(torch.einsum('nij,nkj->nki',a[:,1],h)+b[:,None,1,:])
 h=torch.stack((s0,s1),dim=2).reshape(N,-1,W)
 par=np.stack((par,1-par),axis=1).reshape(-1)
 z=(torch.einsum('nkj,nj->nk',h,v)+c[:,None]).numpy()
 correct&=~np.any((z>0)!=(par[None,:]==1),axis=1)
assert all(bool(correct[i])==r['correct_through_12'] for i,r in enumerate(out))
print('independent PyTorch vs NumPy endpoints agree',N)
