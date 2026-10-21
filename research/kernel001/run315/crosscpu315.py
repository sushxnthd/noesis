"""Run315 cross-CPU reproduction with explicit independent provenance."""
import hashlib,json
from pathlib import Path
from reproduce315 import cone,witness,auc
from independent315 import certificate,wrong
P=Path(__file__).resolve().parent
expected='446ea8779a30e08b523ec27689ef18332518d905079b65ecd9f56ddfd51fcd00'
assert hashlib.sha256((P/'FROZEN_EARLY_SCORES315.json').read_bytes()).hexdigest()==expected
raw=json.loads((P/'checkpoints315.json').read_text())
scores=json.loads((P/'FROZEN_EARLY_SCORES315.json').read_text())
by={(r['seed'],r['epoch']):r for r in raw['rows']}
e={r['seed']:r for r in scores}
rows=[]
for seed in range(22600,22696):
 p=by[seed,80]['p'];proof=cone(p);word=None if proof else witness(p)
 if proof:assert certificate(p,proof)
 if word:assert wrong(p,word)
 rows.append({'seed':seed,'outcome':'certified' if proof else 'incorrect' if word else 'unresolved','proof':proof,'witness':word,**e[seed]})
pos=[r for r in rows if r['outcome']=='certified']
neg=[r for r in rows if r['outcome']=='incorrect']
assert (len(pos),len(neg))==(4,43)
ret=auc(pos,neg,'retention_score');loss=auc(pos,neg,'negative_bce')
assert abs(ret-0.627906976744186)<1e-12 and abs(loss-0.9011627906976745)<1e-12
(P/'crosscpu_results315.json').write_text(json.dumps({'rows':rows,'retention_auc':ret,'loss_auc':loss,'delta':ret-loss},sort_keys=True,indent=2)+'\n')
print('CROSSCPU_EXACT_PASS',len(pos),len(neg),ret,loss,ret-loss)
