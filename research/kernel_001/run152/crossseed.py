"""NOESIS Run 152: cross-seed exhaustive ternary horizon audit.
0:+1, 1:-1 reflected at zero, 2:neutral. Threshold 0.1, depth 14.
"""
import json,sys
from pathlib import Path
from fractions import Fraction
import numpy as np
HERE=Path(__file__).resolve().parent
SEEDS=range(208,216);VARIANTS=('baseline','latent','output')
EXPECTED={208:(12,None,13),209:(10,None,None),210:(None,None,None),
211:(None,None,None),212:(None,None,None),213:(11,None,11),
214:(13,10,13),215:(None,None,None)}
def load():
    path=HERE/'CHECKPOINTS.json'
    if path.exists():return json.loads(path.read_text())
    sys.path.insert(0,str(HERE.parent/'run150'))
    from train_reproduce import train
    models=[train(s,v) for s in SEEDS for v in VARIANTS]
    path.write_text(json.dumps(models,indent=2)+'\n')
    return models
def exact(p,word):
    f=lambda x:Fraction(str(x))
    A=[[f(z) for z in row] for row in p['A']]
    E=[[f(z) for z in row] for row in p['E']]
    w=[f(z) for z in p['w']]
    h=[Fraction(0) for _ in w];q=0
    for ch in word:
        s=int(ch)
        h=[max(Fraction(0),sum(a*x for a,x in zip(row,h))+E[s][j]) for j,row in enumerate(A)]
        q=max(0,q+(1,-1,0)[s])
    return sum(a*b for a,b in zip(h,w))-q
def decode(k,n):
    digits=[]
    for _ in range(n):digits.append(str(k%3));k//=3
    return ''.join(reversed(digits))
def evaluate(p):
    A=np.asarray(p['A'],dtype=np.float64)
    E=np.asarray(p['E'],dtype=np.float64)
    w=np.asarray(p['w'],dtype=np.float64)
    d=len(w);h=np.zeros((1,d));q=np.zeros(1,dtype=np.int16)
    u=2.0**-53;g=8*u/(1-8*u)
    na=np.max(np.sum(abs(A),axis=1))*(1+g)
    nw=np.sum(abs(w))*(1+g);ne=np.max(abs(E));acc=0.
    first=None;witness=None;history=[]
    for n in range(1,15):
        old=float(np.max(abs(h)))
        h=np.stack([np.maximum(0,h@A.T+E[s]) for s in range(3)],axis=1).reshape(-1,d)
        q=np.stack([np.maximum(0,q+inc) for inc in (1,-1,0)],axis=1).reshape(-1)
        acc=na*acc+100*g*(na*old+ne)
        mx=float(np.max(abs(h)))
        errors=h@w-q;ix=int(np.argmax(abs(errors)));err=float(abs(errors[ix]))
        bound=float(nw*acc+100*g*(nw*mx+n))
        if err-bound<=0.1<=err+bound:raise RuntimeError(f'ambiguous depth {n}: {err} +/- {bound}')
        word=decode(ix,n)
        history.append({'depth':n,'maximum':err,'roundoff_bound':bound,'witness':word})
        if first is None and err-bound>0.1:
            first=n;witness=word
            assert abs(exact(p,word))>Fraction(1,10)
    return {'first_failure_le14':first,'first_witness':witness,'depth14_max':history[-1]['maximum'],'depth14_witness':history[-1]['witness'],'history':history}
def main():
    models=load();assert len(models)==24
    rows=[]
    for model in models:
        r=evaluate(model['parameters'])
        rows.append({'seed':model['seed'],'variant':model['variant'],'train_mse':model['train_mse'],**r})
        print(model['seed'],model['variant'],r['first_failure_le14'],r['depth14_max'],flush=True)
    for seed in SEEDS:
        got=tuple(next(r['first_failure_le14'] for r in rows if r['seed']==seed and r['variant']==v) for v in VARIANTS)
        assert got==EXPECTED[seed],(seed,got)
    result={'run':152,'depth':14,'threshold':0.1,'records':rows,
            'counts':{v:sum(r['first_failure_le14'] is not None for r in rows if r['variant']==v) for v in VARIANTS},
            'status':'Retrospective extension, NOT prospective.'}
    assert result['counts']=={'baseline':4,'latent':1,'output':3}
    (HERE/'RAW_OUTCOMES.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: 24 checkpoints, exact rational witnesses, roundoff-bounded enumeration')
if __name__=='__main__':main()
