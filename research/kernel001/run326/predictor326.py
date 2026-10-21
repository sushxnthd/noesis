import numpy as np
from sklearn.svm import LinearSVC
def score(p):
 p=np.asarray(p,float);a=p[:18].reshape(2,3,3);b=p[18:24].reshape(2,3)
 h=np.zeros((1,3));y=np.zeros(1,dtype=int);z=[]
 for n in range(1,9):
  h=np.concatenate([np.maximum(0,h@a[x].T+b[x]) for x in (0,1)])
  y=np.concatenate([y,np.ones_like(y)])
  z.append((h.copy(),y.copy()))
 H=np.concatenate([r[0] for r in z[:6]]);Y=np.concatenate([r[1] for r in z[:6]])
 d=np.sqrt(np.mean(H*H,axis=0));d=np.where(d>1e-12,d,1.)
 m=LinearSVC(C=1,class_weight='balanced',dual=False,tol=1e-7,max_iter=10000,random_state=0)
 m.fit(H/d,Y);den=float(np.std(m.decision_function(H/d)))+1e-12
 return min(min(float(np.quantile(s[v==1],.1)),float(np.quantile(-s[v==0],.1))) for s,v in ((m.decision_function(h/d),y) for h,y in z[6:8]))/den
