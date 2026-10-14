"""Exhaustive directed-rounding certificate for Run147 seed 214.
Stored binary32 coefficients are exact binary64 inputs. Every binary64
multiplication/addition is enclosed by its adjacent representable numbers.
The conclusion concerns exact-real stored-weight semantics, not GPU rollout.
"""
from pathlib import Path
import json
import numpy as np

HERE = Path(__file__).resolve().parent
CHECKPOINT = HERE.parent / "run147" / "checkpoints" / "214.json"
TOLERANCE = 0.1

def down(x):
    return np.nextafter(x, -np.inf)

def up(x):
    return np.nextafter(x, np.inf)

def word_of(code, n):
    return "".join(str((int(code) // (3**j)) % 3) for j in range(n-1, -1, -1))

def run(depth=13, checkpoint=CHECKPOINT):
    p = json.loads(Path(checkpoint).read_text())
    assert p["seed"] == 214
    A, E, w = (np.asarray(p[k], dtype=np.float64) for k in ("A", "E", "w"))
    assert A.shape == (4, 4) and E.shape == (3, 4) and w.shape == (4,)
    assert all(float(np.float32(v)) == float(v) for v in
               np.concatenate((A.ravel(), E.ravel(), w.ravel())))
    lo = np.zeros((1, 4))
    hi = lo.copy()
    q = np.zeros(1, dtype=np.int16)
    codes = np.zeros(1, dtype=np.int64)
    rows = []
    for n in range(1, depth+1):
        count = len(q)
        nextlo = np.zeros((3*count, 4))
        nexthi = nextlo.copy()
        nextq = np.maximum(0, np.repeat(q, 3) +
                           np.tile(np.array([1, -1, 0], dtype=np.int16), count))
        nextcodes = np.repeat(codes, 3)*3 + np.tile(np.arange(3, dtype=np.int64), count)
        for i in range(4):
            for tok in range(3):
                sl = np.zeros(count)
                sh = np.zeros(count)
                for j in range(4):
                    a = A[i, j]
                    vl = lo[:, j] if a >= 0 else hi[:, j]
                    vh = hi[:, j] if a >= 0 else lo[:, j]
                    sl = down(sl + down(a*vl))
                    sh = up(sh + up(a*vh))
                nextlo[tok::3, i] = np.maximum(0, down(sl + E[tok, i]))
                nexthi[tok::3, i] = np.maximum(0, up(sh + E[tok, i]))
        lo, hi, q, codes = nextlo, nexthi, nextq, nextcodes
        yl = np.zeros(len(q))
        yh = np.zeros(len(q))
        for j in range(4):
            a = w[j]
            yl = down(yl + down(a*(lo[:, j] if a >= 0 else hi[:, j])))
            yh = up(yh + up(a*(hi[:, j] if a >= 0 else lo[:, j])))
        error_lo = down(yl-q)
        error_hi = up(yh-q)
        err_bound = np.maximum(abs(error_lo), abs(error_hi))
        maximum = float(np.max(err_bound))
        definitely_bad = np.flatnonzero((error_lo > up(TOLERANCE)) |
                                        (error_hi < -up(TOLERANCE)))
        possibly_bad = np.flatnonzero(err_bound > down(TOLERANCE))
        row = dict(length=n, words=3**n, maximum_abs_error_upper_bound=maximum,
                   definitely_bad_count=int(len(definitely_bad)),
                   possibly_bad_count=int(len(possibly_bad)))
        if n < 13:
            assert maximum < 0.099, (n, maximum)  # strict margin below exact 1/10
        if n == 13:
            assert len(definitely_bad) >= 1
            row["witnesses"] = [
                dict(word=word_of(codes[i], n), error_lower=float(error_lo[i]),
                     error_upper=float(error_hi[i])) for i in definitely_bad
            ]
            assert len(definitely_bad) == len(possibly_bad), "inconclusive interval"
        rows.append(row)
    return dict(seed=p["seed"], tolerance=TOLERANCE,
                arithmetic="exact real stored binary32 parameters, outward binary64 bounds",
                conclusion="global first failure at n=13" if depth == 13 else "prefix bound",
                rows=rows)

if __name__ == "__main__":
    result = run()
    (HERE/"RESULTS.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result["rows"][-2:], indent=2))
