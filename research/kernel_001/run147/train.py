import itertools,torch,json
from pathlib import Path
torch.set_num_threads(1)
def train(seed):
 torch.manual_seed(seed);d=4
 A=torch.nn.Parameter(torch.eye(d)*.75+torch.randn(d,d)*.17)
 E=torch.nn.Parameter(torch.randn(3,d)*.4)
 w=torch.nn.Parameter(torch.randn(d)*.35+.5)
 x=torch.tensor(list(itertools.product(range(3),repeat=6)))
 q=torch.zeros(len(x));ys=[]
 for t in range(6):
  q=(q+torch.tensor([1.,-1.,0.])[x[:,t]]).clamp(min=0);ys.append(q.clone())
 opt=torch.optim.Adam([A,E,w],lr=.025)
 for _ in range(1200):
  opt.zero_grad();h=torch.zeros(len(x),d);loss=0
  for t in range(6):
   h=torch.relu(h@A.T+E[x[:,t]]);loss=loss+((h@w-ys[t])**2).mean()/6
  loss.backward();opt.step()
 return dict(seed=seed,A=A.detach().tolist(),E=E.detach().tolist(),w=w.detach().tolist())
