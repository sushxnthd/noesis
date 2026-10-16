"""NOESIS Run 195: prospective stutter grammar on unseen gradient-trained checkpoints."""
import itertools,json,hashlib,sys
from pathlib import Path
import numpy as np
import torch
SEEDS=(197,199,211,223,227,229,233,239)
def train(path):
 if path.exists():raise RuntimeError("refuse overwrite")
 torch.set_num_threads(1)
 x=torch.tensor(list(itertools.product((0,1),repeat=6)),dtype=torch.long)
 y=torch.cumsum(x,dim=1).remainder(2).to(torch.float64);rows=[]
 for seed in SEEDS:
  torch.manual_seed(seed)
  class Net(torch.nn.Module):
   def __init__(self):
    super().__init__()
    self.W=torch.nn.Parameter(torch.randn(8,8,dtype=torch.float64)*.3)
    self.U=torch.nn.Parameter(torch.randn(2,8,dtype=torch.float64)*.3)
    self.b=torch.nn.Parameter(torch.zeros(8,dtype=torch.float64))
    self.v=torch.nn.Parameter(torch.randn(8,dtype=torch.float64)*.3)
    self.c=torch.nn.Parameter(torch.zeros((),dtype=torch.float64))
   def forward(self,x):
    h=torch.zeros((len(x),8),dtype=torch.float64);z=[]
    for t in range(x.shape[1]):
     h=torch.tanh(h@self.W.T+self.U[x[:,t]]+self.b)
     z.append(h@self.v+self.c)
    return torch.stack(z,1)
  m=Net();opt=torch.optim.Adam(m.parameters(),lr=.02)
  for step in range(1,601):
   opt.zero_grad();z=m(x);loss=torch.nn.functional.binary_cross_entropy_with_logits(z,y)
   loss.backward();opt.step()
   if step in (300,600):
    with torch.no_grad():
     z=m(x);ll=float(torch.nn.functional.binary_cross_entropy_with_logits(z,y))
     acc=float(((z>0)==y).double().mean())
     rows.append({'seed':seed,'epoch':step,'loss':ll,'train_accuracy':acc,
                  'params':{k:v.detach().tolist() for k,v in m.named_parameters()}})
     print('TRAIN',seed,step,ll,acc,flush=True)
 path.write_text(json.dumps({'torch':torch.__version__,'numpy':np.__version__,'rows':rows},indent=1)+'\n')
def params(rows,seed,ep):
 p=next(r['params'] for r in rows if r['seed']==seed and r['epoch']==ep)
 return {k:np.asarray(v,dtype=np.float64) for k,v in p.items()}
def advance(h,p,b):return np.tanh(h@p['W'].T+p['U'][b]+p['b'])
def logits(h,p):return h@p['v']+p['c']
def classify(words,p):
 out=[]
 for w in words:
  h=np.zeros(8)
  for b in w:h=np.tanh(p['W']@h+p['U'][int(b)]+p['b'])
  out.append(float(h@p['v']+p['c']))
 return np.asarray(out)
def grammar(n):
 if n<=6:return [''.join(x) for x in itertools.product('01',repeat=n)]
 ordered=[];seen=set()
 def add(w):
  if len(w)==n and w not in seen:seen.add(w);ordered.append(w)
 add('0'*n);add('1'*n)
 for gap in range(n-2,-1,-1):
  for left in range(n-1-gap):
   right=n-2-gap-left;w='0'*left+'1'+'0'*gap+'1'+'0'*right
   add(w);add(''.join('1' if c=='0' else '0' for c in w))
   if len(ordered)>=32:break
  if len(ordered)>=32:break
 for split in range(1,n):
  add('0'*split+'1'*(n-split));add('1'*split+'0'*(n-split))
  if len(ordered)>=64:break
 for shift in range(n):add(''.join(str((i+shift)%2) for i in range(n)))
 for tup in itertools.product('01',repeat=n):
  if len(ordered)>=64:break
  add(''.join(tup))
 return ordered[:64]
