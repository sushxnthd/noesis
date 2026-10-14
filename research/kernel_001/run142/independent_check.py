"""Independent SymPy checker for Run 142; does not import test_run142."""
import itertools, json
from pathlib import Path
from sympy import Rational as Q
D=Path(__file__).resolve().parent
rows=json.loads((D/"MODEL_PARAMS.json").read_text())["models"]
expected={(202,"float32"):31009438,(202,"float64"):None,
          (206,"float32"):9106639,(206,"float64"):10261932966499288}

def step(A,E,h,t):
    return [max(Q(0),sum(A[i][k]*h[k] for k in range(3))+E[t][i]) for i in range(3)]

def main():
    accepted=0
    for r in rows:
        A=[[Q(x) for x in row] for row in r["A"]]
        E=[[Q(x) for x in row] for row in r["E"]]
        w=[Q(x) for x in r["w"]]
        key=r["seed"],r["dtype"]
        rays=[j for j in range(3) if E[0][j]>0 and A[j][j]==1
              and E[1][j]==-E[0][j] and all(
                A[i][j]<=0 and E[0][i]<=0 and E[1][i]<=0
                for i in range(3) if i!=j)]
        if not rays:
            assert key==(202,"float64") and A[2][2]!=1
            continue
        accepted+=1
        assert len(rays)==1
        j=rays[0];b=E[0][j];gain=w[j]*b
        assert gain!=0 and gain!=1
        for n in range(10):
            for word in itertools.product((0,1),repeat=n):
                h=[Q(0)]*3;q=0
                for t in word:
                    h=step(A,E,h,t)
                    q=max(0,q+(1 if t==0 else -1))
                assert h[j]==b*q
                assert all(h[i]==0 for i in range(3) if i!=j)
                assert sum(w[i]*h[i] for i in range(3))/gain==q
        c=E[2][j]
        assert c!=0 and all(E[2][i]<=0 for i in range(3) if i!=j)
        N=expected[key]
        error=lambda n: Q(n)*c/b if c>0 else min(Q(1),Q(n)*(-c)/b)
        assert error(N-1)<=Q(1,10)<error(N)
        assert A[j][j]+Q(1,2**52)!=1
    assert accepted==3
    print("Independent PASS: 3 binary invariants, 3069 direct words, 3 neutral boundaries")

if __name__=="__main__": main()
