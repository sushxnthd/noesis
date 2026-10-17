from pathlib import Path
import json
from mpmath import iv
iv.dps=75
R=Path(__file__).resolve().parent
rows={r['epoch']:r for r in json.loads((R/'CHECKPOINTS.json').read_text())['rows']}
cert=json.loads((R/'CERTIFICATE.json').read_text())
def exact(x):
 n,d=float(x).as_integer_ratio()
 return iv.mpf(n)/iv.mpf(d)
def tanh(x):
 a,b=iv.exp(2*x.a),iv.exp(2*x.b)
 return iv.mpf([((a-1)/(a+1)).a,((b-1)/(b+1)).b])
def model(row):
 p=row['params']
 W=[[[exact(x) for x in line] for line in mat] for mat in p['W']]
 b=[[exact(x) for x in line] for line in p['b']]
 v=[exact(x) for x in p['v']];c=exact(p['c'])
 def step(h,t):
  return tuple(tanh(sum((W[t][j][i]*h[i] for i in range(3)),b[t][j])) for j in range(3))
 def logit(h):return sum((v[i]*h[i] for i in range(3)),c)
 return step,logit
def proof(row,cert):
 step,logit=model(row)
 boxes={}
 for label,record in cert['boxes'].items():
  q,s=label.split(':')
  boxes[(int(q),s)]=tuple(iv.mpf([record['lo'][j],record['hi'][j]]) for j in range(3))
 assert len(boxes)==5 and cert['k']==1
 def good(q,h):
  z=logit(h)
  return z.a>0 if q else z.b<0
 h0=(iv.mpf('.5'),iv.mpf('-.5'),iv.mpf('.25'))
 for t in range(3):
  h=step(h0,t);q=int(t==1)
  assert good(q,h)
  box=boxes[(q,str(t))]
  assert all(h[j].a>=box[j].a and h[j].b<=box[j].b for j in range(3))
 for (q,s),h in boxes.items():
  assert good(q,h)
  for t in range(3):
   nq=0 if t==2 else q^(t==1)
   dest=boxes[(nq,str(t))];nh=step(h,t)
   assert all(nh[j].a>=dest[j].a and nh[j].b<=dest[j].b for j in range(3))
 return 45
if __name__=='__main__':
 assert proof(rows[100],cert)==45
 step,logit=model(rows[50])
 h=(iv.mpf('.5'),iv.mpf('-.5'),iv.mpf('.25'))
 for t in (1,1):h=step(h,t)
 assert logit(h).a>0
 print('PASS Run226: all-length certificate at epoch100 and incorrect witness at epoch50')
