"""Run170 exact first-failure certificate; standard library only.
Usage: python run170_cert.py path/to/w3_seed406.json
"""
import json,sys
from fractions import Fraction as F
from decimal import Decimal as D,localcontext,ROUND_FLOOR,ROUND_CEILING

def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def mv(A,x):return [dot(row,x) for row in A]
def mm(A,B):return [[dot(row,col) for col in zip(*B)] for row in A]
def plus(a,b):return [x+y for x,y in zip(a,b)]
def step(A,E,h,t):return [max(F(0),v) for v in plus(mv(A,h),E[t])]
class I:
 def __init__(self,a,b=None):self.a=a;self.b=a if b is None else b
 @classmethod
 def of(cls,x):
  with localcontext() as c:c.prec=100;c.rounding=ROUND_FLOOR;lo=D(x.numerator)/D(x.denominator)
  with localcontext() as c:c.prec=100;c.rounding=ROUND_CEILING;hi=D(x.numerator)/D(x.denominator)
  return cls(lo,hi)
 def __add__(self,o):
  with localcontext() as c:c.prec=100;c.rounding=ROUND_FLOOR;lo=self.a+o.a
  with localcontext() as c:c.prec=100;c.rounding=ROUND_CEILING;hi=self.b+o.b
  return I(lo,hi)
 def __mul__(self,o):
  with localcontext() as c:c.prec=100;c.rounding=ROUND_FLOOR;lo=min(x*y for x in (self.a,self.b) for y in (o.a,o.b))
  with localcontext() as c:c.prec=100;c.rounding=ROUND_CEILING;hi=max(x*y for x in (self.a,self.b) for y in (o.a,o.b))
  return I(lo,hi)
def imul(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),I(D(0))) for j in range(len(B[0]))] for i in range(len(A))]
def power(A,k):
 n=len(A);R=[[I(D(int(i==j))) for j in range(n)] for i in range(n)]
 while k:
  if k&1:R=imul(R,A)
  k//=2
  if k:A=imul(A,A)
 return R

def prove(path):
 p=json.loads(open(path).read(),parse_float=D)[0]['parameters']
 A=[[F(v) for v in row] for row in p['A']];E=[[F(v) for v in row] for row in p['E']];w=[F(v) for v in p['w']]
 h=[F(0)]*3
 for _ in range(6):h=step(A,E,h,0)
 h0=h[:];z0=plus(mv(A,h),E[0]);z1=plus(mv(A,step(A,E,h,0)),E[1]);assert [int(v>0) for v in z0]==[1,1,0] and [int(v>0) for v in z1]==[1,1,0]
 T=[[A[i][j] if i<2 else F(0) for j in range(3)] for i in range(3)]
 M=mm(T,T);b=plus(mv(T,[E[0][0],E[0][1],F(0)]),[E[1][0],E[1][1],F(0)])
 d=plus(step(A,E,step(A,E,h,0),1),[-v for v in h]);hs=[h[:]]
 for k in range(4):
  assert dot(w,d)<0 and d[1]<0,(k,'early increment')
  hs.append(plus(hs[-1],d));d=mv(M,d)
 r=F(1,100)
 assert d[0]>0 and d[1]<0 and d[2]==0 and d[0]<r*(-d[1])
 assert M[0][0]>=0 and M[0][1]<0 and M[1][0]<0 and M[1][1]>0
 assert M[0][0]*r-M[0][1]<=r*M[1][1] and w[0]<0 and w[1]>0
 # Cone induction proves all subsequent output increments negative and h2 decreasing.
 Q=[[M[i][j] if j<3 else b[i] for j in range(4)] for i in range(3)]+[[F(0),F(0),F(0),F(1)]]
 Q=[[I.of(x) for x in row] for row in Q];v=[I.of(x) for x in h0]+[I.of(F(1))]
 def at(k):
  B=power(Q,k);hk=[sum((B[i][j]*v[j] for j in range(4)),I(D(0))) for i in range(3)]
  e=sum((I.of(w[i])*hk[i] for i in range(3)),I(D(0)))+I(D(-6))
  return hk,e
 _,e7900=at(7900);h7901,e7901=at(7901)
 assert -F(1,10)<dot(w,h0)-6<F(1,10)
 assert e7900.a>D('-.1') and e7900.b<D('.1') and e7901.b<D('-.1')
 assert h7901[1].a>D('5.68') and h0[1]<F(579,100)
 upper=hs[4][0]+r*(hs[4][1]-F(h7901[1].a))
 assert min(x[0] for x in hs)>F(18,100) and max(upper,max(x[0] for x in hs))<F(20,100)
 # All affine-orbit states k<=7901 lie inside rectangle; check both ReLU masks at its corners.
 for x in (F(18,100),F(20,100)):
  for y in (F(568,100),F(579,100)):
   a=plus(mv(A,[x,y,F(0)]),E[0]);c=plus(mv(A,[a[0],a[1],F(0)]),E[1])
   assert a[0]>0 and a[1]>0 and a[2]<0 and c[0]>0 and c[1]>0 and c[2]<0
 return {'first_failure_cycle':7901,'strict_monotonicity_proven':True,'all_masks_proven':True,'error7900':[str(e7900.a),str(e7900.b)],'error7901':[str(e7901.a),str(e7901.b)],'h2_7901':[str(h7901[1].a),str(h7901[1].b)]}
if __name__=='__main__':print(json.dumps(prove(sys.argv[1]),indent=2))
