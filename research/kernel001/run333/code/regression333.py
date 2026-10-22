from independent_checker333 import verify
def test_bounded_latch():
 p=[0.]*28;p[0]=1.;p[21]=1.;p[24]=1.;p[27]=-.5
 box=[0.,0.,0.,1.,0.,0.,1.,0.,0.]
 assert verify(p,box)
 wrong=p.copy();wrong[24]=-1.
 assert not verify(wrong,box)
 no_memory=p.copy();no_memory[0]=0.
 assert not verify(no_memory,box)
 bad_box=box.copy();bad_box[6]=.25
 assert not verify(p,bad_box)
if __name__=='__main__':
 test_bounded_latch();print('4 exact independent regression gates passed')
