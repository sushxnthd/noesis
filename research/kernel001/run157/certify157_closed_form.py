"""Exact all-length increment-only proof for unchanged gradient-trained RNNs.
For active index k, if A[k,k]=1, E[0,k]=u>0, and A[j,k]<=0,
E[0,j]<=0 for j!=k, then h_n=n*u*e_k for every integer n>=0.
Consequently error_n=n*(w[k]*u-1). All weights are exact decimal rationals.
"""
import json,sys,hashlib
from fractions import Fraction as Q
from pathlib import Path
ACTIVE={222:2,239:4}
def certify(path):
    raw=Path(path).read_bytes()
    r=json.loads(raw,parse_float=str)[0]
    k=ACTIVE[r["seed"]];p=r["parameters"]
    A=[[Q(x) for x in row] for row in p["A"]]
    E=[[Q(x) for x in row] for row in p["E"]]
    w=[Q(x) for x in p["w"]]
    assert r["variant"]=="latent" and A[k][k]==1 and E[0][k]>0
    assert all(A[j][k]<=0 and E[0][j]<=0 for j in range(len(w)) if j!=k)
    u=E[0][k];delta=w[k]*u-1
    assert delta>0
    N=(Q(1,10)//delta)+1
    assert (N-1)*delta<=Q(1,10)<N*delta
    h=[Q(0)]*len(w)
    for n in range(1,101):
        h=[max(Q(0),sum(a*x for a,x in zip(row,h))+E[0][i]) for i,row in enumerate(A)]
        assert h==[n*u if i==k else Q(0) for i in range(len(w))]
        assert sum(a*x for a,x in zip(w,h))-n==n*delta
    return {"seed":r["seed"],"checkpoint_sha256":hashlib.sha256(raw).hexdigest(),
            "active_index":k,"exact_drift":str(delta),
            "first_increment_only_failure":N,
            "error_before":str((N-1)*delta),"error_at":str(N*delta),
            "all_length_identity":"h_n=n*u*e_k for every n>=0",
            "all_n_ge_N_fail":True,
            "scope":"increment-only, not all-alphabet or globally shortest"}
if __name__=="__main__":
    rows=[certify(x) for x in sys.argv[1:]]
    Path("CLOSED_FORM157.json").write_text(json.dumps(rows,indent=2)+"\n")
    print(json.dumps(rows,indent=2))
