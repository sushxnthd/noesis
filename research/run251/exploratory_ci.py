"""Predeclared post-eligibility exploratory analysis; NEVER upgrades frozen primary."""
from pathlib import Path
import json,hashlib
from probes import arms
from evaluate import float_wrong,replay_a,replay_b
D=Path(__file__).resolve().parent
cp=D/'CHECKPOINTS.json';rows=json.loads(cp.read_text())['rows']
eligible=sorted((r for r in rows if r['epoch']==200 and r['train_accuracy']==1),key=lambda r:r['seed'])
counts={k:0 for k in ('switching','fixed_tail','periodic','hold_biased')};results=[]
for row in eligible:
 rec={'seed':row['seed'],'arms':{}}
 for label,words in arms(row).items():
  witness=None
  for w in words:
   if not float_wrong(row,w):continue
   a=replay_a(row,w);b=replay_b(row,w)
   assert a==b,(row['seed'],label)
   if a[0]!=a[1]:witness={'word':list(w),'length':len(w),'prediction':a[0],'target':a[1]};break
  rec['arms'][label]={'witness':witness,'candidate_sha256':hashlib.sha256(('\n'.join(''.join(map(str,w)) for w in words)+'\n').encode()).hexdigest()}
  counts[label]+=witness is not None
 results.append(rec)
 print('SEED',row['seed'],{k:int(v['witness'] is not None) for k,v in rec['arms'].items()},flush=True)
(D/'EXPLORATORY_OUTCOMES.json').write_text(json.dumps(results,indent=2)+'\n')
summary={'run':251,'exploratory_only':True,'eligible':len(eligible),'counts':counts,'advantage':(counts['switching']-max(counts[k] for k in counts if k!='switching'))/max(1,len(eligible)),'checkpoint_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),'no_witness_is_not_certificate':True}
(D/'EXPLORATORY_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
print('SUMMARY',json.dumps(summary))
