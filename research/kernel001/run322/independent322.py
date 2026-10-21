#!/usr/bin/env python3
"""Independent SymPy exact check for Run322 trained-model failures."""
from pathlib import Path
import json
from sympy import Rational,Integer
P=Path(__file__).resolve().parent
def step(z,h):
 return tuple(max(Integer(0),sum((z[3*i+j]*h[j] for j in range(3)),Integer(0))+z[18+i]) for i in range(3))
def check(p,n_expected=None):
 z=[Rational(*float(x).as_integer_ratio()) for x in p]
 h=(Integer(0),)*3
 first=None
 for n in range(1,129):
  h=step(z,h)
  s=sum((z[24+i]*h[i] for i in range(3)),z[27])
  if s>0 and first is None:first=n
  if n_expected is not None and n==n_expected-1:assert s<0
 assert first==n_expected,(first,n_expected)
def main():
 d=json.loads((P/'checkpoints315.json').read_text())['rows']
 p={x['seed']:x['p'] for x in d if x['epoch']==80}
 for seed,n in ((22601,22),(22643,23)):check(p[seed],n)
 for seed in (22621,22654,22675,22686):check(p[seed])
 print('PASS: 2 exact wrong-sign witnesses, 4 certified controls')
if __name__=='__main__':main()
