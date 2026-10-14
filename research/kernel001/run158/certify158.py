import json
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "run157"
K = {222: 2, 239: 4}
TOL = F(1, 10)

def check(seed):
    raw = (BASE / f"RUN157_SEED_{seed}.json").read_text()
    p = json.loads(raw, parse_float=str)[0]["parameters"]
    a = [[F(z) for z in row] for row in p["A"]]
    e = [[F(z) for z in row] for row in p["E"]]
    w = [F(z) for z in p["w"]]
    k = K[seed]
    u, v = e[0][k], e[2][k]
    assert a[k][k] == 1 and u > 0 and w[k] > 0 and v != 0
    for j in range(len(w)):
        if j == k:
            continue
        assert a[j][k] <= 0 and e[0][j] <= 0
        if v < 0:
            assert e[2][j] <= 0
        else:
            assert a[j][k]*u + e[2][j] <= 0
    delta = w[k]*u-1
    slope = w[k]*v
    assert abs(delta) < TOL
    if slope < 0:
        first = (delta+TOL)//(-slope)+1
    else:
        first = (TOL-delta)//slope+1
    def err(m):
        return w[k]*max(F(0),u+m*v)-1
    assert first > 0 and abs(err(first-1)) <= TOL < abs(err(first))
    assert u+first*v > 0
    h = [F(0)]*len(w)
    for t in range(201):
        if t:
            token = 0 if t == 1 else 2
            h = [max(F(0),sum(a[j][i]*h[i] for i in range(len(w)))+e[token][j]) for j in range(len(w))]
            assert h == [max(F(0),u+(t-1)*v) if j == k else F(0) for j in range(len(w))]
    return {"seed":seed,"first_neutral_suffix_failure":first,
            "first_total_length":first+1,"previous_error":str(err(first-1)),
            "failure_error":str(err(first)),"neutral_defect":str(slope),
            "increment_relative_error_all_n":str(abs(delta)),
            "scope":"all n>=1,m>=0 on 0^n2^m only"}

if __name__ == "__main__":
    out = [check(seed) for seed in K]
    Path(__file__).with_name("RESULT158.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
