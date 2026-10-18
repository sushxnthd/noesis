"""Untrusted float interval candidate generator; never a proof."""
import json,numpy as np
from pathlib import Path
R=Path(__file__).parent
D=json.load(open(R/'CHECKPOINTS.json'));rows={(r['seed'],r['epoch']):r for r in D['rows']}
def nextq(q,t):return 0 if t==2 else (1 if t==1 else q)
def step_interval(lo,hi,W,b,t):
 mat=W[t];a=np.where(mat>=0,mat*lo,mat*hi).sum(axis=1)+b[t]
 z=np.where(mat>=0,mat*hi,mat*lo).sum(axis=1)+b[t]
 return np.nextafter(np.tanh(a),-np.inf),np.nextafter(np.tanh(z),np.inf)
def target(word):
 q=0
 for t in word:q=nextq(q,t)
 return q
def candidate(row,k=1,maxiter=500):
 p=row['params'];W=np.array(p['W']);b=np.array(p['b']);v=np.array(p['v']);c=p['c']
 h0=np.array([.5,-.5,.25]);boxes={}
 for length in range(1,k+1):
  for n in range(3**length):
   word=tuple((n//3**(length-1-j))%3 for j in range(length));h=h0.copy()
   for t in word:h=np.tanh(W[t]@h+b[t])
   q=target(word)
   if (h@v+c>0)!=bool(q):return {'status':'prefix_error','word':word}
   if length==k:boxes[(q,word)]=(np.nextafter(h,-np.inf),np.nextafter(h,np.inf))
 for iteration in range(maxiter):
  nxt={key:(lo.copy(),hi.copy()) for key,(lo,hi) in boxes.items()}
  for (q,word),(lo,hi) in boxes.items():
   for t in range(3):
    dest=(nextq(q,t),word[1:]+(t,));a,z=step_interval(lo,hi,W,b,t)
    if dest in nxt:
     l,h=nxt[dest];nxt[dest]=(np.minimum(l,a),np.maximum(h,z))
    else:nxt[dest]=(a,z)
  diff=max(max(float(np.max(np.abs(nxt[key][j]-boxes[key][j]))) for j in (0,1)) for key in boxes)
  boxes=nxt
  if any(np.max(hi-lo)>2.01 for lo,hi in boxes.values()):return {'status':'diverged','iterations':iteration+1}
  if diff<1e-12:break
 else:return {'status':'no_convergence','iterations':maxiter}
 for eps in (1e-10,1e-9,1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2):
  inv={key:(np.maximum(-1,lo-eps),np.minimum(1,hi+eps)) for key,(lo,hi) in boxes.items()}
  min_margin=1e9
  for (q,word),(lo,hi) in inv.items():
   zlo=np.where(v>=0,v*lo,v*hi).sum()+c;zhi=np.where(v>=0,v*hi,v*lo).sum()+c
   min_margin=min(min_margin,zlo if q else -zhi)
  if min_margin<=0:continue
  gap=0
  for (q,word),(lo,hi) in inv.items():
   for t in range(3):
    dest=(nextq(q,t),word[1:]+(t,));a,z=step_interval(lo,hi,W,b,t);l,h=inv[dest]
    gap=max(gap,float(np.max(l-a)),float(np.max(z-h)))
  if gap<=0:
   return {'status':'CANDIDATE','k':k,'iterations':iteration+1,'margin':min_margin,'eps':eps,'boxes':{str(q)+':'+''.join(map(str,word)):{'lo':[format(x,'.17g') for x in lo],'hi':[format(x,'.17g') for x in hi]} for (q,word),(lo,hi) in inv.items()}}
 return {'status':'no_closed_invariant','margin':min_margin,'iterations':iteration+1,'min_gap':gap}
out=[]
for seed in D['seeds']:
 for epoch in (0,50,100,200):
  row=rows[seed,epoch];attempts=[]
  for k in (1,2,3):
   a=candidate(row,k);attempts.append({'k':k,'status':a['status'],'margin':a.get('margin')})
   if a['status']=='CANDIDATE':break
  out.append({'seed':seed,'epoch':epoch,'result':a,'attempts':attempts})
  print(seed,epoch,a['status'],a.get('k'),flush=True)
(R/'CANDIDATES.json').write_text(json.dumps({'results':out},indent=2)+'\n')
