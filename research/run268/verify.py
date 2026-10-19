"""Run268: long-horizon two-family evaluation and exact dual-checker verification.
This is NOT an all-length correctness verifier; survivors remain unresolved.
"""
import json,hashlib
from pathlib import Path
from fractions import Fraction as Q
import numpy as np
P=Path(__file__).resolve().parent
pred=json.loads((P/'FROZEN_PREDICTIONS.json').read_text())['rows']
CK={}
for d in (2,3):
 for r in json.loads((P/f'CHECKPOINTS_dim{d}.json').read_text())['rows']:
  if r['epoch']==600:CK[r['seed']]=r['params']
def scan(p,head,tail,N=2048):
 A=np.asarray(p['A']);E=np.asarray(p['E']);b=np.asarray(p['b']);v=np.asarray(p['v']);c=p['c']
 h=np.maximum(E[head]+b,0);first_hold=None;first_switch=None
 for n in range(N+1):
  g=np.maximum(A@h+E[tail]+b,0)
  if first_switch is None and int(v@g+c>0)!=int(tail==1):first_switch=n
  if n<N:
   h=np.maximum(A@h+E[0]+b,0)
   if first_hold is None and int(v@h+c>0)!=int(head==1):first_hold=n+1
  if not np.all(np.isfinite(h)):return {'switch':first_switch,'hold':first_hold,'nonfinite':n+1}
 return {'switch':first_switch,'hold':first_hold,'nonfinite':None}
def dyadic(p,word):
 vals=[x for row in p['A'] for x in row]+[x for row in p['E'] for x in row]+p['b']+p['v']+[p['c']]
 D=max(float(x).as_integer_ratio()[1] for x in vals)
 def z(x):
  n,d=float(x).as_integer_ratio();return n*(D//d)
 A=[[z(x) for x in row] for row in p['A']];E=[[z(x) for x in row] for row in p['E']]
 b=list(map(z,p['b']));v=list(map(z,p['v']));c=z(p['c']);d=len(b)
 H=[0]*d;scale=1;q=0;first=None
 for t,s in enumerate(word,1):
  q=1 if s==1 else 0 if s==2 else q
  H=[max(0,sum(A[i][j]*H[j] for j in range(d))+(E[s][i]+b[i])*scale) for i in range(d)]
  scale*=D;zz=sum(v[j]*H[j] for j in range(d))+c*scale
  if first is None and int(zz>0)!=q:first=t
 return first
def fraction(p,word):
 A=[[Q.from_float(x) for x in row] for row in p['A']]
 E=[[Q.from_float(x) for x in row] for row in p['E']]
 b=list(map(Q.from_float,p['b']));v=list(map(Q.from_float,p['v']));c=Q.from_float(p['c']);d=len(b)
 h=[Q(0)]*d;q=0;first=None
 for t,s in enumerate(word,1):
  q=1 if s==1 else 0 if s==2 else q
  h=[max(Q(0),sum(A[i][j]*h[j] for j in range(d))+E[s][i]+b[i]) for i in range(d)]
  if first is None and int(sum(v[j]*h[j] for j in range(d))+c>0)!=q:first=t
 return first
out=[];count=0
for r in pred:
 p=CK[r['seed']];fams={}
 for head,tail in ((1,2),(2,1)):fams[f'{head}to{tail}']=scan(p,head,tail)
 errors=[]
 for key,f in fams.items():
  head,tail=map(int,key.split('to'))
  if f['hold'] is not None:errors.append((f['hold']+1,[head]+[0]*f['hold'],'hold'))
  if f['switch'] is not None:errors.append((f['switch']+2,[head]+[0]*f['switch']+[tail],'switch'))
 errors.sort(key=lambda z:z[0])
 exact=None
 if r['train_accuracy']==1 and errors:
  position,word,kind=errors[0]
  assert dyadic(p,word)==position and fraction(p,word)==position,(r['seed'],position,kind)
  exact={'position':position,'type':kind,'word_prefix':word[:1],'hold_count':len(word)-1-(kind=='switch'),'tail':word[-1] if kind=='switch' else None}
  count+=1;print('EXACT',r['seed'],exact,flush=True)
 early=any((f['hold'] is not None and f['hold']<=64) or (f['switch'] is not None and f['switch']<=64) for f in fams.values())
 delayed=any(f['switch'] is not None and 65<=f['switch']<=2048 for f in fams.values())
 out.append({'seed':r['seed'],'dimension':r['dimension'],'train_accuracy':r['train_accuracy'],'prediction':r['predict'],'baseline_spectral':r['baseline_spectral'],'early_error':early,'delayed_switch_error':delayed,'families':fams,'exact_witness':exact})
(P/'VERIFIED_OUTCOMES.json').write_text(json.dumps({'rows':out,'exact_independently_verified':count,'scope':'two switching families, 0..2048 holds; no all-length correctness claim'},indent=2)+'\n')
assert sum(r['train_accuracy']==1 for r in out)==13
assert count==12
assert sum(r['train_accuracy']==1 and r['delayed_switch_error'] for r in out)==2
print('PASS 12/13 finite-perfect exact failures; remaining model unresolved')
