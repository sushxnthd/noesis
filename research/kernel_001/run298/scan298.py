#!/usr/bin/env python3
"""Frozen Run298: exact-checked long-horizon witnesses on trained Run297 latch RNNs."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent
PREV = ROOT.parent / "run297"
EXPECTED = "620d1852010a2889338752b8568689c709b22ba928b674a44c0b559d7b7fc473"
LIMIT = 256


def prefixes():
    return [""] + ["0" * k + "1" for k in range(7)] + ["1" * k for k in range(1, 7)]


def float_step(p, h, x):
    offset = x * 9
    return tuple(max(0.0, sum(p[offset + 3*i+j]*h[j] for j in range(3)) +
                     p[18 + x*3 + i]) for i in range(3))


def exact_first_failure(p, word):
    z = [Q.from_float(float(x)) for x in p]
    h = (Q(0), Q(0), Q(0))
    latch = 0
    for t, char in enumerate(word, 1):
        x = int(char)
        latch |= x
        h = tuple(max(Q(0), sum(z[x*9 + 3*i + j]*h[j] for j in range(3))
                      + z[18 + x*3 + i]) for i in range(3))
        logit = sum(z[24+i]*h[i] for i in range(3)) + z[27]
        if (logit > 0) != bool(latch):
            return t
    return None


def find_witness(p):
    found = []
    float_candidates = 0
    for prefix in prefixes():
        for tail in "01":
            h = (0.0, 0.0, 0.0)
            latch = 0
            for char in prefix:
                x = int(char)
                latch |= x
                h = float_step(p, h, x)
            word = prefix
            for _ in range(len(prefix)+1, LIMIT+1):
                x = int(tail)
                latch |= x
                h = float_step(p, h, x)
                word += tail
                if not all(math.isfinite(v) for v in h):
                    break
                logit = sum(p[24+i]*h[i] for i in range(3)) + p[27]
                if not math.isfinite(logit):
                    break
                if len(word) >= 13 and ((logit > 0) != bool(latch)):
                    float_candidates += 1
                    first = exact_first_failure(p, word)
                    if first is not None and first >= 13:
                        found.append((len(word), word, first))
                        break
    if not found:
        return None, float_candidates
    _, word, first = min(found)
    return {"word": word, "length": len(word), "first_exact_failure": first}, float_candidates


def main():
    raw = (PREV / "checkpoints297.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED, "training source changed"
    ck = json.loads(raw)
    params = {(x["seed"], x["epoch"]): x for x in ck["rows"]}
    prev = json.loads((PREV / "rows297.json").read_text())
    unresolved = sorted(x["seed"] for x in prev if x["outcome"] == "unresolved")
    assert len(unresolved) == 58, len(unresolved)
    assert all(params[(s, 80)]["accuracy"] == 1.0 for s in unresolved)
    rows = []
    for seed in unresolved:
        witness, n_float = find_witness(params[(seed, 80)]["p"])
        rows.append({"seed": seed, "witness": witness, "float_candidates": n_float,
                     "status": "incorrect" if witness else "unresolved"})
        print("seed", seed, "witness_length", witness["length"] if witness else None, flush=True)
    found = sum(r["status"] == "incorrect" for r in rows)
    result = {"run": 298, "parent": 297, "trained_checkpoints_sha256": EXPECTED,
              "previous_unresolved": len(unresolved), "new_exact_wrong": found,
              "still_unresolved": len(unresolved)-found,
              "primary_pass": found >= 10, "learning_threshold_pass": found >= 5,
              "publishable_count_threshold_pass": found >= 25,
              "claim": "targeted all-length incorrectness witnesses, not correctness certification"}
    (ROOT / "rows298.json").write_text(json.dumps(rows, indent=2, sort_keys=True)+"\n")
    (ROOT / "results298.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print("RUN298_SUMMARY", json.dumps(result, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
