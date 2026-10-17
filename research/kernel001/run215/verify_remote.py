"""Run215 remote recheck of strict epoch100 witnesses and two-state positives."""
import json,sys
from pathlib import Path
P=Path('research/run214')
sys.path.insert(0,str(P))
from verify_run210 import check,ex,th
D=json.loads((P/'RUN214_CHECKPOINTS.json').read_text())
rows={r['seed']:r for r in D['rows'] if r['epoch']==100}
L=json.loads(Path('research/kernel001/run215/epoch100_labels.json').read_text())['results']
passed=0
for e in L:
 s=e['seed'];row=rows[s];word=e['word']
 if word is not None:
  p=row['params'];W=[[[ex(x) for x in a] for a in m] for m in p['W']]
  b=[[ex(x) for x in a] for a in p['b']]
  v=[ex(x) for x in p['v']];c=ex(p['c']);h=[ex(.5),ex(-.5)];q=0
  for t in word:
   q=0 if t==2 else q^(t==1)
   h=[th(sum(W[t][j][k]*h[k] for k in range(2))+b[t][j]) for j in range(2)]
  z=sum(v[j]*h[j] for j in range(2))+c
  assert (q==0 and z.a>0) or (q==1 and z.b<0),(s,word)
  passed+=1
 elif s in (967,977,991,1033,1103,1163):
  assert check(row)['status']=='CERTIFIED',s
  passed+=1
 print(s,'CHECKED' if word is not None or s in (967,977,991,1033,1103,1163) else 'LOCAL_ONLY',flush=True)
assert passed==21
print('Run215 remote interval obligations passed:',passed,'of 32; eight five-cell positives and three abstentions not rechecked')
