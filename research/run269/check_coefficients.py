"""Verify exact binary64 coefficient encoding."""
import json
from pathlib import Path
P=Path(__file__).parent
p=json.loads((P/'checkpoint.json').read_text())['params']
vals=[x for row in p['A'] for x in row]+[x for row in p['E'] for x in row]+p['b']+p['v']+[p['c']]
ints=list(map(int,(P/'coefficients.txt').read_text().split()))
D=ints[0]
assert D==max(float(x).as_integer_ratio()[1] for x in vals)
assert ints[1:]==[float(x).as_integer_ratio()[0]*(D//float(x).as_integer_ratio()[1]) for x in vals]
print('All 25 binary64 coefficients match exact dyadic encoding')
