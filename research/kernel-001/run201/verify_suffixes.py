#!/usr/bin/env python3
"""Run201 proof-producing suffix-transfer diagnostic, frozen protocol 448ef7e."""
import sys,json,hashlib,itertools
from pathlib import Path
from mpmath import iv
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'run200'))
import prove as base

def step(h,p,bit):
    return [base.T(p['b'][i]+p['U'][bit][i]+sum(p['W'][i][j]*h[j] for j in range(base.D))) for i in range(base.D)]

def classification(h,p):
    z=base.z(h,p)
    gaps=[min((z[i]-z[j]).a for j in range(3) if j!=i) for i in range(3)]
    good=[i for i in range(3) if gaps[i]>0]
    return (good[0],str(gaps[good[0]].a)) if len(good)==1 else (None,None)

def phase_boxes(row,centers):
    assert base.prove(row,centers)['verified']
    p=base.pars(row);c=[[iv.mpf(v) for v in x] for x in centers]
    A=[[iv.mpf(int(i==j)) for j in range(base.D)] for i in range(base.D)]
    E=[iv.mpf(0)]*base.D
    boxes=[]
    for t in range(base.P):
        d=[sum(base.up(A[i][j])*base.R for j in range(base.D))+E[i] for i in range(base.D)]
        boxes.append([c[t][i]+iv.mpf([-1,1])*d[i].b for i in range(base.D)])
        f=base.F(c[t],p)
        J=[[(1-f[i]*f[i])*p['W'][i][j] for j in range(base.D)] for i in range(base.D)]
        beta=[base.up(f[i]-c[t+1][i]) for i in range(base.D)]
        rem=[sum(base.up(p['W'][i][j])*d[j] for j in range(base.D))**2 for i in range(base.D)]
        E=[sum(base.up(J[i][j])*E[j] for j in range(base.D))+rem[i]+beta[i] for i in range(base.D)]
        A=[[sum(J[i][k]*A[k][j] for k in range(base.D)) for j in range(base.D)] for i in range(base.D)]
    return boxes,p

def run(source):
    raw=Path(source).read_bytes()
    rows=[r for r in json.loads(raw)['rows'] if r['seed']==283 and r['epoch'] in (400,800)]
    assert len(rows)==2
    results={}
    for row in rows:
        centers=base.center(row)
        boxes,p=phase_boxes(row,centers)
        suffixes={}
        for n in range(1,5):
            for bits in itertools.product((0,1),repeat=n):
                s=''.join(map(str,bits));preds=[];margins=[]
                for box in boxes:
                    h=box
                    for bit in bits:h=step(h,p,bit)
                    pred,margin=classification(h,p)
                    preds.append(pred);margins.append(margin)
                stable=preds[0] if all(x is not None and x==preds[0] for x in preds) else None
                suffixes[s]={'truth':sum(bits)%3,'class':stable,'phase_classes':preds,'phase_gap_lowers':margins}
        results[str(row['epoch'])]=suffixes
    primary=[];comparison={}
    for s,a in results['400'].items():
        b=results['800'][s];truth=a['truth']
        label='ABSTAIN'
        if a['class'] is not None and b['class'] is not None:
            label=('400_correct_800_wrong' if a['class']==truth and b['class']!=truth else
                   '400_wrong_800_correct' if a['class']!=truth and b['class']==truth else
                   'both_correct' if a['class']==truth and b['class']==truth else 'both_wrong')
        if '1' in s and label=='400_correct_800_wrong':primary.append(s)
        comparison[s]={'truth':truth,'epoch400':a['class'],'epoch800':b['class'],'label':label}
    out={'frozen_protocol_commit':'448ef7e285b29e7f3ab7e5e0f03c4751e11ba712',
         'source_sha256':hashlib.sha256(raw).hexdigest(),'primary_count':len(primary),
         'primary_suffixes':primary,'success':len(primary)>=1,'comparisons':comparison,'raw_phases':results}
    assert len(comparison)==30
    print('primary',len(primary),'abstains',sum(v['label']=='ABSTAIN' for v in comparison.values()))
    return out

if __name__=='__main__':
    assert len(sys.argv)==3
    Path(sys.argv[2]).write_text(json.dumps(run(sys.argv[1]),indent=2)+'\n')
