#!/usr/bin/env python3
"""Independent exact two-state checker and finite-perfect adversarial family."""
import json,hashlib
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
D=json.loads((P/'checkpoints282.json').read_text())
rows=D['rows']; index={(r['arm'],r['seed'],r['epoch']):r for r in rows}
def check(p):
 a0,a1,b0,b1,v,c=[F.from_float(float(z)) for z in p]
 if b1<=0:return False
 states=(F(0),b1)
 for s in (0,1):
  h=states[s]
  if (v*h+c>0)!=bool(s):return False
  for x in (0,1):
   h2=max(F(0),(a0 if x==0 else a1)*h+(b0 if x==0 else b1))
   if h2!=states[0 if x==0 else 1-s]:return False
 return True
def replay(p,n):
 a0,a1,b0,b1,v,c=[F.from_float(float(z)) for z in p]
 h=F(0);bad=[]
 for k in range(1,n+1):
  h=max(F(0),a1*h+b1)
  if (v*h+c>0)!=(k%2==1):bad.append(k)
 return bad
counts={}
for arm in ('biased','neutral'):
 for epoch in (0,20,40,80,120,160):
  group=[r for r in rows if r['arm']==arm and r['epoch']==epoch]
  counts[f'{arm}_{epoch}']={'sampled_perfect':sum(r['accuracy']==1 for r in group),'certified':sum(check(r['p']) for r in group)}
assert counts['neutral_0']['certified']==0
neutral=[s for s in D['config']['seeds'] if check(index['neutral',s,160]['p'])]
assert len(neutral)>=5
# Independently verify all 25 initial models have a short exact counterexample.
for seed in neutral:
 p=index['neutral',seed,0]['p']
 assert not check(p)
 a0,a1,b0,b1,v,c=[F.from_float(float(z)) for z in p]
 found=False
 for n in range(1,5):
  from itertools import product
  for w in product((0,1),repeat=n):
   h=F(0);y=0
   for x in w:
    h=max(F(0),(a0 if x==0 else a1)*h+(b0 if x==0 else b1))
    y=0 if x==0 else 1-y
    if (v*h+c>0)!=bool(y):found=True;break
   if found:break
  if found:break
 assert found,(seed,'no exact initial witness')
# The five late finite-perfect spoof cases were discovered after heldout training.
late=[(20575,20,40,14),(20531,40,80,17),(20547,40,80,9),(20561,80,120,36),(20567,120,160,244)]
for seed,earlier,later,n in late:
 old=index['neutral',seed,earlier];new=index['neutral',seed,later]
 assert old['accuracy']==new['accuracy']==1
 assert not check(old['p']) and check(new['p'])
 a0,a1,b0,b1,v,c=[F.from_float(float(z)) for z in old['p']]
 assert -1<a1<0 and b1>0 and v>0
 lim=b1/(1-a1); threshold=-c/v
 assert threshold!=lim
 assert (threshold<lim)==(n%2==0)
 assert replay(old['p'],n-1)==[]
 assert replay(old['p'],n)==[n]
 assert replay(old['p'],n+2)==[n,n+2]
 assert replay(new['p'],n+2)==[]
 # Monotone even/odd subsequences converge to lim; all later same-parity n+2k fail.
for seed in neutral:
 p=index['neutral',seed,160]['p']
 a0,a1,b0,b1,v,c=p
 for mutation in ([a0,a1,b0,-abs(b1),v,c],[a0,a1,b0,b1,v,-v*b1-1]):
  assert not check(mutation)
out={'counts':counts,'neutral_initial_wrong_to_certified':len(neutral),'neutral_seeds':neutral,
 'late_finite_perfect_failures':late,'checkpoint_sha256':hashlib.sha256((P/'checkpoints282.json').read_bytes()).hexdigest()}
(P/'verification282.json').write_text(json.dumps(out,indent=2)+'\n')
print('EXACT AUDIT PASSED',len(neutral),'neutral acquisitions, 5 finite-perfect-to-certified transitions, 50 corruptions rejected')
print(json.dumps(counts,indent=2))
