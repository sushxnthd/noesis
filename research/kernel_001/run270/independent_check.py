"""Separate exact interval-image checker for full alphabet."""
import json
from pathlib import Path
from fractions import Fraction as F
def q(x): return F.from_float(float(x))
def image(a,b,lo,hi):
    if a>=0:
        low=max(F(0),a*lo+b)
        high=None if hi is None and a>0 else max(F(0),a*(hi if hi is not None else 0)+b)
    else:
        low=F(0) if hi is None else max(F(0),a*hi+b)
        high=max(F(0),a*lo+b)
    return low,high
def included(a,b):
    return a[0]>=b[0] and (b[1] is None or (a[1] is not None and a[1]<=b[1]))
def verify(p):
    a=[q(x) for x in p["a"]];b=[q(x) for x in p["b"]]
    v=q(p["v"]);c=q(p["c"]);L=max(F(0),b[2]);U=b[1]
    if not (U>L and v>0 and c<0 and v*L+c<0 and v*U+c>0):return False
    regions=((F(0),L),(U,None))
    for state in (0,1):
        for symbol in (0,1,2):
            target=state if symbol==0 else (1 if symbol==1 else 0)
            if not included(image(a[symbol],b[symbol],*regions[state]),regions[target]):return False
    return True
def replay(p,word):
    a=[q(x) for x in p["a"]];b=[q(x) for x in p["b"]]
    v=q(p["v"]);c=q(p["c"]);h=F(0);state=0
    for i,x in enumerate(word,1):
        state=1 if x==1 else (0 if x==2 else state)
        h=max(F(0),a[x]*h+b[x])
        if (v*h+c>0)!=bool(state):return i
    return None
if __name__=="__main__":
    root=Path(__file__).parent
    data=json.loads((root/"checkpoints.json").read_text())
    predictions=json.loads((root/"certificates.json").read_text())
    for row,pred in zip(data["rows"],predictions):
        assert (row["seed"],row["arm"],row["epoch"])==(pred["seed"],pred["arm"],pred["epoch"])
        assert verify(row["params"])==pred["certified"]
    print("independent exact checker agrees",len(predictions),"checkpoints")
    for K in (8,16,32,64,128):
        p={"a":[2,1,2.**(-K)],"b":[-1,2,-1],"v":1,"c":-1}
        assert not verify(p)
        assert replay(p,[1,1]+[0]*K+[2])==K+3
        assert replay(p,[1,1]+[0]*(K-1)+[2]) is None
        print("finite-horizon spoof rejected",K,"first witness length",K+3)
    good={"a":[2,1,-1],"b":[-1,2,-1],"v":1,"c":-1}
    assert verify(good)
    for bad in (dict(good,a=[.5,1,-1]),dict(good,b=[-3,2,-1]),
                dict(good,a=[2,1,1]),dict(good,b=[-1,.5,-1]),dict(good,v=-1)):
        assert not verify(bad)
    print("five corrupted controls rejected")
