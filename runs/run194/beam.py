"""NOESIS Run 194: frozen paired-state beam and matched random tests.
Run with TRAINED.json from Run 190; keep seed ordering fixed.
"""
import json,hashlib,sys
from pathlib import Path
import numpy as np
from mpmath import iv

SRC=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('TRAINED.json')
rows=json.loads(SRC.read_text())['rows']

def model(seed,epoch):
    p=next(r['params'] for r in rows if r['seed']==seed and r['epoch']==epoch)
    return {k:np.asarray(v,dtype=float) for k,v in p.items()}

def step(h,p,b):return np.tanh(h@p['W'].T+p['U'][b]+p['b']
)
def out(h,p):return h@p['v']+p['c']

def beam(a,b):
    x=np.zeros((1,8));y=x.copy();words=[''];budget=[]
    for depth in range(1,25):
        nx=np.concatenate((step(x,a,0),step(x,a,1)))
        ny=np.concatenate((step(y,b,0),step(y,b,1)))
        ws=[w+'0' for w in words]+[w+'1' for w in words]
        u,v=out(nx,a),out(ny,b);budget.append(len(ws))
        hit=np.flatnonzero(np.signbit(u)!=np.signbit(v))
        if len(hit):return {'depth':depth,'witness':ws[int(hit[0])],'per_depth':budget,'evaluations':sum(budget)}
        take=np.argsort(-np.abs(u-v),kind='stable')[:64]
        x,y=nx[take],ny[take];words=[ws[i] for i in take]
    return {'depth':None,'witness':None,'per_depth':budget,'evaluations':sum(budget)}

def random_trial(a,b,counts,seed):
    rng=np.random.default_rng(seed)
    for depth,n in enumerate(counts,1):
        bits=rng.integers(0,2,size=(n,depth),dtype=np.int8)
        x=np.zeros((n,8));y=x.copy()
        for t in range(depth):
            x=np.tanh(x@a['W'].T+a['U'][bits[:,t]]+a['b'])
            y=np.tanh(y@b['W'].T+b['U'][bits[:,t]]+b['b'])
        hit=np.flatnonzero(np.signbit(out(x,a))!=np.signbit(out(y,b)))
        if len(hit):return ''.join(map(str,bits[int(hit[0])]))
    return None

def ivsign(word,p):
    iv.dps=65
    f=lambda v:iv.mpf(float(v).as_integer_ratio()[0])/iv.mpf(float(v).as_integer_ratio()[1])
    W=[[f(t) for t in row] for row in p['W']];U=[[f(t) for t in row] for row in p['U']]
    bb=[f(t) for t in p['b']];vv=[f(t) for t in p['v']];c=f(p['c'])
    h=[iv.mpf(0)]*8
    for bit in word:
        h=[1-2/(1+iv.exp(2*(sum((W[i][j]*h[j] for j in range(8)),iv.mpf(0))+U[int(bit)][i]+bb[i]))) for i in range(8)]
    z=sum((vv[i]*h[i] for i in range(8)),c)
    if z.a>0:return 1
    if z.b<0:return -1
    raise AssertionError('uncertain sign')

result={'checkpoint_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'rows':[]}
for seed in (137,139,149,151):
    a,b=model(seed,300),model(seed,600)
    search=beam(a,b)
    baseline=[random_trial(a,b,search['per_depth'],s) for s in range(194000,194100)]
    if search['witness']:
        signs=[ivsign(search['witness'],p) for p in (a,b)]
        assert signs[0]!=signs[1]
    else:signs=None
    result['rows'].append({'seed':seed,'beam':search,'baseline_witnesses':baseline,'interval_signs':signs})
    print(seed,'beam',search['depth'],'budget',search['evaluations'],'random_hits',sum(w is not None for w in baseline),flush=True)
result['success_scalar']=any(r['beam']['witness'] and r['beam']['evaluations']<=4096 and sum(w is not None for w in r['baseline_witnesses'])<=5 for r in result['rows'])
Path(__file__).with_name('CI_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print('SUCCESS',result['success_scalar'])
