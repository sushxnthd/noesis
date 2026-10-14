import json
from decimal import Decimal as D, getcontext
from pathlib import Path

getcontext().prec = 110
BASE = Path(__file__).resolve().parent.parent / "run157"

def check(seed,k):
    p = json.loads((BASE / f"RUN157_SEED_{seed}.json").read_text(),parse_float=str)[0]["parameters"]
    a = [[D(v) for v in row] for row in p["A"]]
    e = [[D(v) for v in row] for row in p["E"]]
    w = [D(v) for v in p["w"]]
    u,v = e[0][k],e[2][k]
    assert a[k][k] == 1 and u > 0
    for j in range(len(w)):
        if j == k: continue
        assert a[j][k] <= 0 and e[0][j] <= 0
        if v < 0: assert e[2][j] <= 0
        else: assert a[j][k]*u+e[2][j] <= 0
    def error(m):
        return w[k]*max(D(0),u+D(m)*v)-D(1)
    def fails(m):
        return abs(error(m)) > D("0.1")
    assert not fails(0)
    lo,hi = 0,1
    while not fails(hi): hi*=2
    while lo+1 < hi:
        mid=(lo+hi)//2
        if fails(mid): hi=mid
        else: lo=mid
    assert not fails(hi-1) and fails(hi) and u+D(hi)*v > 0
    h=[D(0)]*len(w)
    for t in range(1,201):
        x=0 if t==1 else 2
        h=[max(D(0),sum(a[j][i]*h[i] for i in range(len(w)))+e[x][j]) for j in range(len(w))]
        assert h==[max(D(0),u+D(t-1)*v) if j==k else D(0) for j in range(len(w))]
    return {"seed":seed,"first_neutral_suffix_failure":hi,
            "previous_error":str(error(hi-1)),"failure_error":str(error(hi))}

if __name__=="__main__":
    outcomes=[check(222,2),check(239,4)]
    Path(__file__).with_name("INDEPENDENT158.json").write_text(json.dumps(outcomes,indent=2)+"\n")
    print(json.dumps(outcomes,indent=2))
