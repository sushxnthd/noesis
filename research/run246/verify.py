"""Run246 exact dyadic ReLU state search + sound interval abstraction."""
from fractions import Fraction as F
from collections import deque
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
S=1024;BOUND=1<<20;BUDGET=256*26*3
def frac(x):return F.from_float(float(x))
def target(q,t):return 0 if t==2 else (1 if t==1 else q)
def params(row):
 p=row['params'];A=[[frac(v) for v in rr] for rr in p['A']];E=[[frac(v) for v in rr] for rr in p['E']]
 return A,E,[frac(v) for v in p['b']],[frac(v) for v in p['v']],frac(p['c'])
def exact(row,limit=2500,max_depth=15):
 A,E,b,v,c=params(row);d=len(v);init=(F(0),)*d
 todo=deque([(0,init,(),0)]);seen={(0,init)};checked=0
 while todo:
  q,h,path,depth=todo.popleft()
  if depth>=max_depth:return {'status':'ABSTAIN','reason':'depth','visited':len(seen)}
  for t in range(3):
   h2=tuple(max(F(0),sum(A[j][k]*h[k] for k in range(d))+E[t][j]+b[j]) for j in range(d))
   q2=target(q,t);z=sum(v[j]*h2[j] for j in range(d))+c;checked+=1
   if (z>0)!=bool(q2):return {'status':'INCORRECT','witness':list(path+(t,)),'length':depth+1,'visited':len(seen)}
   key=(q2,h2)
   if key not in seen:
    seen.add(key)
    if len(seen)>limit:return {'status':'ABSTAIN','reason':'state_budget','visited':len(seen)}
    todo.append((q2,h2,path+(t,),depth+1))
 return {'status':'CERTIFIED','visited':len(seen),'checked':checked}
def floor(x):return x.numerator//x.denominator
def ceil(x):return -((-x.numerator)//x.denominator)
def transfer(box,t,A,E,b):
 lo,hi=box;d=len(lo);L=[];U=[]
 for j in range(d):
  low=(E[t][j]+b[j])*S;up=low
  for k in range(d):
   a=A[j][k];low+=a*(lo[k] if a>=0 else hi[k]);up+=a*(hi[k] if a>=0 else lo[k])
  L.append(max(0,floor(low)));U.append(max(0,ceil(up)))
 if max(U)>BOUND:return None
 return tuple(L),tuple(U)
def join(a,b):
 if a is None:return b
 return tuple(min(x,y) for x,y in zip(a[0],b[0])),tuple(max(x,y) for x,y in zip(a[1],b[1]))
def readout(box,v,c):
 lo,hi=box;low=c*S;up=low
 for k,w in enumerate(v):low+=w*(lo[k] if w>=0 else hi[k]);up+=w*(hi[k] if w>=0 else lo[k])
 return low,up
def abstract(row):
 A,E,b,v,c=params(row);d=len(v);start=(0,());boxes={start:((0,)*d,(0,)*d)}
 todo=deque([start]);inq={start};n=0
 while todo:
  state=todo.popleft();inq.remove(state);q,suffix=state
  for t in range(3):
   n+=1
   if n>BUDGET:return {'status':'ABSTAIN','reason':'budget','transitions':n,'cells':len(boxes)}
   dest=(target(q,t),(suffix+(t,))[-2:]);im=transfer(boxes[state],t,A,E,b)
   if im is None:return {'status':'ABSTAIN','reason':'unbounded_box','transitions':n,'cells':len(boxes)}
   new=join(boxes.get(dest),im)
   if new!=boxes.get(dest):
    boxes[dest]=new
    if dest not in inq:todo.append(dest);inq.add(dest)
 margins=[]
 for (q,s),box in boxes.items():
  if not s:continue
  low,up=readout(box,v,c);margin=low if q else -up
  if margin<=0:return {'status':'ABSTAIN','reason':'readout_overlap','transitions':n,'cells':len(boxes)}
  margins.append(margin)
 return {'status':'CERTIFIED','certificate':{'scale':S,'activation':'relu','cells':[{'q':q,'suffix':list(s),'lo':list(box[0]),'hi':list(box[1])} for (q,s),box in sorted(boxes.items())],'minimum_scaled_margin':str(min(margins))},'transitions':n,'cells':len(boxes)}
def run():
 source=R/'CHECKPOINTS.json';rows=json.loads(source.read_text())['rows'];out=[]
 for row in rows:
  if row['epoch'] not in (0,50,200):continue
  ex=exact(row);rec={'seed':row['seed'],'epoch':row['epoch'],'train_accuracy':row['train_accuracy'],'exact':ex}
  if row['epoch']==200:
   a=abstract(row);rec['abstract']=a
   if ex['status']=='INCORRECT' and a['status']=='CERTIFIED':raise AssertionError('UNSOUND certificate')
  out.append(rec)
  (R/'OUTCOMES.json').write_text(json.dumps(out,indent=2)+'\n')
 idx={(r['seed'],r['epoch']):r for r in out};ends=[r for r in out if r['epoch']==200]
 new=[r['seed'] for r in ends if r['exact']['status']=='ABSTAIN' and r['abstract']['status']=='CERTIFIED']
 strict=[r['seed'] for r in ends if idx[(r['seed'],50)]['exact']['status']=='INCORRECT' and (r['exact']['status']=='CERTIFIED' or r['abstract']['status']=='CERTIFIED')]
 summary={'trained':48,'new_abstract_beyond_exact':len(new),'new_seeds':new,'strict_early_incorrect_to_certified':strict,'primary_threshold_pass':len(new)>=2,'learning_threshold_pass':len(strict)>=1,'certified_count':sum(r['exact']['status']=='CERTIFIED' or r['abstract']['status']=='CERTIFIED' for r in ends),'known_incorrect_false_positive':0,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
 (R/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
if __name__=='__main__':run()
