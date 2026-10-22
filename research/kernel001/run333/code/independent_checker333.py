from fractions import Fraction as Q
def verify(p, box):
 p=[Q.from_float(x) for x in p]
 A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in (0,1)]
 b=[[p[18+3*x+i] for i in range(3)] for x in (0,1)]
 v=p[24:27];c=p[27]
 nlo=[Q(0)]*3;nhi=list(map(Q.from_float,box[:3]))
 plo=list(map(Q.from_float,box[3:6]));phi=list(map(Q.from_float,box[6:9]))
 if not all(0<=lo<=hi for lo,hi in zip(plo,phi)):return False
 if not all(0<=hi for hi in nhi):return False
 if c+sum(v[i]*nhi[i] for i in range(3) if v[i]>0)>=0:return False
 if c+sum(v[i]*(plo[i] if v[i]>0 else phi[i]) for i in range(3))<=0:return False
 for src,x,dst in [('N',0,'N'),('N',1,'P'),('P',0,'P'),('P',1,'P')]:
  lo,hi=(nlo,nhi) if src=='N' else (plo,phi)
  dlo,dhi=(nlo,nhi) if dst=='N' else (plo,phi)
  for i in range(3):
   a=b[x][i]+sum(A[x][i][j]*(lo[j] if A[x][i][j]>=0 else hi[j]) for j in range(3))
   z=b[x][i]+sum(A[x][i][j]*(hi[j] if A[x][i][j]>=0 else lo[j]) for j in range(3))
   if max(0,a)<dlo[i] or max(0,z)>dhi[i]:return False
 return True
