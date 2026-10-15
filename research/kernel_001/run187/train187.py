"""NOESIS run187: deterministic CPU gradient-trained parity RNN; no hardcoded transitions."""
from __future__ import annotations
import itertools,json,hashlib,sys,os
from pathlib import Path
import numpy as np
import torch
ROOT=Path(__file__).resolve().parent
SEEDS=(101,103,107,109)
STEPS=(0,100,300,600,1200)
N=8

def make_data():
    x=torch.tensor(list(itertools.product((0,1),repeat=6)),dtype=torch.long)
    y=torch.remainder(torch.cumsum(x,dim=1),2).to(torch.float64)
    return x,y

class RNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.W=torch.nn.Parameter(torch.randn(N,N,dtype=torch.float64)*0.3)
        self.U=torch.nn.Parameter(torch.randn(2,N,dtype=torch.float64)*0.3)
        self.b=torch.nn.Parameter(torch.zeros(N,dtype=torch.float64))
        self.v=torch.nn.Parameter(torch.randn(N,dtype=torch.float64)*0.3)
        self.c=torch.nn.Parameter(torch.zeros((),dtype=torch.float64))
    def forward(self,x,states=False):
        h=torch.zeros((len(x),N),dtype=torch.float64);logits=[];hs=[]
        for t in range(x.shape[1]):
            h=torch.tanh(h@self.W.T+self.U[x[:,t]]+self.b)
            logits.append(h@self.v+self.c);hs.append(h)
        return (torch.stack(logits,1),torch.stack(hs,1)) if states else torch.stack(logits,1)

def export(model,seed,epoch,x,y):
    with torch.no_grad():
        logits,hs=model(x,True)
        loss=float(torch.nn.functional.binary_cross_entropy_with_logits(logits,y))
        acc=float(((logits>0)==y).to(torch.float64).mean())
        return {'seed':seed,'epoch':epoch,'loss':loss,'train_accuracy':acc,'params':{k:v.detach().cpu().tolist() for k,v in model.named_parameters()},'train_states':hs.detach().cpu().tolist()}

def train():
    out=ROOT/'TRAINED.json'
    if out.exists():raise RuntimeError('Refuse to overwrite existing training results')
    torch.set_num_threads(1);x,y=make_data();rows=[]
    for seed in SEEDS:
        torch.manual_seed(seed);model=RNN();opt=torch.optim.Adam(model.parameters(),lr=.02)
        rows.append(export(model,seed,0,x,y))
        for step in range(1,1201):
            opt.zero_grad();pred=model(x)
            loss=torch.nn.functional.binary_cross_entropy_with_logits(pred,y)
            loss.backward();opt.step()
            if step in STEPS:
                row=export(model,seed,step,x,y);rows.append(row)
                print(seed,step,'loss',round(row['loss'],8),'acc',row['train_accuracy'],flush=True)
    payload={'protocol_sha256':hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
             'torch':torch.__version__,'numpy':np.__version__,'rows':rows}
    out.write_text(json.dumps(payload,indent=1)+'\n')
    print('TRAINED_SHA256',hashlib.sha256(out.read_bytes()).hexdigest())

if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1]!='train':raise SystemExit('usage: train187.py train')
    train()
