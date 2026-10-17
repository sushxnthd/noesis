"""NOESIS Run225: independent interval replay for one trained checkpoint.
The 11-checkpoint full cohort and two independent verifiers are in the evidence
archive; this repository CI checks one frozen, non-synthetic trained checkpoint.
"""
import json
from pathlib import Path
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING
from mpmath import iv
iv.dps = 70
R = Path(__file__).resolve().parent
row = json.loads((R / "CHECKPOINT_1409_E100.json").read_text())
p = row["params"]
K = 2**24
delta = 2**-20

def exact(x):
    n, d = float(x).as_integer_ratio()
    return iv.mpf(n) / iv.mpf(d)

def tanh_iv(x):
    low, high = iv.exp(2*x.a), iv.exp(2*x.b)
    return iv.mpf([((low-1)/(low+1)).a, ((high-1)/(high+1)).b])

def explicit_4d(d, k):
    W = [[exact(p["W"][0][i][j]) if i < 3 and j < 3 else iv.mpf(0)
          for j in range(4)] for i in range(4)]
    b = [exact(x) for x in p["b"][0]] + [iv.mpf(d)]
    h = [iv.mpf(".5"), iv.mpf("-.5"), iv.mpf(".25"), iv.mpf(0)]
    h = [tanh_iv(sum((W[i][j]*h[j] for j in range(4)), b[i])) for i in range(4)]
    return sum((exact(p["v"][i])*h[i] for i in range(3)),
               exact(p["c"])+iv.mpf(k)*h[3])

# Independent directed-Decimal implementation; tanh uses a correctly-rounded
# Decimal.exp enclosed by two units in the last place.
P = 80
F = Context(prec=P, rounding=ROUND_FLOOR)
C = Context(prec=P, rounding=ROUND_CEILING)
def D(x): return Decimal(str(x))
def exp_bounds(x):
    mid = x.exp()
    eps = Decimal(2).scaleb(mid.adjusted()-P+1)
    return F.subtract(mid, eps), C.add(mid, eps)
def tanh_bounds(x):
    lo, hi = exp_bounds(x*2)
    return F.divide(F.subtract(lo, D(1)), C.add(lo, D(1))), C.divide(C.subtract(hi, D(1)), F.add(hi, D(1)))
def decimal_one(d, k):
    h = [D(".5"), D("-.5"), D(".25")]
    zs = []
    for i in range(3):
        s = sum((D(p["W"][0][i][j])*h[j] for j in range(3)), D(p["b"][0][i]))
        zs.append(tanh_bounds(s))
    base_lo = F.add(sum((min(D(p["v"][i])*zs[i][0], D(p["v"][i])*zs[i][1]) for i in range(3)), D(p["c"])), D(0))
    base_hi = C.add(sum((max(D(p["v"][i])*zs[i][0], D(p["v"][i])*zs[i][1]) for i in range(3)), D(p["c"])), D(0))
    dlo, dhi = tanh_bounds(D(d))
    return F.add(base_lo, D(k)*dlo), C.add(base_hi, D(k)*dhi)

def test_one():
    for d, k, expected_positive in ((0,K,False),(delta,K,True),(delta,0,False)):
        z = explicit_4d(d,k)
        lo, hi = decimal_one(d,k)
        assert (z.a > 0 if expected_positive else z.b < 0)
        assert (lo > 0 if expected_positive else hi < 0)
    print("PASS: trained seed 1409 epoch100; two interval implementations; controls")
if __name__ == "__main__":
    test_one()
