def deficit(p,W=4):
 assert len(p)==2*W*W+3*W+1
 a=[[[p[x*W*W+i*W+j] for j in range(W)] for i in range(W)] for x in range(2)]
 b=[p[2*W*W+x*W:2*W*W+(x+1)*W] for x in range(2)]
 v=p[2*W*W+2*W:2*W*W+3*W];c=p[-1];eps=1e-5
 odd=tuple(i for i in range(W) if b[1][i]>0)
 if not odd:return 1000.
 lower={i:b[1][i] for i in odd};scale=max(1.,max(abs(z) for z in p));best=1e9
 for mask in range(1<<W):
  even=tuple(i for i in range(W) if mask>>i&1)
  violations=[max(0,c+eps),*[max(0,v[i]) for i in even],*[max(0,-v[i]) for i in odd],max(0,eps-c-sum(v[i]*lower[i] for i in odd))]
  for parity,src in ((0,even),(1,odd)):
   lo={} if parity==0 else lower
   for bit in (0,1):
    tgt=even if parity^bit==0 else odd
    for i in range(W):
     row=a[bit][i];off=b[bit][i]+sum(row[j]*lo.get(j,0.) for j in src)
     if i not in tgt:violations.extend([max(0,off),*[max(0,row[j]) for j in src]])
     elif parity^bit==1:violations.extend([max(0,lower[i]-off),*[max(0,-row[j]) for j in src]])
  best=min(best,sum(violations)/scale)
 return best

def auc(pos,neg):
 return sum((x>y)+.5*(x==y) for x in pos for y in neg)/(len(pos)*len(neg))
