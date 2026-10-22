from fractions import Fraction as Q
def verify(p,E):
 p=[Q.from_float(float(x)) for x in p]
 A=[[[p[9*x+3*i+j] for j in range(3)] for i in range(3)] for x in range(2)]
 b=[p[18+3*x:21+3*x] for x in range(2)]
 v=p[24:27];c=p[27];O=tuple(i for i in range(3) if b[1][i]>0)
 if not O or c>-Q(1,100000) or any(v[i]>0 for i in E):return False
 if any(v[i]<0 for i in O) or c+sum(v[i]*b[1][i] for i in O)<Q(1,100000):return False
 for state,src in [(0,E),(1,O)]:
  for bit in (0,1):
   target=state^bit;dst=E if target==0 else O
   for i in range(3):
    row=A[bit][i]
    z=b[bit][i]+sum(row[j]*b[1][j] for j in src if state==1)
    if i not in dst:
     if z>0 or any(row[j]>0 for j in src):return False
    elif target==1:
     if z<b[1][i] or any(row[j]<0 for j in src):return False
 return True
def certificate(p):
 for mask in range(8):
  E=tuple(i for i in range(3) if mask>>i&1)
  if verify(p,E):return E
 return None
