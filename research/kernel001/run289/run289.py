import json,hashlib,sys
from pathlib import Path
from gauge289 import gauge,canonical,auc,exact_check
P=Path(__file__).resolve().parent;R=P.parent/'run288'
sys.path.insert(0,str(R))
from score288 import relaxed_margin
assert hashlib.sha256((R/'checkpoints288.json').read_bytes()).hexdigest()=='d525a26b8858a0e3ce1edbc1a0b1174c1a57a9335624c0d691bbcf55b5a8e858'
r={(x['seed'],x['epoch']):x for x in json.loads((R/'checkpoints288.json').read_text())['rows']}
e={x['seed']:x for x in json.loads((R/'FROZEN_EARLY_SCORES.json').read_text())}
o={x['seed']:x for x in json.loads((R/'outcomes288.json').read_text())['rows']}
gs=[(1.,1.),(8.,1/8),(1/8,8.),(64.,1/64),(1/64,64.)]
result=[];summary={}
for d in gs:
 k=f'{d[0]:g}_{d[1]:g}';rr=[]
 for seed in range(20928,21184):
  p=r[(seed,20)]['p'];s=float(-relaxed_margin(gauge(p,d)))
  t=float(-relaxed_margin(canonical(gauge(p,d))))
  rr.append(dict(seed=seed,gauge=k,score=s,canonical=t,original=e[seed]['score'],y=int(o[seed]['epoch80']['certificate'] is not None)))
 result+=rr
 pairs=sum(1 for i in range(256) for j in range(i) if (rr[i]['score']-rr[j]['score'])*(rr[i]['original']-rr[j]['original'])<0)
 summary[k]=dict(auc=auc([(x['score'],x['y']) for x in rr]),canonical_auc=auc([(x['canonical'],x['y']) for x in rr]),max_change=max(abs(x['score']-x['original']) for x in rr),changed=sum(abs(x['score']-x['original'])>1e-6 for x in rr),inversions=pairs)
 print(k,summary[k],flush=True)
assert summary['8_0.125']['max_change']>1e-6
for seed in range(20928,21184):
 for d in gs[1:]:exact_check(r[(seed,20)]['p'],d,0)
for seed in (20928,20977,21000,21012,21113):
 for d in gs:exact_check(r[(seed,20)]['p'],d,8)
assert max(abs(result[256*j+i]['canonical']-result[i]['canonical']) for j in range(5) for i in range(256))<1e-6
(P/'results289.json').write_text(json.dumps({'summary':summary,'rows':result,'posthoc_canonical':True},indent=2)+'\n')
