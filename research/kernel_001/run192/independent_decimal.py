"""Independent proof with directed Decimal intervals (no mpmath)."""
import json
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,Context,localcontext,ROUND_FLOOR,ROUND_CEILING
from sympy import Matrix,Rational
R=Path(__file__).resolve().parent
LO=Context(prec=80,rounding=ROUND_FLOOR)
HI=Context(prec=80,rounding=ROUND_CEILING)
NE=Context(prec=80)
class I:
 def __init__(self,a,b=None):
  self.a=D(a);self.b=D(b) if b is not None else self.a
  assert self.a<=self.b
 def __add__(x,y):
  y=cast(y)
  with localcontext(LO):a=x.a+y.a
  with localcontext(HI):b=x.b+y.b
  return I(a,b)
 __radd__=__add__
 def __neg__(x):return I(-x.b,-x.a)
 def __sub__(x,y):return x+-cast(y)
 def __mul__(x,y):
  y=cast(y)
  with localcontext(LO):a=min(u*v for u in (x.a,x.b) for v in (y.a,y.b))
  with localcontext(HI):b=max(u*v for u in (x.a,x.b) for v in (y.a,y.b))
  return I(a,b)
 __rmul__=__mul__
 def __truediv__(x,y):
  y=cast(y);assert y.a*y.b>0
  with localcontext(LO):a=min(D(1)/y.a,D(1)/y.b)
  with localcontext(HI):b=max(D(1)/y.a,D(1)/y.b)
  return x*I(a,b)
 def exp(x):
  with localcontext(NE):return I(x.a.exp().next_minus(),x.b.exp().next_plus())
 def absup(x):return max(abs(x.a),abs(x.b))
def cast(x):return x if isinstance(x,I) else I(x)
def q(v):
 f=F(v)
 with localcontext(LO):a=D(f.numerator)/D(f.denominator)
 with localcontext(HI):b=D(f.numerator)/D(f.denominator)
 return I(a,b)
def load(epoch):
 path=R/("seed163_epoch600_params.json" if epoch==600 else "../run191/seed163_epoch300_params.json")
 def cv(v):return [cv(z) for z in v] if isinstance(v,list) else q(F.from_float(float(v)))
 return {k:cv(v) for k,v in json.loads(path.read_text()).items()}
def dot(a,b):return sum((x*y for x,y in zip(a,b)),I(0))
def step(h,p,bit):
 return [I(1)-I(2)/(I(1)+(I(2)*(dot(p["W"][i],h)+p["U"][bit][i]+p["b"][i])).exp()) for i in range(8)]
def out(h,p):return dot(p["v"],h)+p["c"]
def run():
 p=load(600);cfg=json.loads((R/"candidate_box.json").read_text())
 C=[I(x) for x in cfg["center"]]
 A=Matrix([[Rational(str(v)) for v in row] for row in cfg["T"]]);B=A.inv()
 T=[[q(F(A[i,j])) for j in range(8)] for i in range(8)]
 S=[[q(F(B[i,j])) for j in range(8)] for i in range(8)]
 r=I(cfg["radius"]);h=[I(0)]*8
 for k in range(80):
  h=step(h,p,0);assert out(h,p).b<0
 assert all(dot(S[i],[h[j]-C[j] for j in range(8)]).absup()<r.a for i in range(8))
 WT=[[dot(p["W"][i],[T[k][j] for k in range(8)]) for j in range(8)] for i in range(8)]
 deriv=[]
 for i in range(8):
  u=dot(p["W"][i],C)+p["U"][0][i]+p["b"][i]
  e=sum((WT[i][j].absup()*r for j in range(8)),I(0))
  z=(I(2)*(u+I(-e.b,e.b))).exp()
  deriv.append(I(4)*z/((I(1)+z)*(I(1)+z)))
 f=step(C,p,0);norms=[]
 for i in range(8):
  v=sum((dot([S[i][k]*deriv[k] for k in range(8)],[WT[k][j] for k in range(8)]).absup() for j in range(8)),D(0))
  norms.append(v)
  assert dot(S[i],[f[j]-C[j] for j in range(8)]).absup()+v*r.b<r.a
 upper=out(C,p)+sum((dot(p["v"],[T[k][j] for k in range(8)]).absup()*r for j in range(8)),I(0))
 assert upper.b<0
 print(json.dumps({"independent":True,"epoch600_all_zero_lengths_correct":True,"max_norm":str(max(norms)),"output_upper":str(upper.b)}))
if __name__=="__main__":run()
