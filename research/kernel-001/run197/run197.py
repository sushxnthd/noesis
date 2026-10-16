"""NOESIS Run197: frozen cross-task modulo-3 acquisition and certificate transfer.
Run197 PROTOCOL.md committed before running this file. Candidate interval boxes
are HEURISTIC; never call a positive certificate without independent_check.py.
"""
import argparse, hashlib, itertools, json, sys
from pathlib import Path
import numpy as np
import torch
SEEDS=(241,251,257,263)
CHECKPOINTS=(400,800)
TASKLEN=6
WIDTH=12

class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.W=torch.nn.Parameter(torch.randn(WIDTH,WIDTH,dtype=torch.float64)*.3)
        self.U=torch.nn.Parameter(torch.randn(2,WIDTH,dtype=torch.float64)*.3)
        self.b=torch.nn.Parameter(torch.zeros(WIDTH,dtype=torch.float64))
        self.V=torch.nn.Parameter(torch.randn(3,WIDTH,dtype=torch.float64)*.3)
        self.c=torch.nn.Parameter(torch.zeros(3,dtype=torch.float64))
    def forward(self,x):
        h=torch.zeros((len(x),WIDTH),dtype=torch.float64)
        outs=[]
        for t in range(x.shape[1]):
            h=torch.tanh(h@self.W.T+self.U[x[:,t]]+self.b)
            outs.append(h@self.V.T+self.c)
        return torch.stack(outs,dim=1)

def train(path):
    if path.exists(): raise RuntimeError('Refuse to overwrite frozen results')
    torch.set_num_threads(1)
    x=torch.tensor(list(itertools.product((0,1),repeat=TASKLEN)),dtype=torch.long)
    y=torch.cumsum(x,dim=1).remainder(3)
    rows=[]
    for seed in SEEDS:
        torch.manual_seed(seed)
        m=Net(); opt=torch.optim.Adam(m.parameters(),lr=.02)
        for step in range(1,801):
            opt.zero_grad();z=m(x)
            loss=torch.nn.functional.cross_entropy(z.reshape(-1,3),y.reshape(-1))
            loss.backward();opt.step()
            if step in CHECKPOINTS:
                with torch.no_grad():
                    z=m(x);ll=float(torch.nn.functional.cross_entropy(z.reshape(-1,3),y.reshape(-1)))
                    acc=float((z.argmax(-1)==y).double().mean())
                    rows.append({'seed':seed,'epoch':step,'loss':ll,'train_accuracy':acc,
                        'params':{k:v.detach().tolist() for k,v in m.named_parameters()}})
                    print('TRAIN',seed,step,ll,acc,flush=True)
    path.write_text(json.dumps({'torch':torch.__version__,'numpy':np.__version__,'rows':rows},indent=1)+'\n')

def advance(h,p,bit):
    return np.tanh(h@p['W'].T+p['U'][bit]+p['b'])

def logits(h,p):return h@p['V'].T+p['c']

def params(row):return {k:np.asarray(v,dtype=np.float64) for k,v in row['params'].items()}

def test_finite(p,seed,ep):
    results={}
    for n in (6,10):
        h=np.zeros((1,WIDTH));res=np.zeros(1,dtype=np.int16)
        for depth in range(n):
            h=np.concatenate((advance(h,p,0),advance(h,p,1)))
            res=np.concatenate((res,(res+1)%3))
        pred=logits(h,p).argmax(-1)
        results[f'length_{n}_all_prefix_correct'] = int((pred==res).sum())
        results[f'length_{n}_total']=len(res)
    rng=np.random.default_rng(197064)
    bits=rng.integers(0,2,size=(128,64),dtype=np.int8)
    h=np.zeros((128,WIDTH));res=np.zeros(128,dtype=np.int16)
    all_good=np.ones(128,dtype=bool)
    for t in range(64):
        for b in (0,1):
            ii=np.flatnonzero(bits[:,t]==b)
            if len(ii):h[ii]=advance(h[ii],p,b)
        res=(res+bits[:,t])%3
        all_good &= logits(h,p).argmax(-1)==res
    results['length_64_random_all_prefix_correct']=int(all_good.sum())
    results['length_64_total']=128
    return results

