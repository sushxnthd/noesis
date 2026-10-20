#!/usr/bin/env python3
"""Run301 retrospective missing-label AUC audit. Unknown labels are hypothetical."""
import json,hashlib,sys
from fractions import Fraction
from pathlib import Path
def exact_auc(rows,labels,key):
 p=[r for r in rows if labels[r['seed']]];n=[r for r in rows if not labels[r['seed']]]
 t=sum(2 if a[key]>b[key] else 1 if a[key]==b[key] else 0 for a in p for b in n)
 f=Fraction(t,2*len(p)*len(n))
 return {'twice_concordant':t,'denominator':2*len(p)*len(n),'fraction':str(f),'auc':float(f)}
def evaluate(rows):
 assert len(rows)==384 and {r['seed'] for r in rows}==set(range(22200,22584))
 assert [sum(r['outcome']==s for r in rows) for s in ('correct','incorrect','unresolved')]==[17,175,192]
 assert all(r['epoch80_accuracy']==1.0 for r in rows if r['outcome'] in ('correct','unresolved'))
 known={r['seed']:r['outcome']=='correct' for r in rows if r['outcome']!='unresolved'}
 unknown=[r for r in rows if r['outcome']=='unresolved']
 result={'run':301,'retrospective':True,'known_correct':17,'known_incorrect':175,'unresolved':192,'completions':{}}
 for name,part in [('resolved',[r for r in rows if r['outcome']!='unresolved']),('sampled_perfect_resolved',[r for r in rows if r['outcome']!='unresolved' and r['epoch80_accuracy']==1.0])]:
  assert len(part)==(192 if name=='resolved' else 35)
  result[name]={k:exact_auc(part,known,k) for k in ('gauge_score','negative_bce')}
 for name,key in [('G','gauge_score'),('L','negative_bce')]:
  chosen={r['seed'] for r in sorted(unknown,key=lambda r:(-r[key],r['seed']))[:40]}
  labels={**known,**{r['seed']:r['seed'] in chosen for r in unknown}}
  assert len(labels)==384 and sum(labels.values())==57
  result['completions'][name]={'hypothetical_positive_seeds':sorted(chosen),'scores':{k:exact_auc(rows,labels,k) for k in ('gauge_score','negative_bce')}}
 g=result['completions']['G']['scores'];l=result['completions']['L']['scores']
 result['sign_flip']=g['gauge_score']['auc']>g['negative_bce']['auc'] and l['negative_bce']['auc']>l['gauge_score']['auc']
 return result
if __name__=='__main__':
 src=Path(sys.argv[1]);dst=Path(sys.argv[2]);raw=src.read_bytes();res=evaluate(json.loads(raw))
 res['input_sha256']=hashlib.sha256(raw).hexdigest()
 dst.write_text(json.dumps(res,sort_keys=True,indent=2)+'\n')
 print('RUN301',json.dumps({k:v for k,v in res.items() if k!='completions'},sort_keys=True))
 print('G',res['completions']['G']['scores']);print('L',res['completions']['L']['scores'])
 assert res['sign_flip']
