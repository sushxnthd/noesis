from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
P=70
F=Context(prec=P,rounding=ROUND_FLOOR)
C=Context(prec=P,rounding=ROUND_CEILING)
class I:
 def __init__(self,a,b=None):
  self.lo=D(a);self.hi=D(b) if b is not None else self.lo
  assert self.lo<=self.hi
 def __add__(self,o):
  o=conv(o);return I(F.add(self.lo,o.lo),C.add(self.hi,o.hi))
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,o):return self+-conv(o)
 def __mul__(self,o):
  o=conv(o);xs=[F.multiply(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)];ys=[C.multiply(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
  return I(min(xs),max(ys))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=conv(o);assert o.lo>0
  xs=[F.divide(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)];ys=[C.divide(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
  return I(min(xs),max(ys))
def conv(x):return x if isinstance(x,I) else I(x)
def exact(x):
 n,d=float(x).as_integer_ratio()
 return I(F.divide(D(n),D(d)),C.divide(D(n),D(d)))
def exppt(y):
 with localcontext(Context(prec=P,rounding=ROUND_CEILING)):
  z=y.exp();eps=D(2).scaleb(z.adjusted()-P+1)
 return I(F.subtract(z,eps),C.add(z,eps))
def tanh(x):
 a=exppt(F.multiply(D(2),x.lo));b=exppt(C.multiply(D(2),x.hi))
 return I(((a-I(1))/(a+I(1))).lo,((b-I(1))/(b+I(1))).hi)
