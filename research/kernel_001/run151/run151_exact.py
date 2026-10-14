from fractions import Fraction

def exact_witness(p,word):
    f=lambda x: Fraction(str(x))
    A=[[f(v) for v in row] for row in p["A"]]
    E=[[f(v) for v in row] for row in p["E"]]
    w=[f(v) for v in p["w"]]
    h=[Fraction(0) for _ in w]
    q=0
    for token in map(int,word):
        h=[max(Fraction(0),sum(a*v for a,v in zip(row,h))+E[token][j]) for j,row in enumerate(A)]
        q=max(0,q+(1,-1,0)[token])
    return sum(a*b for a,b in zip(h,w))-q
