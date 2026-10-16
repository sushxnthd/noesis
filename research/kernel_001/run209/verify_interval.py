"""Outward interval verifier; all parameters interpreted as exact binary64 rationals."""
from fractions import Fraction
from mpmath import iv
iv.dps=85
def q(z):
 a=Fraction.from_float(float(z))
 return iv.mpf(a.numerator)/iv.mpf(a.denominator)
def step(h,w,b):return 1-2/(1+iv.exp(2*(w*h+b)))
def hull(v):
 lo=v[0].a;hi=v[0].b
 for x in v[1:]:
  if bool(x.a<lo):lo=x.a
  if bool(x.b>hi):hi=x.b
 return iv.mpf([lo,hi])
def dest(t,s):return 0 if t==2 else s^(t==1)
def prove_first_error(row,n,word):
 p=row['params'];w=list(map(q,p['w']));b=list(map(q,p['b']));v=q(p['v']);c=q(p['c'])
 cur=[iv.mpf('.5'),None]
 for k in range(1,n):
  nxt=[[],[]]
  for s in range(2):
   if cur[s] is None:continue
   for t in range(3):nxt[dest(t,s)].append(step(cur[s],w[t],b[t]))
  cur=[hull(z) if z else None for z in nxt]
  for s in range(2):
   if cur[s] is None:continue
   y=v*cur[s]+c
   assert bool(y.b<0 if s==0 else y.a>0),(row['seed'],k,s,str(y))
 h=iv.mpf('.5');s=0
 for t in word:h=step(h,w[t],b[t]);s=dest(t,s)
 y=v*h+c
 assert bool(y.a>0 if s==0 else y.b<0),(row['seed'],n,str(y))
 return {'first_error':n,'witness':word,'expected':s,'interval_logit':str(y)}
def prove_all(row,boxes):
 p=row['params'];w=list(map(q,p['w']));b=list(map(q,p['b']));v=q(p['v']);c=q(p['c'])
 B=[iv.mpf(pair) for pair in boxes]
 def inside(h,t):return bool(h.a>=B[t].a and h.b<=B[t].b)
 for t in range(3):assert inside(step(iv.mpf('.5'),w[t],b[t]),dest(t,0))
 for s in range(2):
  y=v*B[s]+c
  assert bool(y.b<0 if s==0 else y.a>0)
  for t in range(3):assert inside(step(B[s],w[t],b[t]),dest(t,s))
 return {'all_length_correct':True,'boxes':boxes}
