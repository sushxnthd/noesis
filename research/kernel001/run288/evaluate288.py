#!/usr/bin/env python3
"""Held-out frozen K001 Run288 evaluation. Noncertificate != incorrect."""
import json,random,hashlib
from pathlib import Path
from cert_lp288 import certificate_lp
from exact288 import check,find_witness
P=Path(__file__).resolve().parent
D=json.loads((P/'checkpoints288.json').read_text())
R={(x['seed'],x['epoch']):x for x in D['rows']}
E=json.loads((P/'FROZEN_EARLY_SCORES.json').read_text())
assert [x['seed'] for x in E]==list(range(20928,21184))
def find_cert(p):
 for a in (False,True):
  for b in (False,True):
   mask=[[False,False],[a,b]]
   cert=certificate_lp(p,mask)
   if cert is not None and check(p,cert):return cert
 return None
def auc(pairs):
 pos=[s for s,y in pairs if y==1];neg=[s for s,y in pairs if y==0]
 if not pos or not neg:return None
 return sum((p>n)+.5*(p==n) for p in pos for n in neg)/(len(pos)*len(neg))
out=[]
for early in E:
 seed=early['seed'];rec=dict(early)
 for epoch in (20,40,80,120):
  row=R[(seed,epoch)]
  cert=find_cert(row['p']) if row['accuracy']==1 else None
  wit=find_witness(row['p'],seed) if epoch in (20,80) else None
  assert not (cert is not None and wit is not None)
  rec[f'epoch{epoch}']={'accuracy':row['accuracy'],'bce':row['bce'],'certificate':cert,'witness':wit,'label':'certified' if cert else 'witnessed_incorrect' if wit else 'uncertified_unknown' if row['accuracy']==1 else 'sampled_incorrect'}
 out.append(rec)
labels=[int(x['epoch80']['certificate'] is not None) for x in out]
m={'n':len(out),'cert80':sum(labels),'noncert80':len(out)-sum(labels)}
for key,col in [('distance','score'),('bce','bce_baseline'),('accuracy','accuracy_baseline'),('neg_parameter_norm','parameter_norm_baseline')]:
 m['auc_'+key]=auc([(x[col],y) for x,y in zip(out,labels)])
m['auc_gain_vs_bce']=m['auc_distance']-m['auc_bce']
m['primary_pass']=bool(m['cert80']>=15 and m['noncert80']>=30 and m['auc_distance']>=.70 and m['auc_gain_vs_bce']>=.10)
m['early_sampledperfect_wrong_later_certified']=sum(x['epoch20']['accuracy']==1 and x['epoch20']['witness'] is not None and x['epoch80']['certificate'] is not None for x in out)
m['epoch80_cert_vs_witness_counts']={'cert':m['cert80'],'witness':sum(x['epoch80']['witness'] is not None for x in out)}
known=[x for x in out if x['epoch80']['certificate'] is not None or x['epoch80']['witness'] is not None]
m['auc_known_distance']=auc([(x['score'],int(x['epoch80']['certificate'] is not None)) for x in known])
m['auc_known_bce']=auc([(x['bce_baseline'],int(x['epoch80']['certificate'] is not None)) for x in known])
rng=random.Random(288);deltas=[]
for _ in range(1000):
 ss=[out[rng.randrange(len(out))] for _ in out];y=[int(x['epoch80']['certificate'] is not None) for x in ss]
 a=auc([(x['score'],z) for x,z in zip(ss,y)]);b=auc([(x['bce_baseline'],z) for x,z in zip(ss,y)])
 if a is not None and b is not None:deltas.append(a-b)
deltas.sort();m['auc_gain_bootstrap_95pct']=[deltas[int(.025*len(deltas))],deltas[int(.975*len(deltas))]]
obj={'protocol':'Run288 frozen before training; see FROZEN_PROTOCOL.md','checkpoint_sha256':hashlib.sha256((P/'checkpoints288.json').read_bytes()).hexdigest(),'early_scores_sha256':hashlib.sha256((P/'FROZEN_EARLY_SCORES.json').read_bytes()).hexdigest(),'metrics':m,'rows':out}
(P/'outcomes288.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
print(json.dumps(m,indent=2))
assert obj['checkpoint_sha256']=='d525a26b8858a0e3ce1edbc1a0b1174c1a57a9335624c0d691bbcf55b5a8e858'
assert m['cert80']==47 and m['epoch80_cert_vs_witness_counts']['witness']==132
assert m['primary_pass'] and m['early_sampledperfect_wrong_later_certified']==4
