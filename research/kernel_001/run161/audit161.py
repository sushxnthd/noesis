"""Run 161 frozen exact-rational one-ray sparse repair coverage audit."""
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

SEEDS=(224,)+tuple(range(226,239))
MAX_EDITS=6
MAX_DELTA=Q(1,10**6)

def evaluate(folder):
    rows=[]
    for seed in SEEDS:
        raw=(folder/f"CHECKPOINT_SEED_{seed}.json").read_bytes()
        item=json.loads(raw,parse_float=str)[0]
        assert item["seed"]==seed and item["variant"]=="latent"
        p=item["parameters"]
        A=[[Q(x) for x in row] for row in p["A"]]
        E=[[Q(x) for x in row] for row in p["E"]]
        w=[Q(x) for x in p["w"]]
        d=len(w)
        candidates=[]
        structural=[]
        for k in range(d):
            u=E[0][k]
            if u<=0 or any(A[j][k]>0 or E[0][j]>0 for j in range(d) if j!=k):
                continue
            structural.append(k)
            if A[k][k]!=1:
                continue
            changes=[("E[1,%d]"%k,E[1][k],-u),
                     ("E[2,%d]"%k,E[2][k],Q(0)),
                     ("w[%d]"%k,w[k],1/u)]
            changes.extend((f"E[{t},{j}]",E[t][j],Q(0))
                           for t in (1,2) for j in range(d) if j!=k and E[t][j]>0)
            edits=[{"parameter":name,"before":str(a),"after":str(b),"delta":str(b-a)}
                   for name,a,b in changes if a!=b]
            maxdelta=max([abs(Q(x["delta"])) for x in edits],default=Q(0))
            if len(edits)<=MAX_EDITS and maxdelta<=MAX_DELTA:
                candidates.append({"k":k,"edits":edits,"maxdelta":str(maxdelta)})
        chosen=min(candidates,key=lambda x:(len(x["edits"]),Q(x["maxdelta"]),x["k"])) if candidates else None
        gaps=[abs(A[k][k]-1) for k in range(d)]
        rows.append({"seed":seed,"sha256":hashlib.sha256(raw).hexdigest(),
                     "width":d,"train_mse":str(item["train_mse"]),
                     "certified":chosen is not None,"selected":chosen,
                     "structurally_eligible_coordinates":structural,
                     "min_diagonal_gap":str(min(gaps)),
                     "nearest_diagonal_k":min(range(d),key=lambda k:gaps[k])})
    n=sum(x["certified"] for x in rows)
    return {"run":161,"certified_count":n,"denominator":len(SEEDS),
            "primary_success":n>=7,"kill_condition_triggered":n<3,
            "scope":"fixed A and E[0], exact decimal rational parameters, one-coordinate ray",
            "outcomes":rows}

if __name__=="__main__":
    print(json.dumps(evaluate(Path(sys.argv[1])),indent=2))
