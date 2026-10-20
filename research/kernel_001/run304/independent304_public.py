#!/usr/bin/env python3
"""Independent rational checker of Run304, not importing certificate search."""
import json
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent
def logit(p,word):
 a=list(map(Q.from_float,p));h=[Q(0)]*3
 for ch in word:
  x=int(ch)
  h=[max(Q(0),sum(a[9*x+3*i+j]*h[j] for j in range(3))+a[18+3*x+i]) for i in range(3)]
 return sum(a[24+i]*h[i] for i in range(3))+a[27]
def prove(p,cert):
 a=list(map(Q.from_float,p));v=a[24:27];c=a[27]
 T=Q(cert['T']);mu=list(map(Q,cert['mu']))
 if not (T>0 and c<0 and T+c>0 and min(v)>=0 and max(v)>0):return False
 if max(a[18:21])>0:return False
 if sum(v[i]*max(Q(0),a[21+i]) for i in range(3))<T:return False
 for x in range(2):
  if mu[x]<0:return False
  for j in range(3):
   if sum(v[i]*a[9*x+3*i+j] for i in range(3))<mu[x]*v[j]:return False
  if mu[x]*T+sum(v[i]*a[18+3*x+i] for i in range(3))<T:return False
 return True
def main():
 d=json.loads((P/'results304.json').read_text());c=json.loads((P/'selected_checkpoints304.json').read_text())
 assert len(d['rows'])==len(c)==18
 mutations=0
 for r,entry in zip(d['rows'],c):
  assert r['seed']==entry['seed']
  p=entry['epoch20']['p'];q=entry['epoch80']['p'];w=r['early_witness']
  assert w is not None and 1<=len(w)<=6 and (logit(p,w)>0)!=('1' in w)
  cert=r['epoch80_certificate'];assert prove(q,cert)
  for i,val in [(18,0.25),(27,0.25),(24,-2.0)]:
   corrupt=q.copy();corrupt[i]=val
   assert not prove(corrupt,cert);mutations+=1
  corrupt=dict(cert);corrupt['T']='0';assert not prove(q,corrupt);mutations+=1
 assert d['summary']['exact_transition_pairs']==18
 print('INDEPENDENT304',json.dumps({'pairs':18,'early_exact_wrong':18,'late_all_length_correct':18,'mutation_controls_rejected':mutations}))
if __name__=='__main__':main()
