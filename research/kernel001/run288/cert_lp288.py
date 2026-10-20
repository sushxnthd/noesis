import numpy as np
from scipy.optimize import linprog
def certificate_lp(p,mask):
 A=np.array(p[:8]).reshape(2,2,2);b=np.array(p[8:12]).reshape(2,2);v=p[12:14];c=p[14]
 aub=[];bub=[];eq=[];beq=[]
 def row():return np.zeros(9)
 for s in (0,1):
  for x in (0,1):
   y=0 if x==0 else 1-s
   for i in (0,1):
    r=row();r[4+2*y+i]-=1
    for j in (0,1):r[(4 if A[x,i,j]>=0 else 0)+2*s+j]+=A[x,i,j]
    aub.append(r);bub.append(-b[x,i]-1e-6)
    if mask[y][i]:
     r=row();r[2*y+i]+=1
     for j in (0,1):r[(0 if A[x,i,j]>=0 else 4)+2*s+j]-=A[x,i,j]
     aub.append(r);bub.append(b[x,i]-1e-6)
 for s in (0,1):
  r=row()
  if s==0:
   for i in (0,1):r[(4 if v[i]>=0 else 0)+i]+=v[i]
   r[8]+=1;aub.append(r);bub.append(-c)
  else:
   for i in (0,1):r[(0 if v[i]>=0 else 4)+2+i]-=v[i]
   r[8]+=1;aub.append(r);bub.append(c)
 for s in (0,1):
  for i in (0,1):
   r=row();r[2*s+i]=1;r[4+2*s+i]=-1;aub.append(r);bub.append(0)
 for i in (0,1):
  r=row();r[i]=1;eq.append(r);beq.append(0)
 for s in (0,1):
  for i in (0,1):
   if not mask[s][i]:
    r=row();r[2*s+i]=1;eq.append(r);beq.append(0)
 obj=np.zeros(9);obj[8]=-1
 sol=linprog(obj,A_ub=aub,b_ub=bub,A_eq=eq,b_eq=beq,bounds=[(0,1000)]*8+[(0,100)],method='highs')
 if sol.success and sol.x[8]>1e-6:
  return {'L':sol.x[:4].reshape(2,2).tolist(),'U':sol.x[4:8].reshape(2,2).tolist(),'margin_lp':float(sol.x[8]),'mask':mask}
 return None
