#!/usr/bin/env python3
"""NOESIS Run350: deterministic training and independent exact verification."""
import hashlib, json, subprocess, sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/'run340'))
sys.path.insert(0,str(ROOT/'run349'))
try:
 from cert340 import find
except ImportError:
 from cert340 import certificate as find
try:
 from independent340 import verify as independent_certificate
except ImportError:
 from independent340 import check as independent_certificate
from run349 import generate, exact_states

CASES={
 33053:(30,['0','0100000011','01000000000000000000000','10000000000000000000001','10000000000000000000100']),
 33068:(55,['1','111111101','1111111100000000000000']),
}
SHALLOW=sorted(set([format(i,f'0{n}b') for n in range(1,9) for i in range(2**n)]+['1'*k for k in range(9,17)]+['1'+'0'*a+'1'+'0'*b for a in range(15) for b in range(15-a)]+['1'+'0'*k for k in range(16)]+['111111111111','100000001','10000000000001']),key=lambda w:(len(w),w))
DEEP=generate();D23=[w for w in DEEP if len(w)<=23]
SHORT=[format(i,f'0{n}b') for n in range(1,9) for i in range(2**n)]
assert len(SHALLOW)==618 and len(DEEP)==7006 and len(D23)==2644 and len(SHORT)==510

def rational(x):return sp.Rational(*float(x).as_integer_ratio())
def independent_states(p,words):
 q=list(map(rational,p));a=[sp.Matrix(3,3,q[9*x:9*x+9]) for x in (0,1)];b=[sp.Matrix(q[18+3*x:21+3*x]) for x in (0,1)]
 cache={'':sp.zeros(3,1)}
 def f(w):
  if w not in cache:
   z=a[int(w[-1])]*f(w[:-1])+b[int(w[-1])]
   cache[w]=sp.Matrix([max(sp.Integer(0),z[j]) for j in range(3)])
  return cache[w]
 return [f(w) for w in words]

def exact_margin(p,words,coefs,bias):
 states=exact_states(p,words)
 return min((1 if w.count('1')%2 else -1)*sum((coefs[j]*h[j] for j in range(3)),bias) for w,h in zip(words,states))

def exact_separator(p,words):
 states=exact_states(p,words)
 h=np.asarray([[float(z) for z in row] for row in states]);scale=np.maximum(np.max(np.abs(h),axis=0),1)
 sign=np.asarray([1 if w.count('1')%2 else -1 for w in words]);x=np.column_stack((h/scale,np.ones(len(words))))
 res=linprog(np.zeros(4),A_ub=-sign[:,None]*x,b_ub=-np.ones(len(words)),bounds=[(None,None)]*4,method='highs')
 assert res.success,res.message
 coef=[F.from_float(float(res.x[j]/scale[j])) for j in range(3)];bias=F.from_float(float(res.x[3]))
 margin=exact_margin(p,words,coef,bias)
 assert margin>0
 return {'minimum_margin':str(margin),'coefficients':[str(z) for z in coef],'bias':str(bias)}

def exact_collision(p,words):
 h=independent_states(p,words)
 columns=[[int(w.count('1')%2==1),int(w.count('1')%2==0)]+[(1 if w.count('1')%2 else -1)*h[j] for j in range(3)] for w,h in zip(words,h)]
 m=sp.Matrix([list(row) for row in zip(*columns)]);sol,params=m.gauss_jordan_solve(sp.Matrix([1,1,0,0,0]))
 if params.rows:sol=sol.subs({v:0 for v in params})
 assert all(z>0 for z in sol)
 assert m*sol==sp.Matrix([1,1,0,0,0])
 fr=[F(int(z.p),int(z.q)) for z in sol];hs=exact_states(p,words)
 assert all(sum((fr[i]*hs[i][j]*(1 if words[i].count('1')%2 else -1) for i in range(len(words))),F(0))==0 for j in range(3))
 return [str(z) for z in sol]

def main():
 source=(ROOT/'run348'/'train348.py').read_text()
 assert 'SEEDS=list(range(32000,32192))' in source
 trainer=source.replace('SEEDS=list(range(32000,32192))','SEEDS=list(range(33000,33192))').replace('trajectories348.json','trajectories350.json').replace('training348_summary.json','training350_summary.json')
 (HERE/'train350.py').write_text(trainer)
 subprocess.run([sys.executable,str(HERE/'train350.py')],check=True)
 path=HERE/'trajectories350.json';data=json.loads(path.read_text());rows={(r['seed'],r['epoch']):r for r in data['rows']}
 assert len(rows)==192*201
 results={'protocol_sha256':hashlib.sha256((HERE/'FROZEN_PROTOCOL.md').read_bytes()).hexdigest(),'trajectories_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'cohort_size':192,'endpoint_certificates':[],'cases':[]}
 for seed in range(33000,33192):
  p=rows[seed,200]['p'];m=find(p)
  assert (m is not None)==any(independent_certificate(p,tuple(i for i in range(3) if mask>>i&1)) for mask in range(8))
  if m is not None:results['endpoint_certificates'].append(seed)
 assert len(results['endpoint_certificates'])==10,results['endpoint_certificates']
 for seed,(epoch,words) in CASES.items():
  early=rows[seed,epoch];later=rows[seed,epoch+1]
  assert early['accuracy']==later['accuracy']==1
  assert later['bce']<early['bce']
  p=early['p'];h=exact_states(p,SHORT+words)
  v=list(map(lambda z:F.from_float(float(z)),p[24:27]));bias=F.from_float(float(p[27]))
  logits=[sum((v[j]*z[j] for j in range(3)),bias) for z in h]
  assert all((z>0)==bool(w.count('1')%2) for w,z in zip(SHORT,logits[:510]))
  errors=[w for w,z in zip(words,logits[510:]) if (z>0)!=bool(w.count('1')%2)]
  assert errors
  collision=exact_collision(p,words)
  shallow=exact_separator(p,SHALLOW)
  next_deep=exact_separator(later['p'],D23)
  first_cert=next(t for t in range(201) if find(rows[seed,t]['p']) is not None)
  assert first_cert>epoch
  results['cases'].append({'seed':seed,'obstruction_epoch':epoch,'next_separable_epoch':epoch+1,'first_certified_epoch':first_cert,'witness_words':words,'exact_convex_coefficients':collision,'early_failure':errors[0],'shallow_618_exact_separator':shallow,'next_deep_2644_exact_separator':next_deep,'early_bce':early['bce'],'next_bce':later['bce']})
 selected=[rows[seed,t] for seed,(ep,_) in CASES.items() for t in (ep,ep+1,200)]
 (HERE/'selected_checkpoints350.json').write_text(json.dumps(selected,indent=2)+'\n')
 (HERE/'results350.json').write_text(json.dumps(results,indent=2)+'\n')
 print('EXACT_RUN350_PASS',len(results['cases']),'endpoint certificates',len(results['endpoint_certificates']))
if __name__=='__main__':main()
