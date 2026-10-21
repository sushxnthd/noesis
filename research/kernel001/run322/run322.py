#!/usr/bin/env python3
"""Run322 exact original-head zero-tail audit; requires Run315 public checkpoint artifact."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
SHA='72a273a42258e55f1092dc26664fd91777a8d2e56d6d598469e2abc0e63fab20'

def parse(p):
 z=[F.from_float(float(v)) for v in p]
 assert len(z)==28
 A=[[[z[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
 b=[[z[18+3*x+i] for i in range(3)] for x in (0,1)]
 return A,b,z[24:27],z[27]

def step(h,A,b,x):
 return tuple(max(F(0),sum(A[x][i][j]*h[j] for j in range(3))+b[x][i]) for i in range(3))

def audit(p,nmax=128):
 A,b,w,c=parse(p)
 z=(F(0),)*3
 o=step(z,A,b,1)
 first=None;tail=None;tie=None
 for n in range(1,nmax+1):
  z=step(z,A,b,0)
  l0=sum((w[i]*z[i] for i in range(3)),c)
  l1=sum((w[i]*o[i] for i in range(3)),c)
  wrong0=l0>0;wrong1=l1<0
  if wrong0 or wrong1:
   witness={'n':n,'class':0 if wrong0 else 1,'logit':str(l0 if wrong0 else l1),
            'word':'0'*n if wrong0 else '1'+'0'*(n-1)}
   if first is None:first=witness
   if n>=11 and tail is None:tail=witness
  if tie is None and (l0==0 or l1==0):tie={'n':n,'class':0 if l0==0 else 1}
  o=step(o,A,b,0)
 return {'first_error':first,'first_tail_error':tail,'first_tie':tie}

def main():
 cp=ROOT/'checkpoints315.json'
 assert hashlib.sha256(cp.read_bytes()).hexdigest()==SHA
 labels=ROOT/'results315.json'
 if not labels.exists():labels=ROOT/'portable_results315.json'
 outcome={r['seed']:r['outcome'] for r in json.loads(labels.read_text())['rows']}
 rows=[]
 for r in json.loads(cp.read_text())['rows']:
  if r['epoch']!=80:continue
  rows.append({'seed':r['seed'],'prior_label':outcome[r['seed']],**audit(r['p'])})
 new=[r for r in rows if r['prior_label']=='unresolved' and r['first_tail_error']]
 certified_errors=[r for r in rows if r['prior_label']=='certified' and r['first_error']]
 result={'run':322,'max_n':128,'checkpoint_sha256':SHA,
         'new_unresolved_tail_errors':len(new),'new_seeds':[r['seed'] for r in new],
         'certified_errors':len(certified_errors),'criterion_pass':bool(new) and not certified_errors,
         'rows':rows}
 (ROOT/'results322.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
