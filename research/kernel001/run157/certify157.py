"""Directed-rounding first-failure certificates for trained ReLU RNNs.
Stored decimal parameters are exact; only increment-only words are certified.
"""
import argparse,hashlib,json
from decimal import Decimal as D,localcontext,ROUND_FLOOR,ROUND_CEILING
from pathlib import Path
THRESHOLD=D("0.1")
def load(path):
    raw=Path(path).read_bytes()
    rec=json.loads(raw,parse_float=str)[0]
    assert rec["seed"] in (217,221) and rec["variant"]=="latent"
    p=rec["parameters"]
    return rec["seed"],[[D(str(v)) for v in row] for row in p["A"]],[D(str(v)) for v in p["E"][0]],[D(str(v)) for v in p["w"]],hashlib.sha256(raw).hexdigest()
def linear(A,lows,highs,bias,precision):
    L=[];U=[]
    for row,b in zip(A,bias):
        with localcontext() as ctx:
            ctx.prec=precision;ctx.rounding=ROUND_FLOOR
            lo=b
            for a,x,y in zip(row,lows,highs):
                lo=lo+a*(x if a>=0 else y)
        with localcontext() as ctx:
            ctx.prec=precision;ctx.rounding=ROUND_CEILING
            hi=b
            for a,x,y in zip(row,lows,highs):
                hi=hi+a*(y if a>=0 else x)
        L.append(lo);U.append(hi)
    return L,U
def certify(path,precision=256):
    seed,A,e,w,sha=load(path)
    L=[D(0)]*len(w);U=L[:]
    changes=[];old=None;max_width=D(0)
    selected={}
    for n in range(1,20001):
        L,U=linear(A,L,U,e,precision)
        mask=tuple(1 if lo>0 else 0 if hi<0 else -1 for lo,hi in zip(L,U))
        if mask!=old:changes.append([n,list(mask)]);old=mask
        L=[max(D(0),v) for v in L];U=[max(D(0),v) for v in U]
        lo,hi=linear([w],L,U,[D(-n)],precision)
        lo,hi=lo[0],hi[0]
        max_width=max(max_width,hi-lo)
        if n in (6,64,128,1024,10782,10783,16744,16745):
            selected[str(n)]=[str(lo),str(hi)]
        if lo>D("0.1") or hi<D("-0.1"):
            return {"seed":seed,"checkpoint_sha256":sha,"precision":precision,
                "first_increment_only_failure":n,"error_interval":[str(lo),str(hi)],
                "all_shorter_increment_only_words_below_0.1":True,
                "mask_changes":changes,"max_interval_width":str(max_width),
                "selected_intervals":selected,
                "limits":"not a global ternary or all-length certificate"}
        if lo<=D("-0.1") or hi>=D("0.1"):
            raise AssertionError(f"Interval inconclusive at {n}: [{lo},{hi}]")
    raise AssertionError("No increment-only failure within 20000")
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("checkpoints",nargs="+");ap.add_argument("--output",default="RESULT157.json");a=ap.parse_args()
    rows=[certify(p) for p in a.checkpoints]
    Path(a.output).write_text(json.dumps(rows,indent=2)+"\n")
    for r in rows:print(r["seed"],r["first_increment_only_failure"],r["mask_changes"])
