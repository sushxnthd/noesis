"""Independent exact-rational checker; does not import core.py."""
from fractions import Fraction as F
from collections import deque
import json,sys

def shortest(cap):
    seen={(0,F(0))};q=deque([(0,F(0),0)])
    while q:
        n,h,t=q.popleft()
        if (n==0)!=(h==0):return t
        for s in (-1,1):
            z=(max(0,n+s),max(F(0),min(cap,h+s)))
            if z not in seen:
                seen.add(z);q.append((*z,t+1))

def numeric_derivative(w,cap,eps=F(1,100)):
    def loss(c):
        h=F(0);n=0
        for s in w:
            h=max(F(0),min(c,h+s));n=max(0,n+s)
        return (h-n)**2
    return (loss(cap+eps)-loss(cap-eps))/(2*eps)

def verify(rows):
    for r in rows:
        k=r["k"];m=F(r["initial_cap"]);new=F(r["prefix_cap"])
        assert shortest(m)==2*k+1
        assert shortest(new)==2*k+3
        assert numeric_derivative([1]*(k+1)+[-1]*k,m)==0
        assert numeric_derivative([1]*(k+1),m)==2*(m-(k+1))
        assert F(r["final_only_gradient"])==0
        assert F(r["prefix_gradient"])==2*(m-(k+1))
        assert F(r["final_only_cap"])==m
        assert new==m-F(1,4)*F(r["prefix_gradient"])
    return {"status":"passed","independently_verified":len(rows),"checks_per_row":8}

if __name__=="__main__":
    print(json.dumps(verify(json.load(open(sys.argv[1]))["rows"]),sort_keys=True))
