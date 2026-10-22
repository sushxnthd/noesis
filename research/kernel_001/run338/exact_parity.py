from fractions import Fraction as Q

def certify(p,j):
    p=[Q.from_float(float(x)) for x in p]
    A=[[p[4*x+2*i:4*x+2*i+2] for i in range(2)] for x in (0,1)]
    b=[p[8+2*x:10+2*x] for x in (0,1)]
    v=p[12:14];c=p[14];L=b[1][j];eps=Q(1,100000)
    return (L>0 and c<=-eps and all(t<=0 for t in b[0])
        and all(t>=0 for t in v) and v[j]*L+c>=eps
        and all(t>=0 for t in A[0][j])
        and A[0][j][j]*L+b[0][j]>=L
        and all(t<=0 for row in A[1] for t in row)
        and all(A[1][i][j]*L+b[1][i]<=0 for i in range(2)))
