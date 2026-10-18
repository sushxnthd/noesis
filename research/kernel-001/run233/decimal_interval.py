"""Independent directed Decimal interval arithmetic; exact binary64 inputs."""
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING,localcontext
P=90;F=Context(prec=P,rounding=ROUND_FLOOR);C=Context(prec=P,rounding=ROUND_CEILING)
class I:
 def __init__(self,lo,hi=None):
  self.lo=Decimal(lo);self.hi=Decimal(hi) if hi is not None else self.lo
  assert self.lo<=self.hi
 def __add__(self,o):
  o=asI(o);return I(F.add(self.lo,o.lo),C.add(self.hi,o.hi))
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,o):return self+-asI(o)
 def __rsub__(self,o):return asI(o)+-self
 def __mul__(self,o):
  o=asI(o);a=[F.multiply(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
  b=[C.multiply(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
  return I(min(a),max(b))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=asI(o);assert o.lo>0 or o.hi<0
  a=[F.divide(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
  b=[C.divide(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
  return I(min(a),max(b))
def asI(x):return x if isinstance(x,I) else I(x)
def exact(x):
 n,d=float(x).as_integer_ratio()
 return I(F.divide(Decimal(n),Decimal(d)),C.divide(Decimal(n),Decimal(d)))
def exp_point(y):
 with localcontext(Context(prec=P,rounding=ROUND_CEILING)):
  z=y.exp();eps=Decimal(2).scaleb(z.adjusted()-P+1)
 return I(F.subtract(z,eps),C.add(z,eps))
def tanh_interval(x):
 lo2=F.multiply(Decimal(2),x.lo);hi2=C.multiply(Decimal(2),x.hi)
 a=(exp_point(lo2)-I(1))/(exp_point(lo2)+I(1))
 b=(exp_point(hi2)-I(1))/(exp_point(hi2)+I(1))
 return I(a.lo,b.hi)
