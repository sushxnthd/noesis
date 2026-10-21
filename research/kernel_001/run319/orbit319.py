from cert319 import *
from itertools import permutations
scales=[(F(1),)*3,(F(2),F(1),F(1,2)),(F(1,3),F(3),F(2)),(F(5),F(1,5),F(1))]
assert cert(a,b,w,c)
counts=[]
for perm in permutations(range(3)):
 for d in scales:
  aa=[[[d[perm[i]]*a[x][perm[i]][perm[j]]/d[perm[j]] for j in range(3)] for i in range(3)] for x in range(2)]
  bb=[[d[perm[i]]*b[x][perm[i]] for i in range(3)] for x in range(2)]
  ww=[w[perm[i]]/d[perm[i]] for i in range(3)]
  counts.append(cert(aa,bb,ww,c))
assert len(counts)==24 and sum(counts)==1
print('PASS fixed template 1/24; exact transported-cone proof in independent319.py')