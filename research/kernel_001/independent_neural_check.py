"""Independent Fraction-valued BFS; does not import the experiment implementation."""
from fractions import Fraction
def certify(M):
    states={(0,Fraction(0))}
    for n in range(M+1):
        assert all(t==s for t,s in states),(M,n,states)
        if n<M:
            nxt=set()
            for t,s in states:
                for x in (-1,1):
                    z=s+x
                    nxt.add((max(0,t+x),max(Fraction(0),z)-max(Fraction(0),z-M)))
            states=nxt
    h=Fraction(0)
    for _ in range(M+1):
        z=h+1
        h=max(Fraction(0),z)-max(Fraction(0),z-M)
    assert h==M
    return M+1
if __name__=="__main__":
    print({M:certify(M) for M in range(1,11)})
