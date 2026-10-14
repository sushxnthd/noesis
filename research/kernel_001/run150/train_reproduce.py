"""Deterministic paired training for NOESIS run150; torch CPU, 1 thread."""
import itertools,json,sys
from pathlib import Path
import torch
P=Path(__file__).resolve().parent
torch.set_num_threads(1)
x=torch.tensor(list(itertools.product(range(3),repeat=6)),dtype=torch.long)
target=torch.zeros(729,6);q=torch.zeros(729);d=torch.tensor([1.,-1.,0.])
for t in range(6):
 q=(q+d[x[:,t]]).clamp(min=0);target[:,t]=q

def train(seed,variant):
 torch.manual_seed(seed)
 a0=torch.eye(4)*.75+torch.randn(4,4)*.17
 e0=torch.randn(3,4)*.4
 w0=torch.randn(4)*.35+.5
 A=torch.nn.Parameter(a0.clone());E=torch.nn.Parameter(e0.clone());w=torch.nn.Parameter(w0.clone())
 opt=torch.optim.Adam([A,E,w],lr=.025)
 for _ in range(1200):
  opt.zero_grad();h=torch.zeros(729,4);loss=torch.zeros(());reg=torch.zeros(())
  for t in range(6):
   h=torch.relu(h@A.T+E[x[:,t]])
   loss=loss+((h@w-target[:,t])**2).mean()/6
   if variant!='baseline':
    h2=torch.relu(h@A.T+E[2]);diff=h2-h
    reg=reg+((diff**2).sum(dim=1).mean() if variant=='latent' else ((diff@w)**2).mean())/6
  (loss+(.1*reg if variant!='baseline' else 0)).backward();opt.step()
 with torch.no_grad():
  h=torch.zeros(729,4);mse=0.
  for t in range(6):
   h=torch.relu(h@A.T+E[x[:,t]]);mse+=float(((h@w-target[:,t])**2).mean())/6
 return dict(seed=seed,variant=variant,train_mse=mse,parameters=dict(A=A.detach().tolist(),E=E.detach().tolist(),w=w.detach().tolist()),initial=dict(A=a0.tolist(),E=e0.tolist(),w=w0.tolist()))

if __name__=='__main__':
 rows=[train(s,v) for s in range(208,216) for v in ('baseline','latent','output')]
 (P/'CHECKPOINTS.json').write_text(json.dumps(rows,indent=2)+'\n')
 print('saved',len(rows),'trained checkpoints')
