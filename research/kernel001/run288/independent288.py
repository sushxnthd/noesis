#!/usr/bin/env python3
"""Independent SymPy corner checker, separate from Fraction verifier."""
import json
from pathlib import Path
from sympy import Rational,Integer
P=Path(__file__).resolve().parent
D=json.loads((P/'checkpoints288.json').read_text())
R={(x['seed'],x['epoch']):x['p'] for x in D['rows']}
O=json.loads((P/'outcomes288.json').read_text())
def check(p,box):
 p=[Rational(float(x)) for x in p]
 L=[[Rational(float(x)) for x in z] for z in box['L']]
 U=[[Rational(float(x)) for x in z] for z in box['U']]
 assert all(L[0][j]<=0<=U[0][j] for j in (0,1))
 for s in (0,1):
  for x in (0,1):
   nxt=0 if x==0 else 1-s
   for i in (0,1):
    vals=[]
    for a in (L[s][0],U[s][0]):
     for b in (L[s][1],U[s][1]):
      vals.append(max(Integer(0),p[4*x+2*i]*a+p[4*x+2*i+1]*b+p[8+2*x+i]))
    assert min(vals)>=L[nxt][i] and max(vals)<=U[nxt][i]
  logits=[]
  for a in (L[s][0],U[s][0]):
   for b in (L[s][1],U[s][1]):logits.append(p[12]*a+p[13]*b+p[14])
  assert (max(logits)<0) if s==0 else (min(logits)>0)
def witness(p,w):
 p=[Rational(float(x)) for x in p];h=[Integer(0),Integer(0)];s=0
 for t,c in enumerate(w,1):
  x=int(c)
  h=[max(Integer(0),p[4*x+2*i]*h[0]+p[4*x+2*i+1]*h[1]+p[8+2*x+i]) for i in (0,1)]
  s=0 if x==0 else 1-s
  if (p[12]*h[0]+p[13]*h[1]+p[14]>0)!=bool(s):return t
 return None
counts={'certified':0,'witnessed':0}
for row in O['rows']:
 for epoch in (20,40,80,120):
  d=row[f'epoch{epoch}'];p=R[(row['seed'],epoch)]
  if d['certificate']:check(p,d['certificate']);counts['certified']+=1
  if d['witness']:
   assert witness(p,d['witness']['word'])==d['witness']['length'];counts['witnessed']+=1
  assert not (d['certificate'] and d['witness'])
print('INDEPENDENT_SYMPY_PASS',counts)
assert counts=={'certified':141,'witnessed':378}