def synthesize(p,k,iterations=400):
    n=1<<k; mask=n-1; states=3*n
    h=np.zeros((1,WIDTH));res=np.zeros(1,dtype=np.int16);suf=np.zeros(1,dtype=np.int32)
    for depth in range(k+2):
        h=np.concatenate((advance(h,p,0),advance(h,p,1)))
        res=np.concatenate((res,(res+1)%3))
        suf=np.concatenate(((suf<<1)&mask,((suf<<1)|1)&mask))
    idx=res*n+suf
    lo=np.full((states,WIDTH),np.inf);hi=np.full((states,WIDTH),-np.inf)
    np.minimum.at(lo,idx,h);np.maximum.at(hi,idx,h)
    if not (np.isfinite(lo).all() and np.isfinite(hi).all()):
        return {'k':k,'reason':'uncovered_base_state','covered':int(np.isfinite(lo).all(axis=1).sum())},None
    grid=1e-10
    lo=np.floor((lo-1e-12)/grid)*grid
    hi=np.ceil((hi+1e-12)/grid)*grid
    Wpos=np.maximum(p['W'],0);Wneg=np.minimum(p['W'],0)
    inds=np.arange(states)
    target=[((inds//n+b)%3)*n+(((inds%n)*2+b)&mask) for b in (0,1)]
    closed=False
    for step in range(iterations):
        oldlo=lo.copy();oldhi=hi.copy()
        for bit in (0,1):
            lower=np.tanh(oldlo@Wpos.T+oldhi@Wneg.T+p['U'][bit]+p['b'])
            upper=np.tanh(oldhi@Wpos.T+oldlo@Wneg.T+p['U'][bit]+p['b'])
            np.minimum.at(lo,target[bit],np.floor((lower-1e-12)/grid)*grid)
            np.maximum.at(hi,target[bit],np.ceil((upper+1e-12)/grid)*grid)
        if np.array_equal(oldlo,lo) and np.array_equal(oldhi,hi):
            closed=True;break
    widths=(hi-lo).max(axis=1)
    # rigorous verifier, not this floating-point screen, decides positivity
    margins=[]
    for cls in range(3):
        low=lo[cls*n:(cls+1)*n];high=hi[cls*n:(cls+1)*n]
        for other in range(3):
            if other==cls:continue
            diff=p['V'][cls]-p['V'][other]
            margin=np.minimum(diff,0)@high.T+np.maximum(diff,0)@low.T+p['c'][cls]-p['c'][other]
            margins.append(float(margin.min()))
    minmargin=float(min(margins))
    report={'k':k,'closed_float_screen':closed,'steps':step+1,'max_box_width':float(widths.max()),
            'min_float_output_margin':minmargin,'candidate_only':True,
            'reason':'needs_independent_check' if closed and minmargin>1e-6 else 'abstain'}
    if closed and minmargin>1e-6:
        cert={'k':k,'lo':[[format(x,'.12f') for x in row] for row in lo],
                   'hi':[[format(x,'.12f') for x in row] for row in hi]}
        return report,cert
    return report,None

def evaluate(checkpoints,out):
    if out.exists():raise RuntimeError('Refuse to overwrite outcomes')
    obj=json.loads(checkpoints.read_text())
    report={'checkpoint_sha256':hashlib.sha256(checkpoints.read_bytes()).hexdigest(),
            'protocol':'research/kernel-001/run197/PROTOCOL.md','rows':[]}
    for row in obj['rows']:
        p=params(row)
        finite=test_finite(p,row['seed'],row['epoch'])
        tests=[]
        for k in (6,8):
            stat,cert=synthesize(p,k)
            tests.append(stat)
            if cert is not None:
                dest=out.parent/f"CANDIDATE_{row['seed']}_{row['epoch']}_k{k}.json"
                dest.write_text(json.dumps({'seed':row['seed'],'epoch':row['epoch'],'params':row['params'],**cert},indent=1)+'\n')
        report['rows'].append({'seed':row['seed'],'epoch':row['epoch'],'train_accuracy':row['train_accuracy'],
            'loss':row['loss'],'finite':finite,'certification_screens':tests})
        print('EVAL',row['seed'],row['epoch'],'finite',finite,'screens',tests,flush=True)
    out.write_text(json.dumps(report,indent=1)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('action',choices=('train','eval'));ap.add_argument('source');ap.add_argument('output',nargs='?')
    args=ap.parse_args()
    if args.action=='train':train(Path(args.source))
    else:evaluate(Path(args.source),Path(args.output))