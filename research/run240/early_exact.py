import json
from pathlib import Path
from verify import check as a
from independent import check as b
R=Path(__file__).parent
D=json.load(open(R/'CHECKPOINTS.json'))['rows']
E={(x['seed'],x['arm']):x['status'] for x in json.load(open(R/'EXACT.json')) if x['epoch']==200}
out=[]
for r in D:
 if r['epoch']!=100:continue
 x=a(r);y=b(r)
 assert x['status']==y['status']
 if x['status']=='INCORRECT':assert x['witness']==y['witness']
 if x['status']=='CERTIFIED':assert x['states']==y['states']
 out.append(dict(seed=r['seed'],arm=r['arm'],early=x['status'],final=E[r['seed'],r['arm']]))
(R/'EARLY_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
from collections import Counter
print(Counter((x['early'],x['final']) for x in out))
