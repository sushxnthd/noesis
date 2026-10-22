"""Independent exact Run349 proof checker; no LP is used for witnesses."""
import json
from pathlib import Path
from fractions import Fraction as Q
import sympy as S

P=Path(__file__).resolve().parent
WITNESSES={
 81:['000000000000000010','000100000000000000','101000000000000000'],
 82:['00000000000000000000010','00000000000000000000011',
     '00000000000000000000111','10100000000000000000000'],
}
def weights(epoch):
    d=json.loads((P/f'checkpoint_32135_{epoch}.json').read_text())
    assert d['seed']==32135 and d['epoch']==epoch and len(d['p'])==28
    return d['p']
def states(p,words):
    p=[S.Rational(*Q.from_float(float(z)).as_integer_ratio()) for z in p]
    A=[S.Matrix(3,3,p[9*x:9*x+9]) for x in range(2)]
    b=[S.Matrix(p[18+3*x:21+3*x]) for x in range(2)]
    cache={'':S.zeros(3,1)}
    def h(w):
        if w not in cache:
            t=A[int(w[-1])]*h(w[:-1])+b[int(w[-1])]
            cache[w]=S.Matrix([max(S.Integer(0),z) for z in t])
        return cache[w]
    return [h(w) for w in words]
def prove(epoch,words):
    H=states(weights(epoch),words)
    y=[w.count('1')%2 for w in words]
    M=S.Matrix([[int(t==1) for t in y],[int(t==0) for t in y]]
      +[[z[j]*(1 if label else -1) for z,label in zip(H,y)] for j in range(3)])
    alpha,free=M.gauss_jordan_solve(S.Matrix([1,1,0,0,0]))
    assert free.rows==0 and all(a>0 for a in alpha)
    assert M*alpha==S.Matrix([1,1,0,0,0])
    for j in range(3):
        qsum=sum(Q(int(a.p),int(a.q))*Q(int(h[j].p),int(h[j].q))*
            (1 if label else -1) for a,h,label in zip(alpha,H,y))
        assert qsum==0
    return [float(a) for a in alpha]
def main():
    from wordgen import generate
    for epoch,L in ((81,18),(82,23)):
        W=WITNESSES[epoch]
        assert all(w in generate(L) for w in W)
        alpha=prove(epoch,W)
        print('EXACT COLLISION',epoch,'L',L,'weights',alpha)
    import sys
    sys.path.insert(0,str(P.parent/'run340'))
    from cert340 import certificate
    assert certificate(weights(200)) is not None
    print('EXACT CERTIFIED ENDPOINT epoch 200')
if __name__=='__main__':main()
