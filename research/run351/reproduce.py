#!/usr/bin/env python3
"""Run351 frozen intervention transfer audit."""
import json,hashlib
from pathlib import Path
import numpy as np
R=Path(__file__).resolve().parent
S=R.parent/'run348'/'trajectories348.json'
EXPECTED='c74d2821ae8ae6ea568c1fee80fa11f704efcc62d31416b0d436fc4d1ca60403'
def words():
 w={format(i,f'0{n}b') for n in range(1,11) for i in range(2**n)}
 for n in range(65):w.update(('1'+'0'*n,'0'*n+'1'))
 for a in range(65):
  for b in range(65-a):w.update(('1'+'0'*a+'1'+'0'*b,'0'*a+'1'+'0'*b))
 for k in range(1,9):
  for n in range(65):w.update(('1'*k+'0'*n,'0'*n+'1'*k))
 return sorted((s for s in w if 0<len(s)<=23),key=lambda s:(len(s),s))
W=words();assert len(W)==2644
assert hashlib.sha256(('\n'.join(W)+'\n').encode()).hexdigest()=='401dcad6e544fcf455687caa444394e4ba2014c9a7009cd17778586855354e90'
PREF=sorted({w[:i] for w in W for i in range(1,len(w)+1)},key=lambda w:(len(w),w))
IX={w:i for i,w in enumerate(PREF)}
PA=[IX[w[:-1]] if len(w)>1 else -1 for w in PREF]
BT=[int(w[-1]) for w in PREF];WI=[IX[w] for w in W]
Y=np.array([w.count('1')%2 for w in W],dtype=bool)
def count(p):
 p=np.asarray(p);n=len(p);a=p[:,:18].reshape(n,2,3,3);b=p[:,18:24].reshape(n,2,3)
 h=np.zeros((len(PREF),n,3))
 for i,(j,x) in enumerate(zip(PA,BT)):
  z=h[j] if j>=0 else np.zeros((n,3))
  h[i]=np.maximum(np.einsum('nij,nj->ni',a[:,x],z)+b[:,x],0)
 logit=np.einsum('wnj,nj->wn',h[WI],p[:,24:27])+p[:,27]
 return (((logit>0)==Y[:,None])&(logit!=0)).sum(axis=0).tolist()
def main():
 raw=S.read_bytes();sha=hashlib.sha256(raw).hexdigest();assert sha==EXPECTED,sha
 data=json.loads(raw);d={s:{} for s in range(32000,32064)}
 for row in data['rows']:
  if row['seed'] in d:d[row['seed']][row['epoch']]=row
 rows=[]
 for s in range(32000,32064):
  r=d[s];assert len(r)==201
  t=next((t for t in range(200) if r[t]['accuracy']==1.0),None)
  if t is None:rows.append({'seed':s,'eligible':False});continue
  p=np.array(r[t]['p']);q=np.array(r[t+1]['p']);v=np.tile(p,(26,1));v[1]=q
  for j in range(24):v[2+j,j]=q[j]
  counts=count(v);g=[z-counts[0] for z in counts[2:]]
  rows.append({'seed':s,'eligible':True,'epoch':t,'counts':counts,
   'gain18':g[18],'best_gain':max(g),'best':[j for j,x in enumerate(g) if x==max(g)],
   'candidate':g[18]>=27 and all(g[18]>x for j,x in enumerate(g) if j!=18)})
 out={'run':351,'source_sha256':sha,'rows':rows,'eligible':sum(x['eligible'] for x in rows),
  'N':sum(x.get('candidate',False) for x in rows)}
 assert out['eligible']==29 and out['N']==0
 assert next(r for r in rows if r['seed']==32046)['gain18']==9
 assert next(r for r in rows if r['seed']==32034)['best_gain']==107
 (R/'outcomes.json').write_text(json.dumps(out,indent=2)+'\n')
 print('Frozen transfer FAILED: N=',out['N'],'of required 3; eligible=',out['eligible'])
if __name__=='__main__':main()
