"""Run343 exact independent trained-model spoof verification. Python stdlib only."""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from pathlib import Path
import json
P=Path(__file__).resolve().parent
model=json.loads((P/'model343.json').read_text())
assert (model['seed'],model['epoch'])==(31089,200)
p=[Q.from_float(float(x)) for x in model['p']]
assert len(p)==45
A=[[[p[16*x+4*i+j] for j in range(4)] for i in range(4)] for x in (0,1)]
b=[p[32+4*x:36+4*x] for x in (0,1)]
v=p[40:44];c=p[44]
def step(h,x):
 return tuple(max(Q(0),sum((A[x][i][j]*h[j] for j in range(4)),b[x][i])) for i in range(4))
def output(h):return sum((v[i]*h[i] for i in range(4)),c)
states=[(Q(0),)*4];count=0
for n in range(1,13):
 states=[step(h,x) for h in states for x in (0,1)]
 for j,h in enumerate(states):
  assert (output(h)>0)==bool(j.bit_count()%2),(n,j)
 count+=len(states)
assert count==8190
h=(Q(0),)*4
for bit in '1000000000000':h=step(h,int(bit))
z=output(h)
assert z<0
h=(Q(0),)*4
for n in range(1,17):
 h=step(h,1 if n==1 else 0)
 if n in (13,14,15):assert output(h)<0
assert h[0]>=4 and h[1]>=10*h[0] and h[2]==h[3]==0
M=A[0];d=b[0]
assert M[0][0]>0 and M[0][1]>0
assert M[0][0]+10*M[0][1]>=1
assert (M[0][0]+10*M[0][1]-1)*4+d[0]>=0
assert M[1][1]-10*M[0][1]>=0
assert M[1][0]-10*M[0][0]+10*(M[1][1]-10*M[0][1])>=0
assert d[1]-10*d[0]>=0
for i in (2,3):
 assert M[i][1]<=0 and M[i][0]+10*M[i][1]<=0 and d[i]<=0
assert v[1]<0 and v[0]+10*v[1]<=0 and c<0
with localcontext() as ctx:
 ctx.prec=3000
 q=[Decimal.from_float(float(x)) for x in model['p']]
 h2=[Decimal(0)]*4
 for bit in '1000000000000':
  x=int(bit)
  h2=[max(Decimal(0),sum((q[16*x+4*i+j]*h2[j] for j in range(4)),q[32+4*x+i])) for i in range(4)]
 z2=sum((q[40+i]*h2[i] for i in range(4)),q[44])
 assert z2==Decimal(z.numerator)/Decimal(z.denominator)
print(json.dumps({'seed':31089,'epoch':200,'exact_correct_through_12':count,'first_longer_wrong':'1000000000000','infinite_wrong_family':'1+0^k for all k>=12','exact_fraction':True,'independent_decimal':True}))
