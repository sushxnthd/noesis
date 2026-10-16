"""Run209 untrusted numeric candidate generation; no proof claims."""
import math
def dest(t,s):return 0 if t==2 else s^(t==1)
def first_error(row,limit=4096):
 p=row['params'];bounds=[(.5,.5),None];ptr=[(0,0),None];nodes=[(-1,-1)]
 for n in range(1,limit+1):
  nxt=[[math.inf,-math.inf] for _ in range(2)];np=[[None,None] for _ in range(2)]
  for s in range(2):
   if bounds[s] is None:continue
   for t in range(3):
    for k in range(2):
     z=math.tanh(p['w'][t]*bounds[s][k]+p['b'][t]);d=dest(t,s)
     node=len(nodes);nodes.append((ptr[s][k],t))
     if z<nxt[d][0]:nxt[d][0]=z;np[d][0]=node
     if z>nxt[d][1]:nxt[d][1]=z;np[d][1]=node
  bounds=[tuple(x) if x[0]!=math.inf else None for x in nxt]
  ptr=[tuple(x) if x[0] is not None else None for x in np]
  for s in range(2):
   if bounds[s] is None:continue
   side=(1 if p['v']>=0 else 0) if s==0 else (0 if p['v']>=0 else 1)
   z=p['v']*bounds[s][side]+p['c']
   if (s==0 and z>1e-10) or (s==1 and z< -1e-10):
    word=[];node=ptr[s][side]
    while node>0:
     node,t=nodes[node];word.append(t)
    word.reverse();return n,word
 return None,None
def propose_boxes(row):
 p=row['params'];w=p['w'];b=p['b'];v=p['v'];c=p['c'];grid=1e-6
 def down(z):return math.floor((z-1e-7)/grid)*grid
 def up(z):return math.ceil((z+1e-7)/grid)*grid
 z=[math.tanh(w[t]*.5+b[t]) for t in range(3)]
 lo=[down(min(z[0],z[2])),down(z[1])];hi=[up(max(z[0],z[2])),up(z[1])]
 for _ in range(1000):
  oldlo=lo[:];oldhi=hi[:]
  for s in range(2):
   for t in range(3):
    d=dest(t,s)
    a=math.tanh(w[t]*(oldlo[s] if w[t]>=0 else oldhi[s])+b[t])
    z=math.tanh(w[t]*(oldhi[s] if w[t]>=0 else oldlo[s])+b[t])
    lo[d]=min(lo[d],down(a));hi[d]=max(hi[d],up(z))
  if min(lo)<-1.001 or max(hi)>1.001:return None
  if lo==oldlo and hi==oldhi:
   for s in range(2):
    yl=v*(lo[s] if v>=0 else hi[s])+c
    yh=v*(hi[s] if v>=0 else lo[s])+c
    if not (yh<0 if s==0 else yl>0):return None
   return [[str(lo[s]),str(hi[s])] for s in range(2)]
 return None
