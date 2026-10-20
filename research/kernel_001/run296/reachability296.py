"""Exact reachable-silent-gate quotient for binary-input ReLU RNNs.
Sufficient, deliberately incomplete certificate; all decisions use Fraction.
From h0=0, u'=ReLU(a_u*u+b_u), v'=ReLU(a_v*v+b_v) and
0<=a_u<=a_v, 0<=b_u<=b_v imply v>=u>=0 for every word.
If g'=ReLU(c_u*u+c_v*v+b), c_u>=0, c_v<=-c_u, b<=0,
then g=0 for every word. Erasing gate readout and outgoing edges
followed by backward-invisible pruning preserves all-word output.
"""
from fractions import Fraction as F

def unpack(p,w):
 z=[F.from_float(float(t)) for t in p]
 assert len(z)==2*w*w+3*w+1
 A=[[[z[x*w*w+i*w+j] for j in range(w)] for i in range(w)] for x in range(2)]
 B=[[z[2*w*w+x*w+i] for i in range(w)] for x in range(2)]
 return A,B,z[2*w*w+2*w:-1],z[-1]

def pack(A,B,v,c):
 return [z for X in A for row in X for z in row]+[z for row in B for z in row]+v+[c]

def certificate(A,B,v):
 w=len(v)
 for g in range(w):
  if not v[g]:continue
  for u in range(w):
   if u==g:continue
   for z in range(w):
    if z in (u,g):continue
    if all(A[x][u][j]==0 for x in (0,1) for j in range(w) if j!=u) and all(A[x][z][j]==0 for x in (0,1) for j in range(w) if j!=z) and all(A[x][g][j]==0 for x in (0,1) for j in range(w) if j not in (u,z)) and all(0<=A[x][u][u]<=A[x][z][z] and 0<=B[x][u]<=B[x][z] and 0<=A[x][g][u] and A[x][g][z]<=-A[x][g][u] and B[x][g]<=0 for x in (0,1)):
     return {'u':u,'v':z,'gate':g}
 return None

def quotient(p,w):
 A,B,v,c=unpack(p,w)
 proof=certificate(A,B,v)
 if proof is None:return p,w,None
 g=proof['gate'];v[g]=F(0)
 for x in (0,1):
  for i in range(w):A[x][i][g]=F(0)
 keep={i for i in range(w) if v[i]}
 while True:
  nxt=keep|{j for i in keep for j in range(w) if any(A[x][i][j] for x in (0,1))}
  if nxt==keep:break
  keep=nxt
 keep=sorted(keep)
 a=[[[A[x][i][j] for j in keep] for i in keep] for x in (0,1)]
 b=[[B[x][i] for i in keep] for x in (0,1)]
 return pack(a,b,[v[i] for i in keep],c),len(keep),dict(proof,kept=keep)

def switched(p):
 A,B,v,c=unpack(p,3)
 X=[[[F(0)]*6 for _ in range(6)] for _ in range(2)]
 Y=[[F(0)]*6 for _ in range(2)]
 for x in (0,1):
  for i in range(3):X[x][i][:3]=A[x][i];Y[x][i]=B[x][i]
  X[x][3][3]=[F(3,4),F(2)][x]
  X[x][4][4]=[F(1),F(3)][x]
  Y[x][3:]=([F(2),F(5),F(-1)] if x==0 else [F(1),F(2),F(-1)])
  X[x][5][3]=F(2);X[x][5][4]=F(-3)
 return pack(X,Y,v+[F(0),F(0),F(1)],c)
