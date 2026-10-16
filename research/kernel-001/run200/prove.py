#!/usr/bin/env python3
"""All-length zero-tail checker: exact binary64 weights, directed intervals.
The candidate centers are UNTRUSTED: all conclusions follow from the
interval enclosure and the global |tanh''| <= 2 Taylor bound.
"""
import json,sys,hashlib
from pathlib import Path
from mpmath import iv,mp

iv.dps=95
mp.dps=115
D=12
N=240
P=14
R=iv.mpf('0.000000001')

def q(x):
    a,b=float(x).as_integer_ratio()
    return iv.mpf(a)/iv.mpf(b)
def T(x):
    return 2/(1+iv.exp(-2*x))-1
def up(x):
    return abs(x).b
def pars(row):
    p=row['params']
    return {k:([[q(x) for x in r] for r in p[k]] if k in ('W','U','V')
               else [q(x) for x in p[k]]) for k in ('W','U','V','b','c')}
def F(h,p):
    return [T(p['b'][i]+p['U'][0][i]+sum(p['W'][i][j]*h[j] for j in range(D))) for i in range(D)]
def z(h,p):
    return [p['c'][i]+sum(p['V'][i][j]*h[j] for j in range(D)) for i in range(3)]
def center(row):
    p=row['params']
    w=[[mp.mpf(x) for x in r] for r in p['W']]
    u=[mp.mpf(x) for x in p['U'][0]]
    b=[mp.mpf(x) for x in p['b']]
    h=[mp.mpf(0)]*D
    def f(h):
        return [mp.tanh(b[i]+u[i]+sum(w[i][j]*h[j] for j in range(D))) for i in range(D)]
    for _ in range(N):h=f(h)
    out=[]
    for _ in range(P+1):
        out.append([mp.nstr(x,65) for x in h])
        h=f(h)
    return out
def prove(row,centers):
    p=pars(row)
    h=[iv.mpf(0)]*D
    smallest=None
    for t in range(1,N+1):
        h=F(h,p)
        truth=0 if row['epoch']==400 or t<15 else 1
        zz=z(h,p)
        gap=min((zz[truth]-zz[j]).a for j in range(3) if j!=truth)
        assert gap>0,('finite failure',row['epoch'],t,str(gap))
        smallest=gap if smallest is None else min(smallest,gap)
    c=[[iv.mpf(x) for x in cc] for cc in centers]
    seed=max(up(h[i]-c[0][i]) for i in range(D))
    assert seed<R.a,('seed not enclosed',str(seed))
    A=[[iv.mpf(int(i==j)) for j in range(D)] for i in range(D)]
    E=[iv.mpf(0)]*D
    phase_min=None
    for t in range(P):
        delta=[sum(up(A[i][j])*R for j in range(D))+E[i] for i in range(D)]
        truth=0 if row['epoch']==400 else 1
        zz=z(c[t],p)
        for other in range(3):
            if other==truth:continue
            d=[p['V'][truth][j]-p['V'][other][j] for j in range(D)]
            margin=((zz[truth]-zz[other]).a-sum(up(d[j])*delta[j] for j in range(D))).a
            assert margin>0,('phase output not certified',t,str(margin))
            phase_min=margin if phase_min is None else min(phase_min,margin)
        ff=F(c[t],p)
        J=[[(1-ff[i]*ff[i])*p['W'][i][j] for j in range(D)] for i in range(D)]
        beta=[up(ff[i]-c[t+1][i]) for i in range(D)]
        rem=[sum(up(p['W'][i][j])*delta[j] for j in range(D))**2 for i in range(D)]
        E=[sum(up(J[i][j])*E[j] for j in range(D))+rem[i]+beta[i] for i in range(D)]
        A=[[sum(J[i][k]*A[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
    final=max(up(c[P][i]-c[0][i])+sum(up(A[i][j])*R for j in range(D))+E[i] for i in range(D))
    assert final<R.a,('inductive closure failed',str(final))
    return {'epoch':row['epoch'],'finite_checked':N,'induction_period':P,
            'radius':'1e-9','image_radius_upper':str(final.b),
            'initial_error_upper':str(seed.b),
            'min_finite_margin_lower':str(smallest.a),
            'min_phase_margin_lower':str(phase_min.a),'verified':True}
def main():
    source=Path(sys.argv[1]);output=Path(sys.argv[2])
    rows=[r for r in json.loads(source.read_text())['rows'] if r['seed']==283 and r['epoch'] in (400,800)]
    assert len(rows)==2
    results=[]
    for row in rows:
        cc=center(row)
        out=prove(row,cc)
        print('CERTIFIED',out,flush=True)
        results.append({'result':out,'centers':cc})
    output.write_text(json.dumps({'checkpoint_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'statement':'seed 283: epoch 400 predicts class 0 for all 0^k k>=1; epoch 800 predicts class 0 for k<=14 and class 1 for all k>=15',
        'proofs':results},indent=2)+'\n')
if __name__=='__main__':main()
