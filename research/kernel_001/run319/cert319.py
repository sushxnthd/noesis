from base319 import *
def cert(a,b,w,c):
 e=[max(F(0),v) for v in b[1]]
 ok=all(v<=0 for v in b[0]) and c<0 and e[1]==0 and 0<=e[0]<=k*e[2] and e[2]>=T
 for x in range(2):
  ok &= ge(-a[x][1][0],-a[x][1][2],-b[x][1])
  ok &= ge(a[x][2][0],a[x][2][2],b[x][2]-T)
  ok &= ge(k*a[x][2][0]-a[x][0][0],k*a[x][2][2]-a[x][0][2],k*b[x][2]-b[x][0])
 return ok and ge(w[0],w[2],c-F(1,1000))