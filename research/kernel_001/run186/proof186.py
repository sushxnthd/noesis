"""Directed-rounding interval proof for three unseen trained checkpoint-word pairs."""
import json
from pathlib import Path
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING

P=Path(__file__).resolve().parent
DATA=json.loads((P/"reduced_checkpoint.json").read_text())
A=[[D.from_float(float(x)) for x in row] for row in DATA["parameters"]["A"]]
E=[[D.from_float(float(x)) for x in row] for row in DATA["parameters"]["E"]]
W=[D.from_float(float(x)) for x in DATA["parameters"]["w"]]
LO=Context(prec=80,rounding=ROUND_FLOOR)
HI=Context(prec=80,rounding=ROUND_CEILING)
Z=D(0);TH=D("0.1")

def dot(coeff,state,bias):
    lo=bias;hi=bias
    for a,(l,u) in zip(coeff,state):
        if a>=Z:
            ll=LO.multiply(a,l);uu=HI.multiply(a,u)
        else:
            ll=LO.multiply(a,u);uu=HI.multiply(a,l)
        lo=LO.add(lo,ll);hi=HI.add(hi,uu)
    return lo,hi

def advance(h,symbol):
    pre=[dot(A[i],h,E[symbol][i]) for i in range(3)]
    return [(max(Z,l),max(Z,u)) for l,u in pre]

def prove(word):
    assert word in ("011100","101010","110001")
    h=[(Z,Z)]*3
    for _ in range(6):h=advance(h,0)
    previous=None; at8192=None;maxwidth=Z
    for k in range(1,9001):
        for c in word:h=advance(h,int(c))
        l,u=dot(W,h,-D(6))
        maxwidth=max(maxwidth,HI.subtract(u,l))
        if k==8192:at8192=(str(l),str(u))
        if -TH<=l and u<=TH:
            previous=(k,str(l),str(u))
        elif l>TH or u< -TH:
            assert k==8623 and previous[0]==8622
            return {"word":word,"first_failure":k,"previous":previous,
                    "failure_interval":[str(l),str(u)],
                    "interval_at_8192":at8192,"max_width":str(maxwidth)}
        else:raise AssertionError("inconclusive interval at cycle "+str(k))
    raise AssertionError("no failure before 9000")

if __name__=="__main__":
    for word in ("011100","101010","110001"):
        print(json.dumps(prove(word),sort_keys=True))
