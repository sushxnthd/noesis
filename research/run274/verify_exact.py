#!/usr/bin/env python3
"""Exact dyadic certificate audit; public 18 positive and 9 negative checkpoints."""
import json
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
B=json.loads((P/'baseline_epoch500.json').read_text())
A=json.loads((P/'adverse_epoch500_part1.json').read_text())
def q(x):return F(*float(x).as_integer_ratio())
def unpack(p):return list(map(q,p[0])),list(map(q,p[1])),q(p[2]),q(p[3])
def positive(p):
 a,b,v,c=unpack(p);L=max(F(0),b[2]);U=b[1]
 return all((v>0,c<0,L>=0,U>L,v*L+c<0,v*U+c>0,a[0]>=0,
 a[0]*L+b[0]<=L,a[0]*U+b[0]>=U,a[1]>=0,b[1]>=U,a[2]<=0,b[2]<=L))
def negative(p):
 a,b,v,c=unpack(p)
 if not(a[0]>1 and a[2]>0 and v>0 and c<0):return None
 fixed=-b[0]/(a[0]-1);h=max(F(0),b[1])
 if not(fixed>=0 and h>fixed):return None
 def wrong(z):return v*max(F(0),a[2]*z+b[2])+c>0
 n=0
 while not wrong(h) and n<1000:
  h=max(F(0),a[0]*h+b[0]);n+=1
 if not wrong(h):return None
 assert h==fixed+a[0]**n*(max(F(0),b[1])-fixed)
 assert n==0 or not wrong(fixed+a[0]**(n-1)*(max(F(0),b[1])-fixed))
 return n
expected={'19403':31,'19405':18,'19406':25,'19408':21,'19410':18,'19412':20,'19413':20,'19421':25,'19425':21}
assert len(B)==18 and set(A)==set(expected)
for seed,p in B.items():
 assert positive(p),seed
 mutant=json.loads(json.dumps(p));mutant[0][2]=abs(mutant[0][2])+0.1
 assert not positive(mutant)
for seed,p in A.items():
 assert negative(p)==expected[seed],seed
 mutant=json.loads(json.dumps(p));mutant[0][2]=-abs(mutant[0][2])-0.1
 assert negative(mutant) is None
print('EXACT_PASS 18 positive, 9 negative all-future; 27 mutations rejected')
