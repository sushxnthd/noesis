#!/usr/bin/env python3
"""Exact finite-word audit. Requires original Run300 checkpoints300_late.json.
No conclusion about words longer than MAXLEN."""
import json,hashlib,sys
from fractions import Fraction as Q
from pathlib import Path
SEEDS=(22242,22287,22361,22573)
MAXLEN=16
EXPECTED_SHA="71f384d19e4e5ae95198b6bce2ec35f29f547b166ba293ffae60fe8a2d2d6f8d"
def audit(p):
    a=list(map(Q.from_float,p))
    states=[(Q(0),Q(0),Q(0))]
    total=0
    for n in range(1,MAXLEN+1):
        nxt=[]
        for j,h in enumerate(states):
            for x in (0,1):
                v=tuple(max(Q(0),a[18+3*x+i]+sum(a[9*x+3*i+k]*h[k] for k in range(3))) for i in range(3))
                nxt.append(v)
                y=sum(a[24+k]*v[k] for k in range(3))+a[27]
                expected=(j*2+x)!=0
                if (y>0)!=expected:
                    return {"total":total+len(nxt),"failure":format(j*2+x,f"0{n}b"),"logit":str(y)}
        states=nxt
        total+=len(nxt)
    return {"total":total,"failure":None}
def main():
    source=Path(sys.argv[1])
    raw=source.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==EXPECTED_SHA
    rows=json.loads(raw)["rows"]
    for seed in SEEDS:
        r=audit(rows[seed-22200]["p"])
        print(seed,r,flush=True)
        assert r=={"total":131070,"failure":None}
if __name__=="__main__":main()
