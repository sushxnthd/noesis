"""Independent 90-digit decimal obstruction check; no shared audit functions."""
import hashlib,json,sys
from decimal import Decimal,getcontext
from pathlib import Path
getcontext().prec=90
SEEDS=(224,)+tuple(range(226,239))
def evaluate(folder):
    out=[]
    for seed in SEEDS:
        raw=(folder/f"CHECKPOINT_SEED_{seed}.json").read_bytes()
        item=json.loads(raw,parse_float=Decimal)[0]
        A=item["parameters"]["A"]; E=item["parameters"]["E"]; d=len(A)
        structural=[k for k in range(d) if E[0][k]>0 and
                    all(A[j][k]<=0 and E[0][j]<=0 for j in range(d) if j!=k)]
        unit=[k for k in structural if A[k][k]==1]
        out.append({"seed":seed,"sha256":hashlib.sha256(raw).hexdigest(),
                    "structural":structural,"unit":unit,
                    "min_diagonal_gap":str(min(abs(A[k][k]-1) for k in range(d)))})
    return out
if __name__=="__main__":
    print(json.dumps(evaluate(Path(sys.argv[1])),indent=2))
