from fractions import Fraction as F
import math

def dyadic(xs):
    return [F.from_float(float(x)) for x in xs]

def ceil64(q):
    x=float(q)
    return math.nextafter(x,math.inf) if F.from_float(x)<q else x

def repair(original):
    p=[float(x) for x in original]
    if p[2]>=0: p[2]=-1/1024
    if p[3]>=0: p[3]=-1/1024
    q=dyadic(p)
    if (q[0]-1)*q[4]+q[3]<=q[4]/1024 or q[0]<=1:
        p[0]=ceil64(1-q[3]/q[4]+F(1,128))
    return dyadic(p)

def mutants(p):
    for i in range(8):
        for direction in (-math.inf,math.inf):
            q=list(p)
            q[i]=F.from_float(math.nextafter(float(q[i]),direction))
            yield i, 'minus' if direction<0 else 'plus', q
