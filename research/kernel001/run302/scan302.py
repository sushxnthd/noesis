import numpy as np
from generator302 import patterns
from independent302 import bad
def search_one(p):
 a=np.array(p[:18]).reshape(2,3,3);b=np.array(p[18:24]).reshape(2,3)
 v=np.array(p[24:27]);c=p[27]
 for n in range(13,257):
  for family,w in patterns(n):
   h=np.zeros(3);y=0
   for t,sym in enumerate(w,1):
    x=int(sym);y=max(y,x);h=np.maximum(0,a[x]@h+b[x])
    if int(h@v+c>0)!=y:
     prefix=w[:t];k=bad(p,prefix)
     if k is not None:return family,prefix[:k]
 return None
