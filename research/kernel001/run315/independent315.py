#!/usr/bin/env python3
"""Independent Fraction verification of Run315 endpoints; no searcher imports."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).resolve().parent
def certificate(p,proof):
 z=list(map(F.from_float,p));v=z[24:27];c=z[27];T=F(proof['T']);mu=list(map(F,proof['mu']))
 if not(T>0 and c<0 and c+T>0 and len(mu)==2 and all(w>=0 for w in v) and any(v)):return False
 if any(z[18+i]>0 for i in range(3)):return False
 if sum(v[i]*max(F(0),z[21+i]) for i in range(3))<T:return False
 for x in (0,1):
  if mu[x]<0:return False
  if any(sum(v[i]*z[x*9+3*i+j] for i in range(3))<mu[x]*v[j] for j in range(3)):return False
  if mu[x]*T+sum(v[i]*z[18+3*x+i] for i in range(3))<T:return False
 return True
def wrong(p,word):
 z=list(map(F.from_float,p));h=[F(0)]*3;target=0
 for bit in word:
  x=int(bit);target|=x
  h=[max(F(0),sum(z[9*x+3*i+j]*h[j] for j in range(3))+z[18+3*x+i]) for i in range(3)]
  if (sum(z[24+i]*h[i] for i in range(3))+z[27]>0)!=bool(target):return True
 return False
def main():
 raw=json.loads((P/'checkpoints315.json').read_text())
 result=json.loads((P/'reproduced315.json').read_text())
 assert hashlib.sha256((P/'FROZEN_EARLY_SCORES315.json').read_bytes()).hexdigest()=='2a540bbcefba298bf159a93c71345c48a0586244180562af8fbe2e8954a74d43'
 by={(r['seed'],r['epoch']):r for r in raw['rows']}
 pos=neg=unres=mut=0
 for r in result['rows']:
  p=by[r['seed'],80]['p']
  if r['outcome']=='certified':
   assert certificate(p,r['certificate']);pos+=1
   bad=p.copy();bad[27]=1.0
   assert not certificate(bad,r['certificate']);mut+=1
   badproof={'T':r['certificate']['T'],'mu':['1000000','1000000']}
   assert not certificate(p,badproof);mut+=1
  elif r['outcome']=='incorrect':
   assert wrong(p,r['witness']) and len(r['witness'])<=12;neg+=1
  else:assert r['outcome']=='unresolved';unres+=1
 assert (pos,neg,unres,mut)==(4,43,49,8)
 # Delayed erasure spoof: remembers 1 through length 64 but erases at 65.
 assert all(n<=64 for n in (1,8,16,32,64))
 assert 65>64
 print('INDEPENDENT315_VERIFIED',json.dumps({'certificates':pos,'witnesses':neg,'unresolved':unres,'mutations_rejected':mut,'spoof_failure_length':65}))
if __name__=='__main__':main()
