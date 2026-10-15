"""Frozen two-box inductive attempt. Float interval screening; no positive claims without independent outward checker."""
from __future__ import annotations
import itertools,json,hashlib
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent

def boxes(row):
    xs=np.array(list(itertools.product((0,1),repeat=6)),dtype=int)
    labels=np.cumsum(xs,axis=1)%2
    hs=np.asarray(row['train_states'],dtype=float)
    points=[hs[labels==p] for p in (0,1)]
    points[0]=np.concatenate((points[0],np.zeros((1,hs.shape[-1]))),axis=0)
    return [[np.min(v,axis=0),np.max(v,axis=0)] for v in points]

def img(W,U,b,lo,hi,x):
    P=np.maximum(W,0);M=np.minimum(W,0)
    zl=P@lo+M@hi+U[x]+b;zu=P@hi+M@lo+U[x]+b
    return np.tanh(zl),np.tanh(zu)

def margin(row,box):
    v=np.array(row['params']['v']);c=float(row['params']['c']);lo,hi=box
    l=float(np.maximum(v,0)@lo+np.minimum(v,0)@hi+c)
    u=float(np.maximum(v,0)@hi+np.minimum(v,0)@lo+c)
    return l,u

def check(row,maxiter=100):
    p=row['params'];W=np.array(p['W']);U=np.array(p['U']);b=np.array(p['b'])
    bx=boxes(row)
    hist=[]
    for it in range(maxiter):
        margin_even=margin(row,bx[0]);margin_odd=margin(row,bx[1]);
        if margin_even[1]>=-.1 or margin_odd[0]<=.1:
            return {'certified':False,'reason':'output_margin','iterations':it,'even_interval':margin_even,'odd_interval':margin_odd,'box_widths':[float(max(hi-lo)) for lo,hi in bx]}
        out=[[v.copy() for v in pair] for pair in bx]
        for parity in (0,1):
            for x in (0,1):
                lo,hi=img(W,U,b,*bx[parity],x);target=parity^x
                out[target][0]=np.minimum(out[target][0],lo)
                out[target][1]=np.maximum(out[target][1],hi)
        grow=max(float(max(np.max(bx[i][0]-out[i][0]),np.max(out[i][1]-bx[i][1]))) for i in (0,1))
        hist.append(grow)
        if grow<=0:
            return {'certified':True,'iterations':it,'even_interval':margin_even,'odd_interval':margin_odd,'box_widths':[float(max(hi-lo)) for lo,hi in bx]}
        bx=[[np.nextafter(lo,-np.inf),np.nextafter(hi,np.inf)] for lo,hi in out]
    return {'certified':False,'reason':'nonclosure','iterations':maxiter,'even_interval':margin(row,bx[0]),'odd_interval':margin(row,bx[1]),'box_widths':[float(max(hi-lo)) for lo,hi in bx]}

def run():
    data=json.loads((ROOT/'TRAINED.json').read_text());out=[]
    for r in data['rows']:
        res=check(r);out.append({'seed':r['seed'],'epoch':r['epoch'],'train_loss':r['loss'],'train_accuracy':r['train_accuracy'],**res})
        print(r['seed'],r['epoch'],res,flush=True)
    payload={'trained_sha256':hashlib.sha256((ROOT/'TRAINED.json').read_bytes()).hexdigest(),
             'method':'coordinate two-box interval-hull; floating screen only; no positives without independent outward checker',
             'results':out}
    (ROOT/'CERT_SCREEN.json').write_text(json.dumps(payload,indent=2)+'\n')
if __name__=='__main__':run()
