"""Run206 two-box synthesis (untrusted), exact-real verification, independent interval checker."""
import json,math,hashlib
from pathlib import Path
from decimal import Decimal as D,Context,localcontext,ROUND_FLOOR,ROUND_CEILING
from fractions import Fraction as Q
import numpy as np
from mpmath import iv
R=Path(__file__).resolve().parent
F=Context(prec=95,rounding=ROUND_FLOOR);C=Context(prec=95,rounding=ROUND_CEILING)
iv.dps=85
def down(x):return math.floor((x-1e-7)/1e-6)*1e-6
def up(x):return math.ceil((x+1e-7)/1e-6)*1e-6
def propose(row):
    p=row['params'];w=p['w'];b=p['b'];v=p['v'];c=p['c']
    first=[math.tanh(w[t]*.5+b[t]) for t in range(3)]
    lo=np.array([down(min(first[0],first[2])),down(first[1])]);hi=np.array([up(max(first[0],first[2])),up(first[1])])
    for it in range(1000):
        oldlo=lo.copy();oldhi=hi.copy()
        for par in range(2):
            for t in range(3):
                tar=0 if t==2 else par^(t==1)
                a=math.tanh(w[t]*(oldlo[par] if w[t]>=0 else oldhi[par])+b[t])
                z=math.tanh(w[t]*(oldhi[par] if w[t]>=0 else oldlo[par])+b[t])
                lo[tar]=min(lo[tar],down(a));hi[tar]=max(hi[tar],up(z))
        if (lo<-1.001).any() or (hi>1.001).any():return {'accepted':False,'reason':'box exceeds tanh range'}
        if np.array_equal(lo,oldlo) and np.array_equal(hi,oldhi):
            margins=[]
            for par in range(2):
                y1=v*lo[par]+c;y2=v*hi[par]+c
                margins.append(min(y1,y2) if par else -max(y1,y2))
            if min(margins)<=0:return {'accepted':False,'reason':'no output separation'}
            return {'accepted':True,'intervals':[[format(lo[i],'.6f'),format(hi[i],'.6f')] for i in range(2)],'iterations':it}
    return {'accepted':False,'reason':'no stabilization'}
def dec(q,ctx):
    with localcontext(ctx):return D(q.numerator)/D(q.denominator)
def tlo(x):
    with localcontext(F):
        e=dec(2*x,F).exp().next_minus(F).next_minus(F);den=e+D(1)
    with localcontext(C):z=D(2)/den
    with localcontext(F):out=D(1)-z
    return Q(out)
def thi(x):
    with localcontext(C):
        e=dec(2*x,C).exp().next_plus(C).next_plus(C);den=e+D(1)
    with localcontext(F):z=D(2)/den
    with localcontext(C):out=D(1)-z
    return Q(out)
def q(v):return Q.from_float(float(v))
def exact(row,cert):
    p=row['params'];w=[q(x) for x in p['w']];b=[q(x) for x in p['b']];v=q(p['v']);c=q(p['c'])
    boxes=[tuple(Q(D(x)) for x in pair) for pair in cert['intervals']]
    assert len(boxes)==2 and all(lo<=hi for lo,hi in boxes)
    slack=[];margin=[]
    def step(lo,hi,t):
        a=w[t]*(lo if w[t]>=0 else hi)+b[t];z=w[t]*(hi if w[t]>=0 else lo)+b[t]
        return tlo(a),thi(z)
    for t in range(3):
        nl,nh=step(Q(1,2),Q(1,2),t);tl,th=boxes[0 if t==2 else t]
        assert nl>=tl and nh<=th,('base',t)
        slack.extend([nl-tl,th-nh])
    for par in range(2):
        lo,hi=boxes[par];yl=v*(lo if v>=0 else hi)+c;yh=v*(hi if v>=0 else lo)+c
        m=yl if par else -yh
        assert m>0,('output',par)
        margin.append(m)
        for t in range(3):
            nl,nh=step(lo,hi,t);tar=0 if t==2 else par^(t==1);tl,th=boxes[tar]
            assert nl>=tl and nh<=th,('closure',par,t)
            slack.extend([nl-tl,th-nh])
    return {'verified':True,'minimum_slack':float(min(slack)),'minimum_output_margin':float(min(margin))}
def iq(x):
    a=q(x);return iv.mpf(a.numerator)/iv.mpf(a.denominator)
def independent(row,cert):
    p=row['params'];w=[iq(z) for z in p['w']];b=[iq(z) for z in p['b']];v=iq(p['v']);bias=iq(p['c'])
    boxes=[iv.mpf(pair) for pair in cert['intervals']]
    def step(h,t):return 1-2/(1+iv.exp(2*(w[t]*h+b[t])))
    def inside(h,box):return bool(h.a>=box.a and h.b<=box.b)
    for t in range(3):assert inside(step(iv.mpf('.5'),t),boxes[0 if t==2 else t]),('base',t)
    for par in range(2):
        y=v*boxes[par]+bias
        assert bool(y.a>0 if par else y.b<0),('output',par)
        for t in range(3):
            tar=0 if t==2 else par^(t==1)
            assert inside(step(boxes[par],t),boxes[tar]),('closure',par,t)
    return True
def witness(row,seq):
    p=row['params'];hlo=hhi=Q(1,2);state=0
    for t in seq:
        w=q(p['w'][t]);b=q(p['b'][t]);a=w*(hlo if w>=0 else hhi)+b;z=w*(hhi if w>=0 else hlo)+b
        hlo=tlo(a);hhi=thi(z);state=0 if t==2 else state^(t==1)
    v=q(p['v']);c=q(p['c']);yl=v*(hlo if v>=0 else hhi)+c;yh=v*(hhi if v>=0 else hlo)+c
    pred=1 if yl>0 else 0 if yh<0 else None
    return {'input':list(seq),'expected':state,'predicted':pred,'verified_error':pred is not None and pred!=state}
if __name__=='__main__':
    raw=(R/'CHECKPOINTS.json').read_bytes();rows=json.loads(raw)['rows']
    results=[];certs=[]
    for row in rows:
        c=propose(row);item={'seed':row['seed'],'epoch':row['epoch'],'candidate':c}
        if c['accepted']:
            item['decimal']=exact(row,c);item['mpmath_independent']=independent(row,c)
            certs.append(item)
        results.append(item)
    prior=next(r for r in rows if r['seed']==337 and r['epoch']==50)
    err=witness(prior,[1]);assert err['verified_error']
    spoof={'params':{'w':[1.,-1.,0.],'b':[-.0001,.0001,2.],'v':-1.,'c':0.}}
    reject=propose(spoof);assert not reject['accepted']
    endpoints=[z for z in certs if z['epoch'] in (400,800)]
    passed=len(endpoints)>=2 and bool(err['verified_error'])
    report={'checkpoint_sha256':hashlib.sha256(raw).hexdigest(),'frozen_primary_pass':passed,'certified_count':len(certs),'certified_endpoints':len(endpoints),'earlier_error':err,'spoof_abstention':reject,'results':results}
    (R/'RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print('FROZEN_PRIMARY',passed,'CERTIFIED',len(certs),'ENDPOINTS',len(endpoints),'EARLY_ERROR',err)
    assert passed
