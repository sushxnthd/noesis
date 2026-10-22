"""Exact finite-range clock spoof; constructed control, not a trained network."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from proof333 import prove
p=[1.,-.01,0., 0.,1.,0., 0.,0.,0.,
   0.,0.,0., 0.,0.,0., 0.,0.,0.,
   0.,1.,-1., 1.,-1.,-1., 1.,0.,0.,-.5]
def classify(word):
    q=[F.from_float(t) for t in p]
    h=[F(0)]*3
    for bit in word:
        x=int(bit)
        h=[max(F(0),sum(q[9*x+3*i+j]*h[j] for j in range(3))+q[18+3*x+i]) for i in range(3)]
    return sum(q[24+i]*h[i] for i in range(3))+q[27]>0
for n in range(1,7):
    for bits in product("01",repeat=n):
        word="".join(bits)
        assert classify(word)==("1" in word)
assert not classify("1"+"0"*11)
assert not prove(p)
print("Finite-perfect clock spoof fails at length 12 and is rejected by exact certificate")
