"""Independent mpmath.iv interval verification of committed neural boxes."""
import csv
from fractions import Fraction
from pathlib import Path
from mpmath import iv
iv.dps=75
R=Path(__file__).resolve().parent
def q(s):
 x=Fraction.from_float(float(s));return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def check(r,c):
 w=[q(r['w0']),q(r['w1'])];b=[q(r['b0']),q(r['b1'])];v=q(r['v']);bias=q(r['c'])
 pairs=[(c['even_lo'],c['even_hi']),(c['odd_lo'],c['odd_hi'])]
 boxes=[iv.mpf(p) for p in pairs]
 def step(h,bit):return 1-2/(1+iv.exp(2*(w[bit]*h+b[bit])))
 def inside(h,p):return bool(h.a>=iv.mpf(p[0]).a and h.b<=iv.mpf(p[1]).b)
 for bit in (0,1):assert inside(step(iv.mpf('0.5'),bit),pairs[bit])
 for par in (0,1):
  y=v*boxes[par]+bias
  assert bool(y.a>0 if par else y.b<0)
  for bit in (0,1):assert inside(step(boxes[par],bit),pairs[par^bit])
if __name__=='__main__':
 rows={}
 for path in R.glob('CHECKPOINTS_*.csv'):
  seed=int(path.name.split('_')[1].split('.')[0])
  for r in csv.DictReader(path.open()):rows[seed,int(r['epoch'])]=r
 cert=list(csv.DictReader((R/'CERTIFICATES.csv').open()))
 for c in cert:check(rows[int(c['seed']),int(c['epoch'])],c)
 print('INDEPENDENT_CERTIFICATES_PASSED',len(cert))
