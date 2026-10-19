"""NOESIS K001 run270: paired gradient-trained input-gated latch experiment."""
import json, time, hashlib, itertools
from pathlib import Path
import torch
ROOT=Path(__file__).resolve().parent
D=torch.float64
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
SEEDS=list(range(19000,19024)); N=len(SEEDS); EPOCHS=500; BASE_N=256; T=20; LAMBDA=.2
seqs=[]; tgts=[]; starts=[]
for seed in SEEDS:
    g=torch.Generator().manual_seed(seed)
    x=torch.randint(0,3,(BASE_N,T),generator=g)
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
X=torch.stack(seqs).repeat(2,1,1);Y=torch.stack(tgts).repeat(2,1,1)
A=torch.nn.Parameter(torch.stack([s[0] for s in starts]*2))
B=torch.nn.Parameter(torch.stack([s[1] for s in starts]*2))
V=torch.nn.Parameter(torch.stack([s[2] for s in starts]*2))
C=torch.nn.Parameter(torch.stack([s[3] for s in starts]*2))
opt=torch.optim.Adam([A,B,V,C],lr=.03);idx=torch.arange(2*N)[:,None];rows=[];ts=time.time()
for epoch in range(EPOCHS+1):
    h=torch.zeros((2*N,X.shape[1]),dtype=D);logits=[];states=[]
    for t in range(T):
        x=X[:,:,t];h=torch.relu(A[idx,x]*h+B[idx,x]);states.append(h)
        logits.append(V[:,None]*h+C[:,None])
    Z=torch.stack(logits,dim=2)
    bce=torch.nn.functional.binary_cross_entropy_with_logits(Z,Y,reduction='none').mean((1,2))
    if epoch in (0,100,300,500):
        for k in range(2*N):
            rows.append({'seed':SEEDS[k%N],'arm':'control' if k<N else 'amplification',
                         'epoch':epoch,'train_accuracy':float(((Z[k]>0)==(Y[k]>.5)).to(D).mean().detach()),
                         'train_bce':float(bce[k].detach()),
                         'params':{'a':A[k].detach().tolist(),'b':B[k].detach().tolist(),
                                   'v':float(V[k].detach()),'c':float(C[k].detach())}})
        print('epoch',epoch,'perfect_control',sum(r['train_accuracy']==1 for r in rows if r['epoch']==epoch and r['arm']=='control'),
              'perfect_amplification',sum(r['train_accuracy']==1 for r in rows if r['epoch']==epoch and r['arm']=='amplification'),
              'seconds',round(time.time()-ts,1),flush=True)
    if epoch==EPOCHS:break
    sample_h=torch.stack(states[3::4],dim=2).detach()
    scale=torch.ones((2*N,4),dtype=D);scale[N:,:]=torch.tensor([2.,4.,8.,16.],dtype=D)
    amplified=sample_h[:,:,:,None]*scale[:,None,None,:]
    reset=torch.relu(A[:,2,None,None,None]*amplified+B[:,2,None,None,None])
    set_=torch.relu(A[:,1,None,None,None]*amplified+B[:,1,None,None,None])
    zr=V[:,None,None,None]*reset+C[:,None,None,None]
    zs=V[:,None,None,None]*set_+C[:,None,None,None]
    aux=(torch.nn.functional.softplus(zr)+torch.nn.functional.softplus(-zs)).mean((1,2,3))
    loss=(bce+LAMBDA*aux).sum()
    opt.zero_grad();loss.backward();torch.nn.utils.clip_grad_norm_([A,B,V,C],10.0);opt.step()
out={'schema':'noesis_run270','torch':torch.__version__,'seeds':SEEDS,'config':{'epochs':EPOCHS,'base_n':BASE_N,'T':T,'lr':.03,'aux_weight':LAMBDA,'scale_control':[1,1,1,1],'scale_intervention':[2,4,8,16],'dtype':'float64'},'rows':rows}
path=ROOT/'checkpoints.json';path.write_text(json.dumps(out,indent=2)+'\n')
print('sha256',hashlib.sha256(path.read_bytes()).hexdigest(),'elapsed',round(time.time()-ts,1))
