"""Independent exact integer-dyadic checker, no Fraction, numpy or torch."""
import json
from collections import deque
from pathlib import Path
R=Path(__file__).parent
def dy(n,e=0):
 if n==0:return (0,0)
 while e and n%2==0:n//=2;e-=1
 return (n,e)
def float_dy(x):
 n,d=float(x).as_integer_ratio();return dy(n,d.bit_length()-1)
def add(x,y):
 n,e=x;m,f=y;k=max(e,f)
 return dy((n<<(k-e))+(m<<(k-f)),k)
def mul(x,y):return dy(x[0]*y[0],x[1]+y[1])
def cmp(x,y):
 n,e=x;m,f=y;k=max(e,f);a=n<<(k-e);b=m<<(k-f)
 return (a>b)-(a<b)
def clamp(x):
 if cmp(x,(1,0))>0:return (1,0)
 if cmp(x,(-1,0))<0:return (-1,0)
 return x
def dot(a,b):
 s=(0,0)
 for x,y in zip(a,b):s=add(s,mul(x,y))
 return s
def check(row,limit=2500,max_depth=15):
 p=row['params'];W=[[[float_dy(x) for x in line] for line in mat] for mat in p['W']]
 b=[[float_dy(x) for x in vec] for vec in p['b']];v=[float_dy(x) for x in p['v']];c=float_dy(p['c'])
 start=(0,((1,1),(-1,1),(1,2)));visited={start:()};frontier=deque([start]);edges=0
 while frontier:
  q,h=frontier.popleft();w=visited[(q,h)]
  if len(w)>=max_depth:return {'status':'ABSTAIN','reason':'depth_limit'}
  for t in range(3):
   qq=0 if t==2 else 1 if t==1 else q
   hh=tuple(clamp(add(dot(W[t][j],h),b[t][j])) for j in range(3))
   z=add(dot(v,hh),c);edges+=1
   if (qq==1 and cmp(z,(0,0))<=0) or (qq==0 and cmp(z,(0,0))>=0):
    return {'status':'INCORRECT','witness':list(w),'edges_checked':edges}
   state=(qq,hh)
   if state not in visited:
    if len(visited)>=limit:return {'status':'ABSTAIN','reason':'state_limit'}
    visited[state]=w+(t,);frontier.append(state)
 return {'status':'CERTIFIED','states':len(visited),'edges_checked':edges}
if __name__=='__main__':
 D=json.load(open(R/'CHECKPOINTS.json'));A=json.load(open(R/'EXACT_REACHABILITY.json'))['results']
 lookup={(a['seed'],a['epoch']):a for a in A};out=[]
 for row in D['rows']:
  r=check(row);ref=lookup[row['seed'],row['epoch']]
  agree=r['status']==ref['status'] and (r['status']!='CERTIFIED' or r['states']==ref['states']) and (r['status']!='INCORRECT' or r['witness']==ref['witness'])
  out.append(dict(seed=row['seed'],epoch=row['epoch'],result=r,agrees=agree))
  if not agree:raise AssertionError((row['seed'],row['epoch'],r,ref))
  print(row['seed'],row['epoch'],r['status'],'agree',agree,flush=True)
 (R/'INDEPENDENT_DYADIC.json').write_text(json.dumps(out,indent=2)+'\n')
