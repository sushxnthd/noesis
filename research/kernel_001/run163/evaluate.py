import json, sys
from pathlib import Path
import numpy as np
SEEDS = [224] + list(range(226,239))
def auc(y,s):
    a=[v for v,z in zip(s,y) if z]
    b=[v for v,z in zip(s,y) if not z]
    if not a or not b: return None
    return sum((x>z)+0.5*(x==z) for x in a for z in b)/(len(a)*len(b))
def model(path):
    d=json.loads(path.read_text())[0]; p=d["parameters"]
    A=np.array(p["A"]); E=np.array(p["E"]); w=np.array(p["w"])
    h=np.zeros(len(w))
    for _ in range(6): h=np.maximum(0,A@h+E[0])
    initial=float(w@h-6)
    defect=abs(float(w@(np.maximum(0,A@h+E[2])-h)))
    first=None
    for t in range(1,4097):
        h=np.maximum(0,A@h+E[2])
        if abs(float(w@h-6))>0.1: first=t; break
    return dict(seed=d["seed"],defect=defect,initial=initial,mse=d["train_mse"],first=first)
def run(root):
    result={}
    for name in ("checkpoints_local","remote_checkpoints"):
        rows=[model(root/name/("CHECKPOINT_SEED_%s.json"%s)) for s in SEEDS]
        y=[r["first"] is not None for r in rows]
        result[name]=dict(rows=rows,failures=sum(y),auc={
            "defect":auc(y,[r["defect"] for r in rows]),
            "mse":auc(y,[r["mse"] for r in rows]),
            "initial":auc(y,[abs(r["initial"]) for r in rows])})
    return result
if __name__=="__main__":print(json.dumps(run(Path(sys.argv[1])),indent=2))
