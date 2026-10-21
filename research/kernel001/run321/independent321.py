#!/usr/bin/env python3
"""Independent exact SymPy audit of Run321 reported collisions and minimality."""
import json
from pathlib import Path
from sympy import Rational, Integer
ROOT=Path(__file__).resolve().parent

def step(p,h,x):
 z=[Rational(*float(v).as_integer_ratio()) for v in p]
 return tuple(max(Integer(0),sum((z[9*x+3*i+j]*h[j] for j in range(3)),Integer(0))+z[18+3*x+i]) for i in range(3))

def main():
 params={(r['seed'],r['epoch']):r['p'] for r in json.loads((ROOT/'checkpoints315.json').read_text())['rows']}
 rows=json.loads((ROOT/'results321.json').read_text())['rows']
 count=0
 for r in rows:
  hit=r['first_collision']
  if not hit:continue
  p=params[(r['seed'],r['epoch'])]
  a=(Integer(0),)*3
  b=step(p,a,1)
  for n in range(1,hit['n']+1):
   a=step(p,a,0)
   assert (a==b)==(n==hit['n']),('minimality',r['seed'],r['epoch'],n)
   b=step(p,b,0)
  assert [str(x) for x in a]==hit['state']
  assert a!=(a[0]+Rational(1,2**50),a[1],a[2])
  count+=1
 assert count==31,count
 print('PASS: 31 exact collisions, minimality and 31 mutation controls')
if __name__=='__main__':main()
