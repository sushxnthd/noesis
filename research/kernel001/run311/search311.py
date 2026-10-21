#!/usr/bin/env python3
"""Frozen Run311 search: float screen, exact rational validation of proposed failures."""
import json,random,math
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent
SEEDS=(22242,22287,22361,22573)
def weights(seed):
    j=P/f"seed{seed}.json"
    if j.exists():return json.loads(j.read_text())
    return [float(line.split(": ",1)[1]) for line in (P/f"seed{seed}.txt").read_text().splitlines()]
def words():
    for n in range(7,513):yield "0"*n,"zero-run"
    for n in range(6,512):yield "1"+"0"*n,"one-then-zeros"
    for k in (0,1,2,3,4,5,8,16,32):
        for n in range(257):
            w="0"*k+"1"+"0"*n
            if len(w)>6:yield w,"prefix-one-suffix"
    for n in range(7,513):
        yield ("01"*((n+1)//2))[:n],"alternating-01"
        yield ("10"*((n+1)//2))[:n],"alternating-10"
    for k in (1,2,3,4,8,16,32,64):
        for n in range(257):
            w="1"*k+"0"*n
            if len(w)>6:yield w,"ones-then-zeros"
    rng=random.Random(311)
    for n in (8,16,32,64,128,256):
        for _ in range(128):yield "".join(str(rng.getrandbits(1)) for _ in range(n)),"seeded-random"
def eval_word(p,w,exact=False):
    a=[F.from_float(z) for z in p] if exact else p
    h=[0,0,0]
    for s in w:
        x=int(s);off=9*x;bo=18+3*x
        h=[max(0,a[bo+i]+sum(a[off+3*i+j]*h[j] for j in range(3))) for i in range(3)]
    return a[27]+sum(a[24+i]*h[i] for i in range(3))
def wrong(z,w):return z<=0 if "1" in w else z>0
def main():
    outcomes=[]
    for seed in SEEDS:
        p=weights(seed);count={};found=None
        for w,family in words():
            count[family]=count.get(family,0)+1
            z=eval_word(p,w)
            if math.isfinite(z) and wrong(z,w):
                q=eval_word(p,w,True)
                if wrong(q,w):found={"word":w,"family":family,"exact_logit":str(q)};break
        outcomes.append({"seed":seed,"checked":count,"exact_witness":found})
    result={"run":311,"protocol_commit":"8bfb2cf95148f60a40650f04e9502a29cbae4eac","rows":outcomes,"primary_pass":any(r["exact_witness"] for r in outcomes)}
    (P/"public_results311.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,sort_keys=True))
if __name__=="__main__":main()
