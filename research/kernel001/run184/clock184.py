from fractions import Fraction as F
from research.kernel001.run184.weights184 import A,E,w,h0
a=A[1]
def clock(word):
 alpha,beta=F(1),F(0)
 for x in word:alpha,beta=a*alpha,a*beta+E[int(x)][1]
 assert 0<alpha<1
 fixed=beta/(1-alpha)
 for start in (h0,fixed):
  s=start
  for x in word:
   z=[A[i]*s+E[int(x)][i] for i in range(7)]
   assert z[1]>0 and all(z[i]<0 for i in range(7) if i!=1)
   s=z[1]
  assert s==alpha*start+beta
 def error(k):return w*(fixed+alpha**k*(h0-fixed))-6
 assert abs(error(0))<F(1,10)
 if abs(w*fixed-6)<=F(1,10):return None
 lo,hi=0,1
 while abs(error(hi))<=F(1,10):hi*=2
 while lo+1<hi:
  m=(lo+hi)//2
  if abs(error(m))>F(1,10):hi=m
  else:lo=m
 assert abs(error(hi-1))<=F(1,10)<abs(error(hi))
 return hi
