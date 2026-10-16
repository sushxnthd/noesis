import torch
import torch.nn.functional as F
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
X=torch.tensor([[(n>>(5-j))&1 for j in range(6)] for n in range(64)])
Y=(torch.cumsum(X,1)%2).double()
def train(seed):
 torch.manual_seed(seed)
 w=torch.nn.Parameter(torch.randn(2,dtype=torch.float64));b=torch.nn.Parameter(torch.randn(2,dtype=torch.float64))
 v=torch.nn.Parameter(torch.randn((),dtype=torch.float64));c=torch.nn.Parameter(torch.randn((),dtype=torch.float64))
 opt=torch.optim.Adam([w,b,v,c],lr=.03)
 def loss():
  h=torch.full((64,),.5,dtype=torch.float64);z=[]
  for t in range(6):
   h=torch.tanh(w[X[:,t]]*h+b[X[:,t]]);z.append(v*h+c)
  q=torch.stack(z,1)
  return F.binary_cross_entropy_with_logits(q,Y),float(((q>0)==(Y>.5)).double().mean())
 return w,b,v,c,opt,loss
