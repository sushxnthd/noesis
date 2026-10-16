"""Sound exact-real tanh bounds: float64 parameters -> Fraction, outward Decimal.exp."""
from fractions import Fraction as Q
from decimal import Decimal as D,Context,localcontext,ROUND_FLOOR,ROUND_CEILING
F=Context(prec=85,rounding=ROUND_FLOOR)
C=Context(prec=85,rounding=ROUND_CEILING)
def dec(q,ctx):
 with localcontext(ctx):return D(q.numerator)/D(q.denominator)
def bound(x,upper):
 ctx=C if upper else F
 with localcontext(ctx):
  z=dec(2*x,ctx)
  e=z.exp()
  e=e.next_plus(C).next_plus(C) if upper else e.next_minus(F).next_minus(F)
  den=e+D(1)
 with localcontext(F if upper else C):ratio=D(2)/den
 with localcontext(C if upper else F):out=D(1)-ratio
 return Q(out)
def f(x):return Q.from_float(float(x))
