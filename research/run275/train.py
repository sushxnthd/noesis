"""Deterministic Run275 training reproduction, 128 new BCE-only seeds, epochs 0..200.
Produces raw checkpoints_phase1.json; requires torch CPU, numpy-free.
Frozen protocol also requested 500 epochs; 201..500 extension remains pending.
"""
import torch,itertools,json,hashlib
from pathlib import Path
D=torch.float64;torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
SEEDS=range(19500,19628);T=20;SNAPSHOTS=(0,10,20,30,40,50,75,100,150,200)
seqs=[];tgts=[];starts=[]
for seed in SEEDS:
 g=torch.Generator().manual_seed(seed)
 x=torch.randint(0,3,(256,T),generator=g)
 short=torch.tensor([list(w)+[0]*(T-3) for w in itertools.product(range(3),repeat=3)],dtype=torch.long)
 x=torch.cat([x,short]);q=torch.zeros(len(x),dtype=torch.long);targets=[]
 for t in range(T):
  q=torch.where(x[:,t]==1,1,torch.where(x[:,t]==2,0,q))
  targets.append(q.clone())
 seqs.append(x);tgts.append(torch.stack(targets,dim=1).to(D))
 g=torch.Generator().manual_seed(seed+13000)
 starts.append((torch.randn(3,generator=g,dtype=D)*.25+.1,
                torch.randn(3,generator=g,dtype=D)*.25,
                torch.randn((),generator=g,dtype=D)*.3,
                torch.randn((),generator=g,dtype=D)*.3))
X=torch.stack(seqs);Y=torch.stack(tgts);N=len(SEEDS);idx=torch.arange(N)[:,None]
A=torch.nn.Parameter(torch.stack([s[0] for s in starts]))
B=torch.nn.Parameter(torch.stack([s[1] for s in starts]))
V=torch.nn.Parameter(torch.stack([s[2] for s in starts]))
C=torch.nn.Parameter(torch.stack([s[3] for s in starts]))
opt=torch.optim.Adam([A,B,V,C],lr=.03)
rows=[]
for epoch in range(201):
 h=torch.zeros((N,X.shape[1]),dtype=D);logits=[]
 for t in range(T):
  x=X[:,:,t];h=torch.relu(A[idx,x]*h+B[idx,x]);logits.append(V[:,None]*h+C[:,None])
 Z=torch.stack(logits,dim=2)
 bce=torch.nn.functional.binary_cross_entropy_with_logits(Z,Y,reduction="none").mean((1,2))
 acc=((Z>0)==(Y>.5)).to(D).mean((1,2))
 if epoch in SNAPSHOTS:
  for k,seed in enumerate(SEEDS):
   rows.append({"seed":seed,"epoch":epoch,"train_accuracy":float(acc[k].detach()),
      "train_bce":float(bce[k].detach()),"params":{"a":A[k].detach().tolist(),
      "b":B[k].detach().tolist(),"v":float(V[k].detach()),"c":float(C[k].detach())}})
  print(epoch,int((acc==1).sum()),flush=True)
 if epoch<200:
  opt.zero_grad();bce.sum().backward();opt.step()
path=Path(__file__).parent/"checkpoints_phase1.json"
blob=json.dumps({"schema":"noesis_run275","config":{"seeds":list(SEEDS),"epochs":500,
 "snapshots":list(SNAPSHOTS),"samples_per_seed":283,"length":20,"lr":.03,
 "dtype":"float64","regularizer":"none","torch":torch.__version__},
 "rows":rows},separators=(",",":"))+"\n"
path.write_text(blob)
print("SHA256",hashlib.sha256(blob.encode()).hexdigest())
