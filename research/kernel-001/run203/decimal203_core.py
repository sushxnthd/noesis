"""Directed Decimal interval arithmetic independent of mpmath."""
from decimal import Decimal,localcontext,ROUND_FLOOR,ROUND_CEILING,ROUND_HALF_EVEN
PREC=110
EPS=Decimal('1e-50')
def op(fn,mode):
 with localcontext() as ctx:
  ctx.prec=PREC;ctx.rounding=mode
  return fn()
class D:
 def __init__(self,lo,hi=None):self.lo=Decimal(lo);self.hi=Decimal(hi if hi is not None else lo)
 def __add__(self,other):
  other=asD(other)
  return D(op(lambda:self.lo+other.lo,ROUND_FLOOR),op(lambda:self.hi+other.hi,ROUND_CEILING))
 __radd__=__add__
 def __neg__(self):return D(-self.hi,-self.lo)
 def __sub__(self,other):return self+-asD(other)
 def __mul__(self,other):
  other=asD(other)
  return D(min(op(lambda:a*b,ROUND_FLOOR) for a in (self.lo,self.hi) for b in (other.lo,other.hi)),
           max(op(lambda:a*b,ROUND_CEILING) for a in (self.lo,self.hi) for b in (other.lo,other.hi)))
 __rmul__=__mul__
 def __truediv__(self,other):
  other=asD(other)
  assert other.lo>0 or other.hi<0
  return self*D(op(lambda:Decimal(1)/other.hi,ROUND_FLOOR),op(lambda:Decimal(1)/other.lo,ROUND_CEILING))
 def tanh(self):
  # For |2x|<70, 110-digit correctly rounded Decimal.exp error <1e-77.
  # The explicit 1e-50 inflation dominates rounding errors.
  assert max(abs(self.lo),abs(self.hi))<35
  def endpoint(x,mode):
   with localcontext() as ctx:
    ctx.prec=PREC;ctx.rounding=ROUND_HALF_EVEN
    e=(2*x).exp()
   e=D(e-EPS,e+EPS);y=(e-D(1))/(e+D(1))
   return y.lo if mode==ROUND_FLOOR else y.hi
  return D(endpoint(self.lo,ROUND_FLOOR),endpoint(self.hi,ROUND_CEILING))
def asD(v):return v if isinstance(v,D) else D(v)
def qfloat(f):
 n,d=float(f).as_integer_ratio()
 return D(op(lambda:Decimal(n)/Decimal(d),ROUND_FLOOR),op(lambda:Decimal(n)/Decimal(d),ROUND_CEILING))
