from fractions import Fraction as F

def cert(p):
 a,b,v,c=p[:3],p[3:6],p[6],p[7]; L=max(F(0),b[2]); U=b[1]
 return (v>0 and v*L+c<0 and v*U+c>0 and U>L and a[0]>=0 and
         a[0]*L+b[0]<=L and a[0]*U+b[0]>=U and a[1]>=0 and
         b[1]>=U and a[2]<=0 and b[2]<=L)

def repair(p):
 q=p.copy(); a,b=p[0],p[3]; L=max(F(0),p[5]); U=p[4]
 assert L==0 and U>0
 if q[2]>0:q[2]=F(0)
 if a>=1:
  lo=(1-a)*U;hi=(1-a)*L; bp=min(max(b,lo),hi)
  options=[(abs(bp-b),3,bp)]
  if b<=0:
   ap=max(a,F(1)-b/U);options.append((abs(ap-a),0,ap))
  _,idx,val=min(options,key=lambda t:(t[0],t[1]));q[idx]=val
 elif b<=0:q[0]=F(1)-b/U
 else:q[0]=F(1);q[3]=F(0)
 return q

def witness_wrong(p,family,n,sym=None):
 word=([sym]+[0]*n if family=='symbol-hold' else [1]+[0]*n+[2]);h=F(0);y=0
 for x in word:
  h=max(F(0),p[x]*h+p[3+x]);y=1 if x==1 else (0 if x==2 else y)
 return (p[6]*h+p[7]>0)!=bool(y)
