"""Frozen Run154 checkpoint generator. CPU only; no paid compute."""
import itertools,json,sys
from pathlib import Path
import torch
torch.set_num_threads(1)
P=Path(__file__).parent
x=torch.tensor(list(itertools.product(range(3),repeat=6)),dtype=torch.long)
target=torch.zeros(729,6);q=torch.zeros(729);d=torch.tensor([1.,-1.,0.])
for t in range(6):
 q=(q+d[x[:,t]]).clamp(min=0);target[:,t]=q
def train(seed,width):
 torch.manual_seed(seed)
 a0=torch.eye(width)*.75+torch.randn(width,width)*.17
 e0=torch.randn(3,width)*.4
 w0=torch.randn(width)*.35+.5
 A=torch.nn.Parameter(a0.clone());E=torch.nn.Parameter(e0.clone());w=torch.nn.Parameter(w0.clone())
 opt=torch.optim.Adam([A,E,w],lr=.025)
 for _ in range(1200):
  opt.zero_grad();h=torch.zeros(729,width);loss=torch.zeros(());reg=torch.zeros(())
  for t in range(6):
   h=torch.relu(h@A.T+E[x[:,t]])
   loss=loss+((h@w-target[:,t])**2).mean()/6
   h2=torch.relu(h@A.T+E[2]);reg=reg+((h2-h)**2).sum(dim=1).mean()/6
  (loss+.1*reg).backward();opt.step()
 with torch.no_grad():
  h=torch.zeros(729,width);mse=0.
  for t in range(6):
   h=torch.relu(h@A.T+E[x[:,t]]);mse+=float(((h@w-target[:,t])**2).mean())/6
 return dict(seed=seed,width=width,variant="latent",train_mse=mse,
  parameters=dict(A=A.detach().tolist(),E=E.detach().tolist(),w=w.detach().tolist()),
  initial=dict(A=a0.tolist(),E=e0.tolist(),w=w0.tolist()))
if __name__=="__main__":
 start=int(sys.argv[1]);stop=int(sys.argv[2])
 for seed in range(start,stop):
  width=4 if seed<224 else 5 if seed<232 else 6
  cp=train(seed,width)
  (P/f"CHECKPOINT_SEED_{seed}.json").write_text(json.dumps([cp],indent=2)+"\n")
  print(seed,width,cp["train_mse"],flush=True)
