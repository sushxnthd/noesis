#!/usr/bin/env python3
"""Exact rational finite-horizon neutral-cycle spoof (classical, not novel).

For arbitrary N, a contracting real state can preserve three readout labels
through n=N but collapse two distinct DFA-state representatives at N+1.
"""
from fractions import Fraction as Q

def witness(N=256, contraction=Q(3, 4)):
    assert isinstance(N, int) and N >= 0
    assert Q(0) < contraction < Q(1)
    threshold = (Q(1) + contraction) * contraction**N / 2

    def label(x):
        scores = (-x - threshold, Q(0), x - threshold)
        return max(range(3), key=lambda i: scores[i])

    initial = (-Q(1), Q(0), Q(1))
    for n in range(N + 1):
        assert tuple(label(x * contraction**n) for x in initial) == (0, 1, 2)
    assert tuple(label(x * contraction**(N + 1)) for x in initial) == (1, 1, 1)
    return threshold

if __name__ == "__main__":
    t = witness()
    print("PASS: exact three-state readout through n=256, collapse at n=257")
    print("Threshold numerator digits:", len(str(t.numerator)))
    print("Threshold denominator digits:", len(str(t.denominator)))
