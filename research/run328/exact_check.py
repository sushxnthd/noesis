"""Run328 independent exact witness verifier."""
from fractions import Fraction as Q

def first_wrong(p, word):
    z = [Q.from_float(float(x)) for x in p]
    h = [Q(0)] * 3
    label = 0
    for n, symbol in enumerate(word, 1):
        x = int(symbol)
        label |= x
        h = [max(Q(0), sum(z[9*x+3*i+j]*h[j] for j in range(3)) + z[18+3*x+i]) for i in range(3)]
        y = sum(z[24+i]*h[i] for i in range(3)) + z[27]
        if (y > 0) != bool(label):
            return n
    return None
