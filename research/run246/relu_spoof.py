from itertools import product

def ok(w,H=8):
 x=q=0
 for t in w:
  x=max(0,x+(0,1,1-H)[t]);q=0 if t==2 else (1 if t==1 else q)
  if (2*x-1>0)!=bool(q):return False
 return True

if __name__=='__main__':
 assert all(ok(w) for n in range(1,9) for w in product(range(3),repeat=n))
 assert not ok([1]*8+[2]);print('9840 bounded inputs passed; length-9 failure')
