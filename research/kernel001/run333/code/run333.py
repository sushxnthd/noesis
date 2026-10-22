#!/usr/bin/env python3
"""Run333 frozen two-class interval LP. Exact Fraction replay is authoritative."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent.parent
assert hashlib.sha256((P/'input/checkpoints326.json').read_bytes()).hexdigest()=='628493d45ba6468144e4a771a8d73c01786333eca26fa8afaf25336da480fe1e'
assert hashlib.sha256((P/'input/updated_outcomes329.json').read_bytes()).hexdigest()=='108d462f64cbc925b0420db3fa10f121926506623062518976d02d96c355782f'
EPS=1e-6
def unpack(p):
 p=np.asarray(p,dtype=float);return p[:18].reshape(2,3,3),p[18:24].reshape(2,3),p[24:27],p[27]
def propose(p,mask):
 A,b,v,c=unpack(p)
 ub=[];rhs=[]
 def row():return np.zeros(9)
 for j in range(3):
  a=row();a[3+j]=1;a[6+j]=-1;ub.append(a);rhs.append(0)
 for src,x,dst in [('N',0,'N'),('N',1,'P'),('P',0,'P'),('P',1,'P')]:
  for i in range(3):
   a=row()
   for j in range(3):
    z=A[x,i,j]
    if src=='N':
     if z>0:a[j]+=z
    else:a[(6 if z>0 else 3)+j]+=z
   a[(0 if dst=='N' else 6)+i]-=1
   ub.append(a);rhs.append(-b[x,i])
   if dst=='P' and ((mask>>i)&1):
    a=row()
    for j in range(3):
     z=A[x,i,j]
     if src=='N':
      if z<0:a[j]-=z
     else:a[(3 if z>0 else 6)+j]-=z
    a[3+i]+=1
    ub.append(a);rhs.append(b[x,i])
 a=row()
 for i in range(3):a[i]=max(0,v[i])
 ub.append(a);rhs.append(-EPS-c)
 a=row()
 for i in range(3):a[(3 if v[i]>0 else 6)+i]-=v[i]
 ub.append(a);rhs.append(c-EPS)
 bounds=[(0,1e7)]*3 + [((0,1e7) if (mask>>i)&1 else (0,0)) for i in range(3)]+[(0,1e7)]*3
 objective=np.array([1]*3+[0]*3+[1]*3,dtype=float)
 r=linprog(objective,A_ub=np.array(ub),b_ub=np.array(rhs),bounds=bounds,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
 if r.success:return r.x.tolist(),r.message
 return None,r.message
def verify_exact(p,vals,mask):
 p=list(map(F.from_float,p));A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in range(2)]
 b=[[p[18+3*x+i] for i in range(3)] for x in range(2)];v=p[24:27];c=p[27]
 vals=list(map(F.from_float,vals));Nlo=[F(0)]*3;Nhi=vals[:3];Plo=vals[3:6];Phi=vals[6:9]
 if not all(F(0)<=l<=u for l,u in zip(Plo,Phi)) or any(u<0 for u in Nhi):return False,'invalid_box'
 if any(Plo[i]!=0 for i in range(3) if not (mask>>i)&1):return False,'inactive_lower'
 if not (c+sum(v[i]*Nhi[i] for i in range(3) if v[i]>0)<0):return False,'negative_output'
 if not (c+sum(v[i]*(Plo[i] if v[i]>0 else Phi[i]) for i in range(3))>0):return False,'positive_output'
 for src,x,dst in [('N',0,'N'),('N',1,'P'),('P',0,'P'),('P',1,'P')]:
  lo,hi=(Nlo,Nhi) if src=='N' else (Plo,Phi)
  dlo,dhi=(Nlo,Nhi) if dst=='N' else (Plo,Phi)
  for i in range(3):
   prelo=b[x][i]+sum(A[x][i][j]*(lo[j] if A[x][i][j]>=0 else hi[j]) for j in range(3))
   prehi=b[x][i]+sum(A[x][i][j]*(hi[j] if A[x][i][j]>=0 else lo[j]) for j in range(3))
   if max(F(0),prelo)<dlo[i]:return False,f'lower_{src}{x}_{i}'
   if max(F(0),prehi)>dhi[i]:return False,f'upper_{src}{x}_{i}'
 return True,'certificate'
def run():
 ck=json.loads((P/'input/checkpoints326.json').read_text())
 lab=json.loads((P/'input/updated_outcomes329.json').read_text())
 outcomes={r['seed']:r['outcome'] for r in lab['rows']}
 records=[]
 for r in ck['rows']:
  if r['epoch']!=80:continue
  found=None;status=[]
  for mask in range(8):
   box,msg=propose(r['p'],mask)
   if box is not None:
    ok,reason=verify_exact(r['p'],box,mask)
    status.append({'mask':mask,'lp':'feasible','exact':reason})
    if ok:
     found={'mask':mask,'box':box};break
   else:status.append({'mask':mask,'lp':msg,'exact':None})
  records.append({'seed':r['seed'],'prior':outcomes[r['seed']],'certified':found is not None,'certificate':found,'trials':status})
 assert len(records)==384
 counts={name:{'total':sum(r['prior']==name for r in records),'new':sum(r['prior']==name and r['certified'] for r in records)} for name in ('certified','incorrect','unresolved')}
 assert counts['incorrect']['new']==0,'UNSOUND CERTIFICATE!'
 out={'run':333,'method':'two_class_axis_aligned_interval_lp_exact_replay','frozen_criterion':'>=3 new certificates among 173 unresolved and zero incorrect false positives','counts':counts,'passed':counts['unresolved']['new']>=3,'records':records}
 (P/'results/results333.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'counts':counts,'passed':out['passed']},indent=2))
if __name__=='__main__':run()
