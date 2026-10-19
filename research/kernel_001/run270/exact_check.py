"""Exact-rational, sufficient full-alphabet inductive latch proof."""
import json
from pathlib import Path
from fractions import Fraction as F
def q(x): return F.from_float(float(x))
def cert(p):
    a=[q(x) for x in p["a"]]; b=[q(x) for x in p["b"]]
    v=q(p["v"]); c=q(p["c"]); L=max(F(0),b[2]); U=b[1]
    return all((v>0,c<0,U>L,v*L+c<0,v*U+c>0,a[0]>1,
                a[1]>=0,a[2]<=0,a[0]*L+b[0]<=L,a[0]*U+b[0]>=U))
if __name__=="__main__":
    d=json.loads(Path(__file__).with_name("checkpoints.json").read_text())
    rows=[{"seed":r["seed"],"arm":r["arm"],"epoch":r["epoch"],
           "certified":cert(r["params"]),"sampled_accuracy":r["train_accuracy"]} for r in d["rows"]]
    Path(__file__).with_name("certificates.json").write_text(json.dumps(rows,indent=2)+"\n")
    for arm in ("control","amplification"):
        s=[r for r in rows if r["epoch"]==500 and r["arm"]==arm]
        print(arm,"certified",sum(r["certified"] for r in s),"sampled_perfect",sum(r["sampled_accuracy"]==1 for r in s))
