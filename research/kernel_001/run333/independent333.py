"""Independent exact rational simplex checker. Does not import proof333.py."""
import json,sys
from sympy import Rational as Q
from sympy.solvers.simplex import linprog,InfeasibleLPError,UnboundedLPError

def verify(p):
    z=[Q(*float(t).as_integer_ratio()) for t in p]
    A=[[z[9*x+3*i:9*x+3*i+3] for i in range(3)] for x in (0,1)]
    b=[z[18+3*x:21+3*x] for x in (0,1)]
    v=z[24:27];c=z[27];T=-c+Q(1,100000)
    if c>=0 or any(t>0 for t in b[0]):return False
    if sum(v[i]*max(Q(0),b[1][i]) for i in range(3))<T:return False
    for x in (0,1):
        for mask in range(8):
            lhs=[v];rhs=[T]
            for i in range(3):
                if mask>>i&1:lhs.append(A[x][i]);rhs.append(-b[x][i])
                else:lhs.append([-a for a in A[x][i]]);rhs.append(b[x][i])
            obj=[sum((v[i]*A[x][i][j] for i in range(3) if mask>>i&1),Q(0)) for j in range(3)]
            bias=sum((v[i]*b[x][i] for i in range(3) if mask>>i&1),Q(0))
            try:
                minimum,_=linprog(obj,[[-a for a in row] for row in lhs],[-r for r in rhs])
            except InfeasibleLPError:continue
            except UnboundedLPError:return False
            if minimum+bias<T:return False
    return True

if __name__=='__main__':
    raw=json.load(open(sys.argv[1]))
    for row in raw['rows']:
        if row['epoch']==80:print(row['seed'],verify(row['p']))
