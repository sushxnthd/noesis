from run333 import propose,verify_exact
from independent_checker333 import verify

def test_known_bounded_latch():
 p=[0.]*28;p[0]=1.;p[21]=1.;p[24]=1.;p[27]=-.5
 box,_=propose(p,1)
 assert box is not None
 assert verify_exact(p,box,1)[0]
 assert verify(p,box)
 bad=p.copy();bad[24]=-1
 assert not verify(bad,box)
 bad=p.copy();bad[0]=0
 assert not verify(bad,box)

def test_bounded_negative_readout():
 p=[0.]*28;p[0]=1.;p[21]=1.;p[24]=1.;p[27]=-.5
 box,_=propose(p,1)
 bad=box.copy();bad[6]=0.25
 assert not verify(p,bad)
if __name__=='__main__':
 test_known_bounded_latch();test_bounded_negative_readout();print('3 exact checker regression gates passed')
