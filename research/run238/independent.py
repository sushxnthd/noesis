import json
from collections import deque
from pathlib import Path
R=Path(__file__).parent
def dy(n,e=0):
 if n==0:return (0,0)
 while e and n%2==0:n//=2;e-=1
 return (n,e)
def fd(x):
 n,d=float(x).as_integer_ratio();return dy(n,d.bit_length()-1)
def add(x,y):
 n,e=x;m,f=y;k=max(e,f);return dy((n<<(k-e))+(m<<(k-f)),k)
def mul(x,y):return dy(x[0]*y[0],x[1]+y[1])
def cmp(x,y):
 n,e=x;m,f=y;k=max(e,f);return ((n<<(k-e))>(m<<(k-f)))-((n<<(k-e))<(m<<(k-f)))
def clip(x):return (1,0) if cmp(x,(1,0))>0 else ((-1,0) if cmp(x,(-1,0))<0 else x)
def dot(a,b):
 s=(0,0)
 for x,y in zip(a,b):s=add(s,mul(x,y))
 return s
def check(row,limit=2500,max_depth=15):
 p=row['params'];dim=row['dim']
 W=[[[fd(a) for a in line] for line in mat] for mat in p['W']]
 b=[[fd(a) for a in vec] for vec in p['b']];v=[fd(a) for a in p['v']];c=fd(p['c'])
 h0=((1,1),(-1,1),(1,2))+(((1,3),) if dim==4 else ())
 seen={(0,h0):()};queue=deque([(0,h0)])
 while queue:
  q,h=queue.popleft();w=seen[(q,h)]
  if len(w)>=max_depth:return dict(status='ABSTAIN',reason='depth_limit',states=len(seen))
  for t in range(3):
   qq=0 if t==2 else (1 if t==1 else q)
   hh=tuple(clip(add(dot(W[t][j],h),b[t][j])) for j in range(dim))
   z=add(dot(v,hh),c)
   if (qq==1 and cmp(z,(0,0))<=0) or (qq==0 and cmp(z,(0,0))>=0):
    return dict(status='INCORRECT',witness=list(w+(t,)))
   st=(qq,hh)
   if st not in seen:
    if len(seen)>=limit:return dict(status='ABSTAIN',reason='state_limit',states=len(seen))
    seen[st]=w+(t,);queue.append(st)
 return dict(status='CERTIFIED',states=len(seen))
if __name__=='__main__':
 D=json.load(open(R/'CHECKPOINTS.json'));A=json.load(open(R/'EXACT.json'))
 rows={(r['dim'],r['seed'],r['arm'],r['epoch']):r for r in D['rows']};out=[]
 for a in A:
  key=tuple(a[k] for k in ['dim','seed','arm','epoch']);r=check(rows[key])
  same=r['status']==a['status'] and (r['status']!='CERTIFIED' or r['states']==a['states']) and (r['status']!='INCORRECT' or r['witness']==a['witness'])
  out.append(dict(key=key,agrees=same,result=r))
  if not same:raise AssertionError((key,r,a))
 (R/'INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n')
 print('Independent agreement',len(out),'/',len(A))
