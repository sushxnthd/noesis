"""Independent exact proof checker; no synthesizer or ML dependencies."""
import json
from fractions import Fraction as F
from pathlib import Path
D=Path(__file__).resolve().parent
models=json.loads((D/'SEED18453_CHECKPOINTS.json').read_text())
proofs=json.loads((D/'SEED18453_CERTIFICATES.json').read_text())
def verify(model,cert):
    A=[[F.from_float(x) for x in row] for row in model['params']['A']]
    e=[F.from_float(model['params']['E'][0][i])+F.from_float(model['params']['b'][i]) for i in range(2)]
    v=[F.from_float(x) for x in model['params']['v']]
    b=F.from_float(model['params']['c'])
    def pre(x):return [sum(A[i][j]*x[j] for j in range(2))+e[i] for i in range(2)]
    def step(x):return [max(F(0),z) for z in pre(x)]
    def logit(x):return sum(v[i]*x[i] for i in range(2))+b
    poly=[[F(t) for t in point] for point in cert['poly_vertices']]
    f=[F(t) for t in cert['fixed_point']]
    def cross(a,b,x):return (b[0]-a[0])*(x[1]-a[1])-(b[1]-a[1])*(x[0]-a[0])
    def inside(x):return all(cross(poly[i],poly[(i+1)%len(poly)],x)>=0 for i in range(len(poly)))
    assert cert['k']==0 and cert['mask']==[1,1] and len(poly)==3
    assert inside([F(0),F(0)]) and inside(f)
    assert all(all(z>=0 for z in pre(x)) and inside(step(x)) for x in poly)
    assert step(f)==f and logit(f)==F(cert['fixed_logit'])
    tr=A[0][0]+A[1][1];det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert 1-det>0 and 1-tr+det>0 and 1+tr+det>0
    return step,logit,poly,f
for row in models:
    epoch=row['epoch']
    cert=next(c for c in proofs if c['epoch']==epoch)['certificate']
    step,logit,poly,f=verify(row,cert)
    assert row['train_accuracy']==1
    if epoch==100:
        assert all(logit(x)<0 for x in poly)
        print('PASS epoch100: all-length pure-hold correctness')
    elif epoch==300:
        assert logit(f)>0
        h=[F(0),F(0)]
        for n in range(1,969):
            h=step(h)
            if n<968:assert logit(h)<=0
            else:assert logit(h)>0
        print('PASS epoch300: first pure-hold failure at 968')
    else:raise AssertionError('unexpected epoch')
print('PASS: independent exact transition verification')
