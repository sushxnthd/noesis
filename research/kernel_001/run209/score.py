import json
from pathlib import Path
from candidate import first_error, propose_boxes
from verify_interval import prove_first_error, prove_all
R=Path(__file__).resolve().parent
full=R/'RUN209_CHECKPOINTS.json'
if full.exists():
 rows=[r for r in json.loads(full.read_text())['rows'] if r['epoch']==800]
else:
 compact=json.loads((R/'EPOCH800_COMPACT.json').read_text())
 rows=[{'seed':seed,'epoch':800,'loss':loss,'train_accuracy':1.0,
        'params':{'w':w,'b':b,'v':v,'c':c}}
       for seed,loss,w,b,v,c in compact['rows']]
out=[]
for row in rows:
 n,word=first_error(row)
 if n is None:
  box=propose_boxes(row)
  assert box is not None
  out.append({'seed':row['seed'],'correct_all_lengths':True,'proof':prove_all(row,box)})
 else:
  out.append({'seed':row['seed'],'first_error':n,'family':word==[1]+[0]*(n-2)+[1],
              'proof':prove_first_error(row,n,word)})
bad=[r for r in out if 'first_error' in r]
score=sum(r['family'] for r in bad)/len(bad)
result={'outcomes':out,'n_bad':len(bad),'score':score,'passed':len(bad)>=3 and score>=0.8}
(R/'RUN209_PROOFS.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['n_bad'],result['score'],result['passed'])
assert result['passed']
