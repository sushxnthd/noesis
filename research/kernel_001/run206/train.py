"""NOESIS Run206 frozen reset-parity training. No user hardware required."""
import json, time
from pathlib import Path
import numpy as np
import torch
import torch.nn.functional as F
R=Path(__file__).resolve().parent
SEEDS=(331,337,347,349)
EPOCHS=(0,20,50,100,200,400,800)
torch.set_num_threads(1)
torch.use_deterministic_algorithms(True)
def words():
    return torch.tensor([[(n//(3**(5-j)))%3 for j in range(6)] for n in range(729)],dtype=torch.long)
def targets(x):
    p=torch.zeros(len(x),dtype=torch.long);out=[]
    for t in range(x.shape[1]):
        p=torch.where(x[:,t]==2,0,p^(x[:,t]==1).long())
        out.append(p.clone())
    return torch.stack(out,dim=1).double()
def evaluate(row,length,nseq,seed):
    rng=np.random.default_rng(seed);x=rng.integers(0,3,size=(nseq,length),dtype=np.int64)
    p=row['params'];h=np.full(nseq,.5,dtype=np.float64);state=np.zeros(nseq,dtype=np.int64)
    errors=0;first=None
    for j in range(length):
        tok=x[:,j];h=np.tanh(np.take(p['w'],tok)*h+np.take(p['b'],tok))
        state=np.where(tok==2,0,state^(tok==1))
        e=int(np.count_nonzero((p['v']*h+p['c']>0)!=state));errors+=e
        if e and first is None:first=j+1
    return {'length':length,'nseq':nseq,'errors':errors,'first_error_length':first}
def train(seed):
    torch.manual_seed(seed)
    w=torch.nn.Parameter(torch.randn(3,dtype=torch.float64));b=torch.nn.Parameter(torch.randn(3,dtype=torch.float64))
    v=torch.nn.Parameter(torch.randn((),dtype=torch.float64));c=torch.nn.Parameter(torch.randn((),dtype=torch.float64))
    opt=torch.optim.Adam([w,b,v,c],lr=.03)
    x=words();target=targets(x)
    def loss():
        h=torch.full((len(x),),.5,dtype=torch.float64);logits=[]
        for j in range(6):
            h=torch.tanh(w[x[:,j]]*h+b[x[:,j]])
            logits.append(v*h+c)
        z=torch.stack(logits,dim=1)
        return F.binary_cross_entropy_with_logits(z,target),float(((z>0)==(target>.5)).double().mean())
    def snapshot(epoch):
        with torch.no_grad():
            lv,acc=loss()
            p={'w':[float(a) for a in w],'b':[float(a) for a in b],'v':float(v),'c':float(c)}
        r={'seed':seed,'epoch':epoch,'loss':float(lv),'train_accuracy':acc,'params':p}
        r['heldout64']=evaluate(r,64,128,seed+100000)
        r['heldout256']=evaluate(r,256,32,seed+200000)
        return r
    out=[snapshot(0)]
    for epoch in range(1,801):
        opt.zero_grad();lv,_=loss();lv.backward();opt.step()
        if epoch in EPOCHS:out.append(snapshot(epoch))
    return out
if __name__=='__main__':
    start=time.time();rows=[]
    for seed in SEEDS:
        rr=train(seed);rows+=rr
        print(seed,'end train',rr[-1]['train_accuracy'],'heldout256 errors',rr[-1]['heldout256']['errors'],flush=True)
    result={'architecture':'scalar input-gated tanh RNN','task':'resettable parity','seeds':SEEDS,'epochs':EPOCHS,'optimizer':'Adam lr=0.03 800 steps','train_words':729,'train_length':6,'torch':torch.__version__,'rows':rows,'seconds':time.time()-start}
    (R/'CHECKPOINTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('elapsed',result['seconds'])
