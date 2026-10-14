"""Independent all-word checker: float64 rollouts plus global roundoff budget.
Unlike the primary directed-interval checker, this stores no intervals.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import numpy as np

HERE = Path(__file__).resolve().parent
P = HERE.parent/"run147"/"checkpoints"/"214.json"

def verify():
    p = json.loads(P.read_text())
    A = np.array(p["A"]); E = np.array(p["E"]); w = np.array(p["w"])
    assert max(sum(abs(F.from_float(v)) for v in row) for row in A) < F(143, 100)
    assert max(abs(F.from_float(v)) for v in E.flat) < F(93, 100)
    assert sum(abs(F.from_float(v)) for v in w) < F(184, 100)
    a, b, c = F(143, 100), F(93, 100), F(184, 100)
    gamma = F(1, 10**14)  # conservatively exceeds gamma_16 for IEEE binary64
    h = np.zeros((1, 4)); q = np.zeros(1, dtype=np.int16)
    H = F(0); D = F(0); rows = []
    for n in range(1, 13):
        count = len(q)
        nh = np.empty((3*count, 4))
        nq = np.maximum(0, np.repeat(q, 3) + np.tile([1, -1, 0], count))
        for tok in range(3):
            z = np.zeros((count, 4))
            for i in range(4):
                v = np.zeros(count)
                for j in range(4):
                    v = v + A[i, j]*h[:, j]
                z[:, i] = np.maximum(0, v + E[tok, i])
            nh[tok::3] = z
        h, q = nh, nq
        y = np.zeros(len(q))
        for j in range(4):
            y = y + w[j]*h[:, j]
        measured = float(np.max(np.abs(y-q)))
        D = a*D + gamma*(a*(H+D)+b)
        H = a*H+b
        output_budget = c*D+gamma*(c*(H+D)+n)
        assert measured < .099
        assert output_budget < F(1, 10**8)
        rows.append((n, measured, float(output_budget)))
    return rows

if __name__ == "__main__":
    print("n12", verify()[-1])
