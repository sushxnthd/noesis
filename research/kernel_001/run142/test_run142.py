"""Run 142 exact-rational checks on ordinary-trained 3-state RNN checkpoints.
These are retrospective checkpoints; no training or hidden-state loss is run here.
"""
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "MODEL_PARAMS.json").read_text())["models"]
EXPECTED = {(202, "float32"): 31009438,
            (202, "float64"): None,
            (206, "float32"): 9106639,
            (206, "float64"): 10261932966499288}

def convert(p):
    return [[Q(x) for x in row] for row in p["A"]], [[Q(x) for x in row] for row in p["E"]], [Q(x) for x in p["w"]]

def rays(p):
    A,E,w=convert(p)
    ans=[]
    for j in range(3):
        b=E[0][j]
        if b>0 and A[j][j]==1 and E[1][j]==-b and all(
            A[i][j]<=0 and E[0][i]<=0 and E[1][i]<=0
            for i in range(3) if i!=j):
            ans.append(j)
    return ans

def next_state(A,E,h,t):
    return [max(Q(0), sum((A[i][k]*h[k] for k in range(3)),Q(0))+E[t][i]) for i in range(3)]

def test_binary_inductive_obligations():
    assert len(DATA)==4
    certified=0
    for r in DATA:
        key=r["seed"],r["dtype"]
        p={k:r[k] for k in ("A","E","w")}
        old={"A":r["initial_A"],"E":r["initial_E"],"w":r["initial_w"]}
        assert rays(old)==[]
        found=rays(p)
        if key==(202,"float64"):
            assert found==[] and Q(r["A"][2][2])!=1
            continue
        certified+=1
        assert len(found)==1
        j=found[0]
        A,E,w=convert(p);b=E[0][j];g=w[j]*b
        assert g!=1 and g!=0
        # The proof is induction on the invariant h=b*q*e_j.
        for t in (0,1):
            for q in (0,1,2,7,100):
                h=[Q(0)]*3;h[j]=b*q
                z=next_state(A,E,h,t)
                target=max(0,q+(1 if t==0 else -1))
                assert z[j]==b*target and all(z[i]==0 for i in range(3) if i!=j)
        # Independent direct nonlinear execution on every short binary word.
        for n in range(10):
            for word in itertools.product((0,1),repeat=n):
                h=[Q(0)]*3;q=0
                for t in word:
                    h=next_state(A,E,h,t)
                    q=max(0,q+(1 if t==0 else -1))
                assert h[j]==b*q and all(h[i]==0 for i in range(3) if i!=j)
                assert sum((w[i]*h[i] for i in range(3)),Q(0))/g==q
    assert certified==3

def test_neutral_exact_first_failure_family():
    for r in DATA:
        key=r["seed"],r["dtype"]
        p={k:r[k] for k in ("A","E","w")}
        found=rays(p)
        if not found:
            assert EXPECTED[key] is None
            continue
        j=found[0];A,E,w=convert(p)
        b=E[0][j];c=E[2][j]
        assert c!=0
        assert all(E[2][i]<=0 for i in range(3) if i!=j)
        N=b//(10*abs(c))+1
        assert N==EXPECTED[key]
        def error(n):
            return Q(n)*c/b if c>0 else min(Q(1),Q(n)*(-c)/b)
        assert error(N-1)<=Q(1,10)<error(N)
        # Family is neutral^N for c>0 and + neutral^N for c<0.
        # This does not assert globally shortest failure over ternary words.

def test_perturbed_spoof_rejected():
    for r in DATA:
        p={k:r[k] for k in ("A","E","w")}
        found=rays(p)
        if not found: continue
        j=found[0]
        mutated=json.loads(json.dumps(p))
        mutated["A"][j][j]=float(Q(1)+Q(1,2**51))
        assert rays(mutated)==[]
        mutated=json.loads(json.dumps(p))
        mutated["E"][1][j]=float(Q(mutated["E"][1][j])+Q(1,2**40))
        assert rays(mutated)==[]
