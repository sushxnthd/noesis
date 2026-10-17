"""Rigorous Run225 standalone checker for one gradient-trained RNN checkpoint.

Independent 4D mpmath.iv evaluation and exact-dyadic/directed-Decimal
interval evaluation of tanh. No numerical heuristic is trusted as a proof.
"""
import json
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from mpmath import iv
R=Path(__file__).resolve().parent
p=json.loads((R/'CHECKPOINT_1409_E100.json').read_text())['params']
K=2**24; delta=Fraction(1,2**20)
iv.dps=75

def i_exact(x):
    n,d=float(x).as_integer_ratio();return iv.mpf(n)/iv.mpf(d)
def i_tanh(x):
    a,b=iv.exp(2*x.a),iv.exp(2*x.b)
    return iv.mpf([((a-1)/(a+1)).a,((b-1)/(b+1)).b])
def four_dim(d,k):
    h=[iv.mpf('.5'),iv.mpf('-.5'),iv.mpf('.25'),iv.mpf(0)]
    W=[[i_exact(p['W'][0][j][q]) if j<3 and q<3 else iv.mpf(0) for q in range(4)] for j in range(4)]
    b=[i_exact(x) for x in p['b'][0]]+[iv.mpf(d.numerator)/d.denominator]
    h=[i_tanh(sum((W[j][q]*h[q] for q in range(4)),b[j])) for j in range(4)]
    return sum((i_exact(p['v'][j])*h[j] for j in range(3)),i_exact(p['c'])+iv.mpf(k)*h[3])

P=100;F=Context(prec=P,rounding=ROUND_FLOOR);C=Context(prec=P,rounding=ROUND_CEILING)
def frac(x):return Fraction(*float(x).as_integer_ratio())
def dec(q):
    with localcontext(Context(prec=P)):
        return Decimal(q.numerator)/Decimal(q.denominator)
def exp_bounds(q):
    with localcontext(Context(prec=P)):
        mid=(dec(q)*2).exp()
    ulp=Decimal(2).scaleb(mid.adjusted()-P+1)
    return F.subtract(mid,ulp),C.add(mid,ulp)
def tanh_bounds(q):
    el,eh=exp_bounds(q)
    nl,nh=F.subtract(el,1),C.subtract(eh,1)
    dl,dh=F.add(el,1),C.add(eh,1)
    return (min(F.divide(n,d) for n in (nl,nh) for d in (dl,dh)),
            max(C.divide(n,d) for n in (nl,nh) for d in (dl,dh)))
def decimal_logit(d,k):
    h=[Fraction(1,2),Fraction(-1,2),Fraction(1,4)]
    lo=hi=dec(frac(p['c']))
    for j in range(3):
        s=sum((frac(p['W'][0][j][q])*h[q] for q in range(3)),frac(p['b'][0][j]))
        a,b=tanh_bounds(s);v=dec(frac(p['v'][j]))
        lo=F.add(lo,min(F.multiply(v,a),F.multiply(v,b)))
        hi=C.add(hi,max(C.multiply(v,a),C.multiply(v,b)))
    a,b=tanh_bounds(d)
    return F.add(lo,F.multiply(Decimal(k),a)),C.add(hi,C.multiply(Decimal(k),b))
def test():
    for d,k,positive in ((Fraction(0),K,False),(delta,K,True),(delta,0,False)):
        z=four_dim(d,k);a,b=decimal_logit(d,k)
        assert (z.a>0 if positive else z.b<0),(d,k,z)
        assert (a>0 if positive else b<0),(d,k,a,b)
    print('PASS independent rigorous 4D mpmath.iv and directed Decimal; trained checkpoint 1409 epoch100')
if __name__=='__main__':test()
