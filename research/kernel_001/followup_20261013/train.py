"""Reproduce 16 frozen float64 CPU training runs (torch required).
Writes a separate file; never overwrites frozen raw outcomes.
"""
import csv,itertools,pathlib
import torch
ROOT=pathlib.Path(__file__).resolve().parent
def train(seed):
    torch.set_num_threads(1);torch.manual_seed(seed)
    d=torch.float64
    p=torch.nn.Parameter(0.05+2.4*torch.rand((),dtype=d))
    q=torch.nn.Parameter(-2.45+2.4*torch.rand((),dtype=d))
    cap=torch.nn.Parameter(torch.tensor(16.,dtype=d))
    p0,q0=float(p.detach()),float(q.detach())
    x=torch.tensor(list(itertools.product((-1.,1.),repeat=6)),dtype=d)
    target=[]
    for word in x.tolist():
        h=0;states=[]
        for s in word:
            h=max(0,h+int(s));states.append(h)
        target.append(states)
    target=torch.tensor(target,dtype=d)
    opt=torch.optim.Adam([p,q,cap],lr=.05);max_cap_grad=0.
    for _ in range(350):
        opt.zero_grad(set_to_none=True)
        h=torch.zeros(len(x),dtype=d);seq=[]
        for t in range(6):
            z=h+torch.where(x[:,t]>0,p,q)
            h=torch.relu(z)-torch.relu(z-cap)
            seq.append(h)
        loss=((torch.stack(seq,dim=1)-target)**2).mean()
        loss.backward()
        max_cap_grad=max(max_cap_grad,abs(float(cap.grad.detach())))
        opt.step()
    return [seed,p0,q0,float(p.detach()),float(q.detach()),float(loss.detach()),float(cap.detach()),max_cap_grad]
if __name__=='__main__':
    with (ROOT/'RERUN_OUTCOMES.csv').open('w',newline='') as f:
        w=csv.writer(f)
        w.writerow('seed initial_plus initial_minus final_plus final_minus final_train_mse final_cap max_abs_cap_gradient'.split())
        for seed in range(100,116):w.writerow(train(seed))
