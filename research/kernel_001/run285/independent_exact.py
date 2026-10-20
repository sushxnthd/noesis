"""NOESIS Run285: independent, exact SymPy verifier of stored learned checkpoint.
This proves unrestricted correctness for every nonempty RESET/TOGGLE word.
It does not prove the frozen incremental >=2 criterion.
"""
import itertools
import json
from pathlib import Path
from sympy import Integer, Rational

data = json.loads((Path(__file__).parent / "certificate_20711.json").read_text())
q = [Rational(float(x)) for x in data["p"]]
L = [[Rational(float(x)) for x in row] for row in data["L"]]
U = [[Rational(float(x)) for x in row] for row in data["U"]]

def step(h, token):
    return tuple(
        max(Integer(0), sum(q[4*token + 2*i + j] * h[j]
                            for j in (0, 1)) + q[8 + 2*token + i])
        for i in (0, 1)
    )

def logit(h):
    return q[12]*h[0] + q[13]*h[1] + q[14]

def check(k):
    states = [((Integer(0), Integer(0)), 0)]
    for _ in range(k):
        nxt = []
        for h, state in states:
            for token in (0, 1):
                target = 0 if token == 0 else 1 - state
                h2 = step(h, token)
                assert (logit(h2) > 0) == bool(target)
                nxt.append((h2, target))
        states = nxt
    for h, state in states:
        assert all(L[state][i] <= h[i] <= U[state][i] for i in (0, 1))
    for state in (0, 1):
        corners = itertools.product(*[(L[state][i], U[state][i])
                                       for i in (0, 1)])
        for h in corners:
            z = logit(h)
            assert z != 0 and (z > 0) == bool(state)
            for token in (0, 1):
                target = 0 if token == 0 else 1 - state
                h2 = step(h, token)
                assert all(L[target][i] <= h2[i] <= U[target][i]
                           for i in (0, 1))
    return True

if __name__ == "__main__":
    assert check(1), "prefix-anchored certificate failed"
    assert check(0), "depth-zero ablation failed"
    print("PASS: exact all-length certificate; also valid at k=0")
