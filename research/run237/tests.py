from verify import check as v
from independent import check as i
def check(row,status,witness=None):
 a=v(row);b=i(row)
 assert a['status']==b['status']==status,(a,b)
 if witness is not None:assert a['witness']==b['witness']==witness,(a,b)
def row(W,b,c=0):
 return dict(dim=3,params=dict(W=W,b=b,v=[1,0,0],c=c))
W=[[[0]*3 for _ in range(3)] for _ in range(3)]
W[0][0][0]=5;W[1][0][0]=-4
check(row(W,[[-3,0,0],[3,0,0],[-1,0,0]]),'CERTIFIED')
W[1][0][0]=0
check(row(W,[[-3,0,0],[1,0,0],[-1,0,0]]),'INCORRECT',[1,1])
print('exact automaton and latch spoof tests passed')
