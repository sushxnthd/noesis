"""Run199 prospective finite adversarial tester. Protocol committed before holdout.
Finite search is NEVER an all-length algorithm certificate.
"""
import json, sys, hashlib
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/"run197"))
import run197

SEEDS=(283,293,307,311)
N=1<<15
B=455
L=15
WIDTH=12

def score(p,words):
    words=list(words)
    if not words: return [],[]
    v=np.asarray(words,dtype=np.int64)
    h=np.zeros((len(v),WIDTH),dtype=np.float64)
    residue=np.zeros(len(v),dtype=np.int8)
    for t in range(L-1,-1,-1):
        bits=(v>>t)&1
        for b in (0,1):
            ids=np.flatnonzero(bits==b)
            if len(ids): h[ids]=run197.advance(h[ids],p,b)
        residue=(residue+bits)%3
    z=run197.logits(h,p)
    masked=np.where(np.arange(3)[None,:]==residue[:,None],-np.inf,z)
    margins=z[np.arange(len(v)),residue]-np.max(masked,axis=1)
    errors=z.argmax(axis=1)!=residue
    return margins.tolist(),errors.tolist()

def adaptive(p,budget=B):
    rng=np.random.default_rng(199015)
    seen={}
    expanded=set()
    initial=[]
    for k in range(L+1):
        for _ in range(3):
            x=0
            if k:
                for bit in rng.choice(L,size=k,replace=False):
                    x|=1<<int(bit)
            initial.append(x)
    initial.extend(map(int,rng.integers(0,N,size=48)))
    def query(candidates):
        fresh=[]
        for candidate in candidates:
            x=int(candidate)&(N-1)
            if x not in seen and x not in fresh: fresh.append(x)
            if len(fresh)+len(seen)>=budget: break
        if fresh:
            margins,errors=score(p,fresh)
            for x,m,e in zip(fresh,margins,errors):
                seen[x]=(float(m),bool(e))
    query(initial)
    while len(seen)<budget:
        avail=sorted((m,x) for x,(m,_) in seen.items() if x not in expanded)
        if not avail:
            query(rng.integers(0,N,size=min(24,budget-len(seen))))
            continue
        if len(expanded)%4==3:
            strata={}
            for m,x in avail:
                strata.setdefault(x.bit_count(),(m,x))
            pick=sorted(strata.values())[len(expanded)%len(strata)][1]
        else:
            pick=avail[0][1]
        expanded.add(pick)
        cand=[pick^(1<<i) for i in range(L)]
        cand.extend(pick^(3<<i) for i in range(L-1))
        cand.extend(pick^(7<<i) for i in range(L-2))
        cand.extend(pick^(1<<i)^(1<<((i+7)%L)) for i in range(L))
        cand.extend(pick^(1<<i)^(1<<((i+5)%L))^(1<<((i+10)%L)) for i in range(L))
        query(cand)
    assert len(seen)==budget
    return seen

def baselines():
    rng=np.random.default_rng(199005)
    uniform=list(map(int,rng.choice(N,B,replace=False)))
    pool=np.array([i for i in range(N) if 7<=i.bit_count()<=10],dtype=np.int64)
    high=list(map(int,rng.choice(pool,B,replace=False)))
    strat=[]
    for k in range(L+1):
        pool=np.array([i for i in range(N) if i.bit_count()==k],dtype=np.int64)
        strat.extend(map(int,rng.choice(pool,min(28,len(pool)),replace=False)))
    present=set(strat)
    while len(strat)<B:
        x=int(rng.integers(0,N))
        if x not in present:
            present.add(x)
            strat.append(x)
    assert all(len(set(a))==B for a in (uniform,high,strat))
    return {"uniform":uniform,"weight7to10":high,"hamming_stratified":strat}

def train():
    path=ROOT/"CHECKPOINTS.json"
    if path.exists(): raise RuntimeError("Refusing to overwrite checkpoints")
    run197.SEEDS=SEEDS
    run197.train(path)

def evaluate():
    checkpoint=ROOT/"CHECKPOINTS.json"
    querypath=ROOT/"QUERIES.json"
    output=ROOT/"RESULTS.json"
    if querypath.exists() or output.exists(): raise RuntimeError("Refusing to overwrite results")
    obj=json.loads(checkpoint.read_text())
    assert [(r["seed"],r["epoch"]) for r in obj["rows"]]==[(s,e) for s in SEEDS for e in (400,800)]
    base=baselines()
    rows=[]
    for row in obj["rows"]:
        p=run197.params(row)
        a=adaptive(p)
        record={"seed":row["seed"],"epoch":row["epoch"],"train_loss":row["loss"],
                "train_accuracy":row["train_accuracy"],"methods":{}}
        record["methods"]["adaptive"]=[{"word":format(x,"015b"),"margin":m,"error":e} for x,(m,e) in a.items()]
        for name,words in base.items():
            margins,errors=score(p,words)
            record["methods"][name]=[{"word":format(x,"015b"),"margin":float(m),"error":bool(e)}
                                     for x,m,e in zip(words,margins,errors)]
        rows.append(record)
    querypath.write_text(json.dumps({"checkpoint_sha256":hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
                                    "rows":rows},indent=1)+"\n")
    print("FROZEN_QUERY_LOG",hashlib.sha256(querypath.read_bytes()).hexdigest(),flush=True)
    # Complete enumeration occurs only AFTER all methods' queries are frozen on disk.
    summary=[]
    for row,queryrow in zip(obj["rows"],rows):
        p=run197.params(row)
        _,errors=score(p,range(N))
        counts={name:sum(item["error"] for item in vals) for name,vals in queryrow["methods"].items()}
        ratio=(1+counts["adaptive"])/(1+max(counts[n] for n in base))
        full=int(sum(errors))
        summary.append({"seed":row["seed"],"epoch":row["epoch"],"universe_errors":full,
                        "counts":counts,"ratio":ratio,"train_accuracy":row["train_accuracy"]})
        print("HOLDOUT",row["seed"],row["epoch"],"counts",counts,"all",full,"ratio",ratio,flush=True)
    primary=float(np.median([r["ratio"] for r in summary]))
    outcome={"protocol":"PROTOCOL.md","checkpoint_sha256":hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
             "queries_sha256":hashlib.sha256(querypath.read_bytes()).hexdigest(),
             "rows":summary,"primary_median_ratio":primary,"threshold":1.5,"success":primary>=1.5}
    output.write_text(json.dumps(outcome,indent=1)+"\n")
    print("PRIMARY",primary,"PASS" if primary>=1.5 else "FAIL",flush=True)

def selftest():
    base=baselines()
    assert all(len(x)==B and len(set(x))==B for x in base.values())
    p={"W":np.zeros((WIDTH,WIDTH)),"U":np.zeros((2,WIDTH)),
       "b":np.zeros(WIDTH),"V":np.zeros((3,WIDTH)),"c":np.zeros(3)}
    assert len(adaptive(p))==B
    m,e=score(p,[0,1,2,3])
    assert len(m)==4 and len(e)==4
    print("SELFTEST PASS",flush=True)

if __name__=="__main__":
    action=sys.argv[1]
    if action=="train":train()
    elif action=="eval":evaluate()
    elif action=="selftest":selftest()
    else:raise SystemExit("expected train/eval/selftest")
