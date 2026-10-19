import itertools
from fractions import Fraction as F
from independent import verify
import sympy as S

def verify_box(p):
    eps=F(1,4096)
    for signs in itertools.product((-1,1),repeat=8):
        q=[S.Rational(str(x+s*eps)) for x,s in zip(p,signs)]
        assert verify(q)
    return True
