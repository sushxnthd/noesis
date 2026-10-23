#!/usr/bin/env python3
"""Exact rational sanity check for nontrivial neutral cycles.

P^3 = I does not imply [z I + (1-z) P]^3 = I.
This is elementary spectral algebra, not a novel theorem.
"""
import sympy as sp

z = sp.Rational(1, 2)
P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
I = sp.eye(3)
B = z * I + (1 - z) * P
v = sp.Matrix([1, -1, 0])

assert P**3 == I
assert B**3 != I
assert (B * v).dot(B * v) == sp.Rational(1, 4) * v.dot(v)
assert (B**3 * v).dot(B**3 * v) == sp.Rational(1, 64) * v.dot(v)

q = sp.symbols("q", real=True)
omega = -sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
modulus_sq = sp.expand((q + (1-q)*omega) * (q + (1-q)*sp.conjugate(omega)))
assert sp.simplify(modulus_sq - (1 - 3*q*(1-q))) == 0
print("PASS: a 3-cycle can be neutral as a word yet contract under partial updates")
