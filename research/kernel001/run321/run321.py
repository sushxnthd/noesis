#!/usr/bin/env python3
"""Run321 exact delayed-collision census on original Run315 trained checkpoints."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
N=64
SHA="72a273a42258e55f1092dc26664fd91777a8d2e56d6d598469e2abc0e63fab20"

def step(h,A,b,x):
 return tuple(max(F(0),sum(A[x][i][j]*h[j] for j in range(3))+b[x][i]) for i in range(3))

def collision(params):
 z=[F.from_float(float(v)) for v in params]
 assert len(z)==28
 A=[[[z[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
 b=[[z[18+3*x+i] for i in range(3)] for x in (0,1)]
 a=(F(0),)*3
 q=step(a,A,b,1)
 for n in range(1,N+1):
  a=step(a,A,b,0)
  if a==q:return {'n':n,'state':[str(v) for v in a]}
  q=step(q,A,b,0)
 return None

def main():
 cp=ROOT/'checkpoints315.json'
 assert hashlib.sha256(cp.read_bytes()).hexdigest()==SHA
 lab=ROOT/'results315.json'
 if not lab.exists():lab=ROOT/'portable_results315.json'
 labels={x['seed']:x['outcome'] for x in json.loads(lab.read_text())['rows']}
 rows=[]
 for r in json.loads(cp.read_text())['rows']:
  if r['epoch'] not in (20,80):continue
  rows.append({'seed':r['seed'],'epoch':r['epoch'],'prior_label':labels[r['seed']],
               'first_collision':collision(r['p'])})
 new=[r for r in rows if r['epoch']==80 and r['prior_label']=='unresolved'
      and r['first_collision'] and 11<=r['first_collision']['n']<=64]
 result={'run':321,'max_n':N,'checkpoint_sha256':SHA,'label_sha256':hashlib.sha256(lab.read_bytes()).hexdigest(),
         'epoch20_collisions':sum(bool(r['first_collision']) for r in rows if r['epoch']==20),
         'epoch80_collisions':sum(bool(r['first_collision']) for r in rows if r['epoch']==80),
         'late_unresolved_new_collisions':len(new),'criterion_pass':bool(new),'rows':rows}
 (ROOT/'results321.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
