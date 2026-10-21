"""Run315 portable independent replay using a frozen, platform-stable score digest."""
import hashlib,json
from pathlib import Path
from reproduce315 import cone,witness,auc
from independent315 import certificate,wrong
P=Path(__file__).resolve().parent
scores=json.loads((P/'FROZEN_EARLY_SCORES315.json').read_text())
canon=[{'seed':r['seed'],'retention_score':round(r['retention_score'],8),'negative_bce':round(r['negative_bce'],8),'early_accuracy':round(r['early_accuracy'],8)} for r in scores]
digest=hashlib.sha256((json.dumps(canon,sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
assert digest=='55227737526cab6fac9f51bc2300a22ab6e8cf39413939d2c25d12cfe68d06ad',digest
raw=json.loads((P/'checkpoints315.json').read_text())
by={(r['seed'],r['epoch']):r for r in raw['rows']}
e={r['seed']:r for r in scores};rows=[];mut=0
for seed in range(22600,22696):
 p=by[seed,80]['p'];proof=cone(p);word=None if proof else witness(p)
 if proof:
  assert certificate(p,proof)
  damaged=p.copy();damaged[27]=1.0
  assert not certificate(damaged,proof)
  mut+=1
 if word:assert wrong(p,word)
 rows.append({'seed':seed,'outcome':'certified' if proof else 'incorrect' if word else 'unresolved','proof':proof,'witness':word,**e[seed]})
pos=[r for r in rows if r['outcome']=='certified'];neg=[r for r in rows if r['outcome']=='incorrect']
assert (len(pos),len(neg),mut)==(4,43,4)
ret=auc(pos,neg,'retention_score');loss=auc(pos,neg,'negative_bce')
assert abs(ret-0.627906976744186)<1e-12 and abs(loss-0.9011627906976745)<1e-12
out={'rows':rows,'certified':4,'incorrect':43,'unresolved':49,'auc_retention':ret,'auc_loss':loss,'delta':ret-loss,'canonical_score_sha256':digest}
(P/'portable_results315.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print('RUN315_PORTABLE_EXACT_VERIFIED',4,43,49,ret,loss,ret-loss,digest)
