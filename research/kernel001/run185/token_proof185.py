"""Exact token-level inductive invariant for the two minimal safe generators."""
from fractions import Fraction as F
from research.kernel001.run184.weights184 import A,E,w,h0

def check(word):
    a=A[1]
    s=F(0)
    for c in word:s=a*s+E[int(c)][1]
    fixed=s/(1-a**len(word))
    lo,hi=sorted((h0,fixed))
    maxerr=F(0)
    minmargin=None
    for initial in (lo,hi):
        state=initial
        count=6
        for c in word:
            z=[A[i]*state+E[int(c)][i] for i in range(7)]
            margin=min([z[1]]+[-z[i] for i in range(7) if i!=1])
            minmargin=margin if minmargin is None else min(minmargin,margin)
            assert margin>0
            state=z[1]
            count+=1 if c=='0' else -1
            err=abs(w*state-count)
            maxerr=max(maxerr,err)
            assert err<F(1,10)
        assert lo<=state<=hi
    return float(maxerr),float(minmargin)

def main():
    for word in ('110010','101100'):
        print(word,check(word))
    assert max(check(x)[0] for x in ('110010','101100'))<0.020225

if __name__=='__main__':main()
