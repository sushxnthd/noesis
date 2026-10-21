from base319 import *
from itertools import permutations
D=[(F(1),)*3,(F(2),F(1),F(1,2)),(F(1,3),F(3),F(2)),(F(5),F(1,5),F(1))]
for q in permutations(range(3)):
 for d in D:
  S=lambda v:[d[q[i]]*v[q[i]] for i in range(3)]
  for x in range(2):
   B=[d[q[i]]*b[x][q[i]] for i in range(3)]
   assert B==S(b[x])
   for j in range(3):
    e=[F(int(i==j)) for i in range(3)]
    M=[[d[q[i]]*a[x][q[i]][q[t]]/d[q[t]] for t in range(3)] for i in range(3)]
    mv=lambda mat,v:[sum(mat[i][t]*v[t] for t in range(3)) for i in range(3)]
    assert mv(M,S(e))==S(mv(a[x],e))
  for j in range(3):
   e=[F(int(t==j)) for t in range(3)]
   assert sum(w[q[i]]/d[q[i]]*S(e)[i] for i in range(3))==w[j]
print('PASS 24 exact conjugacy checks')