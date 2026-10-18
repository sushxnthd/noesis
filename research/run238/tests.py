from verify import check as a
from independent import check as b
W=[[[0]*3 for _ in range(3)] for _ in range(3)]
W[0][0][0]=4
def row(c):
 return dict(dim=3,params=dict(W=W,b=[[-3,0,0],[3,0,0],[-3,0,0]],v=[1,0,0],c=c))
for c,status in [(0,'CERTIFIED'),(4,'INCORRECT')]:
 x=a(row(c));y=b(row(c))
 assert x['status']==y['status']==status,(x,y)
print('run238 tests pass')
