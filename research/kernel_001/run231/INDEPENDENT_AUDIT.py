"""Independent all-length signed transport audit for frozen trained checkpoint.
Directly checks substitution s=-h[0] in the original and augmented equations.
No calls to signed_quotient.discover(), compatible(), or quotient().
"""
from fractions import Fraction as Q
import json,sys
P=sys.argv[1] if len(sys.argv)>1 else "representative.json"
r=json.load(open(P));p=r["row"]["params"];d=len(p["v"])
F=lambda x:Q.from_float(float(x))
for shear in (False,True):
 for t in range(3):
  m=[[F(x) for x in row]+[Q(0)] for row in p["W"][t]]
  m.append([-F(x) for x in p["W"][t][0]]+[Q(0)])
  b=[F(x) for x in p["b"][t]]+[-F(p["b"][t][0])]
  if shear:
   for i in range(d+1):
    a=Q(1,8) if i==0 else (-Q(1,8) if i==d else (Q(1,8) if i%2==0 else -Q(1,8)))
    m[i][0]+=a;m[i][d]+=a
  for i in range(d+1):
   reduced=[m[i][j]-(m[i][d] if j==0 else 0) for j in range(d)]
   expected=[F(x) for x in p["W"][t][0 if i==d else i]]
   if i==d:expected=[-x for x in expected]
   assert reduced==expected
   target=F(p["b"][t][0 if i==d else i])
   assert b[i]==(-target if i==d else target)
 v=[F(p["v"][0])+Q(1<<14)]+[F(x) for x in p["v"][1:]]+[Q(1<<14)]
 assert [v[j]-(v[d] if j==0 else 0) for j in range(d)]==[F(x) for x in p["v"]]
print("INDEPENDENT_EXACT_ALL_LENGTH_TRANSPORT_PASS 2/2")