def eligible(a,b):
 x=np.zeros((1,8));z=x.copy();ok=True;fail=[]
 for depth in range(1,13):
  x=np.concatenate([advance(x,a,0),advance(x,a,1)])
  z=np.concatenate([advance(z,b,0),advance(z,b,1)])
  if depth==1:par=np.asarray([0,1],dtype=np.int8)
  else:par=np.concatenate([par,1-par])
  good=((logits(x,a)>0)==(par>0))&((logits(z,b)>0)==(par>0))
  if not bool(good.all()):ok=False;fail.append([depth,int((~good).sum())])
 return ok,fail
def grammar_search(a,b):
 counts=[]
 for n in range(1,25):
  ws=grammar(n);counts.append(len(ws));u=classify(ws,a);v=classify(ws,b)
  hit=np.flatnonzero(np.signbit(u)!=np.signbit(v))
  if hit.size:
   j=int(hit[0])
   return {'depth':n,'witness':ws[j],'logits':[float(u[j]),float(v[j])],
           'evaluations':sum(counts),'per_depth':counts}
 return {'depth':None,'witness':None,'evaluations':sum(counts),'per_depth':counts}
def beam(a,b,counts):
 x=np.zeros((1,8));z=x.copy();ws=[''];used=0
 for n,num in enumerate(counts,1):
  xx=np.concatenate([advance(x,a,0),advance(x,a,1)])
  zz=np.concatenate([advance(z,b,0),advance(z,b,1)])
  ww=[w+'0' for w in ws]+[w+'1' for w in ws]
  assert len(ww)==num,(n,len(ww),num)
  u=logits(xx,a);v=logits(zz,b);used+=len(ww)
  hit=np.flatnonzero(np.signbit(u)!=np.signbit(v))
  if hit.size:return {'depth':n,'witness':ww[int(hit[0])],'evaluations':used}
  take=np.argsort(-np.abs(u-v),kind='stable')[:32]
  x=xx[take];z=zz[take];ws=[ww[j] for j in take]
 return {'depth':None,'witness':None,'evaluations':used}
def random_trial(a,b,counts,seed):
 rng=np.random.default_rng(seed)
 for n,num in enumerate(counts,1):
  bits=rng.integers(0,2,size=(num,n),dtype=np.int8)
  x=np.zeros((num,8));z=x.copy()
  for j in range(n):
   x=np.tanh(x@a['W'].T+a['U'][bits[:,j]]+a['b'])
   z=np.tanh(z@b['W'].T+b['U'][bits[:,j]]+b['b'])
  diff=np.flatnonzero(np.signbit(logits(x,a))!=np.signbit(logits(z,b)))
  if diff.size:return {'depth':n,'witness':''.join(map(str,bits[int(diff[0])]))}
 return {'depth':None,'witness':None}
def evaluate(path,out):
 data=json.loads(path.read_text());rows=data['rows']
 res={'checkpoint_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'rows':[]}
 for seed in SEEDS:
  a,b=params(rows,seed,300),params(rows,seed,600)
  ok,shortfail=eligible(a,b);g=grammar_search(a,b);be=beam(a,b,g['per_depth'])
  random=[random_trial(a,b,g['per_depth'],195000+j) for j in range(100)]
  hits=sum(r['witness'] is not None for r in random)
  success=bool(ok and g['depth'] is not None and 13<=g['depth']<=24 and be['witness'] is None and hits<=5)
  row={'seed':seed,'eligible':ok,'short_failure_depth_counts':shortfail,'grammar':g,'beam':be,
       'random_hits':hits,'random_trials':random,'qualifying':success}
  res['rows'].append(row)
  print('EVAL',seed,'eligible',ok,'grammar',g['depth'],'beam',be['depth'],'random',hits,'qualifies',success,flush=True)
 res['success_scalar']=sum(x['qualifying'] for x in res['rows'])
 out.write_text(json.dumps(res,indent=1)+'\n')
 print('SUCCESS',res['success_scalar'],flush=True)
if __name__=='__main__':
 if len(sys.argv)!=4:raise SystemExit('run195.py train|eval CHECKPOINTS OUT')
 if sys.argv[1]=='train':train(Path(sys.argv[2]))
 elif sys.argv[1]=='eval':evaluate(Path(sys.argv[2]),Path(sys.argv[3]))
