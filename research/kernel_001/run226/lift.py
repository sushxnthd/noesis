"""Prove k4/k5 generator false negatives using lifted k1 inductive boxes."""
from itertools import product
from check_remote import rows,cert,model,iv
from candidate_generator import candidate
def lifted(k):
 step,logit=model(rows[100])
 boxes={}
 for w in product('012',repeat=k):
  s=''.join(w)
  for q in (0,1):
   old=f'{q}:{s[-1]}'
   if old in cert['boxes']:
    r=cert['boxes'][old]
    boxes[(q,s)]=tuple(iv.mpf([r['lo'][j],r['hi'][j]]) for j in range(3))
 def good(q,h):
  z=logit(h);return z.a>0 if q else z.b<0
 layer=[('',0,(iv.mpf('.5'),iv.mpf('-.5'),iv.mpf('.25')))]
 for _ in range(k):
  next_layer=[]
  for w,q,h in layer:
   for t in range(3):
    nq=0 if t==2 else q^(t==1)
    nh=step(h,t);nw=w+str(t)
    assert good(nq,nh)
    next_layer.append((nw,nq,nh))
  layer=next_layer
 for w,q,h in layer:
  dest=boxes[(q,w)]
  assert all(h[j].a>=dest[j].a and h[j].b<=dest[j].b for j in range(3))
 for (q,w),h in boxes.items():
  assert good(q,h)
  for t in range(3):
   nq=0 if t==2 else q^(t==1)
   dest=boxes[(nq,w[1:]+str(t))];nh=step(h,t)
   assert all(nh[j].a>=dest[j].a and nh[j].b<=dest[j].b for j in range(3))
 return len(boxes)
if __name__=='__main__':
 for k in (4,5):
  for eps in (0.,0.003):
   assert candidate(rows[100],k,eps)['status']=='NO_CLOSED'
  print(k,'generator NO_CLOSED; lifted certificate cells',lifted(k))
