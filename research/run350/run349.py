"""Frozen Run349 word generator and exact rational state evaluator for Run350.
This compatibility module is intentionally colocated with the Run350 reproducer.
"""
from fractions import Fraction as F

def generate():
    words={format(i,f'0{n}b') for n in range(1,11) for i in range(2**n)}
    for n in range(65):
        words.update(('1'+'0'*n,'0'*n+'1'))
    for a in range(65):
        for b in range(65-a):
            words.add('1'+'0'*a+'1'+'0'*b)
            words.add('0'*a+'1'+'0'*b)
    for k in range(1,9):
        for n in range(65):
            words.add('1'*k+'0'*n)
            words.add('0'*n+'1'*k)
    words.discard('')
    return sorted(words,key=lambda w:(len(w),w))

def exact_states(p,words):
    p=[F.from_float(float(x)) for x in p]
    A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in range(2)]
    b=[p[18+3*x:21+3*x] for x in range(2)]
    cache={'':(F(0),F(0),F(0))}
    def state(w):
        if w not in cache:
            h=state(w[:-1]);x=int(w[-1])
            cache[w]=tuple(max(F(0),sum((A[x][i][j]*h[j] for j in range(3)),b[x][i])) for i in range(3))
        return cache[w]
    return [state(w) for w in words]
