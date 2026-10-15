import json
from decimal import Decimal as D, localcontext
from pathlib import Path
P=Path(__file__).parent
def read(n):
    return json.loads((P/n).read_text(),parse_float=D)
def replay(word,stop):
    A=read("A_first.json")+[read("A_last_4.json")]
    A+=[[D(s) for s in (P/"A_last_5.txt").read_text().split(",")]]
    A+=[read("A_last_6.json")]
    p=read("E_w.json");E=p["E"];w=p["w"]
    with localcontext() as ctx:
        ctx.prec=100;h=[D(0)]*7
        def step(x):
            nonlocal h
            z=[E[x][i]+sum((A[i][j]*h[j] for j in range(7)),D(0)) for i in range(7)]
            h=[max(D(0),v) for v in z]
            return tuple(v>D(0) for v in z)
        for _ in range(6):step(0)
        ref=[];switch=fail=None
        for k in range(1,stop+1):
            for t,c in enumerate(word):
                mask=step(int(c))
                if k==1:ref.append(mask)
                elif switch is None and mask!=ref[t]:switch=k
            err=sum((w[j]*h[j] for j in range(7)),D(0))-D(6)
            if fail is None and abs(err)>D("0.1"):fail=k
        return switch,fail
