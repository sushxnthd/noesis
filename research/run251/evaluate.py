"""Exact dyadic-rational independent replay and prospectively frozen Run251 evaluation."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import numpy as np
from probes import arms
HERE=Path(__file__).resolve().parent
def target(w):
    q=0
    for t in w:
        if t==2:q=0
        elif t==1:q=1-q
    return q
def float_wrong(row,w):
    p=row['params'];a=np.asarray(p['A']);e=np.asarray(p['E']);b=np.asarray(p['b']);v=np.asarray(p['v']);c=p['c'];h=np.zeros(len(v))
    for t in w:h=np.maximum(0,a@h+e[t]+b)
    return int(float(h@v+c)>0)!=target(w)
def replay_a(row,w):
    p=row['params'];conv=F.from_float
    a=[[conv(x) for x in r] for r in p['A']];e=[[conv(x) for x in r] for r in p['E']];b=[conv(x) for x in p['b']];v=[conv(x) for x in p['v']];c=conv(p['c']);h=[F(0)]*len(v)
    for t in w:
        h=[max(F(0),sum((a[j][k]*h[k] for k in range(len(h))),e[t][j]+b[j])) for j in range(len(h))]
    z=sum((v[j]*h[j] for j in range(len(h))),c)
    return int(z>0),target(w)
def replay_b(row,w):
    p=row['params'];convert=lambda x:F(*float(x).as_integer_ratio())
    mat=[[convert(x) for x in r] for r in p['A']];emb=[[convert(x) for x in r] for r in p['E']];bias=list(map(convert,p['b']));out=list(map(convert,p['v']));offset=convert(p['c']);h=[F(0) for _ in out]
    for sym in w:
        nxt=[]
        for j in range(len(h)):
            val=emb[sym][j]+bias[j]
            for k in range(len(h)):val+=mat[j][k]*h[k]
            nxt.append(val if val>0 else F(0))
        h=nxt
    z=offset
    for i in range(len(h)):z+=out[i]*h[i]
    return int(z>0),target(w)
def main():
    cp=HERE/'CHECKPOINTS.json'; data=json.loads(cp.read_text()); rows=data['rows']
    eligible=sorted((r for r in rows if r['epoch']==200 and r['train_accuracy']==1),key=lambda r:r['seed'])
    selection={'eligible':len(eligible),'selected_seeds':[r['seed'] for r in eligible[:24]],'checkpoint_sha256':hashlib.sha256(cp.read_bytes()).hexdigest()}
    (HERE/'SELECTION.json').write_text(json.dumps(selection,indent=2)+'\n')
    if len(eligible)<24:
        (HERE/'SUMMARY.json').write_text(json.dumps({'status':'ELIGIBILITY_FAIL',**selection},indent=2)+'\n');print('ELIGIBILITY_FAIL',len(eligible));return
    results=[];counts={k:0 for k in ('switching','fixed_tail','periodic','hold_biased')}
    for row in eligible[:24]:
        candidate=arms(row);entry={'seed':row['seed'],'arms':{}}
        for label,words in candidate.items():
            witness=None
            for w in words:
                if not float_wrong(row,w):continue
                a=replay_a(row,w);b=replay_b(row,w)
                if a!=b:raise AssertionError(('CHECKER_DISAGREEMENT',row['seed'],label,a,b))
                if a[0]!=a[1]:
                    witness={'word':list(w),'length':len(w),'prediction':a[0],'target':a[1]};break
            entry['arms'][label]={'witness':witness,'candidate_sha256':hashlib.sha256(('\n'.join(''.join(map(str,w)) for w in words)+'\n').encode()).hexdigest()}
            counts[label]+=witness is not None
        results.append(entry)
        (HERE/'OUTCOMES.json').write_text(json.dumps(results,indent=2)+'\n')
        print('SEED',row['seed'],{k:int(v['witness'] is not None) for k,v in entry['arms'].items()},flush=True)
    advantage=(counts['switching']-max(counts[k] for k in counts if k!='switching'))/24
    summary={'run':251,'status':'COMPLETE','eligible':len(eligible),'selected':24,'counts':counts,'primary_advantage':advantage,'primary_pass':advantage>=.20 and counts['switching']>=8,'exact_checker_agreement':True,'selection':selection,'unwitnessed_is_correct':False}
    (HERE/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    print('SUMMARY',json.dumps(summary))
if __name__=='__main__':main()
