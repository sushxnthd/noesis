#!/usr/bin/env python3
"""Independent Decimal-directed interval proof of Run201 (no mpmath dependency).
exp is correctly rounded at 115 digits and enclosed by +/-2 high-precision ulps.
All other interval operations round outward at 75 digits.
"""
import sys,json,hashlib,itertools
from decimal import Decimal as D,localcontext,ROUND_FLOOR,ROUND_CEILING,ROUND_HALF_EVEN
from pathlib import Path
PREC=75;EXP_PREC=115;R=D('1e-9');N=240;P=14;W=12;ONE=D(1)
def upadd(a,b):
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING
        return a+b
def upmul(a,b):
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING
        return a*b
def upsum(xs):
    a=D(0)
    for x in xs:a=upadd(a,x)
    return a
def dn(x):
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_FLOOR
        return +x
def up(x):
    with localcontext() as c:
        c.prec=PREC;c.rounding=ROUND_CEILING
        return +x
class I:
    def __init__(self,a,b=None):
        self.a=dn(D(a));self.b=up(D(a) if b is None else D(b))
        assert self.a<=self.b
    def __add__(self,o):
        o=iv(o)
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_FLOOR;lo=self.a+o.a
            c.rounding=ROUND_CEILING;hi=self.b+o.b
        return I(lo,hi)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,o):return self+-iv(o)
    def __rsub__(self,o):return iv(o)+-self
    def __mul__(self,o):
        o=iv(o)
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_FLOOR
            lo=min(x*y for x in (self.a,self.b) for y in (o.a,o.b))
            c.rounding=ROUND_CEILING
            hi=max(x*y for x in (self.a,self.b) for y in (o.a,o.b))
        return I(lo,hi)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=iv(o);assert o.a>0 or o.b<0
        with localcontext() as c:
            c.prec=PREC;c.rounding=ROUND_FLOOR;lo=min(ONE/x for x in (o.a,o.b))
            c.rounding=ROUND_CEILING;hi=max(ONE/x for x in (o.a,o.b))
        return self*I(lo,hi)
    def absup(self):return max(abs(self.a),abs(self.b))
def iv(x):return x if isinstance(x,I) else I(x)
def ex(v):
    def bound(x):
        with localcontext() as c:
            c.prec=EXP_PREC;c.rounding=ROUND_HALF_EVEN
            y=x.exp(context=c)
            ulp=D(1).scaleb(y.adjusted()-EXP_PREC+1)
            return y-2*ulp,y+2*ulp
    a,_=bound(v.a);_,b=bound(v.b)
    return I(a,b)
def T(x):return I(2)/(I(1)+ex(-I(2)*iv(x)))-I(1)
def params(row):
    def q(x):return I(D.from_float(float(x)))
    return {k:([[q(x) for x in a] for a in v] if k in ('W','U','V') else [q(x) for x in v]) for k,v in row['params'].items()}
def step(h,p,bit):
    return [T(p['b'][i]+p['U'][bit][i]+sum((p['W'][i][j]*h[j] for j in range(W)),I(0))) for i in range(W)]
def classify(h,p):
    z=[p['c'][i]+sum((p['V'][i][j]*h[j] for j in range(W)),I(0)) for i in range(3)]
    gaps=[min((z[i]-z[j]).a for j in range(3) if i!=j) for i in range(3)]
    wins=[i for i in range(3) if gaps[i]>0]
    return (wins[0],gaps[wins[0]]) if len(wins)==1 else (None,None)
def invariant(row,centers):
    p=params(row);c=[[I(D(s)) for s in h] for h in centers]
    h=[I(0)]*W
    for n in range(1,N+1):
        h=step(h,p,0);pred,gap=classify(h,p)
        assert pred==(0 if row['epoch']==400 or n<15 else 1),('finite',row['epoch'],n,pred)
    assert max((h[i]-c[0][i]).absup() for i in range(W))<R
    A=[[I(int(i==j)) for j in range(W)] for i in range(W)]
    E=[D(0)]*W;boxes=[]
    for t in range(P):
        d=[upadd(upsum(upmul(A[i][j].absup(),R) for j in range(W)),E[i]) for i in range(W)]
        boxes.append([c[t][i]+I(-d[i],d[i]) for i in range(W)])
        pred,gap=classify(boxes[-1],p)
        assert pred==(0 if row['epoch']==400 else 1),('phase',row['epoch'],t,pred)
        f=step(c[t],p,0)
        J=[[(I(1)-f[i]*f[i])*p['W'][i][j] for j in range(W)] for i in range(W)]
        beta=[(f[i]-c[t+1][i]).absup() for i in range(W)]
        rem=[]
        for i in range(W):
            u=upsum(upmul(p['W'][i][j].absup(),d[j]) for j in range(W))
            rem.append(upmul(u,u))
        E=[upadd(upadd(upsum(upmul(J[i][j].absup(),E[j]) for j in range(W)),rem[i]),beta[i]) for i in range(W)]
        A=[[sum((J[i][k]*A[k][j] for k in range(W)),I(0)) for j in range(W)] for i in range(W)]
    bound=[upadd(upadd((c[P][i]-c[0][i]).absup(),upsum(upmul(A[i][j].absup(),R) for j in range(W))),E[i]) for i in range(W)]
    assert max(bound)<R,('closure',row['epoch'],max(bound))
    return boxes,p,str(max(bound))
def main(source,certificate,out):
    raw=Path(source).read_bytes();obj=json.loads(raw);cert=json.loads(Path(certificate).read_text())
    assert hashlib.sha256(raw).hexdigest()==cert['source_sha256']
    results={}
    for row in obj['rows']:
        if row['seed']!=283 or row['epoch'] not in (400,800):continue
        centers=next(x['centers'] for x in cert['centers'] if x['seed']==283 and x['epoch']==row['epoch'])
        boxes,p,bound=invariant(row,centers);suffixes={}
        for n in range(1,5):
            for bits in itertools.product((0,1),repeat=n):
                s=''.join(map(str,bits));preds=[];gaps=[]
                for box in boxes:
                    h=box
                    for bit in bits:h=step(h,p,bit)
                    pred,gap=classify(h,p)
                    preds.append(pred);gaps.append(gap)
                assert all(x is not None and x==preds[0] for x in preds),('undecided',row['epoch'],s)
                suffixes[s]={'class':preds[0],'min_margin':str(min(gaps))}
        results[str(row['epoch'])]={'invariant_radius_upper':bound,'suffixes':suffixes}
    primary=0
    for s in results['400']['suffixes']:
        a=results['400']['suffixes'][s]['class']
        b=results['800']['suffixes'][s]['class']
        truth=s.count('1')%3
        assert a==truth and b==(truth+1)%3,(s,a,b,truth)
        if '1' in s:primary+=1
    assert primary==26
    Path(out).write_text(json.dumps({'checkpoint_sha256':hashlib.sha256(raw).hexdigest(),
        'independent_decimal_primary_count':primary,'epochs':results},indent=2)+'\n')
    print('INDEPENDENT DECIMAL PASS',primary,flush=True)
if __name__=='__main__':
    assert len(sys.argv)==4
    main(*sys.argv[1:])
