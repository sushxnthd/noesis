import sympy as S
def check(p,E):
 q=[S.Rational(*float(x).as_integer_ratio()) for x in p]
 a=[S.Matrix(3,3,q[9*x:9*x+9]) for x in (0,1)]
 b=[S.Matrix(q[18+3*x:21+3*x]) for x in (0,1)]
 v=S.Matrix(q[24:27]);c=q[27]
 O=tuple(i for i in range(3) if b[1][i]>0)
 L=S.Matrix([b[1][i] if i in O else 0 for i in range(3)])
 if not O or c>-S.Rational(1,100000):return False
 if any(v[i]>0 for i in E) or any(v[i]<0 for i in O):return False
 if v.dot(L)+c<S.Rational(1,100000):return False
 for s,base,src in [(0,S.zeros(3,1),E),(1,L,O)]:
  for bit in (0,1):
   dst=E if s==bit else O
   vertex=a[bit]*base+b[bit]
   for i in range(3):
    if i not in dst and (vertex[i]>0 or any(a[bit][i,j]>0 for j in src)):return False
    if i in dst and s!=bit and (vertex[i]<L[i] or any(a[bit][i,j]<0 for j in src)):return False
 return True
