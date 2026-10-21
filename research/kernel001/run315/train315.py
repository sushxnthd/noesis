#!/usr/bin/env python3
"""Frozen Run315 gradient-trained persistent-latch cohort."""
import hashlib,itertools,json,math,time
from pathlib import Path
import numpy as np
import torch
ROOT=Path(__file__).resolve().parent
SEEDS=list(range(22600,22696))
W=3;T=6;N=len(SEEDS);D=torch.float64
torch.set_num_threads(1);torch.use_deterministic_algorithms(True)
def retention_score(p):
 p=np.asarray(p,dtype=np.float64)
 a=p[:18].reshape(2,3,3);b=p[18:24].reshape(2,3);w=p[24:27]
 h0=np.zeros(3,dtype=np.float64);h1=np.zeros(3,dtype=np.float64);ds={}
 with np.errstate(over='ignore',invalid='ignore'):
  for n in range(1,65):
   h0=np.maximum(0,a[0]@h0+b[0])
   h1=np.maximum(0,a[1 if n==1 else 0]@h1+b[1 if n==1 else 0])
   if n in (1,8,16,32,64):ds[n]=float(w@(h1-h0))
  if not all(math.isfinite(x) for x in ds.values()):return -1e300
  z=min(ds[n]/(1+abs(ds[1])) for n in (8,16,32,64))
  return float(z) if math.isfinite(z) else -1e300
def main():
 xs=[];ys=[];init=[]
 for seed in SEEDS:
  g=torch.Generator().manual_seed(seed);x=torch.randint(0,2,(160,T),generator=g)
  fixed=torch.tensor([list(w)+[0]*(T-2) for w in itertools.product((0,1),repeat=2)],dtype=torch.long)
  x=torch.cat([x,fixed]);q=torch.zeros(len(x),dtype=torch.long);targets=[]
  for t in range(T):
   q=torch.bitwise_or(q,x[:,t]);targets.append(q.clone())
  xs.append(x);ys.append(torch.stack(targets,dim=1).to(D))
  g=torch.Generator().manual_seed(seed+51000)
  init.append(torch.randn(28,generator=g,dtype=D)*.5)
 X=torch.stack(xs);Y=torch.stack(ys);params=torch.nn.Parameter(torch.stack(init))
 opt=torch.optim.Adam([params],lr=.025);rows=[]
 for epoch in range(81):
  a=params[:,:18].reshape(N,2,W,W);b=params[:,18:24].reshape(N,2,W)
  v=params[:,24:27];c=params[:,27]
  h=torch.zeros((N,X.shape[1],W),dtype=D);logits=[]
  for t in range(T):
   sym=X[:,:,t];ii=torch.arange(N)[:,None]
   h=torch.relu(torch.einsum('nmij,nmj->nmi',a[ii,sym],h)+b[ii,sym])
   logits.append((h*v[:,None,:]).sum(-1)+c[:,None])
  z=torch.stack(logits,dim=2)
  bce=torch.nn.functional.binary_cross_entropy_with_logits(z,Y,reduction='none').mean((1,2))
  acc=((z>0)==(Y>.5)).to(D).mean((1,2))
  if epoch in (0,20,80):
   for k,seed in enumerate(SEEDS):
    rows.append({'seed':seed,'epoch':epoch,'accuracy':float(acc[k].detach()),'bce':float(bce[k].detach()),'p':params[k].detach().tolist()})
   print('epoch',epoch,'sampled_perfect',int((acc==1).sum()),flush=True)
  if epoch<80:
   opt.zero_grad();bce.sum().backward();opt.step()
 raw={'config':{'seeds':SEEDS,'length':T,'random_sequences':160,'enumerated_prefixes':4,'epochs':80,'snapshots':[0,20,80],'lr':.025,'dtype':'float64','torch':torch.__version__,'width':W,'init_sigma':.5,'task':'persistent_latch'},'rows':rows}
 data=json.dumps(raw,sort_keys=True,separators=(',',':'))+'\n'
 (ROOT/'checkpoints315.json').write_text(data)
 early=[{'seed':r['seed'],'retention_score':retention_score(r['p']),'negative_bce':-r['bce'],'early_accuracy':r['accuracy']} for r in rows if r['epoch']==20]
 frozen=json.dumps(early,sort_keys=True,separators=(',',':'))+'\n'
 (ROOT/'FROZEN_EARLY_SCORES315.json').write_text(frozen)
 sha=hashlib.sha256(frozen.encode()).hexdigest()
 (ROOT/'EARLY_COMMITMENT315.md').write_text('# Frozen early-score commitment\n\nSHA256: `'+sha+'`\n\nEpoch80 endpoint adjudication must not be used to modify these scores.\n')
 print('EARLY_SCORES_SHA256',sha,'CHECKPOINTS_SHA256',hashlib.sha256(data.encode()).hexdigest(),flush=True)
if __name__=='__main__':main()
