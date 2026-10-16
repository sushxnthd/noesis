"""Independently verify three finite errors preceding all-length certificates."""
import csv
from pathlib import Path
from fractions import Fraction as Q
from mpmath import iv
from proof_core import bound,f
iv.dps=75
R=Path(__file__).resolve().parent
rows={}
for path in R.glob('CHECKPOINTS_*.csv'):
 seed=int(path.name.split('_')[1].split('.')[0])
 for r in csv.DictReader(path.open()):rows[seed,int(r['epoch'])]=r
def iq(s):
 x=f(s);return iv.mpf(x.numerator)/iv.mpf(x.denominator)
for seed,epoch,word in [(223,0,'0'),(227,50,'11'),(229,50,'10')]:
 r=rows[seed,epoch];w=[f(r['w0']),f(r['w1'])];b=[f(r['b0']),f(r['b1'])];v=f(r['v']);c=f(r['c'])
 lo=hi=Q(1,2);h=iv.mpf('0.5')
 for s in word:
  bit=int(s);a=w[bit]*(lo if w[bit]>=0 else hi)+b[bit];z=w[bit]*(hi if w[bit]>=0 else lo)+b[bit]
  lo,hi=bound(a,False),bound(z,True)
  h=1-2/(1+iv.exp(2*(iq(r['w'+str(bit)])*h+iq(r['b'+str(bit)]))))
 yl=v*(lo if v>=0 else hi)+c;yh=v*(hi if v>=0 else lo)+c
 y=iq(r['v'])*h+iq(r['c']);par=word.count('1')%2
 assert (yh<0 and bool(y.b<0)) if par else (yl>0 and bool(y.a>0))
 print(seed,epoch,word,'CERTIFIED_WRONG',float(yl),float(yh))
