#!/usr/bin/env python3
"""Independent exact binary64 checker for 12 Run351 intervention cases."""
import json
from pathlib import Path
from fractions import Fraction as Q
import sympy as S
R=Path(__file__).resolve().parent
D=json.loads((R.parent/'run348'/'trajectories348.json').read_text())
OUT=json.loads((R/'outcomes.json').read_text())
def words():
 w=set()
 for n in range(1,11):
  for i in range(2**n):w.add(bin(i)[2:].zfill(n))
 for a in range(65):
  w.update(('1'+'0'*a,'0'*a+'1'))
  for b in range(65-a):w.update(('1'+'0'*a+'1'+'0'*b,'0'*a+'1'+'0'*b))
 for k in range(1,9):
  for n in range(65):w.update(('1'*k+'0'*n,'0'*n+'1'*k))
 return sorted((x for x in w if 0<len(x)<=23),key=lambda x:(len(x),x))
W=words();assert len(W)==2644
def exact(p):
 q=[Q.from_float(float(x)) for x in p];memo={'':(Q(0),)*3}
 def state(w):
  if w not in memo:
   h=state(w[:-1]);s=int(w[-1])
   memo[w]=tuple(max(Q(0),q[18+3*s+i]+sum(q[9*s+3*i+j]*h[j] for j in range(3))) for i in range(3))
  return memo[w]
 wrong=[]
 for w in W:
  h=state(w);z=q[27]+sum(q[24+j]*h[j] for j in range(3))
  if (z>0)!=bool(w.count('1')%2) or z==0:wrong.append(w)
 return len(W)-len(wrong),wrong[0] if wrong else None
def main():
 selected={32046:[18,17],32034:[18,8],32035:[18,7],32026:[18,5]}
 checkpoints={(r['seed'],r['epoch']):r['p'] for r in D['rows'] if r['seed'] in selected}
 audited=[]
 for s,coords in selected.items():
  row=next(r for r in OUT['rows'] if r['seed']==s);t=row['epoch']
  p=checkpoints[s,t];q=checkpoints[s,t+1]
  for j in [None]+coords:
   v=p.copy()
   if j is not None:v[j]=q[j]
   n,first=exact(v)
   expected=row['counts'][0 if j is None else 2+j]
   assert n==expected,(s,j,n,expected)
   audited.append({'seed':s,'coordinate':j,'correct':n,'first_error':first})
 # Independent SymPy witness for the apparently perfect coordinate-17 finite-family repair.
 s=32046;t=next(r for r in OUT['rows'] if r['seed']==s)['epoch']
 p=checkpoints[s,t].copy();p[17]=checkpoints[s,t+1][17]
 word='01110101010';h=[S.Rational(0)]*3
 for c in word:
  x=int(c);h=[max(S.Rational(0),S.Rational(p[18+3*x+i])+sum(S.Rational(p[9*x+3*i+j])*h[j] for j in range(3))) for i in range(3)]
 z=S.Rational(p[27])+sum(S.Rational(p[24+j])*h[j] for j in range(3))
 assert z>0 and word.count('1')%2==0
 (R/'exact_outcomes.json').write_text(json.dumps({'audits':audited,'adversarial_word':word,'adversarial_logit_positive_exact':True},indent=2)+'\n')
 print('Independent exact audit: 12/12 counts agree; length-11 spoof verified.')
if __name__=='__main__':main()
