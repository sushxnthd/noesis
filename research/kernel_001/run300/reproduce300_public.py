#!/usr/bin/env python3
"""Public reproduction of frozen Run300: trained latch diagnostic falsification."""
import hashlib,json,math,types
from pathlib import Path
import importlib.util
from sklearn.metrics import roc_auc_score
P=Path(__file__).resolve().parent
BASE=P.parent

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main():
    # Exact training source from prior public Run294; frozen modifications only.
    source=(BASE/'run294'/'train291.py').read_text()
    replacements={
      'W=3;N=256;T=6':'W=3;N=384;T=6',
      'range(21440,21696)':'range(22200,22584)',
      'q=torch.where(x[:,t]==0,0,1-q)':'q=torch.bitwise_or(q,x[:,t])',
      "'checkpoints291.json'":"'checkpoints300_repro.json'",
      'range(121)':'range(81)',
      'if epoch<120:':'if epoch<80:'
    }
    for old,new in replacements.items():
        assert source.count(old)==1,old
        source=source.replace(old,new)
    exec(compile(source,str(P/'train300_repro.py'),'exec'),
         {'__file__':str(P/'train300_repro.py'),'__name__':'__main__'})
    raw=json.loads((P/'checkpoints300_repro.json').read_text())
    by={(r['seed'],r['epoch']):r for r in raw['rows']}
    assert all((s,20) in by and (s,80) in by for s in range(22200,22584))
    # The predictor is Run297's frozen gauge-fixed LP, not a fitted new score.
    diag=(BASE/'run294'/'diagnostic291.py').read_text()
    assert diag.count('y=0 if x==0 else 1-s')==1
    mod=types.ModuleType('latch_lp');mod.__file__=str(P/'diagnostic300.py')
    exec(compile(diag.replace('y=0 if x==0 else 1-s','y=s|x'),mod.__file__,'exec'),mod.__dict__)
    scores={}
    for seed in range(22200,22584):
        r=by[seed,20]
        scores[seed]={'gauge_score':-mod.lp(mod.canonical(r['p'])),
                      'negative_bce':-r['bce']}
    frozen=[{'seed':s,**scores[s],'early_accuracy':by[s,20]['accuracy'],
             'negative_param_norm':-math.sqrt(sum(z*z for z in by[s,20]['p']))}
            for s in range(22200,22584)]
    score_blob=json.dumps(frozen,sort_keys=True,separators=(',',':'))+'\n'
    score_hash=hashlib.sha256(score_blob.encode()).hexdigest()
    (P/'early_scores300_public.json').write_text(score_blob)
    print('PUBLIC_EARLY_HASH',score_hash,flush=True)
    # Run299 independent rational certificate checker and Run297 exact witness search.
    cert=load(BASE/'run299'/'run299_public.py','noesis_cert299')
    witness=load(BASE/'run297'/'reproduce297.py','noesis_witness297')
    rows=[]
    for seed in range(22200,22584):
        r=by[seed,80];p=r['p'];proof=cert.candidate(p)
        if proof is not None:
            assert cert.independent(p,proof),('false certificate',seed)
        word=None if proof else witness.witness(p)
        if word is not None:
            assert cert.wrong(p,word),('false witness',seed)
        outcome='correct' if proof else 'incorrect' if word else 'unresolved'
        rows.append({'seed':seed,'outcome':outcome,'certificate':proof,
                     'witness':word,'epoch80_accuracy':r['accuracy'],**scores[seed]})
    pos=[r for r in rows if r['outcome']=='correct']
    neg=[r for r in rows if r['outcome']=='incorrect']
    resolved=pos+neg
    y=[r['outcome']=='correct' for r in resolved]
    auc_g=float(roc_auc_score(y,[r['gauge_score'] for r in resolved]))
    auc_b=float(roc_auc_score(y,[r['negative_bce'] for r in resolved]))
    result={'run':300,'correct':len(pos),'incorrect':len(neg),
            'unresolved':384-len(resolved),'auc_gauge':auc_g,'auc_loss':auc_b,
            'delta_loss_minus_gauge':auc_b-auc_g,'early_hash':score_hash,
            'sampled_perfect':sum(by[s,80]['accuracy']==1.0 for s in range(22200,22584)),
            'sampled_perfect_wrong':sum(r['outcome']=='incorrect' and r['epoch80_accuracy']==1.0 for r in rows)}
    (P/'rows300_public.json').write_text(json.dumps(rows,indent=2,sort_keys=True)+'\n')
    (P/'results300_public.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    assert len(pos)==17 and len(neg)==175 and result['unresolved']==192,result
    assert abs(auc_g-0.3376470588235294)<1e-6 and abs(auc_b-0.9233613445378152)<1e-6,result
    assert auc_b-auc_g>=0.20 and len(pos)>=4 and len(neg)>=50
    print('RUN300_PUBLIC_VERIFIED',json.dumps(result,sort_keys=True),flush=True)

if __name__=='__main__':main()
