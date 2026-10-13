"""NOESIS kernel 001: two-ReLU recurrent cap spoof and training control."""
import itertools, json
def target_step(h,x): return max(0,h+x)
def neural_step(h,x,M):
    z=h+x
    return max(0,z)-max(0,z-M)
def exact_enumeration(M):
    count=0
    for n in range(M+1):
        for w in itertools.product((-1,1),repeat=n):
            t=s=0
            for x in w:
                t=target_step(t,x); s=neural_step(s,x,M)
            assert t==s,(M,w)
            count+=1
    t=s=0
    for x in (1,)*(M+1):
        t=target_step(t,x); s=neural_step(s,x,M)
    assert (t,s)==(M+1,M)
    return dict(cap=M,enumerated_sequences=count,shortest_failure_length=M+1,witness="+"*(M+1),target=t,spoof=s)
def train_control(seed,horizon=6,cap=12.,steps=350):
    import torch,numpy as np
    torch.set_num_threads(1); torch.manual_seed(seed)
    dtype=torch.float64
    words=list(itertools.product((-1,1),repeat=horizon))
    x=torch.tensor(words,dtype=dtype)
    targets=[]
    for w in words:
        h=0; row=[]
        for v in w:
            h=target_step(h,v);row.append(h)
        targets.append(row)
    y=torch.tensor(targets,dtype=dtype)
    bp=torch.nn.Parameter(torch.tensor(.8+.4*torch.rand((),dtype=dtype).item(),dtype=dtype))
    bm=torch.nn.Parameter(torch.tensor(-1.2+.4*torch.rand((),dtype=dtype).item(),dtype=dtype))
    m=torch.nn.Parameter(torch.tensor(cap,dtype=dtype))
    opt=torch.optim.Adam([bp,bm,m],lr=.05)
    max_cap_grad=0.
    for _ in range(steps):
        opt.zero_grad(set_to_none=True)
        h=torch.zeros(len(words),dtype=dtype);out=[]
        for t in range(horizon):
            z=h+torch.where(x[:,t]>0,bp,bm)
            h=torch.relu(z)-torch.relu(z-m)
            out.append(h)
        loss=((torch.stack(out,dim=1)-y)**2).mean()
        loss.backward()
        max_cap_grad=max(max_cap_grad,abs(float(m.grad)))
        opt.step()
    p,q,M=map(lambda z:float(z.detach()),(bp,bm,m))
    hidden=np.array([0.]); symbolic=np.array([0],dtype=np.int64)
    first_bad=None; tested=0
    for length in range(1,15):
        a=hidden+q;b=hidden+p
        hidden=np.concatenate([np.maximum(a,0)-np.maximum(a-M,0),np.maximum(b,0)-np.maximum(b-M,0)])
        symbolic=np.concatenate([np.maximum(symbolic-1,0),symbolic+1])
        tested+=len(hidden)
        if np.any(np.abs(hidden-symbolic)>=.5):
            first_bad=length;break
    return dict(seed=seed,initial_cap=cap,final_cap=M,max_cap_gradient=max_cap_grad,
        learned_plus=p,learned_minus=q,train_mse=float(loss.detach()),
        first_bad_length_le_14=first_bad,tested_sequences=tested,
        train_prefixes_exact=float(loss.detach())<1e-9)
if __name__=="__main__":
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument("--train",action="store_true");args=ap.parse_args()
    data={"exact":[exact_enumeration(m) for m in range(1,9)]}
    if args.train:data["training"]=[train_control(s) for s in range(8)]
    print(json.dumps(data,indent=2,sort_keys=True))
